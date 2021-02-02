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

```html
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
```

Also note the use of `role="img"` and `aria-label="Error"` to ensure an appropriate accessible label for the ❌ icon.

## Submission errors

If the form is invalid upon submission, a message should be displayed. Importantly, if submission is handled with JavaScript (and without a page load) this message should appear directly above the submit button, so the user can see it without scrolling.

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
    <div role="alert">
      <div class="ds-error">
        <span role="img" aria-label="Error">❌</span> Your email or password is incorrect. <a href="#">Forgot your password?</a>
      </div>
    </div>
    <div class="ds-field">
      <button class="ds-button" type="submit">Log in</button>
    </div>
  </form>
</div>

In addition, it should be appended to an [ARIA live region](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/ARIA_Live_Regions). This will announce its content in screen readers, ensuring blind screen reader users are aware the error has been invoked. Note the `role="alert"` in the below example:

```html
<div role="alert">
  <div class="ds-error">
    <span role="img" aria-label="Error">❌</span> Your email or password is incorrect. <a href="#">Forgot your password?</a>
  </div>
</div>
```

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