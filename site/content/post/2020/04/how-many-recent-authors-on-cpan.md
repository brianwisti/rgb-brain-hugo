---
aliases:
- /note/2020/119/how-many-recent-authors-on-cpan/
- /note/2020/04/how-many-recent-authors-on-cpan/
category: note
created: 2024-01-15 15:26:27-08:00
date: 2020-04-28 11:40:00-07:00
slug: how-many-recent-authors-on-cpan
syndication:
  mastodon: https://hackers.town/@randomgeek/104077745261496400
  twitter: https://twitter.com/brianwisti/status/1255210221124886533
tags:
- perl
- gist
title: How many recent authors on CPAN?
updated: 2024-01-26 11:02:35-08:00
---

Sorry, I couldn’t fit this in a tweet.

[Yanick](http://techblog.babyl.ca/)'s concerned about [Perl](../../../card/Perl.md)'s [CPAN](https://cpan.org).

{{\< tweet user="yenzie" id="1254874808774516738" >}}

So I grabbed the authors of the last 5,000 releases and counted authors, using [Mojolicious](https://mojolicious.org) and the [MetaCPAN](https://metacpan.org) API.

````console
$ export MCP_LATEST='https://fastapi.metacpan.org/v1/release/_search?q=status:latest&fields=author&sort=date:desc&size=5000'
$ http $MCP_LATEST > _search.json
$ perl -Mojo -E 'say c(j(f("_search.json")->slurp)->{hits}{hits}->@*)->map( sub { $_->{fields}->{author} } )->uniq->size . " authors made the last 5000 releases"'
974 authors made the last 5000 releases
````

Downloaded the file with [httPie](https://httpie.org/) because I felt bad hammering MetaCPAN with [`-Mojo g()`](https://mojolicious.org/perldoc/ojo#g) while sorting out the rest of the "one-liner."

I have no idea if these results are good or bad, but I half-expected less than 100 authors.

Getting useful information like spread of release dates is left as an exercise for the reader.