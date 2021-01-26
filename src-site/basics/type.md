---
title: Type
---

These are the basic typography styles. Typically, you should simply `@import` them in your `index.scss` file. However, you can scope them to the `.dc-type` class by setting `$scope-type` to `true`. This allows you to sandbox the styles to a particular section of your production site, to avoid conflicts. The scoping option can also be used to bump up specificity where existing (non design system) styles are taking precedence. You can place `class="ds-scope"` on the body element if this is all you need.

## Headings

<table class="site-table">
  <tr>
    <th>Markup</th>
    <th>Demo</th>
  </tr>
  <tr>
    <td>

```html
<h1>Who can I vote for</h1>
```

</td>
    <td class="ds-scope">
      <h1>Who can I vote for?</h1>
    </td>
  </tr>
  <tr>
    <td>

```html
<h2>Who can I vote for</h2>
```

</td>
    <td class="ds-scope">
      <h2>Who can I vote for?</h2>
    </td>
  </tr>
  <tr>
    <td>

```html
<h3>Who can I vote for</h3>
```

</td>
    <td class="ds-scope">
      <h3>Who can I vote for?</h3>
    </td>
  </tr>
  <tr>
    <td>

```html
<h4>Who can I vote for</h4>
```

</td>
    <td class="ds-scope">
      <h4>Who can I vote for?</h4>
    </td>
  </tr>
  <tr>
    <td>

```html
<h5>Who can I vote for</h5>
```

</td>
    <td class="ds-scope">
      <h5>Who can I vote for?</h5>
    </td>
  </tr>
</table>

Classes in the form `.ds-[heading level]` (e.g. `.ds-h2`) are provided to match heading font sizes where the use of a semantic heading is not appropriate. Headings should only be used to introduce sections of content.

## Paragraphs

<table class="site-table" style="table-layout: fixed">
  <tr>
    <th>Markup</th>
    <th>Demo</th>
  </tr>
  <tr>
    <td>

```html
  <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro voluptatum inventore fugiat, esse ducimus enim totam numquam adipisci? Ipsa cum sequi iste ex eius magni <a href="#">culpa praesentium</a> aliquam magnam temporibus.</p>
```

</td>
    <td class="ds-scope">
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro voluptatum inventore fugiat, esse ducimus enim totam numquam adipisci? Ipsa cum sequi iste ex eius magni <a href="#">culpa praesentium</a> aliquam magnam temporibus.</p>
    </td>
  </tr>
</table>

{% warning 'White space' %}

For consistency, the design system does not apply margin directly to elements. Instead, it is applied contextually using the [Stack]({{site.basedir}}/components/stack) component.

{% endwarning %}