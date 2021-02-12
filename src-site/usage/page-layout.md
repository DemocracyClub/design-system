---
title: Page layout
layout: layouts/page.njk
---

Instate a standard page layout by wrapping a [Header]({{site.basedir}}/components/header), a main content area, and a [Footer]({{site.basedir}}/components/footer) in a `<div>` with `class="ds=page"` directly inside the `<body>` element.

```html
<body>
  <div class="ds-page">
    <header class="ds-header">...</header>
    <main id="main" tabindex="-1" class="ds-stack">...</main>
    <footer class="ds-footer">...</footer>
  </div>
</body>
```

{% note 'Demo' %}

See a [demo of this basic page layout]({{site.basedir}}/layout-demo).

{% endnote %}

## Notes

* The [Header]({{site.basedir}}/components/header) component’s prescribed markup includes a [skip link](https://webaim.org/techniques/skipnav/), so don’t implement one separately.
* For the skip link to work reliably in all browsers, the `<main>` element needs `id="main"` and `tabindex="-1"`.
* The `<main>` element needs `class="ds-stack"` (see [Stack]({{site.basedir}}/components.stack)) to insert margin between all the flow elements. For dealing with flow content, see [Composing content]({{site.basedir}}/usage/composition).

