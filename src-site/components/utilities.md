---
title: Utility classes
---

These utility classes are a toolkit for making simple design/layout adjustments to individual elements. For generic layout helpers (concerning multiple elements), see [Cluster]({{site.basedir}}/components/cluster), [Stack]({{site.basedir}}/components/stack), and [Grid]({{site.basedir}}/components/cluster).

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

Match the size of arbitrary text to a heading level. Only use where a heading is not appropriate.
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