---
title: Utility classes
---

These utility classes are a toolkit for making simple design/layout adjustments to individual elements. For generic layout helpers (concerning multiple elements), see [Cluster]({{site.basedir}}/components/cluster), [Stack]({{site.basedir}}/components/stack), [Grid]({{site.basedir}}/components/grid), and [Sidebar]({{site.basedir}}/components/sidebar).

<table class="site-table">
  <tr>
    <th>
      Class name
    </th>
    <th>
      What it does
    </th>
    <th>
      Demo
    </th>
  </tr>
  <tr>
    <td>

`ds-padded`
    </td>
    <td>

Adds padding of `$s1` ({% var '$s1' %}) on all sides
    </td>
    <td class="ds-scope">
      <div class="ds-padded" style="background-color: #ddd">
        Basic padding
      </div>
    </td>
  </tr>
  <tr>
    <td>

`ds-padded-large`
    </td>
    <td>

Adds padding of `$s3` ({% var '$s3' %}) on all sides
    </td>
    <td class="ds-scope">
      <div class="ds-padded-large" style="background-color: #ddd">
        Large padding
      </div>
    </td>
  </tr>
  <tr>
    <td>

`ds-text-left`
    </td>
    <td>
Applies left justified text (usually to override centre or right justified text that has been applied to a parent)
    </td>
    <td class="ds-scope">
      <p class="ds-text-left">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae hic culpa, accusantium fuga, voluptate magnam excepturi. Lorem ipsum dolor sit amet consectetur adipisicing elit. Rem temporibus facilis, libero ratione cum quod id excepturi, tenetur dolorem, saepe similique dignissimos magni.
      </p>
    </td>
  </tr>
  <tr>
    <td>

`ds-text-centered`
    </td>
    <td>

Applies center justified text
    </td>
    <td class="ds-scope">
      <p class="ds-text-centered">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae hic culpa, accusantium fuga, voluptate magnam excepturi. Lorem ipsum dolor sit amet consectetur adipisicing elit. Rem temporibus facilis, libero ratione cum quod id excepturi, tenetur dolorem, saepe similique dignissimos magni.
      </p>
    </td>
  </tr>
  <tr>
    <td>

`ds-text-right`
    </td>
    <td>

Applies right justified text
    </td>
    <td class="ds-scope">
      <p class="ds-text-right">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae hic culpa, accusantium fuga, voluptate magnam excepturi. Lorem ipsum dolor sit amet consectetur adipisicing elit. Rem temporibus facilis, libero ratione cum quod id excepturi, tenetur dolorem, saepe similique dignissimos magni.
      </p>
    </td>
  </tr>
  <tr>
    <td>

`ds-bordered`
    </td>
    <td>
Adds a `2px` solid border matching the element’s `color`
    </td>
    <td class="ds-scope">
      <div class="ds-padded ds-bordered">
        Bordered and padded
      </div>
    </td>
  </tr>
  <tr>
    <td>

`ds-visually-hidden`
    </td>
    <td>
Hides an element visually <em>but</em> leaves it available to screen readers. May help to clarify things for screen reader users.
    </td>
    <td class="ds-scope">
      <p class="ds-visually-hidden">I am in screen reader output</p>
    </td>
  </tr>
  <tr>
    <td>

`ds-block-centered`
    </td>
    <td>

Centers a block element, using `auto` margins, with a `max-width` of `$measure` ({% var '$measure' %}).
    </td>
    <td class="ds-scope">
      <small>(demo not possible in this context)</small>
    </td>
  </tr>
  <tr>
    <td>

`ds-block-centered-narrow`
    </td>
    <td>

Same as `ds-block-centered` but uses `$measureReduced` ({% var '$measureReduced' %})
    </td>
    <td class="ds-scope">
      <small>(demo not possible in this context)</small>
    </td>
  </tr>
  <tr>
    <td>

`ds-h1`, `ds-h2`, `ds-h3`, `ds-h4`, `ds-h5`, `ds-h6`
    </td>
    <td>
Match the size of arbitrary text to a heading level. Only use where a heading element is not appropriate.
    </td>
    <td class="ds-scope">
      <span class="ds-h1">A</span>
      <span class="ds-h2">A</span>
      <span class="ds-h3">A</span>
      <span class="ds-h4">A</span>
      <span class="ds-h5">A</span>
      <span class="ds-h6">A</span>
    </td>
  </tr>
