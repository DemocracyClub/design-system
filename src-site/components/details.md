---
title: Details
---

Use `<details>` and `<summary>` to summarize longform content and make it easier to locate sections. If you have multiple sections, wrap the `<details>` elements in a list, using `class="ds-details"` on the `<ul>`.

{% ds-example %}

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
{% endds-example %}


It’s recommended each `<summary>` element contains a heading of the appropriate level for the surrounding document structure. This makes it easier for screen reader users to navigate between details elements / subsections.

```html
<ul class="ds-details">
  <li>
    <details>
      <summary>
        <h2>Where to vote</h2>
      </summary>
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
  <p>This should be visible as the user arrives on the page.</p>
</details>
```

{% ds-example %}

  <details open>
    <summary>
      <h2>I should be open already</h2>
    </summary>
    <p>This should be visible as the user arrives on the page.</p>
  </details>
{% endds-example %}


{% endnote %}

## Details inside `<blockquote>`s

To truncate candidate statements, you can use a Details component with the summary label “Full statement”:

{% ds-example %}
<blockquote class="ds-stack-smaller">
    <p>To stand again as the UKIP candidate for Redcar is fantastic and reflects the fact I was born in Middlesbrough.</p>
    <details>
      <summary>Full statement</summary>
      <p>I work, run my business, and live in the constituency. What also makes me unique among the other candidates is my military service, having served in both the Regular Army and what is now the Reserve for forty two years.</p>
    </details>
  </blockquote>
{% endds-example %}
