---
aliases:
- /coolnamehere/2011/08/23_moose.html
- /post/2011/moose/
- /2011/08/23/moose/
category: post
created: 2024-01-15 15:25:32-08:00
date: 2011-08-23 00:00:00-07:00
slug: moose
tags:
- perl
- coolnamehere
title: Moose
updated: 2024-02-01 20:26:15-08:00
---

I have been dabbling a lot with [Moose](https://metacpan.org/module/Moose), a solid framework
for object oriented programming in [Perl](../../../card/Perl.md). It is remarkably powerful
and has transformed the way I look at Perl OO. It is also different
enough from object oriented programming in other languages that I needed
to create a section for it on [coolnamehere](../../../card/coolnamehere.md).

<!--more-->

## Boilerplate

Perl OO has a reputation for boilerplate: large chunks of code that
have little relation to the task at hand, but are necessary for the
application to work at all. Fortunately, [Moose](https://metacpan.org/module/Moose) cuts down 
significantly on the boilerplate. You can cut it down even more by taking
advantage of the features available in recent versions of Perl, and
that is exactly what I do in my code templates.

````perl
# MyClass.pm
use 5.14.0;

package MyClass 1.0 {
    use Moose;

    # Attributes and methods go here.

    no Moose;
    __PACKAGE__->meta->make_immutable;
}
    
=head1 NAME

MyClass

=cut
````

Since I am not being paid by the word, I ignored most of the Perldoc
boilerplate that I use. 

That's it, really. You can move on if you're not interested in my rambling
explanations.

## The Rambling Explanation

Let's examine the boilerplate code.

````perl
use 5.14.0;
````

This tells `perl` that the program requires features that only become
available in [Perl 5.14](http://perldoc.perl.org/perl5140delta.html). If I tried to load this library in an 
application using a different version of Perl, it simply would not work:

````
Perl v5.14.0 required--this is only v5.12.3, stopped at MyClass.pm line 1.
BEGIN failed--compilation aborted at MyClass.pm line 1.
````

I also get [Perl 5.12](http://perldoc.perl.org/perl5120delta.html) and [Perl 5.10](http://perldoc.perl.org/perl5100delta.html) features, as long as they
haven't been made redundant by a change in the newest Perl.

````perl
package MyClass 1.0 {
````

This is one of those [syntactical enhancements](http://perldoc.perl.org/perl5140delta.html#Syntactical-Enhancements) that I like in Perl 5.14.
Here's my package. It's called "MyClass". It has a `$VERSION` of `1.0`.
I suppose I could use [MooseX::Declare](https://metacpan.org/module/MooseX::Declare), but I'm still getting the
hang of core [Moose](https://metacpan.org/module/Moose) functionality. 

````perl
use Moose;
````

Now I've told Perl that the `MyClass` package is actually a [Moose](https://metacpan.org/module/Moose) class.
A *lot* of stuff is going on the background now, as all the Moose support
structure is loaded and set up.

````perl
# Attributes and methods go here.
````

Okay, yeah. That part's kind of obvious, isn't it?

````perl
no Moose;
````

Now that I'm done with `MyClass`, I want to get all the special Moose names
out of the way.

````perl
__PACKAGE__->meta->make_immutable;
````

A fully fleshed Moose object maintains a lot of flexibility. Unless I explicitly
*need* that flexibility, I should make the class a little lighter.

````perl
}
````

That's it. The package is done. It's worth noticing what's missing: the classic `1;` 
that has ended Perl modules for years. As far as I can tell, the new `package` syntax
makes it unnecessary. Perl 5.14 doesn't complain about it missing.