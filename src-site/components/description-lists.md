---
title: Description lists
---

Use a description (or “definition”) list to highlight key information, such a contact details. Use a [Table]({{site.basedir}}/components/table) if the information is more complex than simple key/value pairs.

{% ds-example %}
<dl class="ds-descriptions">
    <div>
      <dt>Facebook</dt>
      <dd><a href="https://www.facebook.com/shaunbaileyuk">www.facebook.com/shaunbaileyuk</a></dd>
    </div>
    <div>
      <dt>Homepage</dt>
      <div>
        <dd><a href="https://shaunbailey.uk/">https://shaunbailey.uk</a></dd>
      </div>
    </div>
    <div>
      <dt>Instagram</dt>
      <dd><a href="https://www.instagram.com/shaunbaileyam/">https://www.instagram.com/shaunbaileyam</a></dd>
    </div>
    <div>
      <dt>Email</dt>
      <dd>shaunbailey@shaunbailey.co.uk</dd>
    </div>
  </dl>
{% endds-example %}


## Markup

The container must be a `<dl>` and must have `class="ds-descriptions"`. Each row is wrapped in an unattributed `<div>`.

```html
<dl class="ds-descriptions">
  <div>
    <dt>Facebook</dt>
    <dd><a href="https://www.facebook.com/shaunbaileyuk">www.facebook.com/shaunbaileyuk</a></dd>
  </div>
  <div>
    <dt>Homepage</dt>
    <div>
      <dd><a href="https://shaunbailey.uk/">https://shaunbailey.uk</a></dd>
    </div>
  </div>
  <div>
    <dt>Instagram</dt>
    <dd><a href="https://www.instagram.com/shaunbaileyam/">https://www.instagram.com/shaunbaileyam</a></dd>
  </div>
  <div>
    <dt>Email</dt>
    <dd>shaunbailey@shaunbailey.co.uk</dd>
  </div>
</dl>
```

{% note 'Multiple definitions' %}

You are unlikely to need multiple definitions per definition title (`<dt>`). However, this is supported by allowing the wrapping of `<dd>`s in a nested `<div>`:

```html
<dl class="ds-descriptions">
  <div>
    <dt>Definition title</dt>
    <div>
      <dd>Definition 1</dd>
      <dd>Definition 2</dd>
    </div>
  </div>
</dl>
```

{% endnote %}
