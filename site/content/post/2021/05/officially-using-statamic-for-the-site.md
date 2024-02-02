---
category: post
date: 2021-05-07 00:00:00-07:00
description: Hugo's fine but I needed to try something new
slug: officially-using-statamic-for-the-site
syndication:
  mastodon: https://hackers.town/@randomgeek/106198056018245380
  twitter: https://twitter.com/brianwisti/status/1390910408601608192
tags:
- site
- statamic
- cause-it-s-there
- my-brand
- oooh-a-sparkly
title: Officially Using Statamic For The Site
created: 2024-01-15T15:26:11-08:00
updated: 2024-02-01T20:32:42-08:00
---

![attachments/img/2021/cover-2021-05-07.png](../../../attachments/img/2021/cover-2021-05-07.png)
Hey look it's a Web page, but with Statamic!

Got the [Webmention](https://webmention.io) pingbacks up.  Got the [Plausible](https://plausible.io) token in place.  Got server configuration and deployment working.

Got — server configuration?  Well yeah.  The [Statamic](../../../card/Statamic.md) CMS runs on [PHP](../../../card/PHP.md).  I *could* generate and push a static site with it, but I want to try some [Laravel](../../../card/Laravel.md) stuff.  Been watching [Laracasts](https://laracasts.com/) even.

## What’s different?

The visual style, obviously.  But I cycle through those routinely.  This one’s [PaperCSS](https://www.getpapercss.com/) with a few tweaks.

I added a new section for my art — specifically for the art you can buy somewhere.  That’s been on my task list for a long time.  Feels nice to get it out of the way.  I have a sizable backlog of stuff I wanted to put on my [store](https://www.designbyhumans.com/shop/randomgeek/).  That art section will remind me to get through that backlog a bit more quickly.

You can search! Just by title or tag for now, but I’ll add more as I figure out how to fine tune it. And because you can search, I’m not *as* worried about how pagination is handled. I’m sure I’ll add something later.

And also because you can search, I haven’t gotten to the page aliases yet. Lots of broken inbound links, I expect. If this were some kind of professional site, I would’ve waited until I had those in place. But it’s not. So I don’t.

## Anything else?

From your perspective, that’s about it.  It’s pretty much the same site.

From my perspective, so much!  I get an awesome control panel to manage and edit content.  All my pages are still in flat text files, so I can edit them in my favorite text editor with no fuss.

Okay that’s not new for the site.  It’s new compared to when I tried this with WordPress though.

## What’s different from stock Statamic Solo?

The styling is set up with [SASS](https://sass-lang.com/) instead of the starter’s default of [Tailwind](https://tailwindcss.com/).  Probably shift back once I figure out an approach to content styling that I prefer to Tailwind Prose.

I don’t entirely trust server-side for a blog.  Nothing to do with Statamic or PHP mind you.  It’s just too easy to miss important details when you’re running a solo project.

With that in mind, I added [2FA](https://statamic.com/addons/jrc9designstudio/2fa) for two factor authentication and [Gitamic](https://statamic.com/addons/simonhamp/gitamic) for Git integration.  Both are paid add-ons.  Much as I love open source software, I love knowing that good developers get a good dinner even more.  Sponsorship and patronage only go so far — on my monthly budget, at least.

## What’s next?

There’s still some basic deployment stuff to figure out.  Metadata for sharing, or what the boring kids call "SEO." Ugh.  I ain’t optimizing *nothin’*, least of all some search engine’s job.

Anyways.  Then comes automating the non-RSS syndication: posting toots and tweets when I hit "Publish." Until I get that code in it’s manual, so I’ll probably skip those for my notes.

After that?  Watch Laracasts.  Learn Laravel.  Learn Statamic.  Have fun.
