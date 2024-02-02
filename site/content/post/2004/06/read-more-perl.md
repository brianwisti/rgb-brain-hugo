---
aliases:
- /coolnamehere/2004/06/05_read-more-perl.html
- /post/2004/read-more-perl/
category: post
date: 2004-06-05 00:00:00-07:00
slug: read-more-perl
tags:
- perl
- coolnamehere
title: Read More Perl
created: 2024-01-15T15:26:15-08:00
updated: 2024-02-01T20:42:57-08:00
---

This was originally a [meditation](http://perlmonks.org/?node_id=349236) on [Perl](../../../card/Perl.md) that I wrote at wrote at [Perlmonks](http://perlmonks.org). 

<!--more-->

Make no mistake about it. Perl code has a reputation for being ugly and hard to maintain. This reputation has been earned by years of programmers hacking out the code that gets the job done. There isn't anything wrong with this. You don't need to use double spacing, one inch margins, and a grammar checker if you are making a laundry list. The problem is that your Perl laundry list may continue to be used and referred to for months or years to come.

It doesn't have to be like that. People who really know Perl understand that it is a very expressive language. Perl can be used to state your thoughts cleanly and clearly. The same language that is used to make a laundry list is also used to make "The Catcher in the Rye". Some folks write poetry in Perl, for crying out loud! I usually aim for more of a "Green Eggs and Ham" kind of vibe, but maybe that's just me.

This meditation is intended to provide a few straightforward hints and habits to bear in mind in the quest to make Perl readable. They aren't solid rules, and I honestly don't follow them all the time myself. That's really why I'm writing this article: to remind myself that I can make my life easier by exposing myself to code that is already out there in the big wide world.

So without further ado ...

## Read About Common Guidelines.

`perldoc perlstyle` is a good starting point for questions of code style and legibility. It's as close as we get to an official declaration of what good Perl might look like, although Larry Wall would probably never be so bold as to state that this is what good Perl *should* look like. As benevolent dictators go, he ranks as much more casual than the average. Still, keep the `perlstyle` guidelines in mind, and most people will be able to read what you write and have a good idea what your intent is.

"Regular" languages are good for more than a source of analogy and comparison. The single most useful programming book I have read in the last three years is Strunk and White's "Elements of Style". It has a lot of good common sense guidelines related to communicating with the written word. Perl (along with the other very high level languages) is still the written word, despite all the numbers and funny symbols.

## Read Other People's Code.

Do you want to learn how to write code with good style? You want to look at as many samples of code as possible. Not just the good stuff, either. Look at good code, look at bad code, look at deliberately obfuscated code. Look at code written by deranged mutant gerbils from Dimension X. You need to understand *why* bad code is considered bad code. You also need to get past the urge to perceive *all* Perl code as bad code. I honestly believe that the only reason people consider Perl unreadable is the fact that they haven't sat down and read enough of it. Written English was confusing and bizarre to me when I was a child. *("I before E, except after C. What about 'weird'?")* Okay, it's still a little bizarre to me, despite the fact that it is my native tongue. Now, though, I understand more of the subtleties that can be expressed with the right combination of vocabulary, expression, and context.

Perl is the same way. Learn the language. Read it like you would read a book or a magazine. You will get a better idea why most of us are told to use strict. At the same time you'll see why some people complain about how strict just gets in their way, and the steps they take to make assurances that their code is clean and solid.

Except, you know, when they don't want it to be clean at all. We call that "art".

## Read Your Own Code.

It isn't as silly as it sounds. You want to revisit your code for a few reasons. First, you will be able to see what you've learned since the last time you saved that file. Second, it will encourage you to write cleaner code, because you know that you will be looking at it again. Third, it gets you ready for the next good habit.

## Let Others Read Your Code.

This is scary, and the hardest advice for me to follow. I get attached to my code, and feel a sense of ownership. "This is mine, and I don't want somebody else telling me what's wrong with it." You know what, though? I need to get over it, and so do any of you that share my delicate geek ego. The fastest way to learn what you're doing wrong is to get a fresh set of eyes on your code. For that matter, it's also the best way to get an honest appraisal of what you're doing right.

I'm not telling you to go out and start pair programming. It might not be a bad idea, but it's not the same as what I'm suggesting. Most of these habits don't relate to methodologies for building software. They are about looking at code as language or literature. Again: the best argument against "Perl is unreadable" is to spend more time reading it.

## Wrapping it up.

People complain constantly about the readability of Perl code. I think that this can be fixed by reading more Perl code to get a better understanding of Perl as a language (as opposed to Perl as a notation for expressing algorithms). There is definitely more to cover (`perldoc`, CPAN, etcetera), but I think that the simple act of reading can do a lot to enhance both the readability of what you produce and your appreciation for what can be written in this language.
