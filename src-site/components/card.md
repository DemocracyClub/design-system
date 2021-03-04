---
title: Card
---

Use the Card component to encapsulate and highlight key information among prose. To make the _whole_ card clickable apply `class="ds-card-link"` to the principle link inside the card. Other, supplementary links are raised above this clickable area to still be operable.

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

{% warning 'Not everything is a card!' %}

At the time of writing, Cards are used liberally across the Democracy Club sites. Don’t “turn everything up to eleven”; as a rule of thumb, only use a standalone Card once or twice in a page.

Only use multiple successive cards within a [Grid]({{site.basedir}}/components/grid). See an example on the [Grid]({{site.basedir}}/components/grid) page.

{% endwarning %}

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

## Dark theme

Invoke the dark theme on any component by applying `class="ds-dark"` to a container element.

<div class="ds-scope">
  <div class="ds-dark ds-padded">
    <div class="ds-card">
      <div class="ds-card-body">
        <h3><a class="ds-card-link" href="#">Card</a></h3>
        <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Iste rem <a href="#other-link">aliquid provident</a> aspernatur molestiae, totam voluptatibus fugit perspiciatis quo corrupti esse, voluptates, tenetur explicabo. Blanditiis provident dolor molestias hic. Aut!</p>
      </div>
    </div>
  </div>
</div>
