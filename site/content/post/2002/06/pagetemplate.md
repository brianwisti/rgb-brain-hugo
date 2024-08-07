---
aliases:
- /coolnamehere/2002/06/02_pagetemplate.html
- /post/2002/pagetemplate/
- /2002/06/02/pagetemplate/
category: post
created: 2024-01-15 15:26:18-08:00
date: 2002-06-02 00:00:00-07:00
slug: pagetemplate
tags:
- pagetemplate
- coolnamehere
title: PageTemplate
updated: 2024-02-01 20:34:41-08:00
---

> 
 > **WARNING**
>
 > Haven't touched PageTemplate in ages. This stuff is only here for the historical record.

## Introduction

PageTemplate was a [Ruby](../../../card/Ruby.md) package which allowed you to utilize text templates for your Web projects. It was mainly intended for use in a CGI environment, but designed to be helpful in a broad range of similar applications. It was inspired by, yet almost entirely unlike, the [HTML::Template](http://html-template.sourceforge.net/) package available for Perl. It has many features in common with other templating engines:

* Variable substitution
* “if/else” blocks - inserting chunks of content depending on the existence of a flag variable
* “loop/no” blocks - repeatedly inserting a chunk of content, using values from a list
* Simple default syntax - *I hope it’s simple*

It also has a few features of its own (otherwise, where’s the fun?).

* Ruby-style access to fields and methods of objects
* Preprocessors to alter formatting of variables
* Support for defining values inside template
* Our Loops Are Crazy Fun:
  * Iteration over multiple loop variables
  * Named loop variables for easy-to-read object access
  * Loop meta-variables to simplify things like formatting alternate rows
* Customizable markup syntax to simplify integration with your own tools
  * Included `HTGlossary` for HTML::Template style syntax
* Cached templates for faster output

More features were planned, such as support for localization to allow native-language markup. But life had other demands, and I never did get back to PageTemplate.

Let's go back to 2002 present-tense verb usage while I decide what to do with these pages.

## What PageTemplate Is Not

* It’s not a programming language. If you want a programming language for your Web pages, try [PHP](../../../card/PHP.md)
* It’s not a tool for embedding Ruby code into your Web pages. [ERB](http://ruby-doc.org/stdlib-2.4.1/libdoc/erb/rdoc/ERB.html) already does a fine job of that.
* It is *definitely* not XML. PageTemplate serves a much narrower field. If you want to use Ruby with XML, there are [excellent resources](http://www.rubyxml.org/) for that.
* PageTemplate is a personal project, which means that it’s not a commercial product. As much as I hope that it’s functional and stable on your computer, I can’t make any promises. If installing PageTemplate levels New Jersey, there’s nothing I can do about it. This is my version of the standard “no warranty” warranty.
* Last but not least, PageTemplate is not HTML::Template. HTML::Template has been growing and evolving for years, while PageTemplate was the result of a week alone with 5 pounds of coffee. Things have improved, but PT still suffers from the fact that it’s written and supported by two guys in their ever-dwindling spare time.

## Motivation

Brian has been a fan of Perl’s HTML::Template package for a long time, and he missed its robust usefulness whenever using a language that isn’t Perl. After delving deeper into other languages, he thought it might be fun to make some of that utility available in [Ruby](/tags/ruby/). It would give Brian a decent-sized personal project, which would stretch his skills with project development and unit testing. Plus, if a templating system was available, maybe he wouldn’t miss Perl so badly.

So those were the primary motivations: personal education and homesickness.

Once the code started taking shape, though, he decided that he wanted this to be useful for other people. “Download and use” kind of useful. Greg Millam found PageTemplate to be *so* useful that he opted to join in the development process and add loads of new features. PageTemplate has continued to be used by a small but apparently loyal group of people, despite Brian and Greg’s periodic hibernation. The continued contributions of Greg Millam have made PageTemplate a powerful tool for Web development rather than the mild distraction it started out as.

## Using PageTemplate

First, you’ll want to [download and install](../07/pagetemplate-getting-it.md) the latest version of PageTemplate. Then, [designers](pagetemplate-the-designers-perspective.md) will make templates, [programmers](pagetemplate-the-programmers-perspective.md) will write code, and some of us will do both. Eventually, you will probably get tired of the default syntax, and want to make your own. If you’re an especially geeky sort of person, you’ll no doubt want to look at the source for lasses and methods that are available in the PageTemplate package.

Most importantly, *enjoy yourself!* PageTemplate is supposed to be good geeky fun, not hard work with lots of sweat and turmoil!

## Users

I would love to hear about what you’ve done with PageTemplate. Until then, I’ll be forced to look PageTemplate up on Google and see what I find:

* [A Web-based library consult service for evidence-based medicine](http://www.pubmedcentral.nih.gov/articlerender.fcgi?artid=1484475)
  * We’re mentioned a ways down there, but they are using PageTemplate. If you have the keen eye required to read names in big letters near the top of the page, you’ll notice Greg was part of this team.
* [Weft QDA](http://www.pressure.to/qda/) - Text analysis? Sounds impressive. I’m guessing PageTemplate gets used for exporting to HTML.
* PageTemplate also seems to be available on a lot of Web hosts out there via RubyGems. I don’t know if it is *used*, but at least it’s available.

## The License

PageTemplate is distributed under The MIT License, which is detailed below.

### The MIT License

Copyright (c) 2002-2006 Brian Wisti, Greg Millam

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Changelog

* Version 1.0
  * Basic logic structure (var, if, and in)
  * Support for multiple Namespaces
* Version 1.1
  * include content from external files
* Version 1.2
  * New Command: unless
  * Added support for CommentCommands
  * Loop Metavariables: `FIRST`, `LAST`, `ODD`
  * include\_path can be a list of paths
  * Loosened rules for VariableCommands (check respond\_to? rather
    than has\_method?)
  * Lessened penalty for missing files in IncludeCommands (returns
    an error string rather than raising an exception)
  * Strengthened the system for running in tainted environments.
* Version 2.0
  * Added Preprocessors
    * `[%var sampleCode :escapeHTML %]`
  * Added a CaseCommand
  * Better access of object fields and subfields
* Version 2.1
  * LoopCommands can accept multiple iterators now
  * Added else if functionality
  * New Glossary allows HTML::Template-style syntax.
* Version 2.1.1
  * In-memory caching
* Version 2.1.5
  * Improvements on working with `mod_ruby`
* Version 2.1.7
  * Added Namespace\#delete method
* Version 2.2.0
  * DefineCommand
  * FilterCommand
  * Fixed bug in FileSource\#get\_filename