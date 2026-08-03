---
title: Colors
---

Every colour is defined as a CSS custom property in `tokens.css`. 
This project is migrating from SASS vars to CSS vars. At the moment the SASS 
vars still exist and are aliases of the CSS vars. SASS vars are deprecated 
and should be converted to CSS vars. See [CSS custom properties]({{site.basedir}}/basics/css-custom-properties) for the background.

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
    <td>{% var '$black' %}</td>
    <td>
      <div class="site-swatch ds-bg-color-black"></div>
    </td>
  </tr>
  <tr>
    <td><code>$darkBlack</code></td>
    <td><code>{% cssvar '$darkBlack' %}</code></td>
    <td>{% var '$darkBlack' %}</td>
    <td>
      <div class="site-swatch" style="background-color: var(--ds-colour-grey-950)"></div>
    </td>
  </tr>
  <tr>
    <td><code>$blackOpacity</code></td>
    <td><code>{% cssvar '$blackOpacity' %}</code></td>
    <td>{% var '$blackOpacity' %}</td>
    <td>
      <div class="site-swatch ds-bg-color-blackOpacity"></div>
    </td>
  </tr>
  <tr>
    <td><code>$white</code></td>
    <td><code>{% cssvar '$white' %}</code></td>
    <td>{% var '$white' %}</td>
    <td>
      <div class="site-swatch ds-bg-color-white"></div>
    </td>
  </tr>
  <tr>
    <td><code>$pinkForWhite</code></td>
    <td><code>{% cssvar '$pinkForWhite' %}</code></td>
    <td>{% var '$pinkForWhite' %}</td>
    <td>
      <div class="site-swatch ds-bg-color-pinkForWhite"></div>
    </td>
  </tr>
  <tr>
    <td><code>$blueLight</code></td>
    <td><code>{% cssvar '$blueLight' %}</code></td>
    <td>{% var '$blueLight' %}</td>
    <td>
      <div class="site-swatch ds-bg-color-blueLight"></div>
    </td>
  </tr>
  <tr>
    <td><code>$blueForWhite</code></td>
    <td><code>{% cssvar '$blueForWhite' %}</code></td>
    <td>{% var '$blueForWhite' %}</td>
    <td>
      <div class="site-swatch ds-bg-color-blueForWhite"></div>
    </td>
  </tr>
  <tr>
    <td><code>$blueForBlack</code></td>
    <td><code>{% cssvar '$blueForBlack' %}</code></td>
    <td>{% var '$blueForBlack' %}</td>
    <td>
      <div class="site-swatch ds-bg-color-blueForBlack"></div>
    </td>
  </tr>
  <tr>
    <td><code>$greenForWhite</code></td>
    <td><code>{% cssvar '$greenForWhite' %}</code></td>
    <td>{% var '$greenForWhite' %}</td>
    <td>
      <div class="site-swatch ds-bg-color-greenForWhite"></div>
    </td>
  </tr>
  <tr>
    <td><code>$greenForBlack</code></td>
    <td><code>{% cssvar '$greenForBlack' %}</code></td>
    <td>{% var '$greenForBlack' %}</td>
    <td>
      <div class="site-swatch ds-bg-color-greenForBlack"></div>
    </td>
  </tr>
  <tr>
    <td><code>$redForWhite</code> and <code>$redForBlueLight</code></td>
    <td><code>{% cssvar '$redForWhite' %}</code></td>
    <td>{% var '$redForWhite' %}</td>
    <td>
      <div class="site-swatch ds-bg-color-redForWhite"></div>
    </td>
  </tr>
  <tr>
    <td><code>$redForBlack</code></td>
    <td><code>{% cssvar '$redForBlack' %}</code></td>
    <td>{% var '$redForBlack' %}</td>
    <td>
      <div class="site-swatch" style="background-color: var(--ds-colour-red-400)"></div>
    </td>
  </tr>
  <tr>
    <td><code>$amber</code></td>
    <td><code>{% cssvar '$amber' %}</code></td>
    <td>{% var '$amber' %}</td>
    <td>
      <div class="site-swatch ds-bg-color-amber"></div>
    </td>
  </tr>
</table>

## Semantic properties

These describe the role a colour plays rather than what it looks like. They are
the better choice in application code: when the design system gains theme-aware
values, these are the properties that will change.

They have no Sass equivalent — they are new.

<table class="site-table">
  <tr>
    <th>CSS property</th>
    <th>Value</th>
    <th>Used for</th>
  </tr>
  <tr>
    <td><code>--ds-colour-text</code></td>
    <td>{% token '--ds-colour-text' %}</td>
    <td>Body and heading text</td>
  </tr>
  <tr>
    <td><code>--ds-colour-text-inverse</code></td>
    <td>{% token '--ds-colour-text-inverse' %}</td>
    <td>Text on a dark background</td>
  </tr>
  <tr>
    <td><code>--ds-colour-link</code></td>
    <td>{% token '--ds-colour-link' %}</td>
    <td>Links and interactive text</td>
  </tr>
  <tr>
    <td><code>--ds-colour-action</code></td>
    <td>{% token '--ds-colour-action' %}</td>
    <td>Buttons and calls to action</td>
  </tr>
  <tr>
    <td><code>--ds-colour-action-inverse</code></td>
    <td>{% token '--ds-colour-action-inverse' %}</td>
    <td>The same, on a dark background</td>
  </tr>
  <tr>
    <td><code>--ds-colour-focus</code></td>
    <td>{% token '--ds-colour-focus' %}</td>
    <td>Keyboard focus outlines</td>
  </tr>
  <tr>
    <td><code>--ds-colour-background-page</code></td>
    <td>{% token '--ds-colour-background-page' %}</td>
    <td>The page background</td>
  </tr>
  <tr>
    <td><code>--ds-colour-background-panel</code></td>
    <td>{% token '--ds-colour-background-panel' %}</td>
    <td>Forms, tables and filters</td>
  </tr>
  <tr>
    <td><code>--ds-colour-background-inverse</code></td>
    <td>{% token '--ds-colour-background-inverse' %}</td>
    <td>Dark headers and footers</td>
  </tr>
  <tr>
    <td><code>--ds-colour-background-subtle</code></td>
    <td>{% token '--ds-colour-background-subtle' %}</td>
    <td>Code blocks and highlighted text</td>
  </tr>
  <tr>
    <td><code>--ds-colour-border</code></td>
    <td>{% token '--ds-colour-border' %}</td>
    <td>Card, form and table borders</td>
  </tr>
  <tr>
    <td><code>--ds-colour-border-inverse</code></td>
    <td>{% token '--ds-colour-border-inverse' %}</td>
    <td>Borders on a dark background</td>
  </tr>
  <tr>
    <td><code>--ds-colour-success</code></td>
    <td>{% token '--ds-colour-success' %}</td>
    <td>Success states</td>
  </tr>
  <tr>
    <td><code>--ds-colour-error</code></td>
    <td>{% token '--ds-colour-error' %}</td>
    <td>Errors and validation failures</td>
  </tr>
  <tr>
    <td><code>--ds-colour-info</code></td>
    <td>{% token '--ds-colour-info' %}</td>
    <td>Informational states</td>
  </tr>
</table>

{% note 'The partials have not moved across yet' %}

The design system’s own component styles still reference the Sass variables,
which resolve to the *primitive* properties. Moving them onto the semantic
properties is separate work — it is what will let `.ds-dark` become a handful
of property overrides instead of a rule per component.

{% endnote %}

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
