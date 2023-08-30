---
title: Language
---

Include the language component as the first element after the skip link (see the [layout demo]({{site.basedir}}/layout-demo) source). 

{% ds-example %}
  <aside class="ds-language" aria-labelledby="language-label">
    <ul>
      <li id="language-label" aria-hidden="true">Language:</li>
      <li><a href="/english" lang="en" aria-current="true">English</a></li>
      <li><a href="/cymraeg" lang="cy">Cymraeg</a></li>
    </ul>
  </aside>
{% endds-example %}


## Markup

```html
<aside class="ds-language" aria-labelledby="language-label">
  <ul>
    <li id="language-label" aria-hidden="true">Language:</li>
    <li><a href="/english" lang="en" aria-current="true">English</a></li>
    <li><a href="/cymraeg" lang="cy">Cymraeg</a></li>
  </ul>
</aside>
```

* The language component is discoverable using screen readers as a complementary landmark (`<aside>`) with the identifying label “language”
* The languages appear as a list. The first item, acting as the labeling element is not counted in the list in screen reader output since it uses `aria-hidden="true"`
* Each language must be identified using the correct ISO. For example, Cymraeg (Welsh) takes `lang="cy"`
* The currently selected language is indicated using `aria-current="true"`

## Behavior

It is recommended the language component is removed from the top of the page once a language has been selected, to reduce clutter. This should be persisted across pages using `localStorage` or similar. The language options should be repreated in the footer and persist so they can be accessed at all times.
