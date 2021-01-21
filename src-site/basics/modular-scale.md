---
title: Modular scale
---

## Large scale

The large scale is designed for `font-size`, `padding`, and `margin`. It ranges from `$s1` (`1rem`) up to `$s8`:

<table class="site-table">
  <tr>
    <th>Token</th>
    <th>Value</th>
    <th>Demo</th>
  </tr>
  <tr>
    <td><code>$s1</code></td>
    <td>{% var '$s1' %}</td>
    <td>
      <p class="site-nowrap ds-font-size-s1">A</p>
    </td>
  </tr>
  <tr>
    <td><code>$s2</code></td>
    <td>{% var '$s2' %}</td>
    <td>
      <p class="site-nowrap ds-font-size-s2">A</p>
    </td>
  </tr>
  <tr>
    <td><code>$s3</code></td>
    <td>{% var '$s3' %}</td>
    <td>
      <p class="site-nowrap ds-font-size-s3">A</p>
    </td>
  </tr>
  <tr>
    <td><code>$s4</code></td>
    <td>{% var '$s4' %}</td>
    <td>
      <p class="site-nowrap ds-font-size-s4">A</p>
    </td>
  </tr>
  <tr>
    <td><code>$s5</code></td>
    <td>{% var '$s5' %}</td>
    <td>
      <p class="site-nowrap ds-font-size-s5">A</p>
    </td>
  </tr>
  <tr>
    <td><code>$s6</code></td>
    <td>{% var '$s6' %}</td>
    <td>
      <p class="site-nowrap ds-font-size-s6">A</p>
    </td>
  </tr>
  <tr>
    <td><code>$s7</code></td>
    <td>{% var '$s7' %}</td>
    <td>
      <p class="site-nowrap ds-font-size-s7">A</p>
    </td>
  </tr>
  <tr>
    <td><code>$s8</code></td>
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
    <th>Token</th>
    <th>Value</th>
    <th>Demo</th>
  </tr>
  <tr>
    <td><code>$ss1</code></td>
    <td>{% var '$ss1' %}</td>
    <td>
      <div class="site-block-black ds-height-ss1"></div>
    </td>
  </tr>
  <tr>
    <td><code>$ss2</code></td>
    <td>{% var '$ss2' %}</td>
    <td>
      <div class="site-block-black ds-height-ss2"></div>
    </td>
  </tr>
  <tr>
    <td><code>$ss3</code></td>
    <td>{% var '$ss3' %}</td>
    <td>
      <div class="site-block-black ds-height-ss3"></div>
    </td>
  </tr>
  <tr>
    <td><code>$ss4</code></td>
    <td>{% var '$ss4' %}</td>
    <td>
      <div class="site-block-black ds-height-ss4"></div>
    </td>
  </tr>
  <tr>
    <td><code>$ss5</code></td>
    <td>{% var '$ss5' %}</td>
    <td>
      <div class="site-block-black ds-height-ss5"></div>
    </td>
  </tr>
  <tr>
    <td><code>$ss6</code></td>
    <td>{% var '$ss6' %}</td>
    <td>
      <div class="site-block-black ds-height-ss6"></div>
    </td>
  </tr>
  <tr>
    <td><code>$ss7</code></td>
    <td>{% var '$ss7' %}</td>
    <td>
      <div class="site-block-black ds-height-ss7"></div>
    </td>
  </tr>
  <tr>
    <td><code>$ss8</code></td>
    <td>{% var '$ss8' %}</td>
    <td>
      <div class="site-block-black ds-height-ss8"></div>
    </td>
  </tr>
</table>

{% note 'Creating new points' %}

It is okay to create new scale points on the fly, if needed. But they should be based on the existing scales’ algorithms. To create a 9th step in the large scale, use Sass’s multiplication operator.

```css
.ds-font-size-s9 {
  font-size: $s8 * $ratio;
}
```

{% endnote %}