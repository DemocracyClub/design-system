---
title: Logo
---

The logo component is a link back to the local site’s homepage, most commonly included in the [Header]({{site.basedir}}/components/header). This text-based logo replaces purely image-based versions for ease of translation.

{% ds-example %}

  <div class="ds-stack-smaller">
    <div>
      <a class="ds-logo" href="/">
        <img src="{{site.basedir}}/images/logo_icon.svg" alt="" />
        <span>democracy<br>club</span>
      </a>
    </div>
    <div>
      <a class="ds-logo" href="/">
        <img src="{{site.basedir}}/images/logo_icon.svg" alt="" />
        <span>Who Can I Vote For?</span>
      </a>
    </div>
    <div>
      <a class="ds-logo" href="/">
        <img src="{{site.basedir}}/images/logo_icon.svg" alt="" />
        <span>Where Do I Vote?</span>
      </a>
    </div>
  </div>
{% endds-example %}


## Markup

Since the text itself acts as the accessible label for the `ds-logo` link, the check mark graphic can be considered decorative. Therefore, it is supplied an empty `alt` string to suppress its readout in screen readers.

```html
<a class="ds-logo" href="/">
  <img src="{{site.basedir}}/images/logo_icon.svg" alt="" />
  <span>democracy club</span>
</a>
```

### Welsh variant

{% ds-example %}

  <a class="ds-logo" href="/">
    <img src="{{site.basedir}}/images/logo_icon.svg" alt="" />
    <span>
      Where Do I Vote?
      <em lang="cy">Ble Ydw i’n Pleidleisio?</em>
    </span>
  </a>
{% endds-example %}


Welsh versions of the logo should be in English _and_ Welsh, using an `<em>` element to encapsulate the Welsh translation. The `<em>` needs to take `lang="cy"`.

```html
<a class="ds-logo" href="/">
  <img src="{{site.basedir}}/images/logo_icon.svg" alt="" />
  <span>
    Where Do I Vote?
    <em lang="cy">Ble Ydw i’n Pleidleisio?</em>
  </span>
</a>
```
