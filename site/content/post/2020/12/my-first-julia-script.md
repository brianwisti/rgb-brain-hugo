---
category: post
date: 2020-12-25 00:00:00-08:00
description: Weaving code in Hugo posts with Julia
slug: my-first-julia-script
syndication:
  mastodon: https://hackers.town/@randomgeek/105443065345953821
tags:
- julialang
- literateprogramming
- literateblogging
- site
- programming
title: My first Julia script
---

![attachments/img/2020/cover-2020-12-25.png](../../../attachments/img/2020/cover-2020-12-25.png)
Drawn with [Luxor.jl](http://juliagraphics.github.io/Luxor.jl/stable/)

Merry Christmas! I wrote a little [Julia](https://julialang.org) code.

## The inspiration

Been getting frustrated with [card/Python](../../../card/Python.md)'s type hinting system. I usually start with loose and informal code, but eventually I specify types. And when I do, I want the language to check my work. I dislike relying on an external tool like [MyPy](https://mypy.readthedocs.io/en/stable/) that runs separately.

I've also been looking at [Pandas](https://pandas.pydata.org) a lot recently for work stuff. Okay, Pandas looks interesting to my non-data science brain. I mainly use it to filter Excel files for database updates. But I can't help noticing how often the Julia programming language comes up in those posts about Data Science in Python.

So I check out Julia. It intrigues me. The type system and concurrency tools look nice, of course. But what's this? Math code that looks more like math?

````julia
julia> f(x) = √2x^2 - 5
f (generic function with 1 method)

julia> [f(x) for x in [0, 1, 2, 3]]
4-element Vector{Float64}:
 -5.0
 -3.585786437626905
  0.6568542494923806
  7.727922061357857
````

By way of contrast, this is Python's equivalent of those two lines of Julia code.

````python
from math import sqrt

def f(x):
	return sqrt(2 * x ** 2) - 5

[f(x) for x in [0, 1, 2, 3]]
````

It's similar enough that I don't feel massively disoriented. But the math stuff is just a little bit friendlier.

Time to run through the "is this language worth my time" checklist.

* Julia is [well-documented](https://docs.julialang.org/en/v1/)
* even though scientific programming is Julia's main niche, it includes a solid  base and standard library for the general-purpose utility code I write
* the [package ecosystem](https://juliapackages.com) looks healthy
* I found at least one useful-looking [Web framework](https://www.genieframework.com)
* I found at least one [high-level library](https://juliapackages.com/p/octo) to interact with assorted database
  servers
* and — of course — somebody's written a [card/Static Site Generator](../../../card/Static%20Site%20Generator.md) in Julia, called [Franklin.jl](https://franklinjl.org)

So yeah. I can poke around a little more.

I love [literate programming](http://literateprogramming.com/index.html). One of the first things I did was look to see if someone in the Julia world did too. And they do!

There's [Literate.jl](https://fredrikekre.github.io/Literate.jl/v2/), which processes Markdown and code in Julia scripts. [Weave.jl](http://weavejl.mpastell.com/stable/) is more my style, processing Julia code in Markdown files. I can write my post and weave it into an ordinary-looking Markdown file. [card/Hugo](../../../card/Hugo.md) won't have to know the difference.

## The setup

Julia treats environment and package management as core functionality. Everything I need is in [Pkg](https://docs.julialang.org/en/v1/stdlib/Pkg/). Not to pick too much on Python — it really is a great language — but its environment management options are [infamously byzantine](https://xkcd.com/1987/).

To set up a package for my existing site, I drop into the REPL's `pkg` mode.

````txt
julia> ]
````

Here I can initialize my project and add dependencies.

````
(v1.5) pkg> initialize .
(rgb-hugo-legacy)> add Weave
...
````

Now I have `Project.toml` and `Manifest.toml` files describing my Hugo site's new Julia needs. I can start writing this post.

### Writing with Weave

Write the stuff you want to write, using [Julia-flavored Markdown](https://docs.julialang.org/en/v1/stdlib/Markdown/). Any code block fenceposted with triple backticks and labeled as "julia" gets evaluated by
Weave.

Set different [chunk options](http://weavejl.mpastell.com/stable/chunk_options/) for the block if you want to tweak the code's treatment.

````
```julia; term = true
f(x) = √2x^2 - 5
[f(x) for x in [0, 1, 2, 3]]
```
````

Weave does its thing, and produces something interesting depending on what output options you use.

````
```julia
julia> f(x) = √2x^2 - 5
f (generic function with 1 method)

julia> [f(x) for x in [0, 1, 2, 3]]
4-element Array{Float64,1}:
-5.0
-3.585786437626905
0.6568542494923806
7.727922061357857
```
````

## The script

AKA the point of this blog post. It looks in my content folder for recently modified `.jmd` files. Anything found gets handed off to `weave`, which does the hard work. Heck, `weave` even has a `hugo` option so I can generate Markdown specifically formatted to satisfy Hugo.

````julia
using Logging

using Weave

const content_folder = "content"
const weave_extensions = [".jmd"]

function main()
    weave_files = []
    @debug "content is in $content_folder"

    for (root, dirs, files) in walkdir(content_folder)
        for file in files
            ext = splitext(file)[2]

            if ext in weave_extensions
                weave_file = joinpath(root, file)
                @debug "Found weave file" weave_file
                target_file = joinpath(dirname(weave_file), "index.md")

                if isfile(target_file) && mtime(weave_file) >= mtime(target_file)
                    push!(weave_files, weave_file)
                end
            end
        end
    end

    @info "Weave-able files found:" weave_files

    for weave_file in weave_files
        @info "Weaving" weave_file
        weave(weave_file; out_path=:doc, doctype="hugo")
    end
    @info "Done?"
end

main()
````

This is probably not idiomatic Julia. Maybe it'll get there when I learn what idiomatic Julia even looks like.

Obviously there's no error handlng of any kind. That can come later.

A few things I noticed:

* functions like `walkdir` end up making the flow look a bit like Python
* I kept making my code more complicated than it needed to be, when both Julia and Weave were ready with reasonable defaults
* especially in regard to types; everything works fine without specifying  details; I can find out what happens when I add details later

````
❯ just weave
julia --project=. scripts/weave-content.jl
┌ Info: Files that need weaving:
│   weave_files =
│    1-element Array{Any,1}:
└     "content/post/2020/12/my-first-julia-script/index.jmd"
┌ Info: Weaving
└   weave_file = "content/post/2020/12/my-first-julia-script/index.jmd"
┌ Info: Weaving chunk 1 from line 45
└   progress = 0.0
┌ Info: Weaving chunk 2 from line 163
└   progress = 0.3333333333333333
┌ Info: Weaving chunk 3 from line 249
└   progress = 0.6666666666666666
┌ Info: Weaved all chunks
└   progress = 1
[ Info: Weaved to /home/random/Sites/rgb-hugo-legacy/content/post/2020/12/my-first-julia-script/index.md
[ Info: Done?
````

Okay. That's great. I mean — all that so I could do a little math, but whatever.

## That's it?

Hey. Maybe we could do something cool. Make a cover image for this post with [Luxor](http://juliagraphics.github.io/Luxor.jl/stable/).

Let's try it out. I'll borrow heavily from the Luxor manual since I don't really know what I'm doing,

````julia
using Colors
using Luxor

function draw(x, y)
    foregroundcolors = Colors.diverging_palette(rand(0:360), rand(0:360), 200, s = 0.99, b=0.8)
    gsave()
    translate(x-100, y-150)
    julialogo(action=:clip)

    for i in 1:500
        sethue(foregroundcolors[rand(1:end)])
        circle(rand(-50:350), rand(0:300), 15, :fillstroke)
    end

    clipreset()
    sethue("black")
    julialogo(action=:stroke)
    translate(x-125, y+150)
    spiral(100, -1, period=20π, :stroke)
    grestore()
end

currentwidth = 850
currentheight = 500
Drawing(currentwidth, currentheight, "cover.png")
origin()
background("white")
setopacity(.4)
scale(1.5)
draw(0, 0)
finish()
````

 > 
 > **NOTE**
>
 > First off, PNG format works better than SVG when you're drawing 500 random circles.
 > 
 > ````shell
 > ❯ exa -l content/post/2020/12/my-first-julia-script/cover*
 > .rw-r--r--  99k random 25 Dec 12:42 cover.png
 > .rw-r--r-- 4.8M random 25 Dec 12:37 cover.svg
 > ````
 > 
 > Second, I added an `eval = false` chunk option after the image was good enough. No point regenerating the cover every time I fix a typo.

That's enough writing about writing with Julia. I have a couple other drafts I want to revisit now.

Besides, it's Christmas! Christmas 2020. Which means my only regret is forgetting to order Christmas-themed face masks.