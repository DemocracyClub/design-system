---
title: Sub-navigation
---

Use the Sub-navigation component when there are pages available related to the chosen main navigation link (as indicated by `aria-current="true"` in the [Header]({{site.basedir}}/components/header) component above it). For example, if the chosen route on [democracyclub.org.uk](https://democracyclub.org.uk) is “About”, use Sub-navigation to provide links to “About” (the index page), “The Team”, “Jobs”, and “Funding”. This group of pages represents a subsection of the site called “About”.

{% ds-example %}

  <nav class="ds-subnav" aria-label="About">
    <ul>
      <li>
        <a href="/about" aria-current="true">About</a>
      </li>
      <li>
        <a href="/team">The Team</a>
      </li>
      <li>
        <a href="/jobs">Jobs</a>
      </li>
      <li>
        <a href="/funding">Funding</a>
      </li>
    </ul>
  </nav>
{% endds-example %}


{% note 'Breadcrumbs' %}

If you wish to indicate _depth_ of location (how many links deep into a subsection of the site), use the [Breadcrumbs]({{site.basedir}}/components/breadcrumbs) component instead.

{% endnote %}

The `class="ds-subnav"` element is a `<nav>`, exposing it as a landmark region to screen readers. Note the use of `aria-label="About"`. This differentiates this navigation landmark from the main one above it in screen reader landmark listings. Where the section is “Our work”, use `aria-label="Our work"`.

The `aria-current="true"` attribution indicates the current page, in this case the first, index page.

```html
  <nav class="ds-subnav" aria-label="About">
    <ul>
      <li>
        <a href="/about" aria-current="true">About</a>
      </li>
      <li>
        <a href="/team">The Team</a>
      </li>
      <li>
        <a href="/jobs">Jobs</a>
      </li>
      <li>
        <a href="/funding">Funding</a>
      </li>
    </ul>
  </nav>
```

{% warning 'Source order' %}

As demonstrated in the [page layout demo]({{site.basedir}}/layout-demo), the Sub-navigation component should appear first inside the `<main>` element, _before_ the page’s `<h1>`. This is better for screen reader accessibility than the reverse configuration used in the live [democracyclub.org.uk](https://democracyclub.org.uk) site at the time of writing.

```html
<main id="main" tabindex="-1">
  <nav class="ds-subnav" aria-label="About">
    <!-- Sub-navigation links -->
  </nav>
  <h1>About</h1>
  <!-- main content -->
</main>
```

{% endwarning %}
