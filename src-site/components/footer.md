---
title: Footer
---

Use the Footer component to add quick links, company, and contact information to the foot of a page.

A basic footer looks something like the following (as seen in [the page layout demo]({{site.basedir}}/layout-demo/). All the `ds-footer` class does is add some padding, the blue top border, and extend the [Dark theme]({{site.basedir}}/basics/dark).

Aside from that, only `ds-copyright` is unique to this component. The content of the footer can be constructed from other components according to your needs. In the following example, a list of “quick links” is provided alongside the copyright.

{% ds-example %}
  <footer class="ds-footer">
    <div class="ds-block-centered ds-text-centered ds-stack">
      <div class="ds-cluster-center">
        <ul>
          <li>
            <a href="/">Home</a>
          </li>
          <li>
            <a aria-current="true" href=".path/to/about">About</a>
          </li>
          <li>
            <a href="/path/to/">Our work</a>
          </li>
          <li>
            <a href="#">Quests</a>
          </li>
          <li>
            <a href="#">Blog</a>
          </li>
          <li>
            <a href="#">Contact</a>
          </li>
          <li>
            <a href="#">Donate</a>
          </li>
        </ul>
      </div>
      <div class="ds-copyright">
        <a class="ds-logo" href="https://democracyclub.org.uk/">
            <img src="{{site.basedir}}/images/logo_icon.svg" alt="Democracy Club" width='80'/>
            <span class="ds-text-left">democracy<br>club</span>
        </a>
        <p>Copyright © 2021 Democracy Club</p>
        <p>Community Interest Company</p>
        <p>Company No: <a href="https://beta.companieshouse.gov.uk/company/09461226">09461226</a></p>
      </div>
    </div>
  </footer>
{% endds-example %}


## Markup

The unique class names for this component are the containing `ds-footer` and `ds-copyright`. Everything else, including the dark theme, the “clustered” navigation and the center alignment is achieved with other component helpers and utilities.

```html
<footer class="ds-footer">
  <div class="ds-block-centered ds-text-centered ds-stack">
    <div class="ds-cluster-center">
      <ul>
        <!-- list items -->
      </ul>
    </div>
    <div class="ds-copyright">
      <a href="https://democracyclub.org.uk/">
        <img src="{{site.basedir}}/images/logo_white_text.svg" alt="Democracy Club Home" />
        <span>democracy<br>club</span>
      </a>
      <p>Copyright © 2021 Democracy Club</p>
      <p>Community Interest Company</p>
      <p>Company No: <a href="https://beta.companieshouse.gov.uk/company/09461226">09461226</a></p>
    </div>
  </div>
</footer>
```
