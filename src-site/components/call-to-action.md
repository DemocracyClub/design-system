---
title: Call-to-action
---

Use Calls-to-action (CTAs) for linking to important places. Calls-to-action are highlighted hyperlinks. Accordingly, styles are only honored for `<a>` elements with `href` attributes. For button styles see [Button]({{site.basedir}}/components/button).

Omitting the `href` is equivalent to using `disabled` on a `<button>` element, hence the opacity and cursor styles matching those of disabled [Buttons]({{site.basedir}}/components/button).

To accomodate consistency, there is a modified style for CTA's used in header navigation. 

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
<div class="ds-scope">
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
<div class="ds-scope">
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
<div class="ds-scope">
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
<div class="ds-scope">
  <a class="ds-cta ds-cta-blue">Link to something</a>
</div>
</td>
  </tr>
</table>

## Dark theme

Invoke the dark theme on any component by applying class="ds-dark" to a container element.

<table class="site-table" style="table-layout: fixed">
  <tr>
    <th>markup</th>
    <th>demo</th>
  </tr>
  <tr>
    <td>

```html
<div class="ds-dark">
  <a class="ds-cta" href="#">Link to something</a>
</div>
```

</td>
<td>
  <div class="ds-scope">
    <div class="ds-dark" style="padding: 1rem">
      <a class="ds-cta" href="#">Link to something</a>
    </div>
  </div>
</td>
  </tr>
  <tr>
    <td>

```html
<div class="ds-dark">
  <a class="ds-cta">Link to something</a>
</div>
```

</td>
<td>
  <div class="ds-scope">
    <div class="ds-dark" style="padding: 1rem">
      <a class="ds-cta">Link to something</a>
    </div>
  </div>
</td>
  </tr>
  <tr>
    <td>

```html
<div class="ds-dark">
  <a class="ds-cta ds-cta-blue" href="#">Link to something</a>
</div>
```

</td>
<td>
  <div class="ds-scope">
    <div class="ds-dark" style="padding: 1rem">
      <a class="ds-cta ds-cta-blue" href="#">Link to something</a>
    </div>
  </div>
</td>
  </tr>
  <tr>
    <td>

```html
<div class="ds-dark">
  <a class="ds-cta ds-cta-blue">Link to something</a>
</div>
```

</td>
<td>
  <div class="ds-scope">
    <div class="ds-dark" style="padding: 1rem">
      <a class="ds-cta ds-cta-blue">Link to something</a>
    </div>
  </div>
</td>
  </tr>
</table>