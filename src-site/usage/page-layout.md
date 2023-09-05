---
title: Page layout
layout: layouts/page.njk
---

Instate a standard page layout by wrapping a skip link, [Language]({{site.basedir}}/components/language) component, [Header]({{site.basedir}}/components/header), a main content area, and a [Footer]({{site.basedir}}/components/footer) in a `<div>` with `class="ds-page"` directly inside the `<body>` element.

{% note 'Skip link' %}

The first thing that appears in the page source should be a skip link, which is provided to satisfy WCAG’s [2.4.1 Bypass Blocks](https://www.w3.org/WAI/WCAG21/Understanding/bypass-blocks.html) criterion. This link appears on keyboard focus and lets keyboard (including screen reader) users _bypass_ the page’s preamble. **Importantly**, for the skip link to work, you will need to place `id="main"` and `tabindex="-1"` on the page’s `<main>` element (of which there should only be one).

{% endnote %}

```html
<body>
  <div class="ds-page">
    <a class="ds-skip-link" href="#main">skip to content</a>
    <aside class"ds-language">...</aside>
    <header class="ds-header">...</header>
    <main id="main" tabindex="-1" class="ds-stack">...</main>
    <footer class="ds-footer">...</footer>
  </div>
</body>
```

{% note 'Demo' %}

See a [demo of this basic page layout]({{site.basedir}}/layout-demo) [dark 
theme]({{site.basedir}}/layout-demo-dark).

{% endnote %}

## Notes

* The [Header]({{site.basedir}}/components/header) component’s prescribed markup includes a [skip link](https://webaim.org/techniques/skipnav/), so don’t implement one separately.
* For the skip link to work reliably in all browsers, the `<main>` element needs `id="main"` and `tabindex="-1"`.
* The `<main>` element needs `class="ds-stack"` (see [Stack]({{site.basedir}}/components.stack)) to insert margin between all the flow elements. For dealing with flow content, see [Composing content]({{site.basedir}}/usage/composition).
