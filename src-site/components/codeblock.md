---
title: Code block
---

When sharing blocks of code, you have two formatting options: _wrapping_ or _scrolling_.

## Wrapping code

This is the default, using `class="ds-codeblock"`.

<div class="ds-scope">
<pre class="ds-codeblock"><code>{
  "notifications": [
    {
      "url": "http://www.eoni.org.uk/Vote/Voting-at-a-polling-place",
      "title": "You need to show photographic ID to vote in this election",
      "detail": "Voters in Northern Ireland are required to show one form of photo ID, like a passport or driving licence.",
      "type": "voter_id"
    }
  ]
}</code></pre>
</div>

```html
<pre class="ds-codeblock"><code>{
  "notifications": [
    {
      "url": "http://www.eoni.org.uk/Vote/Voting-at-a-polling-place",
      "title": "You need to show photographic ID to vote in this election",
      "detail": "Voters in Northern Ireland are required to show one form of photo ID, like a passport or driving licence.",
      "type": "voter_id"
    }
  ]
}</code></pre>
```

{% note 'Are you confused?' %}

To be clear, the black code blocks here are part of the documentation _for_ code blocks. The grey code blocks are what you’ll actually see in the product/site. 😬

{% endnote %}

## Scrolling code

Add `class="ds-codeblock-scroll"`. This option may be better for readability for some kinds of code.

<div class="ds-scope">
<pre class="ds-codeblock ds-codeblock-scroll"><code>{
  "notifications": [
    {
      "url": "http://www.eoni.org.uk/Vote/Voting-at-a-polling-place",
      "title": "You need to show photographic ID to vote in this election",
      "detail": "Voters in Northern Ireland are required to show one form of photo ID, like a passport or driving licence.",
      "type": "voter_id"
    }
  ]
}</code></pre>
</div>

```html
<pre class="ds-codeblock ds-codeblock-scroll"><code>{
  "notifications": [
    {
      "url": "http://www.eoni.org.uk/Vote/Voting-at-a-polling-place",
      "title": "You need to show photographic ID to vote in this election",
      "detail": "Voters in Northern Ireland are required to show one form of photo ID, like a passport or driving licence.",
      "type": "voter_id"
    }
  ]
}</code></pre>
```

## Inline code

Snippets of inline code (placed in paragraphs, typically) are styled by default. Just use the `<code>` tag:

<div class="ds-scope">
  <p>Let me tell you about the <code>$variable</code> I came up with.</p>
</div>