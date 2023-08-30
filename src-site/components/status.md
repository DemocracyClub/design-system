---
title: Status
---

Use a status component to keep users informed of the changing state of the site and the status of tasks they’ve undertaken using the site. You can include multiple status messages of different varieties (`ds-status-message` (standard), `ds-status-success`, `ds-status-error`) within the `ds-status` element.

{% ds-example %}

  <aside class="ds-status" aria-label="Status">
    <ul class="ds-stack-smallest">
      <li class="ds-status-message">A basic status message</li>
      <li class="ds-status-success">A success message</li>
      <li class="ds-status-error">An error message</li>
    </ul>
  </aside>
{% endds-example %}


## Markup

The status component is a simple `<aside>` with the label “Status” which collects status messages together in a list. Successive status messages are separated by applying `ds-stack-smallest` to the `<ul>` element.

```html
<aside class="ds-status" aria-label="Status">
  <ul class="ds-stack">
    <li class="ds-status-message">A basic status message</li>
    <li class="ds-status-success">A success message</li>
    <li class="ds-status-error">An error message</li>
  </ul>
</aside>
```

The status component should typically be added to the page just below the `<h1>` (main) heading. See the [layout demo]({{site.basedir}}/layout-demo).
