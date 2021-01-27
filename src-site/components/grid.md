---
title: Grid
---

The Grid component progressively enhances a single column layout (with basic [Stack]({{site.basedir}}/components/stack)-like spacing) into a configurable CSS Grid layout.

<div class="ds-scope site-resizer">
  <div class="ds-grid">
    <div class="ds-card">
      <div class="ds-card-body ds-stack">
        <h3><a href="#" class="ds-card-link">Card 1</a></h3>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quas, quae eos laboriosam vero aliquid quam soluta ad officiis quia omnis molestiae optio dolore nesciunt tempora? Dolor doloremque illum quasi exercitationem?<p>
      </div>
    </div>
    <div class="ds-card">
      <div class="ds-card-body ds-stack">
        <h3><a href="#" class="ds-card-link">Card 2</a></h3>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo qui delectus eos sapiente. Necessitatibus quis ratione praesentium esse culpa accusantium est, tempore qui deleniti molestias fugit doloremque debitis tempora illum.</p>
      </div>
    </div>
    <div class="ds-card">
      <div class="ds-card-body ds-stack">
        <h3><a href="#" class="ds-card-link">Card 3</a></h3>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse laboriosam recusandae illo non accusamus vero cupiditate aspernatur incidunt nostrum, commodi quos dicta ducimus quidem debitis et reiciendis dolores minima velit.</p>
      </div>
    </div>
    <div class="ds-card">
      <div class="ds-card-body ds-stack">
        <h3><a href="#" class="ds-card-link">Card 4</a></h3>
        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quae eum, id perspiciatis explicabo soluta enim debitis dicta? Quia molestiae at odio perspiciatis veniam illo nisi quis, necessitatibus, nam et accusamus!</p>
      </div>
    </div>
    <div class="ds-card">
      <div class="ds-card-body ds-stack">
        <h3><a href="#" class="ds-card-link">Card 5</a></h3>
        <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Laudantium temporibus commodi, voluptatum nisi accusantium voluptate quaerat. Sapiente, placeat cumque. Quod dolor deserunt dolorem reprehenderit cumque quos quas molestiae voluptate nemo.</p>
      </div>
    </div>
    <div class="ds-card">
      <div class="ds-card-body ds-stack">
        <h3><a href="#" class="ds-card-link">Card 6</a></h3>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat earum, doloremque sit commodi tempora magnam provident enim explicabo quis ducimus distinctio eaque veritatis veniam culpa fuga, molestiae natus odit porro!</p>
      </div>
    </div>
  </div>
</div>

## Configuration

Wherever CSS Grid is supported, so are custom properties. Hence, you can configure your Grid by adjusting the `--gridCellMin` and `--gridGap` values within a `style` attribute.

<table class="site-table" style="table-layout: fixed">
  <tr>
    <th>Property</th>
    <th>Purpose</th>
    <th>Default value</th>
  </tr>
  <tr>
    <td>
      <code>--gridCellMin</code>
    </td>
    <td>
      The minimum width of a grid cell. This is entered into the <code>min()</code> function so that the smaller of this value versus <code>100%</code> is applied. This prevents overflow on small screens.
    </td>
    <td>
      20ch (20 characters)
    </td>
  </tr>
  <tr>
    <td>
      <code>--gridGap</code>
    </td>
    <td>
      The gap between Grid cells (property: <code>grid-gap</code>)
    </td>
    <td>
      {% var '$s2' %}
    </td>
  </tr>
</table>

### Example

In the following example `--gridCellMin` is set to 30ch and `--gridGap` to `3rem`.

```html
<div class="ds-grid" style="--gridCellMin: 30ch; --gridGap: 3rem;">
  <!-- grid cells/items here -->
</div>
```