---
title: Getting started
eleventyExcludeFromCollections: true
---

## Installation

Install the design system in your project as a python package:

```python
pip install git+https://github.com/DemocracyClub/design-system.git@python-package
```

Now simply import `dc_design_system`:

```
import dc_design_system
```

The only thing this package does is to expose the directory it lives in, which we’ll use in the **Sass compilation** step to follow. It’s also needed to path to the images and fonts folders.

```
>>> import dc_design_system
>>> dc_design_system.DC_SYSTEM_PATH
'/home/symroe/.envs/design_system/lib/python3.8/site-packages/dc_design_system'
```

## Structure

The design system folder contains fonts, images and Sass partials:

```html
📁 fonts
📁 images
📁 partials
index.template.scss
docs.scss
```

The `docs.scss` file can be ignored. This just powers the design system used inside this documentation.

The `index.template.scss` file is a template for how you would pull in the partials and get the system running in your project.

## Sass compilation

The first thing you need to do is take `index.template.scss`, rename it if you desire, and make it the “in” file for Sass compilation. To reach the associated partials, you will need to configure `libsass` to use the folder exposed in the installation step above as an `include-path`.

Note the `optional-styles` block in that file. For efficiency, you should comment out any components here you know you don’t need, keeping the design system’s footprint as small as possible. In the following example, I have commented out the [Sidebar]({{site.basedir}}/components/sidebar), [Table]({{site.basedir}}/components/table), and [Select]({{site.basedir}}/components/select) components.

```css
@mixin optional-styles {
  @include description-lists;
  @include button;
  @include cta;
  @include cluster;
  @include grid;
  // @include sidebar;
  @include details;
  @include card;
  @include candidate;
  @include breadcrumbs;
  // @include table;
  @include header;
  @include footer;
  @include radio;
  @include checkbox;
  // @include select;
  @include filter;
  @include party;
}
```

## Scoping

Also in `index.template.scss` you will notice the following line:

```
$scope: false;
```

If set to true, all of the styles you generate are scoped to the `ds-scope` class. For example, the `.ds-stack > *` selector will become `.ds-scope .ds-stack > *`, meaning you must have a parent with `class="ds-scope"` for the styles to be honoured.

```html
<div class="ds-scope">
  <!-- design system styles honoured -->
</div>

<div>
  <!-- design system styles NOT honoured -->
</div>
```

This allows you to more safely add design system components alongside existing styles. Ideally, you would not use scoping and just defer to the design system for all your styling. Unless there is a real need for scoping, best to leave it as `false`.

## CSS optimization

Although the design system—even including _all_ of the components—is relatively small, it’s still recommended you minimize the output CSS using a tool like CSSO(https://github.com/css/csso). Include the minimized file in a `<link>` element in the head of your document in the standard fashion.

```html
<link rel="stylesheet" href="path/to/system.min.css" />
```

## Local development
This project can be run locally if you want to view the in-browser docs/demo.

In order to do this, you'll need to have node v14 in use due to this project's dependency on node-sass.

Run the following commands to get everything nicely set up.

```commandline
npm install
npm run exportSass
npm start
```

You will then be able to access via localhost in your browser.
The demo page is at `/layout-demo/index.html`.

If you want to run the Lighthouse tests locally, you'll also need to make sure the Lighthouse node package is available globally:
`npm install -g lighthouse`

## Next steps

Follow the HTML examples in individual components docs. If you are making a page layout from scratch, see [Page layout]({{site.basedir}}/usage/page-layout).




