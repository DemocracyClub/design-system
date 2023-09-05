---
title: Type
---

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
    <td>
{% ds-example %}
<div>
<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro voluptatum inventore fugiat, esse ducimus enim totam numquam adipisci? Ipsa cum sequi iste ex eius magni <a href="#">culpa praesentium</a> aliquam magnam temporibus.</p>
</div>
{% endds-example %}

</td>
  </tr>
</table>

## Blockquotes

<table class="site-table" style="table-layout: fixed">
  <tr>
    <th>Markup</th>
    <th>Demo</th>
  </tr>
  <tr>
    <td>

```html
  <blockquote>Porro voluptatum inventore fugiat, esse ducimus enim totam numquam adipisci? Ipsa cum sequi iste ex eius magni aliquam magnam temporibus.</blockquote>
```

</td>
    <td>
{% ds-example %}
<div>
      <blockquote>Porro voluptatum inventore fugiat, esse ducimus enim totam numquam adipisci? Ipsa cum sequi iste ex eius magni aliquam magnam temporibus.</blockquote>
</div>
{% endds-example %}

</td>
  </tr>
</table>

{% warning 'White space' %}

For consistency, the design system does not apply margin directly to elements. Instead, it is applied contextually using the [Stack]({{site.basedir}}/components/stack) component.

{% endwarning %}
