---
title: Call-to-action
---

Use Calls-to-action (CTAs) for linking to important places. Calls-to-action are highlighted hyperlinks. Accordingly, styles are only honored for `<a>` elements with `href` attributes. For button styles see [Button]({{site.basedir}}/components/button).

Omitting the `href` is equivalent to using `disabled` on a `<button>` element, hence the opacity and cursor styles matching those of disabled [Buttons]({{site.basedir}}/components/button).

Avoid using `target="_blank"` to open a window in a new tab, unless necessary. See [this issue](https://github.com/DemocracyClub/WhoCanIVoteFor/issues/658) for guidance.

When linking to an external site, prefer inline hyperlinks over CTAs or buttons. Use text that makes it clear that the link is external, like "[The LGBCE Website]()".

To accomodate consistency, there is a modified style for CTA's used in header navigation. 

{% ds-example %}

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

{% endds-example %}
