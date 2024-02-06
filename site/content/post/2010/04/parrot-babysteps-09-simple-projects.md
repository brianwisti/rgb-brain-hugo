---
aliases:
- /coolnamehere/2010/04/29_09-simple-projects.html
- /post/2010/09-simple-projects/
- /2010/04/29/parrot-babysteps-09-simple-projects/
category: post
created: 2024-01-15 15:25:33-08:00
date: 2010-04-29 00:00:00-07:00
series:
- Parrot Babysteps
slug: parrot-babysteps-09-simple-projects
tags:
- parrot
- learn
- coolnamehere
title: Parrot Babysteps 09 - Simple Projects
updated: 2024-01-26 10:09:42-08:00
---

# Introduction

I spent a lot of time exploring [Parrot](../../../card/Parrot.md) testing with [Test::More](https://github.com/parrot/parrot/blob/RELEASE_3_0_0/runtime/parrot/library/Test/More.pir) in the [last step](/post/2009/12/parrot-babysteps-08-testing-with-testmore). That's because
I want to start building larger projects, and testing is a vital part of most
projects. Another major part is a properly organized workspace with a script that
can simplify testing or other tasks.

# Creating a Simple Project

A nice Parrot project layout includes a `t` folder for tests, a `lib` folder for
library code, and a `setup.pir` file to drive the whole thing.

````
$ mkdir simple-pir
$ mkdir simple-pir/t
$ mkdir simple-pir/lib
$ cd simple-pir
````

What gets placed in `setup.pir`? Not much, considering how much it does.
`setup.pir` takes advantage of the Parrot [distutils](https://github.com/parrot/parrot/blob/RELEASE_3_0_0/runtime/parrot/library/distutils.pir) module for a whole range
of tasks. All I'm concerned about today is *testing*, so my setup is going to be
rather lightweight.

````
# example-09-01/setup.pir
.sub 'main' :main
    .param pmc args
    $S0 = shift args # Ignore my own filename
    load_bytecode 'distutils.pbc'

    # Find out what command the user has issued
    .local string directive
    directive = shift args

    setup(directive)
.end
````

This is not exciting code, but it is enough to see what distutils *can* give me.
The first command line parameter is shifted onto a dummy register variable, 
because I don't really care about the name of `setup.pir` from within
`setup.pir`.  Then I load the [distutils](https://github.com/parrot/parrot/blob/RELEASE_3_0_0/runtime/parrot/library/distutils.pir) bytecode so I can get access to the `setup` subroutine. 

This `setup.pir` will get more complicated as we go on, and you will
*definitely* see more complex `setup.pir` files out in the wild, but this will
get us started.

````
$ parrot setup.pir help
usage: parrot setup.pir [target|--key value]*

    Default targets are :

        build:          Build the library.

        test:           Run the test suite.

        install:        Install the library.

        uninstall:      Uninstall the library.

        clean:          Basic cleaning up.

        update:         Update from the repository.

        plumage:        Output a skeleton for Plumage

        sdist:          Create a source distribution

        bdist:          Create a binary distribution

        help:           Print this help message.
````

What happens when I tell `setup.pir` that I want to test?

````
$ parrot setup.pir test
Files=0, Tests=0,  0.000 wallclock secs
Result: NOTESTS
````

Well of course it failed. There aren't any test files, and `setup.pir` wouldn't
know how to run them if there were!

I'll fix the second part first.

````
# example-09-02/setup.pir
.sub 'main' :main
    .param pmc args
    $S0 = shift args # Ignore my own filename
    load_bytecode 'distutils.pbc'

    # Find out what command the user has issued
    .local string directive
    directive = shift args

    # Used by the test mode
    .local string prove_exec
    prove_exec = get_parrot()

    setup(directive, 'prove_exec' => prove_exec)
.end
````

Parrot allows you to use [named parameters](http://docs.parrot.org/parrot/latest/html/docs/book/pir/ch06_subroutines.pod.html#Named_Parameters) for some subroutines, and `setup`
takes full advantage of that feature. If you're used to [Perl](/tags/perl/) or [Ruby](/tags/ruby/),
named parameters look a lot like a hash. That's close enough for our purposes. A
named parameter generally follows a simple format:

````
'<key-1>' => '<value-1>'
````

Thankfully, `distutils.pir` is a well-documented module, and you
can find details about the many options by checking the documentation.

````
$ perldoc /usr/local/lib/parrot/3.0.0/library/distutils.pir
````

I only care about a single option: `prove_exec`, which tells `setup` what program 
will be used to run the tests. Why does `setup` care? Well, Parrot is a VM. Your 
tests can be in PIR, NQP, [Rakudo](/tags/raku-lang/), or even a language of your own design.
These [Babysteps](/post/2009/07/parrot-babysteps) are about Parrot PIR, so it makes sense that the tests will be in
the same language.

Oh yes, the tests. Let's write one. I'll follow the convention I see in the Perl
world of a number followed by a description for the test filename, and the test
itself will be for a simple area calculating function.

````
# example-09-02/t/01-radius.t
.sub 'main' :main
    .include 'test_more.pir'
    .local num radius
    .local num expected_area, actual_area

    plan(1)

    radius = 1.0
    expected_area = 3.1415926
    actual_area = area_of_circle(radius)
    is(expected_area, actual_area, 'Circle with radius 1 should have area PI', 1e-6)
.end
````

So - this should fail, right?

````
$ parrot setup.pir test
t/01-radius.t .. Dubious, test returned 1
Failed 1/1 subtests 

Test Summary Report
-------------------
t/01-radius.t (Tests: 0 Failed: 0)
  Non-zero exit status: 1
  Parse errors: Unknown TAP token: "Could not find sub area_of_circle"
                Unknown TAP token: "current instr.: 'main' pc 40
(t/01-radius.t:13)"
                Bad plan.  You planned 1 tests but ran 0.
Files=1, Tests=0,  0.021 wallclock secs
Result: FAIL
test fails
current instr.: 'setup' pc 883 (runtime/parrot/library/distutils.pir:376)
called from Sub 'main' pc 29 (setup.pir:18)
````

Excellent. Parrot didn't just tell us that the test failed. It also told us
about some unexpected output from our test script. What's that unexpected
output? Oh, something about not having a subroutine called `area_of_circle`.
Let's fix that by adding a new library file called `lib/area.pir`, and adding
the missing subroutine.

````
# example-09-03/lib/area.pir

.sub area_of_circle
    .param num radius
    .const num PI = 3.1415926
    .local num area

    area = PI
    area *= radius
    area *= radius

    .return(area)
.end
````

This is code borrowed from [step 2](/post/2009/07/parrot-babysteps-02-variables-and-types) and dropped into a subroutine.

Don't forget to include this library code from your test file.

````
# example-09-03/lib/area.pir

.include 'lib/area.pir'

.sub 'main' :main
    # ...
.end
````

Did it work?

````
$ parrot setup.pir test
t/01-radius.t .. ok
All tests successful.
Files=1, Tests=1,  0.016 wallclock secs
Result: PASS
````

Yay!

Hold on a second. I snuck an extra argument back when I wrote the `is` assertion. What was that
all about? Well, [Jonathan Leto](http://leto.net) explained to me that `is` takes an additional argument
for precision, which is useful in the fuzzy world of [floating point 
math](http://en.wikipedia.org/wiki/Floating_point#Accuracy_problems) on
a modern computer. The `1e-6` requirement asks Parrot to make sure `expected_area`
and `actual_area` look the same down to six places past the decimal point.

This approach of writing the tests before you write the code is called TDD, for
[Test Driven Development](http://en.wikipedia.org/wiki/Test-driven_development). I like TDD because I'm basically describing the next
thing I want my library or application to do. That's perfect for me, since I'm such
a chatty person. Well, I'm chatty when typing at the computer. 

You don't need to follow a
test driven approach, but other developers will like you more if you consistently
test the code you write. The easiest way to consistently test it is to write the
test before you write the code.

# Conclusion

Combining what we've learned about [Test::More](https://github.com/parrot/parrot/blob/RELEASE_3_0_0/runtime/parrot/library/Test/More.pir) with `setup.pir` allows us to
confidently build more complicated applications, testing as we go along. It is
true that all we know how to do with `setup.pir` at this point is ask it to run
tests for us, but even that can save a lot of work.

I don't know about you, but I'm ready to take another look at that star catalog.