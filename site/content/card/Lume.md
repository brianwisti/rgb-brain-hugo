---
created: 2024-03-21 04:45:31-07:00
title: Lume
updated: 2024-03-21 04:46:33-07:00
---

[Static Site Generator](Static%20Site%20Generator.md) powered by [Deno](Deno.md)

[Lume, the static site generator for Deno - Lume](https://lume.land)

From your project folder:

````sh
deno run -Ar https://deno.land/x/lume/init.ts
````

It looks a lot like [Eleventy](Eleventy.md) but tidier

`_data.*` and `_data/*`hold shared data and frontmatter defaults

[Shared data - Lume](https://lume.land/docs/creating-pages/shared-data/)

Components are invoked via `comp`

````nunjucks
{% comp "container" %}
	...
{% endcomp %}
````

or simpler invocations without a content block

````nunjucks
{{ comp.button({ text: "Login" }) | safe }}
````

Components can have custom CSS in their frontmatter, which gets loaded into `/components.css`

````nunjucks
---
css: |
    .container {
        max-width: 80%;
        margin: auto;
        padding: 0.25em;
        border: thin solid;
    }
---
<section class="container">{{ content | safe }}</section>
````

Use generator functions to generate pages from data

[Create multiple pages - Lume](https://lume.land/docs/core/multiple-pages/)

Scoped updates for incremental rebuilds of large sites

[Scoped updates - Lume](https://lume.land/docs/core/scoped-updates/)

````typescript
site.scopedUpdates(
  (path) => path.endsWith(".css"), //Select all *.css files
  (path) => /\.(js|ts)$/.test(path), //Select all *.js and *.ts files
);
````

Task runner in site config instead of `package.json` — which obvs a Deno project won't have

[Scripts - Lume](https://lume.land/docs/core/scripts/)

Supports scripts with multiple steps

Supports dependencies / executing other scripts

 > 
 > **NOTE**
>
 > Deno still has `deno.json` for task / script definition

They have data cascade too

[Merged keys - Lume](https://lume.land/docs/core/merged-keys/)

They modestly provide an Eleventy migration guide

 > 
 > if you have an Eleventy project and want to migrate to Lume (maybe it's not a good idea)

[Migrate from Eleventy - Lume](https://lume.land/docs/advanced/migrate-from-11ty/)