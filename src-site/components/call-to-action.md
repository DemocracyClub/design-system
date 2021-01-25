---
title: Call-to-action
---

Calls-to-action (CTAs) are links, therefore styles are only honored for `<a>` elements with `href` attributes. For button styles see [button]({{site.basedir}}/components/button).

Omitting the `href` is equivalent to using `disabled` on a `<button>` element, hence the opacity and cursor styles matching those of disabled [buttons]({{site.basedir}}/components/button).

<table class="site-table" style="table-layout: fixed">
  <tr>
    <th>markup</th>
    <th>demo</th>
  </tr>
  <tr>
    <td>

```html
<a class="ds-cta" href="#">Link to something</a>
```

</td>
<td>
<div class="ds-type">
  <a class="ds-cta" href="#">Link to something</a>
</div>
</td>
  </tr>
  <tr>
    <td>

```html
<a class="ds-cta">Link to something</a>
```

</td>
<td>
<div class="ds-type">
  <a class="ds-cta">Link to something</a>
</div>
</td>
  </tr>
  <tr>
    <td>

```html
<a class="ds-cta ds-cta-blue" href="#">Link to something</a>
```

</td>
<td>
<div class="ds-type">
  <a class="ds-cta ds-cta-blue" href="#">Link to something</a>
</div>
</td>
  </tr>
  <tr>
    <td>

```html
<a class="ds-cta ds-cta-blue">Link to something</a>
```

</td>
<td>
<div class="ds-type">
  <a class="ds-cta ds-cta-blue">Link to something</a>
</div>
</td>
  </tr>
</table>