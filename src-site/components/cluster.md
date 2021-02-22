---
title: Cluster
---

Use a Cluster when you want to group inline elements closely together without having to worry about margin and wrapping behavior. Cluster elements have margin between them but no “left over” margin around them.

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

## Tighter clustering

You can reduce the space/margin between Cluster elements by using the `ds-cluster-tight` class _in addition_ to your chosen Cluster class. For example, a tightly clustered, right-justified example would be attributed like this:

```html
<div class="ds-cluster-right ds-cluster-tight">
  <!-- cluster innards -->
</div>
```