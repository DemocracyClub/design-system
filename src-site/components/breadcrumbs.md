---
title: Breadcrumbs
---

Breadcrumbs are best used as a supplement to a principle navigation system.

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

Since breadcrumbs constitute a kind of navigation, a `<nav>` element is required, along with a descriptive label using `aria-label`. The current page (the final breadcrumb) should be unlinked..

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