---
title: Breadcrumbs
---

Use the Breadcrumbs component when the site structure is several levels deep and a secondary wayfinding mechanism (in addition to the [Header’s]({{site.basedir}}/components/header) navigation links) may be useful.

Unlike [Sub-navigation]({{site.basedir}}/components/subnavigation), breadcrumbs represent levels of depth reading from left to right. Use [Sub-navigation]({{site.basedir}}/components/subnavigation) where each link represents a topic belonging to the _same_ level.

<div class="ds-scope">
  <nav class="ds-breadcrumbs" aria-label="Where you are">
    <ol>
      <li>
        <a href="/">Home</a>
      </li>
      <li>
        <a href="https://whocanivotefor.co.uk/elections/">Elections</a>
      </li>
      <li>
        Cheltenham local election
      </li>
    </ol>
  </nav>
</div>

Since breadcrumbs constitute a kind of navigation, a `<nav>` element is required, along with a descriptive label using `aria-label`. The current page (the final breadcrumb) should be unlinked.

```html
<nav class="ds-breadcrumbs" aria-label="Where you are">
  <ol>
    <li>
      <a href="/">Home</a>
    </li>
    <li>
      <a href="/elections">Elections</a>
    </li>
    <li>
      Cheltenham local election
    </li>
  </ol>
</nav>
```