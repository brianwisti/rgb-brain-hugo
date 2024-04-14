---
aliases:
- /post/2020/07/tangling-code-from-hugo-content-with-raku/
category: post
created: 2024-01-15 15:26:25-08:00
date: 2020-07-08 21:45:00-07:00
description: I could just use Org mode, but noo that's too easy
slug: tangling-code-from-hugo-content-with-raku
syndication:
  mastodon: https://hackers.town/@randomgeek/104482085213153476
  twitter: https://twitter.com/brianwisti/status/1281087955398991874
tags:
- raku-lang
- literateprogramming
- files
- hugo
- sortof
- programming
title: Tangling code from Hugo content with Raku
updated: 2024-02-01 20:58:43-08:00
---

![attachments/img/2020/cover-2020-07-08.jpg](../../../attachments/img/2020/cover-2020-07-08.jpg)
You know what else I can tangle? Yarn!

I spend a while using [Raku](../../../card/Raku.md) to extract code from a [Hugo](../../../card/Hugo.md) post.

<!--more-->


 > 
 > **2020-09-03**
>
 > [@codesections@fosstodon.org](https://fosstodon.org/@codesections) found a typo! I forgot to *show* the target file name once command line arguments are in place. It should go `raku tangle-fragments.raku index.md`.

Let's say I have a file.  The one you're reading, perhaps.  Well, its original Markdown content.

It has a [Hugo](../../../card/Hugo.md) shortcode in it.

````html
{{</* code file="hello.py" */>}}
print("Hello")
{{</* /code */>}}
````

I based `{{</* code */>}}` here on a shortcode from the [Hugo docs](https://github.com/gohugoio/hugoDocs/blob/master/layouts/shortcodes/code.html). It presents highlighted code with additional context.

````python{title="hello.py"}
 print("Hello")
````

Really handy when you're writing about code.  Thing is, now I have two copies. There's one here in the shortcode, and another in a `hello.py` file that I'm writing about.  I'd prefer there was only a single copy.  That way they don't get out of sync.

I *could* use Hugo's [readFile](https://gohugo.io/functions/readfile/) function in a new shortcode, including the contents of `hello.py` in this Markdown file.  Something like this:

````html
{{</* include file="hello.py" */>}}
````

 > 
 > **NOTE**
>
 > Actual shortcode logic left as an exercise for the reader.

But that still breaks up the writing flow a little bit.  I'm writing the code over here, and writing *about* it over there.  It's a tiny complaint, but working with [Org](../../../card/Org.md) has spoiled me.  I get to write the code in the same document that I'm writing about it in.  Everything stays in sync, more or less.

What I want is to write about `hello.py` here, and with a command have `hello.py` appear on my filesystem, containing the Python code I've been describing.

And I want to do it without disturbing Hugo. Let it turn Markdown into HTML.

## Tangling

This process is called "tangling," and it's popular in the admittedly small
world of [Literate Programming](http://literateprogramming.com/).  The code is interleaved
throughout some kind of document.  A tool like [noweb](https://www.cs.tufts.edu/~nr/noweb/) or [Babel](https://orgmode.org/worg/org-contrib/babel/intro.html)
parses the document to create code files.  Could be any kind of file, really.
The process can get fancy.

But the start is not fancy: given a text file containing a `{{</* code file="(something)" */>}}`, write the contents of that shortcode to the named file.

````raku
sub MAIN() {
  my $filename = "index.md";
  my $opener = '{{</* ';
  my $closer = ' */>}}';
  my regex shortcode {
    $opener
      code \s
      'file="' $<filename> = .+? '"'  # Remember the filename
      .*?
    $closer
    \n                # Ignore leading newline
    $<content> = .+?  # Remember everything else in the block
    \n                # Ignore leading newline
    $opener '/code' $closer
  }

  my $markdown = slurp $filename;

  if $markdown.match(/ <shortcode> /) {
    my $tangle-file = $/<shortcode><filename>;
    my $tangle-content = $/<shortcode><content>;
    spurt $tangle-file, $tangle-content;
    say "Tangled to $tangle-file";
  }
}
````

I love Raku's approach to [regular expressions](https://docs.raku.org/language/regexes).  For starters, the syntax looks a bit more like describing a grammar.  I can break the funny regex characters up with spaces, and clarify them with comments.  In fact, I could someday build this up to a real [grammar](https://docs.raku.org/language/grammars).

Secondly, it addresses the fact that most text we look at these days contains multiple lines.  I didn't have to worry about any special multiline flags to get this working.

Finally, getting at the named captures was — I wouldn't say "obvious," but at least "coherent." I can treat the match variable `$/` as a nested [Hash](https://docs.raku.org/language/hashmap). The important bits look something like this::

````text
shortcode =>
  filename => ｢hello.py｣
  content => ｢print("Hello")｣
````

I can grab the named capture `filename` of my matched `shortcode` regex with `$/<shortcode><filename>` — or `~$<shortcode><filename>`, depending on your preferred syntax.

This is all possible in languages like Perl with assorted flags, but I haven't seen parsing treated so well by default since maybe [REBOL](../../2004/12/rebol.md).

Anyways, let's run this thing.

````console
$ raku tangle.raku
Tangled to hello.py
$ bat hello.py
───────┬──────────────────────────────────────────────────────────────────────
       │ File: hello.py
───────┼──────────────────────────────────────────────────────────────────────
   1   │ print("Hello")
───────┴──────────────────────────────────────────────────────────────────────
````

Sweet.

Except — this Markdown file I'm writing.  It has *two* file code blocks now.  I want to tangle both of them.

## Multiple output files

This requires a couple changes, since I'm writing code about Hugo shortcodes in a Hugo post.

To show shortcode directives without Hugo evaluating them, they need to look like shortcode comments.  Their contents will get passed straight through as part of your post.  To show `{{</* shortcode */>}}` in a post, your Hugo content needs `{{</*/* shortcode */*/>}}`.

So that's lovely and all, but can be a headache of its own for this specific situation of extracting code from a blog post.

I need to remember this commented shortcode syntax.

````raku{title="define-commented-shortcodes"}
 my $commented-opener = '{{' ~ '</* ';
 my $commented-closer = ' */>' ~ '}}';
````

 > 
 > **NOTE**
>
 > Goodness, that looks silly.  Well, I'm writing this blog post as a test case
 > for the code.  I couldn't figure out how to cleanly present the  commented shortcode delimiters without Hugo and my code getting into a fierce argument.
 > 
 > If I wasn't writing the code *in* this post, I could use something simpler, like this:
 > 
 > ````raku
 > my $commented-opener = '{{​</* ';
 > my $commented-closer = ' */>}}';
 > ````
 > 
 > But that's not the path I chose.  It's not easy to write programs that write themselves.  Sometimes you must help them along.

That way I can replace those commented shortcode delimiters with their normal counterparts when I tangle later.

````raku{title="define-commented-shortcodes"}
my $tangle-content = $block<shortcode><content>
  .subst(:global, / $commented-opener /, $opener)
  .subst(:global, / $commented-closer /, $closer);
````

Now that I have that particular detail out of the way, tangle every block? Sure!  Make a regular expression match `:global` and it returns a list containing every match.

````raku{title="tangle-every-block"}
my $markdown  = slurp $filename;
my @fragments = $markdown.match(/<shortcode>/, :global);

for @fragments -> $block {
  my $tangle-file = $block<shortcode><filename>;
  «replace-commented-shortcodes»
  spurt $tangle-file, $tangle-content;
  say "Tangled to $tangle-file";
}
````

I think that about covers it.  The shortcode recognition logic can stay the same.

````raku{title="tangle-multi.raku"}
sub MAIN() {
  my $filename = "index.md";
  my $opener = '{{</* ';
  my $closer = ' */>}}';

  my regex shortcode {
    $opener
      code \h
      'file="' $<filename> = .+? '"'  # Remember the filename
      .*?
    $closer
    \n                # Ignore leading newline
    $<content> = .+?  # Remember everything else in the block
    \n                # Ignore trailing newline
    $opener '/code' $closer
  }

  «define-commented-shortcodes»

  «tangle-every-block»
}
````

And it works!

````console
$ raku tangle-multi.raku
Tangled to hello.py
Tangled to tangle.raku
$ bat tangle.raku
───────┬──────────────────────────────────────────────────────────────────────
       │ File: tangle.raku
───────┼──────────────────────────────────────────────────────────────────────
   1   │ sub MAIN() {
   2   │   my $filename = "index.md";
   3   │   my $opener = '{{</* ';
   4   │   my $closer = ' */>}}';
   5   │   my regex shortcode {
   6   │     $opener
   7   │       code \s
   8   │       'file="' $<filename> = .+? '"'  # Remember the filename
   9   │       .*?
  10   │     $closer
  11   │     \n                # Ignore leading newline
  12   │     $<content> = .+?  # Remember everything else in the block
  13   │     \n                # Ignore leading newline
  14   │     $opener '/code' $closer
  15   │   }
  16   │
  17   │   my $markdown = slurp $filename;
  18   │
  19   │   if $markdown.match(/ <shortcode> /) {
  20   │     my $tangle-file = $/<shortcode><filename>;
  21   │     my $tangle-content = $/<shortcode><content>;
  22   │     spurt $tangle-file, $tangle-content;
  23   │     say "Tangled to $tangle-file";
  24   │   }
  25   │ }
  ───────┴──────────────────────────────────────────────────────────────────────
````

Unfortunately, I'm not quite done yet.

## Multiple fragments

I'm not done yet because I don't like to describe my code a full file at a time.  I'd rather talk about this bit here, explain that bit over there, then mash it all up in the end.

Consistency counts, so I need to pick a syntax.  Well — you've been reading along.  You can see that I already made my choice.  I got used to `<<fragment-name>>` in Babel, where the attribute is called `name`. Might as well keep doing that over here.  Oh but hang on. I want it to stand out a bit.  I'll use angle quotes `«‥»`.

 > 
 > **NOTE**
>
 > On a US keyboard using [Vim](../../../card/Vim.md) or [Neovim](../../../card/Neovim.md), `«` is a [digraph](https://vimhelp.org/digraph.txt.html#digraph.txt) which can be entered via <kbd>Control-k</kbd> followed by <kbd>\<\<</kbd>.  Or if you've set up a [Compose](https://en.wikipedia.org/wiki/Compose_key) key, it's <kbd>Compose</kbd> followed by <kbd>\<\<</kbd> in any editor.
 > 
 > `»` is the same, but <kbd>\>></kbd> instead.
 > 
 > *Or* you can use `<<…>>` in your code and ignore my recent obsession with fancy characters.
 > 
 > Yes, I know I could practically write it *all* with fancy characters in Raku. One step at a time.

Let's go back to the Python code because it's still so small.

Say I want to demonstrate the delightful [Rich](../../../card/Rich.md) terminal library for Python.

````python{title="import-libraries"}
 from rich import print
 from rich.panel import Panel
 from rich.markdown import Markdown
````

But before I really use it in my code, I spend 1,500 words singing its praises.

It's nice.  I like it.

Okay, done singing.  Time to write the rest of the program.

````python{title="rich-hello.py"}
«import-libraries»

md = Markdown("**Hello**, *World*.")
print(Panel(md))
````

I identify the fragment with a `name` attribute:

````html
{{</* code name="import-libraries" lang="python" */>}}
from rich import print
from rich.panel import Panel
from rich.markdown import Markdown
{{</* /code */>}}
````

My `code` block references the `import-libraries` fragment by name when I'm ready for it.

````html
{{</* code file="rich-hello.py" */>}}
«import-libraries»

md = Markdown("**Hello**, *World*.")
print(Panel(md))
{{</* /code */>}}
````

I *might* spend some time talking about the `code` shortcode in another post, but I dislike Go's templating enough that this does not sound like fun.

### Rounding up fragments to tangle

Recognizing an additional parameter doesn't make my regular expression *that* much more complicated, but I can see things getting  ore complex.  I could even find a better pattern later.  Let's give the params their own named regex for some encapsulation.

````raku{title="shortcode-params-regex"}
my regex params {
   'file="' $<filename> = .+? '"'
   ||
   'name="' $<fragment> = .+? '"'
}
````

That way I can drop it in `shortcode` to say "oh and look for `params` while you're at it please."

````raku{title="nested-shortcode-regex"}
«shortcode-params-regex»
my $opener = '{{</* ';
my $closer = ' */>}}';

my regex shortcode {
  $opener code \s <params> .*? $closer
  \n                # Ignore leading newline
  $<content> = .+?  # Remember everything else in the block
  \n                # Ignore trailing newline
  $opener '/code' $closer
}
````

Okay, we recognize `file` and `name` parameters.  What do we do with them? We gather them!

````raku{title="gather-fragments-and-files"}
my %fragment-for;
my @filenames;
my $markdown = slurp $filename;

for $markdown.match(/<shortcode>/, :global) -> $block {
  my $tangle-content = $block<shortcode><content>;
  my $params = $block<shortcode><params>;
  my $fragment = $params<fragment> || $params<filename>;

  if $fragment {
    say "fragment: $fragment";
    %fragment-for{ $fragment.Str } = $tangle-content;
  }

  if my $filename = $params<filename> {
    @filenames.push($filename.Str);
  }
}
````

### Tangling my fragments

Let's see here.  I know before I can write any files, I need to make sure everything's tangled Trying to keep fragments easy to identify.  They sit on a line by themselves, possibly with some leading whitespace.

````raku{title="tangle-fragments"}
my regex fragment { ^^ \h*? "«" $<name> = .+? "»" $$ }
my %tangle-for;

«tangle-function»

for %fragment-for.keys -> $name { tangle($name); }
````

Raku functions are lexically scoped, which means it's perfectly okay to declare a function inside another function.  Though next time I revisit  his, I may want to think about a [class](https://docs.raku.org/language/classtut) or something to hold the  complexity.

But what does that function need to look like?  I'm still not sure I got it quite right.  I mean I know the *basic* shape of it.

````raku{title="tangle-function"}
sub tangle(Str $name) {
  «tangle-error-checking»

  «tangle-text»
}
````

It needs some error checking.  I know that much.  Oh, and if it's already been tangled I should avoid going through it again.

````raku{title="tangle-error-checking"}
   return "" unless $name;

   if %tangle-for{ $name } {
     return %tangle-for{ $name }.Str;
   }

   my $content = %fragment-for{ $name };
   unless $content {
     die "«$name» is not a valid fragment";
   }
````

The idea of the thing is clear enough.  Find and recursively `tangle` each fragment found in this text, replacing the fragment references with their tangled text.  Once that's all done, cache and return the tangled text.

````raku{title="tangle-text"}
   for $content.match(/ <fragment> /, :global) -> $match {
     my $fragment-ref = $match.Str;
     my $fragment-name = $match<fragment><name>.Str;
     say "$name ← «$fragment-name»";
     $content.subst-mutate(/$fragment-ref/, tangle( $fragment-name));
   }

   %tangle-for{ $name } = $content;
````

I flailed while tangling fragments.  Lots of complaints from Raku about the difference between a `Match` and a `String`.  There *must* be better ways. But the most important thing?  I got it to work eventually.

### Writing tangled files

After all that, writing the tangled files felt easy.

````raku{title="write-tangled-fragments"}
   «define-commented-shortcodes»

   for @filenames -> $tangle-file {
     my $tangle-content = %tangle-for{ $tangle-file }
       .subst(:global, / $commented-opener /, $opener)
       .subst(:global, / $commented-closer /, $closer);
     spurt $tangle-file, $tangle-content;
     say "Tangled to $tangle-file";
   }
````

Then — theoretically — all these fragments I wrote will make a useful code tangler!

Might as well make it so this script can look at more than just the file I'm editing right now.

````raku{title="tangle-fragments.raku"}
sub MAIN(Str $filename) {
  «nested-shortcode-regex»

  «gather-fragments-and-files»

  «tangle-fragments»

  «write-tangled-files»
}
````

Easiest [CLI](https://docs.raku.org/language/create-cli) I ever wrote, by the way.  See?

````console
$ raku tangle-fragments.raku
Usage:
  tangle-fragments.raku <filename>
````

Time for the real thing.  I'm nervous.  I shouldn't be nervous.  I know how this story ends.  Then again I keep rewriting the middle.

````console
$ raku tangle-fragments.raku index.md
fragment: hello.py
fragment: tangle.raku
fragment: define-commented-shortcodes
fragment: replace-commented-shortcodes
fragment: tangle-every-block
fragment: tangle-multi.raku
fragment: import-libraries
fragment: rich-hello.py
fragment: shortcode-params-regex
fragment: nested-shortcode-regex
fragment: gather-fragments-and-files
fragment: tangle-fragments
fragment: tangle-function
fragment: tangle-error-checking
fragment: tangle-text
fragment: write-tangled-files
fragment: tangle-fragments.raku
tangle-function <-- (tangle-error-checking)
tangle-function <-- (tangle-text)
nested-shortcode-regex <-- (shortcode-params-regex)
tangle-every-block <-- (replace-commented-shortcodes)
tangle-fragments <-- (tangle-function)
write-tangled-files <-- (define-commented-shortcodes)
tangle-fragments.raku <-- (nested-shortcode-regex)
tangle-fragments.raku <-- (gather-fragments-and-files)
tangle-fragments.raku <-- (tangle-fragments)
tangle-fragments.raku <-- (write-tangled-files)
rich-hello.py <-- (import-libraries)
tangle-multi.raku <-- (define-commented-shortcodes)
tangle-multi.raku <-- (tangle-every-block)
Tangled to hello.py
Tangled to tangle.raku
Tangled to tangle-multi.raku
Tangled to rich-hello.py
Tangled to tangle-fragments.raku
````

That overwrote my test version of `tangle-fragments.raku`.  Scary.  Ran the new version to keep myself honest.  It produced the same output, and appears to have correctly tangled my fragments!

````python{title="Generated rich-hello.py", verbatim=false}
from rich import print
from rich.panel import Panel
from rich.markdown import Markdown

md = Markdown("**Hello**, *World*.")
print(Panel(md))
````

Running `rich-hello.py` looks more interesting with a screenshot than a text block:

![Formatted output using Rich](attachments/img/2020/rich-panel.png)

Okay.  Now I'm done.

I *could* have done this in Python.  There are decent parsing libraries out there.  But Raku did this on its own, without pulling in any extra — without pulling in *any* libraries.

## Done? You barely started!

My tangle script is no competition for Org mode's Babel.

* it needs more error checking
  * circular fragment references
  * unreachable files (path, permissions)
* smart handling of whitespace and indentation to keep Python from becoming a chore
* rendering fragment names in such a way that syntax highlighters can do something pretty with them
  * especially when writing code in a language that [Chroma](https://github.com/alecthomas/chroma) has heard of
* hidden blocks
* code evaluation and display of results

But it'll do for now.