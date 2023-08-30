---
title: Select
---

Democracy Club’s custom select components use the standard `<select>` element under the hood, and no JavaScript.

{% ds-example %}

  <form>
    <div class="ds-field">
      <label for="select-example">Favorite type of democracy</label>
      <div class="ds-select">
        <select id="select-example" name="select-example">
          <option>Representative</option>
          <option>Direct</option>
          <option>Monitory</option>
        </select>
      </div>
    </div>
  </form>
{% endds-example %}


The following markup structure is needed. Remember to match the `for` and `id` values to ensure accessible labeling.

```html
<div class="ds-field">
  <label for="select-example">Favorite type of democracy</label>
  <div class="ds-select">
    <select id="select-example" name="select-example">
      <option>Representative</option>
      <option>Direct</option>
      <option>Monitory</option>
    </select>
  </div>
</div>
```
