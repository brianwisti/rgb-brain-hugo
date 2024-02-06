---
aliases:
- /2018/02/17/my-sloppy-floppy-fingerless-mitten/
category: post
created: 2024-01-15 15:26:13-08:00
date: 2018-02-17 00:00:00-08:00
slug: my-sloppy-floppy-fingerless-mitten
tags:
- knitting
- glove
- hugo
- craft
title: My Sloppy Floppy Fingerless Mitten
updated: 2024-02-01 20:27:47-08:00
---

I knit a fingerless mitten. Mistakes were made. I also figured out some stuff about Hugo Page Bundles and image processing.

<!--more-->

![attachments/img/2018/cover-2018-02-17.jpg](../../../attachments/img/2018/cover-2018-02-17.jpg)

I modified a mitten pattern from [Knitter's Handy Book of Patterns](https://www.goodreads.com/book/show/85015.Knitters_Handy_Book_Of_Patterns?from_search=true). The book's template approach works for me. I adjusted the pattern for fingerless mittens — my preference.

I will knit the mittens again, making additional adjustments.

* Cast on fewer stitches. I prefer less ease in my gloves.
* Stop an inch shorter on the upper part of the hand. Cover the knuckles, and no more.
* Knock at least four stitches off the thumb gusset.

It isn't all negative. I kept consistent gauge, and the [stretchy bind off](https://www.thespruce.com/stretchy-bind-off-stich-knitting-tutorial-2115677) stayed stretchy.

## Hugo?

I wrote this post to learn [image processing](https://gohugo.io/content-management/image-processing/) in [Hugo](../../../card/Hugo.md) 0.36. My suggestion: follow the documentation, especially where it says to name your content file `index.md`.

Maybe I can say a little more about that. I'll just focus on the bits relevant to [Page Resources](https://gohugo.io/content-management/page-resources/), since the rest of it is specific to the details of my site.

Up until today my site images relied on a Python script to generate post cover images and thumbnails from master images in `static/`. Hugo 0.36 can now create those images itself, but you have to organize your content and its images correctly.

### Post organization

Instead of a single file, your post becomes a directory, with `index.md` for the content itself.

````
content
+-> craft
  +-> 2018
    +-> my-sloppy-floppy-fingerless-mitten
      +-> index.md
      +-> cover.jpg
````

### Templates

Posts might have a primary images, which Hugo displays at the top of the post itself, and as a thumbnail in summary pages. I named the image `cover.jpg`.

#### Cover Image

If I have a cover image, Hugo's image processing creates a version of the image 800 pixels wide. Display this image, along with a link to the original.

````
{{- $description := .Title -}}
{{- $coverImage := .Page.Resources.GetMatch "cover*" -}}
{{- if $coverImage -}}
  {{- $image := $coverImage.Resize "800x" -}}
  <figure>
    <img src="{{ $image.RelPermalink }}" alt="{{ $description }}"
         height="{{ $image.Height }}" width="{{ $image.Width }}">
    <figcaption>
      {{ $description }}<br>
      <a href="{{ $coverImage.RelPermalink }}" target="_blank">
        (see full size in new window)
      </a>
    </figcaption>
  </figure>
{{- else -}}
  legacy cover image handling
{{- end -}}
````

#### Thumbnail

If I have a cover image, I create 128 pixel square [smart crop](https://gohugo.io/content-management/image-processing/#smart-cropping-of-images) — a thumbnail which should show the original's most interesting part. The thumbnail is presented along with a link to the post itself.

````
{{ $title := .Title }}
{{- $coverImage := .Page.Resources.GetMatch "cover*" -}}
{{- if $coverImage -}}
  {{- $thumbnail := $coverImage.Fill "128x128" -}}
  <a href="{{ .Permalink }}" title="{{ $title }}">
    <img class="summary-thumbnail"
         src="{{ $thumbnail.RelPermalink }}"
         alt="{{ $title }}"
         height="{{ $thumbnail.Height }}"
         width="{{ $thumbnail.Width }}">
  </a>
{{- else -}}
  legacy thumbnail handling
{{- end -}}
````

### Conclusion

This flow replaces my Python image script and a fair amount of templating logic. Once I remove the legacy templating logic, I'll put the cover image and thumbnail dimensions in site config, making it easier to redesign page layout later.

I better get to it.