---
title: Modular scale
---

Both scales are defined as CSS custom properties in `tokens.css`. The Sass
variables still work — they are now aliases onto those properties — but new
code should use the custom properties directly. See
[CSS custom properties]({{site.basedir}}/basics/css-custom-properties) for the
background.

The scale is named `--ds-size-*` rather than `--ds-font-size-*` or
`--ds-space-*` because it is used for all three: font sizes, padding and
margins.

## Large scale

The large scale is designed for `font-size`, `padding`, and `margin`. It is a
modular scale with a ratio of `1.25`, ranging from `$s1` (`1rem`) up to `$s8`.

<table class="site-table">
  <tr>
    <th>Sass variable</th>
    <th>CSS property</th>
    <th>Value</th>
    <th>Demo</th>
  </tr>
  <tr>
    <td><code>$s1</code></td>
    <td><code>{% cssvar '$s1' %}</code></td>
    <td>{% var '$s1' %}</td>
    <td>
      <p class="site-nowrap ds-font-size-s1">A</p>
    </td>
  </tr>
  <tr>
    <td><code>$s2</code></td>
    <td><code>{% cssvar '$s2' %}</code></td>
    <td>{% var '$s2' %}</td>
    <td>
      <p class="site-nowrap ds-font-size-s2">A</p>
    </td>
  </tr>
  <tr>
    <td><code>$s3</code></td>
    <td><code>{% cssvar '$s3' %}</code></td>
    <td>{% var '$s3' %}</td>
    <td>
      <p class="site-nowrap ds-font-size-s3">A</p>
    </td>
  </tr>
  <tr>
    <td><code>$s4</code></td>
    <td><code>{% cssvar '$s4' %}</code></td>
    <td>{% var '$s4' %}</td>
    <td>
      <p class="site-nowrap ds-font-size-s4">A</p>
    </td>
  </tr>
  <tr>
    <td><code>$s5</code></td>
    <td><code>{% cssvar '$s5' %}</code></td>
    <td>{% var '$s5' %}</td>
    <td>
      <p class="site-nowrap ds-font-size-s5">A</p>
    </td>
  </tr>
  <tr>
    <td><code>$s6</code></td>
    <td><code>{% cssvar '$s6' %}</code></td>
    <td>{% var '$s6' %}</td>
    <td>
      <p class="site-nowrap ds-font-size-s6">A</p>
    </td>
  </tr>
  <tr>
    <td><code>$s7</code></td>
    <td><code>{% cssvar '$s7' %}</code></td>
    <td>{% var '$s7' %}</td>
    <td>
      <p class="site-nowrap ds-font-size-s7">A</p>
    </td>
  </tr>
  <tr>
    <td><code>$s8</code></td>
    <td><code>{% cssvar '$s8' %}</code></td>
    <td>{% var '$s8' %}</td>
    <td>
      <p class="site-nowrap ds-font-size-s8">A</p>
    </td>
  </tr>
</table>

## Small scale

The small scale is designed for `border`, `outline`, and smaller (hairline) spaces. It ranges from `$ss1` (`0.125rem`) to `$ss8` (`1rem`; equal to `$s1`).

<table class="site-table">
  <tr>
    <th>Sass variable</th>
    <th>CSS property</th>
    <th>Value</th>
    <th>Demo</th>
  </tr>
  <tr>
    <td><code>$ss1</code></td>
    <td><code>{% cssvar '$ss1' %}</code></td>
    <td>{% var '$ss1' %}</td>
    <td>
      <div class="site-block-black ds-height-ss1"></div>
    </td>
  </tr>
  <tr>
    <td><code>$ss2</code></td>
    <td><code>{% cssvar '$ss2' %}</code></td>
    <td>{% var '$ss2' %}</td>
    <td>
      <div class="site-block-black ds-height-ss2"></div>
    </td>
  </tr>
  <tr>
    <td><code>$ss3</code></td>
    <td><code>{% cssvar '$ss3' %}</code></td>
    <td>{% var '$ss3' %}</td>
    <td>
      <div class="site-block-black ds-height-ss3"></div>
    </td>
  </tr>
  <tr>
    <td><code>$ss4</code></td>
    <td><code>{% cssvar '$ss4' %}</code></td>
    <td>{% var '$ss4' %}</td>
    <td>
      <div class="site-block-black ds-height-ss4"></div>
    </td>
  </tr>
  <tr>
    <td><code>$ss5</code></td>
    <td><code>{% cssvar '$ss5' %}</code></td>
    <td>{% var '$ss5' %}</td>
    <td>
      <div class="site-block-black ds-height-ss5"></div>
    </td>
  </tr>
  <tr>
    <td><code>$ss6</code></td>
    <td><code>{% cssvar '$ss6' %}</code></td>
    <td>{% var '$ss6' %}</td>
    <td>
      <div class="site-block-black ds-height-ss6"></div>
    </td>
  </tr>
  <tr>
    <td><code>$ss7</code></td>
    <td><code>{% cssvar '$ss7' %}</code></td>
    <td>{% var '$ss7' %}</td>
    <td>
      <div class="site-block-black ds-height-ss7"></div>
    </td>
  </tr>
  <tr>
    <td><code>$ss8</code></td>
    <td><code>{% cssvar '$ss8' %}</code></td>
    <td>{% var '$ss8' %}</td>
    <td>
      <div class="site-block-black ds-height-ss8"></div>
    </td>
  </tr>
</table>

## Semantic font sizes

The heading sizes are also exposed by role. Each heading element additionally
applies a `clamp()` for fluid sizing, so these are the upper bound rather than
the size rendered at every viewport width.

<table class="site-table">
  <tr>
    <th>CSS property</th>
    <th>Value</th>
    <th>Used for</th>
  </tr>
  <tr>
    <td><code>--ds-font-size-body</code></td>
    <td>{% token '--ds-font-size-body' %}</td>
    <td>Body copy</td>
  </tr>
  <tr>
    <td><code>--ds-font-size-heading-1</code></td>
    <td>{% token '--ds-font-size-heading-1' %}</td>
    <td><code>h1</code></td>
  </tr>
  <tr>
    <td><code>--ds-font-size-heading-2</code></td>
    <td>{% token '--ds-font-size-heading-2' %}</td>
    <td><code>h2</code></td>
  </tr>
  <tr>
    <td><code>--ds-font-size-heading-3</code></td>
    <td>{% token '--ds-font-size-heading-3' %}</td>
    <td><code>h3</code></td>
  </tr>
  <tr>
    <td><code>--ds-font-size-heading-4</code></td>
    <td>{% token '--ds-font-size-heading-4' %}</td>
    <td><code>h4</code></td>
  </tr>
  <tr>
    <td><code>--ds-font-size-heading-5</code></td>
    <td>{% token '--ds-font-size-heading-5' %}</td>
    <td><code>h5</code></td>
  </tr>
  <tr>
    <td><code>--ds-font-size-heading-6</code></td>
    <td>{% token '--ds-font-size-heading-6' %}</td>
    <td><code>h6</code></td>
  </tr>
</table>

{% note 'Creating new points' %}

It is okay to create new scale points on the fly, if needed. But they should be
based on the existing scales’ algorithms. To create a 9th step in the large
scale, multiply the last step by the ratio using `calc()`.

```css
.ds-font-size-s9 {
  font-size: calc(var(--ds-size-8) * 1.25);
}
```

Note that Sass arithmetic such as `$s8 * $ratio` no longer works: the Sass
variables hold `var()` references rather than lengths, so the multiplication
has to happen in CSS.

{% endnote %}
