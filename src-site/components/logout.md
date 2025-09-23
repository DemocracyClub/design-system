---
title: Logout
---

Django uses HTTP POST for logging users out. This generally a good idea
because browsers can 'pre-fetch' links on pages, or malicious actors could
log users out using XSS attacks on other sites.

However, from a user's point of view, 'log out' should look the same as 'log
in'. We use links for logging in (the link goes to a login form), so for
consistency we want the logout button to look the same.

{% ds-example %}

<form class="ds-logout">
    <button type="submit">Logout</button>
</form>

{% endds-example %}

```html

<form class="ds-logout">
    <button type="submit">Logout</button>
</form>
```

## In a header

A `ds-logout` can be used inside a list element in the header component. 

{% ds-example %}

<div data-nosnippet>
  <header class="ds-header">
    <a class="ds-skip-link" href="#main">skip to content</a>
    <nav>
      <ul>
        <li>
          <a href="#">Home</a>
        </li>
        <li>
          <a aria-current="true" href="#">About</a>
        </li>
        <li>
          <a href="#">Contact</a>
        </li>
        <li>
          <form class="ds-logout">
            <button type="submit">Logout</button>
          </form>
        </li>
      </ul>
    </nav>
  </header>
</div>
{% endds-example %}
