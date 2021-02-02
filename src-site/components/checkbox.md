---
title: Checkbox
---

Democracy club has custom checkbox styling 🙌.

<div class="ds-scope">
  <form>
    <label class="ds-field-checkbox">
      <input type="checkbox" name="agree" checked>
      <span>I agree</span>
    </label>
  </form>
</div>

But this needs you to use the following markup structure. Note the `ds-field-checkbox` class and the `<span>` wrapping the label text.

```html
<label class="ds-field-checkbox">
  <input type="checkbox" name="agree" checked>
  <span>I agree</span>
</label>
```

## Dark theme

Invoke the dark theme on any component by applying `class="ds-dark"` to a container element.

<div class="ds-scope">
  <form class="ds-dark">
    <label class="ds-field-checkbox">
      <input type="checkbox" name="agree" checked>
      <span>I agree</span>
    </label>
  </form>
</div>

