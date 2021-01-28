---
title: Header
---

The Header is intended for all Democracy Club sites. It includes a logo which links to [https://democracyclub.org.uk/](https://democracyclub.org.uk/) and a set of main navigation links for the local site. The “Home” link should link to the local site’s homepage, not [https://democracyclub.org.uk/](https://democracyclub.org.uk/) (unless the site in question _is_ democracyclub.org.uk).

<div class="ds-scope site-resizer">
  <header class="ds-header">
    <a class="ds-skip-link" href="#main">skip to content</a>
    <a class="ds-header-home" href="https://democracyclub.org.uk/">
      <img src="{{site.basedir}}/images/system/logo.svg" alt="Democracy Club home" />
    </a>
    <nav class="ds-cluster">
      <ul>
        <li>
          <a href="/">Home</a>
        </li>
        <li>
          <a aria-current="true" href=".path/to/about">About</a>
        </li>
        <li>
          <a href="/path/to/">Our work</a>
        </li>
        <li>
          <a href="#">Quests</a>
        </li>
        <li>
          <a href="#">Blog</a>
        </li>
        <li>
          <a href="#">Contact</a>
        </li>
        <li>
          <a href="#">Donate</a>
        </li>
      </ul>
    </nav>
  </header>
</div>

Built into the Header is a skip link, which is provided to satisfy WCAG’s [2.4.1 Bypass Blocks](https://www.w3.org/WAI/WCAG21/Understanding/bypass-blocks.html) criterion. This link appears on keyboard focus and lets keyboard (including screen reader) users _bypass_ the page’s preamble. **Importantly**, for the skip link to work, you will need to place `id="main"` and `tabindex="-1"` on the page’s `<main>` element (of which there should only be one).

```html
<header class="ds-header">
  <a class="ds-skip-link" href="#main">skip to content</a>
  <a class="ds-header-home" href="/">
    <img src="/path/to/logo.svg" alt="Democracy Club home" />
  </a>
  <nav class="ds-cluster">
    <ul>
      <li>
        <a href="#">Home</a>
      </li>
      <li>
        <a aria-current="true" href="#">About</a>
      </li>
      <li>
        <a href="#">Our work</a>
      </li>
      <li>
        <a href="#">Quests</a>
      </li>
      <li>
        <a href="#">Blog</a>
      </li>
      <li>
        <a href="#">Contact</a>
      </li>
      <li>
        <a href="#">Donate</a>
      </li>
    </ul>
  </nav>
</header>
```

Note the use of `aria-current` which indicates the current page. This is placed on “About” (as in the previous code sample) where the user is currently on the about page. This attribute helps screen reader users with wayfinding and is the non-visual equivalent of the pink underline.