</table>

## Widths

Widths are set relative to font-size, using the `ch` unit and `max-width` to allow wrapping. 

### ds-width-full

This resets an element to use the full width of the container (`width: auto` on a block-level element; `display: block` is enforced).

<div class="ds-scope">
  <p class="ds-width-full">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vehicula, est ac sodales maximus, eros purus ultricies libero, non tempor ex augue eu diam. Proin a lectus risus. In pulvinar, tortor quis vulputate scelerisque, ligula est faucibus nisi, varius tincidunt purus nibh eget dui. In ut sollicitudin elit.</p>
</div>

```html
<p class="ds-width-full">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vehicula, est ac sodales maximus, eros purus ultricies libero, non tempor ex augue eu diam. Proin a lectus risus. In pulvinar, tortor quis vulputate scelerisque, ligula est faucibus nisi, varius tincidunt purus nibh eget dui. In ut sollicitudin elit.</p>
```

### ds-width-full-text

This uses the full measure of {% var '$measure' %} (`$measure`). Where the container is narrower than {% var '$measure' %}, it will take up the full width.

<div class="ds-scope">
  <p class="ds-width-full-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vehicula, est ac sodales maximus, eros purus ultricies libero, non tempor ex augue eu diam. Proin a lectus risus. In pulvinar, tortor quis vulputate scelerisque, ligula est faucibus nisi, varius tincidunt purus nibh eget dui. In ut sollicitudin elit.</p>
</div>

```html
<p class="ds-width-full-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vehicula, est ac sodales maximus, eros purus ultricies libero, non tempor ex augue eu diam. Proin a lectus risus. In pulvinar, tortor quis vulputate scelerisque, ligula est faucibus nisi, varius tincidunt purus nibh eget dui. In ut sollicitudin elit.</p>
```

### ds-width-reduced-text

A reduced value of {% var '$measureReduced' %} (`$measureReduced`).

<div class="ds-scope">
  <p class="ds-width-reduced-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vehicula, est ac sodales maximus, eros purus ultricies libero, non tempor ex augue eu diam. Proin a lectus risus. In pulvinar, tortor quis vulputate scelerisque, ligula est faucibus nisi, varius tincidunt purus nibh eget dui. In ut sollicitudin elit.</p>
</div>

```html
<p class="ds-width-reduced-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vehicula, est ac sodales maximus, eros purus ultricies libero, non tempor ex augue eu diam. Proin a lectus risus. In pulvinar, tortor quis vulputate scelerisque, ligula est faucibus nisi, varius tincidunt purus nibh eget dui. In ut sollicitudin elit.</p>
```

### ds-width-half-text

Half the `$measure` value.

<div class="ds-scope">
  <p class="ds-width-half-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vehicula, est ac sodales maximus, eros purus ultricies libero, non tempor ex augue eu diam. Proin a lectus risus. In pulvinar, tortor quis vulputate scelerisque, ligula est faucibus nisi, varius tincidunt purus nibh eget dui. In ut sollicitudin elit.</p>
</div>

```html
<p class="ds-width-half-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vehicula, est ac sodales maximus, eros purus ultricies libero, non tempor ex augue eu diam. Proin a lectus risus. In pulvinar, tortor quis vulputate scelerisque, ligula est faucibus nisi, varius tincidunt purus nibh eget dui. In ut sollicitudin elit.</p>
```

### ds-width-half-text

A third of the `$measure` value.

<div class="ds-scope">
  <p class="ds-width-third-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vehicula, est ac sodales maximus, eros purus ultricies libero, non tempor ex augue eu diam. Proin a lectus risus. In pulvinar, tortor quis vulputate scelerisque, ligula est faucibus nisi, varius tincidunt purus nibh eget dui. In ut sollicitudin elit.</p>
</div>

```html
<p class="ds-width-third-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vehicula, est ac sodales maximus, eros purus ultricies libero, non tempor ex augue eu diam. Proin a lectus risus. In pulvinar, tortor quis vulputate scelerisque, ligula est faucibus nisi, varius tincidunt purus nibh eget dui. In ut sollicitudin elit.</p>
```