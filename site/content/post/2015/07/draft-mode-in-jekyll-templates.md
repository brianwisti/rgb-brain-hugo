---
aliases:
- /tools/2015/07/20_draft-mode-in-jekyll-templates.html
- /post/2015/draft-mode-in-jekyll-templates/
- /2015/07/20/draft-mode-in-jekyll-templates/
category: post
date: 2015-07-20 00:00:00-07:00
description: |
  Use site.show_drafts in your template to keep site development from cluttering analytics
slug: draft-mode-in-jekyll-templates
syndication:
  twitter: https://twitter.com/brianwisti/status/623300128145715201
tags:
- jekyll
- tools
title: Draft Mode in Jekyll Templates
---


 > 
 > \[!NOTE\] [tldr](../../../card/tldr.md)
 > Use `site.show_drafts` in templates if the local and live versions of your [Jekyll](../../../card/Jekyll.md) site need to be different.

Yesterday I published a post about [Jekyll collections](making-a-jekyll-collection.md).  Today I checked [Google Analytics](http://www.google.com/analytics/) to see if anybody looked at my site. 99 visits! Hey, nice. But I also noticed several "localhost" entries: those times I was double-checking my page locally with `jekyll serve -Dw` counted as visits, because the browser saw the analytics code and dutifully notified Google's servers. So - less than 99 visits to my site. Oh well.

At some point I may disconnect Analytics altogether and go back to analyzing server logs directly. That certainly solves the localhost entries. Today I only want to adjust Jekyll's build process so that it skips analytics code when building drafts.

Turns out that the [configuration documentation](http://jekyllrb.com/docs/configuration/) lists `show_drafts: null` down there in the default configuration. I only needed an `unless` block in my template.

````handlebars
{% unless site.show_drafts %}
  {% include analytics.html %}
{% endunless %}
````

I added a similar block for comments, since [Disqus](https://disqus.com/) handles those -  another external service I don't need in draft mode.

You may need something more elaborate than this for your needs, such as  ad code for a live site and a placeholder image when building drafts. No matter what the details, `site.show_drafts` provides the key that you need.
