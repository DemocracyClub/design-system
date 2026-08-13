---
title: Colors
---

Every colour is defined as a CSS custom property in `tokens.css`. This project
is migrating from SASS vars to CSS vars. At the moment the SASS vars still exist
and are aliases of the CSS vars. SASS vars are deprecated and should be
converted to CSS vars.
See [CSS custom properties]({{site.basedir}}/basics/css-custom-properties) for
the background.

## Semantic properties

These describe the role a colour plays rather than what it looks like. They are
the better choice in application code: when the design system gains theme-aware
values, these are the properties that will change.

They have no Sass equivalent — they are new.

<table class="site-table">
  <tr>
    <th>CSS property</th>
    <th>Used for</th>
    <th>Value</th>
    <th>Demo</th>
  </tr>
  <tr>
    <td><code>--ds-colour-text</code></td>
    <td>Body and heading text</td>
    <td><code>{% token '--ds-colour-text' %}</code></td>
    <td><div class="site-swatch" style="background-color: var(--ds-colour-text)"></div></td>
  </tr>
  <tr>
    <td><code>--ds-colour-text-inverse</code></td>
    <td>Text on a dark background</td>
    <td><code>{% token '--ds-colour-text-inverse' %}</code></td>
    <td><div class="site-swatch" style="background-color: var(--ds-colour-text-inverse)"></div></td>
  </tr>
  <tr>
    <td><code>--ds-colour-link</code></td>
    <td>Links and interactive text</td>
    <td><code>{% token '--ds-colour-link' %}</code></td>
    <td><div class="site-swatch" style="background-color: var(--ds-colour-link)"></div></td>
  </tr>
  <tr>
    <td><code>--ds-colour-action</code></td>
    <td>Buttons and calls to action</td>
    <td><code>{% token '--ds-colour-action' %}</code></td>
    <td><div class="site-swatch" style="background-color: var(--ds-colour-action)"></div></td>
  </tr>
  <tr>
    <td><code>--ds-colour-action-inverse</code></td>
    <td>The same, on a dark background</td>
    <td><code>{% token '--ds-colour-action-inverse' %}</code></td>
    <td><div class="site-swatch" style="background-color: var(--ds-colour-action-inverse)"></div></td>
  </tr>
  <tr>
    <td><code>--ds-colour-focus</code></td>
    <td>Keyboard focus outlines</td>
    <td><code>{% token '--ds-colour-focus' %}</code></td>
    <td><div class="site-swatch" style="background-color: var(--ds-colour-focus)"></div></td>
  </tr>
  <tr>
    <td><code>--ds-colour-background-page</code></td>
    <td>The page background</td>
    <td><code>{% token '--ds-colour-background-page' %}</code></td>
    <td><div class="site-swatch" style="background-color: var(--ds-colour-background-page)"></div></td>
  </tr>
  <tr>
    <td><code>--ds-colour-background-panel</code></td>
    <td>Forms, tables and filters</td>
    <td><code>{% token '--ds-colour-background-panel' %}</code></td>
    <td><div class="site-swatch" style="background-color: var(--ds-colour-background-panel)"></div></td>
  </tr>
  <tr>
    <td><code>--ds-colour-background-inverse</code></td>
    <td>Dark headers and footers</td>
    <td><code>{% token '--ds-colour-background-inverse' %}</code></td>
    <td><div class="site-swatch" style="background-color: var(--ds-colour-background-inverse)"></div></td>
  </tr>
  <tr>
    <td><code>--ds-colour-background-subtle</code></td>
    <td>Code blocks and highlighted text</td>
    <td><code>{% token '--ds-colour-background-subtle' %}</code></td>
    <td><div class="site-swatch" style="background-color: var(--ds-colour-background-subtle)"></div></td>
  </tr>
  <tr>
    <td><code>--ds-colour-border</code></td>
    <td>Card, form and table borders</td>
    <td><code>{% token '--ds-colour-border' %}</code></td>
    <td><div class="site-swatch" style="background-color: var(--ds-colour-border)"></div></td>
  </tr>
  <tr>
    <td><code>--ds-colour-border-inverse</code></td>
    <td>Borders on a dark background</td>
    <td><code>{% token '--ds-colour-border-inverse' %}</code></td>
    <td><div class="site-swatch" style="background-color: var(--ds-colour-border-inverse)"></div></td>
  </tr>
  <tr>
    <td><code>--ds-colour-success</code></td>
    <td>Success states</td>
    <td><code>{% token '--ds-colour-success' %}</code></td>
    <td><div class="site-swatch" style="background-color: var(--ds-colour-success)"></div></td>
  </tr>
  <tr>
    <td><code>--ds-colour-error</code></td>
    <td>Errors and validation failures</td>
    <td><code>{% token '--ds-colour-error' %}</code></td>
    <td><div class="site-swatch" style="background-color: var(--ds-colour-error)"></div></td>
  </tr>
  <tr>
    <td><code>--ds-colour-info</code></td>
    <td>Informational states</td>
    <td><code>{% token '--ds-colour-info' %}</code></td>
    <td><div class="site-swatch" style="background-color: var(--ds-colour-info)"></div></td>
  </tr>
</table>

{% note 'The partials have not moved across yet' %}

