---
title: Checkbox
---

Democracy club has custom checkbox styling 🙌.

{% ds-example %}

  <form>
    <label class="ds-field-checkbox">
      <input type="checkbox" name="agree" checked>
      <span>I agree</span>
    </label>
  </form>
{% endds-example %}


But this needs you to use the following markup structure. Note the `ds-field-checkbox` class and the `<span>` wrapping the label text.

```html
<label class="ds-field-checkbox">
  <input type="checkbox" name="agree" checked>
  <span>I agree</span>
</label>
```
