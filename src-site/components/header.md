---
title: Header
---

Use the Header to brand your Democracy Club site and provide the main navigation. It includes a logo which links to [https://democracyclub.org.uk/](https://democracyclub.org.uk/) and a set of main navigation links for the local site. The “Home” link should link to the local site’s homepage, not [https://democracyclub.org.uk/](https://democracyclub.org.uk/) (unless the site in question _is_ democracyclub.org.uk).

{% ds-example %}
<div class="site-resizer">
  <header class="ds-header">
    <a class="ds-logo" href="/">
      <img src="{{site.basedir}}/images/logo_icon.svg" alt="" />
      <span>democracy<br>club</span>
    </a>
    <nav>
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
{% endds-example %}


```html
<header class="ds-header">
  <a class="ds-skip-link" href="#main">skip to content</a>
  <a class="ds-header-home" href="/">
    <img src="/path/to/logo.svg" alt="Democracy Club home" />
    <span>democracy<br>club</span>
  </a>
  <nav>
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

{% note 'Current page indication' %}

The `aria-current="true"` attribution indicates which navigation link corresponds to the current location (the `true` value is used in place of `page` because of the relationship to [Sub-navigation]({{site.basedir}}/components/subnavigation)). This is placed on “About” (as in the previous code sample) where the user is currently on the about page. This attribute helps screen reader users with wayfinding and is the non-visual equivalent of the pink underline.

{% endnote %}
