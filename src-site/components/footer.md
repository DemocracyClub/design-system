---
title: Footer
---

Use the Footer component to add quick links, company, and contact information to the foot of a page.

A basic footer looks something like the following (as seen in [the page layout demo]({{site.basedir}}/layout-demo/). All the `ds-footer` class does is add some padding, the blue top border, and extend the [Dark theme]({{site.basedir}}/basics/dark).

Aside from that, `ds-copyright` and `ds-footer-links` are unique to this 
component. The content of the footer can be constructed from other components according 
to your needs. In the following example, a list of “quick links” is provided alongside the copyright.

Footers should be wrapped in a `<div data-nosnippet>` to stop google from using the content in [snippets](https://developers.google.com/search/docs/appearance/snippet).

{% ds-example %}

<footer class="ds-footer">
    <a class="ds-logo" href="https://democracyclub.org.uk/">
        <img src="{{site.basedir}}/images/logo_icon.svg" alt="Democracy Club" width='80'/>
    </a>
    <div class="ds-footer-links"> 
        <nav>
          <h2>ProjectName</h2>
          <ul>
            <li>
              <a href="#">Home</a>
            </li>
            <li>
              <a href="#">About</a>
            </li>
            <li>
              <a href="#">Our work</a>
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
        </nav>
        <nav>
          <h2>About</h2>
          <ul>
            <li>
              <a href="#">Home</a>
            </li>
            <li>
              <a href="#">About</a>
            </li>
            <li>
              <a href="#">Our work</a>
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
        </nav>
        <nav>
          <h2>Contact</h2>
          <ul>
            <li>
              <a href="#">Email</a>
            </li>
            <li>
              <a href="#">Mastodon</a>
            </li>
            <li>
              <a href="#">LinkedIn</a>
            </li>
          </ul>
        </nav>
      </div>
      <div class="ds-copyright">
        <p>Democracy Club is a UK-based Community Interest Company that builds digital infrastructure for a 21st century democracy.</p>
        <p>Copyright © 2024 Democracy Club Community Interest Company No: <a href="https://beta.companieshouse.gov.uk/company/09461226">09461226</a></p>
      </div>
</footer>
{% endds-example %}


## Markup

```html
<div data-nosnippet>
  <footer class="ds-footer">
    <a class="ds-logo" href="https://democracyclub.org.uk/">
        <img src="{{site.basedir}}/images/logo_icon.svg" alt="Democracy Club" width='80'/>
    </a>
    <div class="ds-footer-links"> 
        <nav>
          <h2>ProjectName</h2>
          <ul>
            <li>
              <a href="#">Home</a>
            </li>
            <li>
              <a href="#">About</a>
            </li>
            <li>
              <a href="#">Our work</a>
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
        </nav>
        <nav>
          <h2>About</h2>
          <ul>
            <li>
              <a href="#">Home</a>
            </li>
            <li>
              <a href="#">About</a>
            </li>
            <li>
              <a href="#">Our work</a>
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
        </nav>
        <nav>
          <h2>Contact</h2>
          <ul>
            <li>
              <a href="#">Email</a>
            </li>
            <li>
              <a href="#">Mastodon</a>
            </li>
            <li>
              <a href="#">LinkedIn</a>
            </li>
          </ul>
        </nav>
      </div>
      <div class="ds-copyright">
        <p>Democracy Club is a UK-based Community Interest Company that builds digital infrastructure for a 21st century democracy.</p>
        <p>Copyright © 2024 Democracy Club Community Interest Company No: <a href="https://beta.companieshouse.gov.uk/company/09461226">09461226</a></p>
      </div>
  </footer>
</div>
```
