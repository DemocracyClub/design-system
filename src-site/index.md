---
layout: layouts/page.njk
title: Democracy Club’s Design System
---

The **Democracy Club** design system, like any good design system, helps you efficiently and consistently create **Democracy Club** web interfaces.

If there is something you need to create an interface that is not, so far, included in the system, [raise an issue](https://github.com/DemocracyClub/design-system/issues/new/choose). **DO NOT** design and code your own, bespoke components. If you need it, it belongs here so others can use it too.

## Contributing

Before contributing a new component to the design system, you must do two things:

1. **Find out if it already exists**. It’s likely the component you want either exists (just not exactly as you imagined), has an equivalent that does the same job (you probably just want that), or can be created using a combination of existing components and [utility classes]({{site.basedir}}/components/utilities/). If you encounter problems, [raise an issue](https://github.com/DemocracyClub/design-system/issues/new/choose).
2. **Raise an issue**. Before embarking on making the component (part component or other feature), raise an issue to make your intent public and confirm the necessity. Use the **addition** label.

When creating your component, follow these steps.

{% note 'My Component' %}

Throughout, the hypothetical component will be referred to simply as “Component”, `component`, and/or `ds-component`.

{% endnote %}

### 1. Create a partial

The CSS for your component will consist of a Sass partial and will exist in the partials folder inside the repo’s top-level [`system` folder](https://github.com/DemocracyClub/design-system/tree/master/system). For a component named “Component”, the filename should be `_component.scss`.

```html
📁 fonts
📁 images
📁 partials <-- in here!
index.template.scss
docs.scss
```

The Sass code for that partial should use [placeholders](https://sass-lang.com/documentation/style-rules/placeholder-selectors). This allows for the extension of the code by other components, reducing redundant CSS in the output.

Let’s say our component just changes the text color to the design system’s `$blueForWhite` color. This is the correct format:

```css
%ds-component {
  color: $blueForWhite;
}

@mixin component {
  .ds-component {
    @extend %ds-component;
  }
}
```

{% note 'Variables' %}

The variable `$blueForWhite` is part of [Colors](https://democracyclub.github.io/design-system/basics/colors/) and is included automatically. No need to import or include this explicitly here.

{% endnote %}

### 2. Import and include the partial

The partial now needs to be imported in both the `docs.scss` and `index.template.css` files.

```css
@import 'partials/_component.scss';
```
In both these files, you also need to `@include` the mixin in the “optional styles” block. Then it’s at the design system consumer’s discretion whether they want to comment it out.

```css
@mixin optional-styles {
  @include some-component;
  @include component;
  @include another-component;
  ... etc ...
}
```

### 3. Document the component

You must document your component!

The documentation site is built in Eleventy and lives in the [`src-site` folder](https://github.com/DemocracyClub/design-system/tree/master/src-site), adjacent to the `system` folder you have just been working in.

Create a markdown file in the `src-site/components` folder. The only frontmatter you need is a title.

```html
---
title: Component
---

TODO: describe the component
```

In the body of the markdown file, you will need to include the following:

1. An introduction to the component starting “Use the [component name] when you need to...”
2. A code block showing the HTML needed for the component, and further code blocks to demonstrate changes to the markup based on state (where applicable)
3. An inline demo of the component. This should use the same markup as the code block in (2) (except (2) might be truncated or use dummy paths). Importantly, it must be nested in a `<div>` with `class="ds-scope"` since styles need to be scoped/separated within the docs pages. See below for a demo&hellip; of a demo.

```html
Here’s a demo:

<div class="ds-scope">
  <div class="ds-component">
    <!-- contents of the component -->
  </div>
</div>
```

### Other contribution

If you see anything missing or not right with these docs, [raise an issue](https://github.com/DemocracyClub/design-system/issues/new) using the **docs** label.