The design system’s own component styles still reference the Sass variables,
which resolve to the *primitive* properties. Moving them onto the semantic
properties is separate work — it is what will let `.ds-dark` become a handful of
property overrides instead of a rule per component.

{% endnote %}

## Primitive palette

These are the raw palette values. The number describes relative strength, not a
measurement: within each hue, `-700` is contrast-safe against white and `-400`
is contrast-safe against the dark backgrounds. That is the distinction the
`...ForWhite` and `...ForBlack` Sass names were making.

Prefer the semantic properties below these where one fits.

<table class="site-table">
  <tr>
    <th>Sass variable</th>
    <th>CSS property</th>
    <th>Value</th>
    <th>Demo</th>
  </tr>
  <tr>
    <td><code>$black</code></td>
    <td><code>{% cssvar '$black' %}</code></td>
    <td><code>{% var '$black' %}</code></td>
    <td>
      <div class="site-swatch ds-bg-color-black"></div>
    </td>
  </tr>
  <tr>
    <td><code>$darkBlack</code></td>
    <td><code>{% cssvar '$darkBlack' %}</code></td>
    <td><code>{% var '$darkBlack' %}</code></td>
    <td>
      <div class="site-swatch" style="background-color: var(--ds-colour-grey-950)"></div>
    </td>
  </tr>
  <tr>
    <td><code>$blackOpacity</code></td>
    <td><code>{% cssvar '$blackOpacity' %}</code></td>
    <td><code>{% var '$blackOpacity' %}</code></td>
    <td>
      <div class="site-swatch ds-bg-color-blackOpacity"></div>
    </td>
  </tr>
  <tr>
    <td><code>$white</code></td>
    <td><code>{% cssvar '$white' %}</code></td>
    <td><code>{% var '$white' %}</code></td>
    <td>
      <div class="site-swatch ds-bg-color-white"></div>
    </td>
  </tr>
  <tr>
    <td><code>$pinkForWhite</code></td>
    <td><code>{% cssvar '$pinkForWhite' %}</code></td>
    <td><code>{% var '$pinkForWhite' %}</code></td>
    <td>
      <div class="site-swatch ds-bg-color-pinkForWhite"></div>
    </td>
  </tr>
  <tr>
    <td><code>$blueLight</code></td>
    <td><code>{% cssvar '$blueLight' %}</code></td>
    <td><code>{% var '$blueLight' %}</code></td>
    <td>
      <div class="site-swatch ds-bg-color-blueLight"></div>
    </td>
  </tr>
  <tr>
    <td><code>$blueForWhite</code></td>
    <td><code>{% cssvar '$blueForWhite' %}</code></td>
    <td><code>{% var '$blueForWhite' %}</code></td>
    <td>
      <div class="site-swatch ds-bg-color-blueForWhite"></div>
    </td>
  </tr>
  <tr>
    <td><code>$blueForBlack</code></td>
    <td><code>{% cssvar '$blueForBlack' %}</code></td>
    <td><code>{% var '$blueForBlack' %}</code></td>
    <td>
      <div class="site-swatch ds-bg-color-blueForBlack"></div>
    </td>
  </tr>
  <tr>
    <td><code>$greenForWhite</code></td>
    <td><code>{% cssvar '$greenForWhite' %}</code></td>
    <td><code>{% var '$greenForWhite' %}</code></td>
    <td>
      <div class="site-swatch ds-bg-color-greenForWhite"></div>
    </td>
  </tr>
  <tr>
    <td><code>$greenForBlack</code></td>
    <td><code>{% cssvar '$greenForBlack' %}</code></td>
    <td><code>{% var '$greenForBlack' %}</code></td>
    <td>
      <div class="site-swatch ds-bg-color-greenForBlack"></div>
    </td>
  </tr>
  <tr>
    <td><code>$redForWhite</code> and <code>$redForBlueLight</code></td>
    <td><code>{% cssvar '$redForWhite' %}</code></td>
    <td><code>{% var '$redForWhite' %}</code></td>
    <td>
      <div class="site-swatch ds-bg-color-redForWhite"></div>
    </td>
  </tr>
  <tr>
    <td><code>$redForBlack</code></td>
    <td><code>{% cssvar '$redForBlack' %}</code></td>
    <td><code>{% var '$redForBlack' %}</code></td>
    <td>
      <div class="site-swatch" style="background-color: var(--ds-colour-red-400)"></div>
    </td>
  </tr>
  <tr>
    <td><code>$amber</code></td>
    <td><code>{% cssvar '$amber' %}</code></td>
    <td><code>{% var '$amber' %}</code></td>
    <td>
      <div class="site-swatch ds-bg-color-amber"></div>
    </td>
  </tr>
</table>

## Accessible pairings

As the names suggest, the “forWhite” colors can be safely paired with `$white`
and the “forBlack” colors can be safely paired with `$black`. For example:

```css
.ds-my-component {
    color: var(--ds-colour-white);
    background-color: var(--ds-colour-green-700);
}

.ds-my-component-reversed {
    color: var(--ds-colour-green-700);
    background-color: var(--ds-colour-white);
}
```

The is no `$pinkForBlack` because we tried to make one and it looked _gross_.
