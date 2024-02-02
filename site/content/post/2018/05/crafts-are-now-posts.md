---
aliases:
- /2018/05/26/crafts-are-now-posts/
category: post
date: 2018-05-26 00:00:00-07:00
slug: crafts-are-now-posts
tags:
- site
- ruby
- hugo
- programming
title: Crafts Are Now Posts
created: 2024-01-15T15:26:53-08:00
updated: 2024-02-01T22:12:22-08:00
---

I turned the craft section into a Craft category — then a tag years later. Drawing, Knitting, and Crochet became tags. The rest of this post is just notes about that.

<!--more-->

## Why?

I want to improve the organization of my site content.

I created the *Crafting* pages in 2015 as a [Jekyll collection](../../2015/07/making-a-jekyll-collection.md). This kept them out of the site RSS feed, which made sense to me at the time. Craft pages were nothing like posts.

[Switching to Hugo](../../2015/09/next-hugo.md) resulted in turning the Jekyll collection into its own section, with a layout that prominently featured an image of the finished project. I liked the layout so much that I incorporated it into posts. The only differences between craft and post content were their URLs and the folders I saved them in.

During my attempts to get Disqus working here, I changed the [permalink](http://gohugo.io/content-management/urls/#permalinks) configuration to something more blog-like — `/:year/:month/:day/:title` — scrubbing section out of the permalink as I slowly admitted to myself there was little to distinguish crafts and posts.

I finally abandoned Disqus — and Google Analytics — to prevent anyone tracking my site visitors. I was GDPR compliant before it was cool!

I complete the last step of this process today: transforming craft content into post content, and updating site configuration to handle this change.

## How?

How much craft content will I need to migrate?

````console
$ find content/craft/ -name '*.md' | wc -l
51
````

51 items is not bad, but it is more than I want to update manually. Time for a little code. Today I choose [Ruby](../../../card/Ruby.md).

### Transform front matter in Craft content

The plan is to transform craft content [front matter](http://gohugo.io/content-management/front-matter/) for craft content, then manually move everything into `content/post`.

Here are the basic changes I need to make:

For every markdown file in `content/craft`:

* Category becomes "craft"
* Former category ("knitting", "drawing", "crochet") becomes first tag.
* Oops I have some word case inconsistencies ("Knitting", "knitting"). Fix those.
* Rewrite the file with the new front matter.

I use [YAML](../../../card/YAML.md) for front matter. Ruby includes a [core library](http://ruby-doc.org/stdlib-2.5.1/libdoc/yaml/rdoc/YAML.html) for handling YAML. [Find.find](http://ruby-doc.org/stdlib-2.5.1/libdoc/find/rdoc/Find.html#method-c-find) helps me find the markdown content files. This means I do not need to install extra libraries!

````ruby{title="migrate-craft.rb"}
require 'find'
require 'yaml'

CRAFT_DIR = 'content/craft'

Find.find(CRAFT_DIR) do |path|
  # Rule out everything but markdown files
  next unless FileTest.file? path

  next unless File.extname(path) == ".md"

  # Load front matter and content
  fence_count = 0
  front_matter_text = ''
  content_text = ''

  File.open(path).each_line do |line|
    if line.chomp == '---'
      fence_count += 1
    end

    if fence_count == 1
      front_matter_text += line
    else
      content_text += line
    end
  end

  front_matter = YAML.load front_matter_text

  # category becomes a tag
  old_category = front_matter['categories'][0].downcase
  front_matter['tags'].prepend old_category

  # craft becomes the new category
  front_matter['categories'][0] = 'craft'

  File.open(path, 'w') do |f|
    f.puts front_matter.to_yaml
    f.puts content_text
  end
end
````

I run it and add changes with `-p` to double check the output. It worked!

````console
$ ruby migrate-craft.rb
$ git add -p
$ git commit -m 'Craft section front matter shift to craft category'
````

Really, that's all the Ruby we need. The rest is dealing with git and other details manually.

I must specify that "craft" is an active category, since some categories represent archives that I do not want on the main navigation menu.

````json{title="config.json"}
  "Params": {
    "activeCategories": [
      "craft",
      "marginalia",
      "programming",
      "tools"
    ]
  }
````

### Move page bundles to content/post

Next I want to move content files from `content/craft` to `content/post`. You could do this sort of thing from the command line, but I just used [GNOME Files](https://wiki.gnome.org/Apps/Files).

I tell Git to delete the missing files with `git rm -r content/craft` then add the moved files under `content/post`.

Right. Let's see how this builds.

````console
$ hugo server -D
Building sites … ERROR 2018/05/25 20:31:05 error processing shortcode "_internal/shortcodes/ref.html" for page
"post/2018/interviewed-about-facebook/index.md": template: _internal/shortcodes/ref.html:1:73: executing
"_internal/shortcodes/ref.html" at <ref .Page (.Get 0)>: error calling ref: No page found with path or logical
name "craft/2018/my-new-boy-beanie/index.md".
ERROR 2018/05/25 20:31:05 error processing shortcode "_internal/shortcodes/ref.html" for page
"post/2018/my-new-boy-beanie/index.md": template: _internal/shortcodes/ref.html:1:73: executing
"_internal/shortcodes/ref.html" at <ref .Page (.Get 0)>: error calling ref: No page found with path or logical
name "craft/2018/a-couple-crochet-hats/index.md".
Total in 1039 ms
Error: Error building site: logged 2 error(s)
````

Oops. Fix the [`ref`](http://gohugo.io/content-management/shortcodes/#ref-and-relref) shortcodes in my content.

### Handle section, category, and tag details

Anyways, the last little bit is just tidying. Move the old knitting, crochet, and drawing category branch bundles to corresponding tag folders.

## Done?

I probably forgot something, but everything seems to work correctly.
