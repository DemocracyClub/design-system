---
title: Filter
---

The Filter component offers a set of filters for selecting pertinent data.

<div class="ds-scope">
  <aside class="ds-filter ds-stack-smaller" aria-labelledby="filter-label">
    <div class="ds-cluster">
      <ul>
        <li id="filter-label" class="ds-filter-label" aria-hidden="true">Filter:</li>
        <li><a href="?all" aria-current="page">All</a></li>
        <li><a href="?ready">Ready for data entry</a></li>
      </ul>
    </div>
    <details>
      <summary>Advanced filters</summary>
      Advanced filters here
    </details>
  </aside>
</div>

## Markup

```html
<aside class="ds-filter ds-stack-smaller" aria-labelledby="filter-label">
  <div class="ds-cluster">
    <ul>
      <li id="filter-label" class="ds-filter-label" aria-hidden="true">Filter:</li>
      <li><a href="?all" aria-current="page">All</a></li>
      <li><a href="?ready">Ready for data entry</a></li>
    </ul>
  </div>
  <details>
    <summary>Advanced filters</summary>
    [Advanced filters here]
  </details>
</aside>
```

* The component incorporates a [Cluster]({{site.basedir}}/components/cluster) and a [Stack](({{site.basedir}}/components/stack)) for layout.
* The element is an `<aside>` so it is discoverable using screen readers and is labeled using the first list item of the filters list (`aria-labelledby` and the `id` match).
* This element is hidden to assistive technologies with `aria-hidden` so is it is not enumerated as part of the list (this does not negate the `aria-labelledby` labeling mechanism).
* Advanced filters can be accessed using a [Details]({{site.basedir}}/components/details) component.
* The `aria-current="page"` attribution is used on the currently selected filter (as defined by the query parameter).