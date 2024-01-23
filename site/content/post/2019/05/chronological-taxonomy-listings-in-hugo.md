---
aliases:
- /2019/05/20/chronological-taxonomy-listings-in-hugo/
category: post
date: 2019-05-20 00:00:00-07:00
slug: chronological-taxonomy-listings-in-hugo
syndication:
  mastodon: https://hackers.town/@randomgeek/102132792782409820
  twitter: https://twitter.com/brianwisti/status/1130733283384410112
tags:
- site
- hugo
- tools
title: Chronological Taxonomy Listings in Hugo
---

The archive pages now list tags and categories such that the ones with most recent posts come first!

That may not sound impressive or even necessary. [card/Hugo](../../../card/Hugo.md)’s normal [taxonomy](https://gohugo.io/variables/taxonomy/) ordering `.Data.Terms.ByCount` and `.Data.Terms.Alphabetical` are sufficient for normal cases, and taxonomy detail pages already present their posts in a reverse chronology.

This site isn’t *quite* a normal case. The Random Geekery Blog is almost six years  old, and includes archived content from other sites dating back to 2000. My many obsessions have waxed and waned over the years. Presenting tags by name or by number of posts means we must dig to find out what’s relevant to me lately. I find that frustrating because of the way my brain holds information: fresh topics are near the top, and older stuff is somewhere down below when I need it.

After the traditional grumbling about how this would be a two minute task with Perl, I set to the task of figuring it out. Let’s skip the bits where I messed around with `$.Scratch` and get straight to what worked in `layout/_default/terms.html`.

First, I built a list of relevant information by stepping through the terms of that particular taxonomy. For each tag, category, or whatever, [convert](https://gohugo.io/functions/unix/) the publishing date of the most recent post with that tag (or category, or whatever) to a `.Unix` timestamp.  Create a [dict](https://gohugo.io/functions/dict/) with the term and its associated timestamp, then [append](https://gohugo.io/functions/append/) it to a [slice](https://gohugo.io/functions/slice/).

````text
{{- $stamped_terms := slice -}}
{{- range $term, $value := .Data.Terms -}}
  {{- $last_stamp := (index $value.Pages.ByDate.Reverse 0).Date.Unix -}}
  {{- $term_stamp := dict "term" $term "stamp" $last_stamp -}}
  {{- $stamped_terms = $stamped_terms | append $term_stamp -}}
{{- end -}}
````

Momentarily setting aside concerns for [falsehoods programmers believe about UNIX time](https://alexwlchan.net/2019/05/falsehoods-programmers-believe-about-unix-time/), I have a list of terms and their freshest post’s timestamp. Leap seconds probably won’t be an issue here.

````text
map[stamp:1143504000 term:43-things]
...
map[stamp:1526515200 term:zentangle]
````

I [sort](https://gohugo.io/functions/sort/) that list based on the timestamp, in descending order. Grab the term
from the `dict` and then it’s pretty much the same taxonomy summary I had
before.

````text
<dl>
 {{ range $stamp := sort $stamped_terms "stamp" "desc" -}}
   {{- $key := index $stamp "term" -}}
   {{- $value := index $.Data.Terms $key -}}
   <dt>
     <a href="/{{ $.Data.Plural | urlize }}/{{ $key | urlize }}/">{{ $key }}</a>
   </dt>
   <dd>
     {{- $first_post := index $value.Pages.ByDate 0 -}}
     {{ if eq $value.Count 1 }}
       Includes 1 post from {{ $first_post.Date.Format $.Site.Params.DateForm }}
     {{ else }}
       {{- $last_post := index $value.Pages.ByDate.Reverse 0 -}}
       Includes {{ $value.Count }} posts from
       {{ $first_post.Date.Format $.Site.Params.DateForm }}
       to
       {{ $last_post.Date.Format $.Site.Params.DateForm }}
     {{ end }}
   </dd>
 {{ end }}
</dl>
````

And that’s pretty much it! Had to post in case I needed this information later.
