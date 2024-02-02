---
created: 2024-01-26 17:56:20-08:00
tags:
- process
title: Getting Usable Browser Scrollbars
updated: 2024-01-26 18:03:24-08:00
---

Pencil-thin scrollbars. I hate 'em.  I can't escape them either.

But I can put some *CSS* on my site and my Chromium-based browser will at least give me sidebars my old eyes can see on my own site.

Started directly from looking at the style rules on https://pinafore.social but there's some relevant links below.

````scss
body {
    &::-webkit-scrollbar {
        width: var(--scrollbar-width);
        height: var(--scrollbar-height);
    }

    &::-webkit-scrollbar-corner {
        background-color: var(--scrollbar-background-color);
    }

    &::-webkit-scrollbar-thumb {
        background: var(--scrollbar-face-color);
        border-radius: var(--scrollbar-border-radius);

        &:hover {
            background: var(--scrollbar-face-color-hover);
        }
    }

    &::-webkit-scrollbar-track,
    &::-webkit-scrollbar-track:active,
    &::-webkit-scrollbar-track:hover {
        background-color: var(--scrollbar-track-color);
    }
}
````

The color variables are currently based on [MVP.css](https://andybrewer.github.io/mvp/)

````scss
:root {
    --scrollbar-face-color: var(--color-text-secondary);
    --scrollbar-track-color: var(--color-shadow);
    --scrollbar-border-radius: 5px;
    --scrollbar-face-color-hover: var(--color-secondary-accent);
    --scrollbar-width: calc(20px + .25em);
    --scrollbar-height: calc(20px + .25em);
    --scrollbar-background-color: transparent;
}
````

 > 
 > **NOTE**
>
 > Doesn't work on Firefox. Haven't checked on Safari.

# Related

* [The Current State of Styling Scrollbars in CSS (2022 Update) | CSS-Tricks - CSS-Tricks](https://css-tricks.com/the-current-state-of-styling-scrollbars-in-css/)