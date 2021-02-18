---
title: Description lists
---

Use a description (or “definition”) list to highlight key information, such a contact details. Use a [Table]({{site.basedir}}/components/table) if the information is more complex than simple key/value pairs.

<div class="ds-scope">
  <section class="ds-card">
    <div class="ds-card-body">
      <h2 class="ds-candidate-name ds-h3">
        Vicky Ford online
      </h2>
      <dl class="ds-descriptions">
        <!-- row 1 -->
        <div>
          <dt>Facebook</dt>
          <div>
            <dd>
              <a href="https://www.facebook.com/vicky.ford.142" title="Vicky Ford's Facebook personal page">
                vicky.ford.142
              </a><br>
            </dd>
            <dd><a href="https://www.facebook.com/vicky4chelmsford" title="Vicky Ford's Facebook page">
                vicky4chelmsford
              </a>
            </dd>
          </div>
        </div>
        <!-- end row 1 -->
        <!-- row 2 -->
        <div>
          <dt>LinkedIn</dt>
          <dd>
            <a href="https://www.linkedin.com/in/vicky-ford/" title="Vicky Ford's LinkedIn profile">
              vicky-ford
            </a>
          </dd>
        </div>
        <!-- end row 2 -->
        <div>
          <dt>Home page</dt>
          <dd>
            <a href="http://www.vickyford.uk/" title="Vicky Ford's home page">
              http://www.vickyford.uk/
            </a>
          </dd>
        </div>
        <div>
          <dt>Instagram</dt>
          <dd>
            <a href="https://www.instagram.com/vickyfordmp" title="Vicky Ford's instagram">
              vickyfordmp
            </a>
          </dd>
        </div>
        <div>
          <dt>The party's candidate page for this person</dt>
          <dd>
            <a href="https://www.chelmsfordconservatives.co.uk/people/vicky-ford-mep" title="Party page for Vicky Ford">
              https://www.chelmsfordconservatives.co.uk/people/vicky-ford-mep
            </a>
          </dd>
        </div>
        <div>
          <dt>We don't know Vicky Ford's email address.</dt>
          <dd><a href="https://candidates.democracyclub.org.uk/person/34298/">Can you add it?</a></dd>
        </div>
      </dl>
    </div>
  </section>
</div>

## Markup

The container must be a `<dl>` and must have `class="ds-descriptions"`. Each row is wrapped in an unattributed `<div>`.

```html
<dl class="ds-descriptions">
  <div>
    <dt>Facebook</dt>
    <dd><a href="https://www.facebook.com/shaunbaileyuk">www.facebook.com/shaunbaileyuk</a></dd>
  </div>
  <div>
    <dt>Homepage</dt>
    <div>
      <dd><a href="https://shaunbailey.uk/">https://shaunbailey.uk</a></dd>
    </div>
  </div>
  <div>
    <dt>Instagram</dt>
    <dd><a href="https://www.instagram.com/shaunbaileyam/">https://www.instagram.com/shaunbaileyam</a></dd>
  </div>
  <div>
    <dt>Email</dt>
    <dd>shaunbailey@shaunbailey.co.uk</dd>
  </div>
</dl>
```

{% note 'Multiple definitions' %}

You are unlikely to need multiple definitions per definition title (`<dt>`). However, this is supported by allowing the wrapping of `<dd>`s in a nested `<div>`:

```html
<dl class="ds-descriptions">
  <div>
    <dt>Definition title</dt>
    <div>
      <dd>Definition 1</dd>
      <dd>Definition 2</dd>
    </div>
  </div>
</dl>
```

{% endnote %}