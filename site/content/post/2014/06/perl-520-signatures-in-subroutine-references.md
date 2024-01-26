---
aliases:
- /programming/2014/06/25_perl-subref-signatures.html
- /post/2014/perl-subref-signatures/
- /2014/06/25/perl-5.20-signatures-in-subroutine-references/
category: post
date: 2014-06-25 00:00:00-07:00
slug: perl-520-signatures-in-subroutine-references
tags:
- perl
- programming
title: Perl 5.20 Signatures in Subroutine References
created: 2024-01-15T15:25:28-08:00
updated: 2024-01-26T10:11:42-08:00
---

[Perl](../../../card/Perl.md) 5.20 has experimental support for function signatures. That's  good news. I just thought to check if signatures can be used in subroutine references. They can.

<!--more-->


````perl
# Set a base set of features.
use 5.20.0;

# Signatures are experimental, so are not enabled by default.
use feature 'signatures';

# Otherwise Perl will warn about using the experimental feature
no warnings 'experimental::signatures';

sub hello($person) {
  say "Hello, $person";
}

my $goodbye = sub($person) {
  say "Goodbye, $person";
};

my $me = "Brian";

hello( $me );
$goodbye->( $me );
````

It's a simple test. Just checking to see if I can maybe use this feature in my own projects.

````console
$ perl sig-test.pl
Hello, Brian
Goodbye, Brian
````

This pleases me. It's not going to make life easier for [Pygments](http://pygments.org/), though.
