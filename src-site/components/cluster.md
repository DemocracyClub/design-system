---
title: Cluster
---

The cluster helper component lets you group smaller elements together in “clusters”. These elements are spaced evenly along both axes without “left over” margin indenting the elements undesirably (irrespective of wrapping).

<table class="site-table" style="table-layout: fixed">
  <tr>
    <th>Alignment</th>
    <th>Markup</th>
    <th colspan="2">Demo</th>
  </tr>
  <tr>
    <td>left (default)</td>
    <td>

```html
<div class="ds-cluster">
  <div>
    <button class="ds-button ds-button-blue">Cancel</button>
    <button class="ds-button">Confirm</button>
  </div>
</div>
```

  </td>
  <td class="ds-scope" colspan="2">
    <div class="ds-cluster">
  <div>
    <button class="ds-button ds-button-blue">Cancel</button>
    <button class="ds-button">Confirm</button>
  </div>
</div>
  </td>
  </tr>
  <tr>
    <td>center</td>
    <td>

```html
<div class="ds-cluster-center">
  <div>
    <button class="ds-button ds-button-blue">Cancel</button>
    <button class="ds-button">Confirm</button>
  </div>
</div>
```

  </td>
  <td class="ds-scope" colspan="2">
    <div class="ds-cluster-center">
  <div>
    <button class="ds-button ds-button-blue">Cancel</button>
    <button class="ds-button">Confirm</button>
  </div>
</div>
  </td>
  </tr>
  <tr>
    <td>right</td>
    <td>

```html
<div class="ds-cluster-right">
  <div>
    <button class="ds-button ds-button-blue">Cancel</button>
    <button class="ds-button">Confirm</button>
  </div>
</div>
```

  </td>
  <td class="ds-scope" colspan="2">
    <div class="ds-cluster-right">
  <div>
    <button class="ds-button ds-button-blue">Cancel</button>
    <button class="ds-button">Confirm</button>
  </div>
</div>
  </td>
  </tr>
</table>