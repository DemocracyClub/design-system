---
title: Stack
---

Use the Stack to inject margin between adjacent elements along a vertical axis. This is preferred to adding margin directly to individual elements because the need for margin is a question of context.

You will more than likely want to use a Stack when dealing with any kind of flow content.

<table class="site-table">
  <tbody><tr>
    <th>Value</th>
    <th>Markup</th>
    <th>Demo</th>
  </tr>
  <tr>
    <td><code>$ss5</code> ({% var '$ss5' %})</td>
    <td>
<pre><code class="language-html">&lt;div class="ds-stack-smallest"&gt;
  &lt;div&gt;First element&lt;/div&gt;
  &lt;div&gt;Next element&lt;/div&gt;
&lt;/div&gt;
</code></pre>
  </td>
    <td class="ds-scope">
      <div class="ds-stack-smallest">
        <div class="site-box-dashed">First element</div>
        <div class="site-box-dashed">Next element</div>
      </div>
    </td>
  </tr>
  <tr>
    <td><code>$s3</code> ({% var '$s3' %})</td>
    <td>
<pre><code class="language-html">&lt;div class="ds-stack-smaller"&gt;
  &lt;div&gt;First element&lt;/div&gt;
  &lt;div&gt;Next element&lt;/div&gt;
&lt;/div&gt;
</code></pre>
  </td>
    <td class="ds-scope">
    <div class="ds-stack-smaller">
      <div class="site-box-dashed">First element</div>
      <div class="site-box-dashed">Next element</div>
    </div>
    </td>
  </tr>
  <tr>
    <td><code>$s6</code> ({% var '$s6' %})</td>
    <td>
<pre><code class="language-html">&lt;div class="ds-stack"&gt;
  &lt;div&gt;First element&lt;/div&gt;
  &lt;div&gt;Next element&lt;/div&gt;
&lt;/div&gt;
</code></pre>
  </td>
    <td class="ds-scope">
      <div class="ds-stack">
        <div class="site-box-dashed">First element</div>
        <div class="site-box-dashed">Next element</div>
      </div>
    </td>
  </tr>
  <tr>
    <td><code>$s8</code> ({% var '$s8' %})</td>
    <td>
<pre><code class="language-html">&lt;div class="ds-stack-larger"&gt;
  &lt;div&gt;First element&lt;/div&gt;
  &lt;div&gt;Next element&lt;/div&gt;
&lt;/div&gt;
</code></pre>
  </td>
    <td class="ds-scope">
      <div class="ds-stack-larger">
        <div class="site-box-dashed">First element</div>
        <div class="site-box-dashed">Next element</div>
      </div>
    </td>
  </tr>
</tbody>
</table>

{% note 'Paragraphs' %}

Paragraphs are immune to stack value variations. In all cases, successive paragraphs are separated by a value of `$s1` ({% var '$s1' %}). This is enforced using an `!important` marker.

```css
p + p {
  margin-top: $s1 !important;
}
```

{% endnote %}