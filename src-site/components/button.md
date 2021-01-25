---
title: Button
---

Buttons should always use the `<button>` element, with either the `type="button"` attribution or `type="submit"` for forms. for call-to-action links see [call-to-action]({{side.basedir}}/components/call-to-action). If you do not use a `<button>` element, the styles will not be honoured (they are scoped in the selector as `button.ds-button`).

Only use the blue version as a supplementary option; the pink (default version) should be used where there is only one button in the context.

<table class="site-table" style="table-layout: fixed">
  <tr>
    <th>markup</th>
    <th>demo</th>
  </tr>
  <tr>
    <td>

```html
<button class="ds-button" type="button">Press me</button>
```

</td>
<td>
<div class="ds-type">
  <button class="ds-button" type="button">Press me</button>
</div>
</td>
  </tr>
  <tr>
    <td>

```html
<button class="ds-button" type="button" disabled>Press me</button>
```

</td>
<td>
<div class="ds-type">
  <button class="ds-button" type="button" disabled>Press me</button>
</div>
</td>
  </tr>
  <tr>
    <td>

```html
<button class="ds-button ds-button-blue" type="button">Press me</button>
```

</td>
<td>
<div class="ds-type">
  <button class="ds-button ds-button-blue" type="button">Press me</button>
</div>
</td>
  </tr>
  <tr>
    <td>

```html
<button class="ds-button ds-button-blue" type="button" disabled>Press me</button>
```

</td>
<td>
<div class="ds-type">
  <button class="ds-button ds-button-blue" type="button" disabled>Press me</button>
</div>
</td>
  </tr>
</table>
