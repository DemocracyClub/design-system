---
title: Sidebar
---

Use a Sidebar component when you want a responsive layout with one narrow (“sidebar”) column and another column that takes up the rest of the available space.

By default, the non-sidebar column wraps to form a single column layout when its width is less-than-or-equal-to `50%` the sidebar’s width.

<div class="ds-scope">
  <div class="ds-with-sidebar">
    <div>
      <ul class="ds-sidebar">
        <li>Some</li>
        <li>Things</li>
        <li>To</li>
        <li>The</li>
        <li>Side</li>
      </ul>
      <div class="ds-not-sidebar">
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Libero reprehenderit a ipsa veniam molestias numquam blanditiis? Ab soluta odit consectetur commodi totam, quae debitis incidunt? Numquam consequuntur distinctio laboriosam culpa.</p>
        <p>Dolorem rem veniam, animi magni eius excepturi nesciunt rerum doloribus numquam ducimus, deserunt tenetur accusamus voluptates, iure nobis aperiam. Commodi rerum iste sunt eaque repellat, impedit similique amet totam molestias.</p>
        <p>Natus deleniti temporibus porro eligendi ratione ea provident, recusandae deserunt, omnis placeat laudantium facilis. Illo, ipsa ullam eaque, harum omnis doloribus expedita ab ad laudantium qui deserunt fugiat recusandae repudiandae.</p>
      </div>
    </div>
  </div>
</div>

## Markup

The basic Sidebar markup looks like the following. The elements do not need to be `<div>`s. Use semantic elements where appropriate. Note the “inner wrapper” (an arbitrary div). This is used to help with the margin code.

```html
<div class="ds-with-sidebar">
  <div> <!-- inner wrapper element -->
    <div class="ds-sidebar">
      <!-- sidebar content -->
    </div>
    <div class="ds-not-sidebar">
      <!-- not sidebar content -->
    </div>
  </div>
</div>
```

{% note 'Right sidebars' %}

You can have the sidebar on the right instead, simply by switching the `class="ds-sidebar"` and `class="ds-not-sidebar"` elements over.

{% endnote %}

By default, the sidebar (`class="ds-sidebar"`) is the width of the content it contains. But you may want to prescribe a width. To make sure the sidebar “flexes” to `100%` width in the single column configuration, apply this width with `flex-basis`, _not_ `width`, `min-width`, or `max-width`.

In the following example, the sidebar has an inline style of `style="flex-basis: 15rem"`. The image inside it takes up the whole of its width, whether it is `15rem` or `100%`. Resize the container below to see this in action.

<div class="ds-scope site-resizer">
  <div class="ds-with-sidebar">
    <div>
      <div class="ds-sidebar" style="flex-basis: 20rem">
        <img src="{{site.basedir}}/images/card_example.jpg" alt="">
      </div>
      <div class="ds-not-sidebar">
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Libero reprehenderit a ipsa veniam molestias numquam blanditiis? Ab soluta odit consectetur commodi totam, quae debitis incidunt? Numquam consequuntur distinctio laboriosam culpa.</p>
        <p>Dolorem rem veniam, animi magni eius excepturi nesciunt rerum doloribus numquam ducimus, deserunt tenetur accusamus voluptates, iure nobis aperiam. Commodi rerum iste sunt eaque repellat, impedit similique amet totam molestias.</p>
        <p>Natus deleniti temporibus porro eligendi ratione ea provident, recusandae deserunt, omnis placeat laudantium facilis. Illo, ipsa ullam eaque, harum omnis doloribus expedita ab ad laudantium qui deserunt fugiat recusandae repudiandae.</p>
      </div>
    </div>
  </div>
</div>