---
title: Card
---

The Card component is an accessible solution to clickable cards. The `class="ds-card-link"` element is activated by clicking anywhere on the card _except_ where there is a supplementary link. These are positioned above the Card’s clickable area to be clickable themselves by pointer/mouse.

<div class="ds-scope">
  <div class="ds-card">
    <div class="ds-card-body">
      <h3><a class="ds-card-link" href="#">Card</a></h3>
      <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Iste rem <a href="#other-link">aliquid provident</a> aspernatur molestiae, totam voluptatibus fugit perspiciatis quo corrupti esse, voluptates, tenetur explicabo. Blanditiis provident dolor molestias hic. Aut!</p>
    </div>
  </div>
</div>

The `.ds-card-body` class extends the `.ds-card-smaller` class from [Stack]({{site.basedir}}/components/stack) to space the elements inside it.

```html
<div class="ds-card">
  <div class="ds-card-body">
    <h3><a class="ds-card-link" href="#">Card</a></h3>
    <p>
      Lorem ipsum dolor sit, amet consectetur adipisicing elit. Iste rem <a href="#other-link">aliquid provident</a> aspernatur molestiae, totam voluptatibus fugit perspiciatis quo corrupti esse, voluptates, tenetur explicabo. Blanditiis provident dolor molestias hic. Aut!
    </p>
  </div>
</div>
```

## Image cards

Insert an element with `class="ds-card-image"` enclosing an image above the `class="ds-card-body"` element. Regardless of the aspect ratio of the supplied image, it will be displayed at 16:9. The `object-fit: cover` declaration ensures the image is cropped rather than squashed within the space.

<div class="ds-scope">
  <div class="ds-card">
    <div class="ds-card-image">
      <img src="{{site.basedir}}/images/card_example.jpg" alt="">
    </div>
    <div class="ds-card-body">
      <h3><a class="ds-card-link" href="#">Card with image</a></h3>
      <p>
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Iste rem <a href="#other-link">aliquid provident</a> aspernatur molestiae, totam voluptatibus fugit perspiciatis quo corrupti esse, voluptates, tenetur explicabo. Blanditiis provident dolor molestias hic. Aut!
      </p>
    </div>
  </div>
</div>

{% note 'Card grids' %}

For an example of Cards configured into a grid, see the [Grid]({{site.basedir}}/components/grid) page.

{% endnote %}

## Dark theme

Invoke the dark theme on any component by applying `class="ds-dark"` to a container element.

<div class="ds-scope">
  <div class="ds-card ds-dark">
    <div class="ds-card-body">
      <h3><a class="ds-card-link" href="#">Card</a></h3>
      <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Iste rem <a href="#other-link">aliquid provident</a> aspernatur molestiae, totam voluptatibus fugit perspiciatis quo corrupti esse, voluptates, tenetur explicabo. Blanditiis provident dolor molestias hic. Aut!</p>
    </div>
  </div>
</div>
