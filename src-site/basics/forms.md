---
title: Forms
---

Basic form styles are provided automatically. Each input/field should be organized inside a `class="dc-field"` element.

```html
<div class="ds-field">
  <label for="username">
    Username
    <small>Or enter your email address</small>
  </label>
  <input type="text" id="username">
</div>
```

Note the use of the `<small>` element to provide “hint” text to the label. Placing the hint text inside the `<label>` ensures it is not missed by screen reader users.

## Basic example

Each input must be associated to its label by making their respective `id` and `for` attributes share the same value.

<div class="ds-scope">
  <form>
    <div class="ds-field">
      <label for="username">
        Username
        <small>Or enter your email address</small>
      </label>
      <input type="text" id="username">
    </div>
    <div class="ds-field">
      <label for="password">
        Password
      </label>
      <input type="password" id="password">
    </div>
    <div class="ds-field">
      <button class="ds-button" type="submit">Log in</button>
    </div>
  </form>
</div>

## Invalid fields

For accessibility, each invalid field must have

* `aria-invalid="true"`
* An error message associated to the input with `aria-describedby` and placed below the input
* An cross emoji prefixed to the error message with alternative text reading “error”

<div class="ds-scope">
  <form>
    <div class="ds-field">
      <label for="username">
        Username
        <small>Or enter your email address</small>
      </label>
      <input type="text" id="username" aria-invalid="true" aria-describedby="username-error">
      <small class="ds-field-error" id="username-error">
        <span role="img" aria-label="Error">❌</span>
        Your username must be more than one character
      </small>
    </div>
  </form>
</div>

Field errors are `<small>` elements with `class="ds-field-error"`. Their `id` value must match the input’s `aria-describedby` value.

## Fieldsets

Fieldsets are useful for grouping fields together under a group label (`<legend>`). In fact, fieldsets/legends are the recommended way to label groups of radio buttons. The legend must be the first child element inside the fieldset.

<div class="ds-scope">
  <form>
    <fieldset>
      <legend>Favorite type of democracy</legend>
      <div class="ds-stack-smallest">
        <label class="ds-field-radio">
          <input type="radio" name="democracy" checked>
          <span>Representative</span>
        </label>
        <label class="ds-field-radio">
          <input type="radio" name="democracy">
          <span>Direct</span>
        </label>
        <label class="ds-field-radio">
          <input type="radio" name="democracy">
          <span>Monitory</span>
        </label>
      </div>
    </fieldset>
  </form>
</div>

```html
<fieldset>
  <legend>Favorite type of democracy</legend>
  <div class="ds-stack-smallest">
    <label class="ds-field-radio">
      <input type="radio" name="democracy" checked>
      <span>Representative</span>
    </label>
    <label class="ds-field-radio">
      <input type="radio" name="democracy">
      <span>Direct</span>
    </label>
    <label class="ds-field-radio">
      <input type="radio" name="democracy">
      <span>Monitory</span>
    </label>
  </div>
</fieldset>
```

{% note 'Stack spacing' %}

Note the use of the [Stack]({{site.basedir}}/components/stack) component (`class="ds-stack-smallest"`) to space out each `class="ds-field-radio"` element.

{% endnote %}