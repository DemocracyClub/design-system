---
title: Radio buttons
---

Sets of radio buttons come in a common fieldset and are labeled by the fieldset’s legend.

{% ds-example %}
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
{% endds-example %}


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

{% ds-example %}

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
{% endds-example %}


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
