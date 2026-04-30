---
title: Input
---

HTML has many special [input types](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input).
Remember to use the correct input type for the information you are collecting.

{% ds-example %}
<form>
  <div class="ds-field">
    <label for="example-input-email">Email address</label>
    <input type="email" id="example-input-email">
  </div>
  <div class="ds-field">
    <label for="example-input-number">Number</label>
    <input type="number" id="example-input-number">
  </div>
  <div class="ds-field">
    <label for="example-input-password">Password</label>
    <input type="password" id="example-input-password">
  </div>
  <div class="ds-field">
    <label for="example-input-search">Search</label>
    <input type="search" id="example-input-search">
  </div>
  <div class="ds-field">
    <label for="example-input-tel">Telephone number</label>
    <input type="tel" id="example-input-tel">
  </div>
  <div class="ds-field">
    <label for="example-input-text">Text</label>
    <input type="text" id="example-input-text">
  </div>
  <div class="ds-field">
    <label for="example-input-readonly">Read-only</label>
    <input type="text" id="example-input-readonly" readonly value="Can't touch this!">
  </div>
  <div class="ds-field">
    <label for="example-input-disabled">Disabled</label>
    <input type="text" id="example-input-disabled" disabled value="Not available">
  </div>
  <div class="ds-field">
    <label for="example-input-url">URL</label>
    <input type="url" id="example-input-url">
  </div>
</form>
{% endds-example %}

```html
<div class="ds-field">
  <label for="example-input-text">Text</label>
  <input type="text" id="example-input-text">
</div>
```
