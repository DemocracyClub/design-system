---
title: Select
---

Democracy Club’s custom select components use the standard `<select>` element under the hood, and no JavaScript.

<div class="ds-scope">
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
</div>

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

## Dark theme

Invoke the dark theme on any component by applying `class="ds-dark"` to a container element.

<div class="ds-scope">
  <form class="ds-dark">
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
</div>