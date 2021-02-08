---
title: Details
---

The Details component wraps a set of standard `<details>` elements in an unordered list. Use this component to summarize longform content and make it easier to locate sections.

<div class="ds-scope">
  <ul class="ds-details">
    <li>
      <details>
        <summary><h2>Where to vote</h2></summary>
        <p>At your local polling station</p>
      </details>
    </li>
    <li>
      <details>
        <summary><h2>How do I vote</h2></summary>
        <p>This election uses Single Transferable Vote.</p >
        <p>Rank the candidates by your preference: 1, 2, 3… You don't have to rank all the candidates, but you must at least mark your first choice.</p>
        <p>Read the instructions at the top of your ballot paper carefully.</p>
      </details>
    </li>
  </ul>
</div>

Note the `class="ds-details"` class on the containing `<ul>`. It’s recommended each `<summary>` element contains a heading of the appropriate level for the surrounding document structure. This makes it easier for screen reader users to navigate between details elements / subsections.

```html
<ul class="ds-details">
  <li>
    <details>
      <summary><h2>Where to vote</h2></summary>
      <p>At your local polling station</p>
    </details>
  </li>
  <li>
    <details>
      <summary>
        <h2>How do I vote</h2>
      </summary>
      <p>This election uses Single Transferable Vote.</p >
      <p>Rank the candidates by your preference: 1, 2, 3… You don't have to rank all the candidates, but you must at least mark your first choice.</p>
      <p>Read the instructions at the top of your ballot paper carefully.</p>
    </details>
  </li>
</ul>
```

{% note 'Open by default' %}

In some cases, it might be pertinent to have a Details component open by default. You can use the `open` property for this.

```html
<details open>
  <summary>
    <h2>I should be open already</h2>
  </summary>
  <p>This should be visible as the user arrives on the page</p>
</details>
```

<details open>
  <summary>
    <h2>I should be open already</h2>
  </summary>
  <p>This should be visible as the user arrives on the page</p>
</details>

{% endnote %}