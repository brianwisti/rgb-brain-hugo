---
aliases:
- /note/2021/05/statamix-xml-handler-rss/
category: note
created: 2024-01-15 15:26:11-08:00
date: 2021-05-08 00:00:00-07:00
slug: statamic-xml-handler-rss
tags:
- site
- statamic
- i-fixed-it
title: 'So here''s my first Statamic tip: don''t forget xml_handler in your RSS template'
updated: 2024-01-26 10:21:50-08:00
---

<blockquote class="twitter-tweet"><p lang="en" dir="ltr"><a href="https://twitter.com/brianwisti?ref_src=twsrc%5Etfw">@brianwisti</a> what&#39;s the proper way to subscribe to <a href="https://t.co/6QUV8FCUgL">https://t.co/6QUV8FCUgL</a> now? Not finding an RSS.</p>&mdash; Captain Macho Pirate Mick Rackam (@tw2113) <a href="https://twitter.com/tw2113/status/1390887717261561857?ref_src=twsrc%5Etfw">May 8, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Yeah, the link was at `/index.xml`, but [Statamic](../../../card/Statamic.md) wasn't outputting valid XML until I replaced my raw `<?xml` with the `xml_handler` tag:

````
{{ xml_handler }}
````

Should be all better now. Or at least better than it was.