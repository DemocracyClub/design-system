---
title: Button
---

Use the `<button>` element for submitting forms or—in rare cases—triggering JavaScript events such as toggling menus. Use the `type="submit"` for form submission or `type="button"` for any other functionality.

If the control redirects the user to a different location (another page or a location in the current page) use the [Call-to-action]({{side.basedir}}/components/call-to-action) component instead.

Buttons should always use the `<button>` element, with either the `type="button"` attribution or `type="submit"` for forms. For call-to-action links see [call-to-action]({{side.basedir}}/components/call-to-action). If you do not use a `<button>` element, the styles will not be honoured (they are scoped in the selector as `button.ds-button`).

Only use the blue version as a supplementary option; the pink (default version) should be used where there is only one button in the context.

{% ds-example %}

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
<div class="ds-scope">
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
<div class="ds-scope">
  <button class="ds-button" type="button" disabled>Press me</button>
</div>
</td>
  </tr>
  <tr>
    <td>

```html
<button class="ds-button-blue" type="button">Press me</button>
```

</td>
<td>
<div class="ds-scope">
  <button class="ds-button-blue" type="button">Press me</button>
</div>
</td>
  </tr>
  <tr>
    <td>

```html
<button class="ds-button-blue" type="button" disabled>Press me</button>
```

</td>
<td>
<div class="ds-scope">
  <button class="ds-button-blue" type="button" disabled>Press me</button>
</div>
</td>
  </tr>
</table>

{% endds-example %}
