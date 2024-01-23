---
aliases:
- /blogspot/2007/12/29_now-that-both-of-my-machines-are.html
- /post/2007/now-that-both-of-my-machines-are/
- /2007/12/29/dv9310-bios-issues/
category: post
date: 2007-12-29 00:00:00-08:00
slug: dv9310-bios-issues
tags:
- i-fixed-it
- blogspot
title: dv9310 bios issues
---

I turned an offhand comment about how I fixed my problem into more of a step-by-step guide, in case some poor soul is in the same spot and finds me via Google.

Now that both of my machines are healing again - did I mention that a BIOS update flattened my HP dv9310? Oh, it flattened my HP all right. The new one effectively  makes the computer forget that it has a video card. If you do an update and the machine starts spontaneously rebooting, try this:

1. Boot into Safe Mode
1. Go to your Device Manager and disable the NVidia card. It's okay, you'll still have normal VGA.
1. Reboot in normal mode.
1. Go to the HP support site and download an older BIOS version.
1. Install that older BIOS.
1. Reboot.
1. Go to your Device Manager and re-enable the NVidia card.</li>

Everything should be okay now.

Anyways, the machines are reconfigured, I've sparked my brain with a little Python code, and now I can get back to a Perl project that's been waiting over a month.
