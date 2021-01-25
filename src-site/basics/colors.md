---
title: Colors
---

<table class="site-table">
  <tr>
    <th>Token</th>
    <th>Value</th>
    <th>Demo</th>
  </tr>
  <tr>
    <td><code>$black</code></td>
    <td>{% var '$black' %}</td>
    <td>
      <div class="site-swatch ds-bg-color-black"></div>
    </td>
  </tr>
  <tr>
    <td><code>$blackOpacity</code></td>
    <td>{% var '$blackOpacity' %}</td>
    <td>
      <div class="site-swatch ds-bg-color-blackOpacity"></div>
    </td>
  </tr>
  <tr>
    <td><code>$white</code></td>
    <td>{% var '$white' %}</td>
    <td>
      <div class="site-swatch ds-bg-color-white"></div>
    </td>
  </tr>
  <tr>
    <td><code>$pinkForWhite</code></td>
    <td>{% var '$pinkForWhite' %}</td>
    <td>
      <div class="site-swatch ds-bg-color-pinkForWhite"></div>
    </td>
  </tr>
  <tr>
    <td><code>$blueForWhite</code></td>
    <td>{% var '$blueForWhite' %}</td>
    <td>
      <div class="site-swatch ds-bg-color-blueForWhite"></div>
    </td>
  </tr>
  <tr>
    <td><code>$blueForBlack</code></td>
    <td>{% var '$blueForBlack' %}</td>
    <td>
      <div class="site-swatch ds-bg-color-blueForBlack"></div>
    </td>
  </tr>
  <tr>
    <td><code>$greenForWhite</code></td>
    <td>{% var '$greenForWhite' %}</td>
    <td>
      <div class="site-swatch ds-bg-color-greenForWhite"></div>
    </td>
  </tr>
  <tr>
    <td><code>$greenForBlack</code></td>
    <td>{% var '$greenForBlack' %}</td>
    <td>
      <div class="site-swatch ds-bg-color-greenForBlack"></div>
    </td>
  </tr>
  <tr>
    <td><code>$amber</code></td>
    <td>{% var '$amber' %}</td>
    <td>
      <div class="site-swatch ds-bg-color-amber"></div>
    </td>
  </tr>
</table>

## Accessible pairings

As the names suggest, the “forWhite” colors can be safely paired with `$white` and the “forBlack” colors can be safely paired with `$black`. For example:

```css
.ds-my-component {
  color: $white;
  background-color: $greenForWhite;
}

.ds-my-component-reversed {
  color: $greenForWhite;
  background-color: $white;
}
```

The is no `$pinkForBlack` because we tried to make one and it looked _gross_.