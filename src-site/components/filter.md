---
title: Filter
---

The Filter component offers a set of filters for selecting pertinent data.

<div class="ds-scope">
  <aside class="ds-filter" aria-labelledby="filter-label">
    <div class="ds-filter-cluster">
      <ul>
        <li id="filter-label" class="ds-filter-label" aria-hidden="true">Filter:</li>
        <li><a href="?all" aria-current="true">All</a></li>
        <li><a href="?ready">Ready for data entry</a></li>
      </ul>
    </div>
    <details>
      <summary>Advanced filters</summary>
      <div class="ds-advanced-filters">
        <div class="ds-filter-cluster">
          <ul aria-labelledby="adv-filter-label-1">
            <li id="adv-filter-label-1" class="ds-filter-label" aria-hidden="true">Lock status:</li>
            <li><a href="?all" aria-current="true">All</a></li>
            <li><a href="?locked">Locked</a></li>
            <li><a href="?locksuggestion">Lock suggestion</a></li>
            <li><a href="?locksuggestion">Unlocked</a></li>
          </ul>
        </div>
        <div class="ds-filter-cluster">
          <ul aria-labelledby="adv-filter-label-2">
            <li id="adv-filter-label-2" class="ds-filter-label" aria-hidden="true">Has SoPN:</li>
            <li><a href="?all" aria-current="true">All</a></li>
            <li><a href="?yes">Yes</a></li>
            <li><a href="?no">No</a></li>
          </ul>
        </div>
        <div class="ds-filter-cluster">
          <ul aria-labelledby="adv-filter-label-3">
            <li id="adv-filter-label-3" class="ds-filter-label" aria-hidden="true">Election type:</li>
            <li><a href="?all" aria-current="true">All</a></li>
            <li><a href="?greaterlondon">Greater London Assembly</a></li>
            <li><a href="?local">Local</a></li>
            <li><a href="?mayoral">Mayoral</a></li>
            <li><a href="?police">Police &amp; Crime Commissioner</a></li>
            <li><a href="?scottish">Scottish parliament</a></li>
            <li><a href="?cymru">Senedd Cymru</a></li>
          </ul>
        </div>
      </div>
    </details>
  </aside>
</div>

## Markup

```html
<aside class="ds-filter" aria-labelledby="filter-label">
  <div class="ds-filter-cluster">
    <ul>
      <li id="filter-label" class="ds-filter-label" aria-hidden="true">Filter:</li>
      <li><a href="?all" aria-current="true">All</a></li>
      <li><a href="?ready">Ready for data entry</a></li>
    </ul>
  </div>
  <details>
    <summary>Advanced filters</summary>
    <div class="ds-advanced-filters">
      <div class="ds-filter-cluster">
        <ul aria-labelledby="adv-filter-label-1">
          <li id="adv-filter-label-1" class="ds-filter-label" aria-hidden="true">Advanced filter label:</li>
          <!-- filter option <li>s -->
        </ul>
      </div>
      <div class="ds-filter-cluster">
        <ul aria-labelledby="adv-filter-label-1">
          <li id="adv-filter-label-2" class="ds-filter-label" aria-hidden="true">Advanced filter label:</li>
          <!-- filter option <li>s -->
        </ul>
      </div>
      <div class="ds-filter-cluster">
        <ul aria-labelledby="adv-filter-label-1">
          <li id="adv-filter-label-3" class="ds-filter-label" aria-hidden="true">Advanced filter label:</li>
          <!-- filter option <li>s -->
        </ul>
      </div>
    </div>
  </details>
</aside>
```

* The element is an `<aside>` so it is discoverable using screen readers and is labeled using the first list item of the top-level filters list (`aria-labelledby` and the `id` match).
* This element is hidden to assistive technologies with `aria-hidden` so is it is not enumerated as part of the list (this does not negate the `aria-labelledby` labeling mechanism).
* Advanced filters can be accessed using a [Details]({{site.basedir}}/components/details) component.
* Advanced filters are grouped inside the `class="ds-advanced-filters"` element.
* Each advanced filter `<ul>` is labeled by the first `<li>` element using `aria-labelledby`
* The `aria-current="true"` attribution is used on the currently selected filter (as defined by the query parameter).