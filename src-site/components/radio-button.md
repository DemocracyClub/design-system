---
title: Radio buttons
---

Sets of radio buttons come in a common fieldset and are labeled by the fieldset’s legend.

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

Each radio button is wrapped in a `<label>` with `class="ds-field-radio"` and the label text must be wrapped in a `<span>` for custom styling purposes.

We can use a [Stack]({{site.basedir}}/components/stack) component to space out each `class="ds-field-radio"` element (`class="ds-stack-smallest"`).

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

## Inline radio buttons

<div class="ds-scope">
  <form class="ds-cluster">
    <fieldset>
      <legend>Favorite type of democracy</legend>
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
    </fieldset>
  </form>
</div>

For inline radio buttons, we can use a [Cluster]({{site.basedir}}/components/cluster) component, like so:

```html
<div class="ds-cluster">
  <fieldset>
    <legend>Favorite type of democracy</legend>
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
  </fieldset>
</div>
```

## Dark theme

Invoke the dark theme on any component by applying `class="ds-dark"` to a container element.

<div class="ds-scope">
  <form class="ds-cluster ds-dark">
    <fieldset>
      <legend>Favorite type of democracy</legend>
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
    </fieldset>
  </form>
</div>