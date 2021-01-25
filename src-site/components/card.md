---
title: Card
---

The Card component is an accessible solution to clickable cards. The `class="ds-card-link"` element is activated by clicking anywhere on the card _except_ where there is a supplementary link. These are positioned above the Card’s clickable are to be clickable themselves by pointer/mouse.

<div class="ds-type">
  <div class="ds-card ds-stack">
    <h3><a class="ds-card-link" href="#">Card</a></h3>
    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Iste rem <a href="#other-link">aliquid provident</a> aspernatur molestiae, totam voluptatibus fugit perspiciatis quo corrupti esse, voluptates, tenetur explicabo. Blanditiis provident dolor molestias hic. Aut!</p>
  </div>
</div>

Cards containing more than one child element should use a [Stack]({{site.basedir}}/components/stack) to place margin between child elements. Accordingly, the example takes `class="ds-card ds-stack"`.

```html
<div class="ds-card ds-stack">
  <h3><a class="ds-card-link" href="#">Card</a></h3>
  <p>
    Lorem ipsum dolor sit, amet consectetur adipisicing elit. Iste rem <a href="#other-link">aliquid provident</a> aspernatur molestiae, totam voluptatibus fugit perspiciatis quo corrupti esse, voluptates, tenetur explicabo. Blanditiis provident dolor molestias hic. Aut!
  </p>
</div>
```

{% note 'Card grids' %}

For an example of Cards configured into a grid, see the [Grid]({{site.basedir}}/components/grid) page.

{% endnote %}