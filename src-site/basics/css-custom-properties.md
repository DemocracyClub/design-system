---
title: CSS custom properties
---

The design system’s values — colours, the modular scales, type, widths — are
defined as CSS custom properties in `system/tokens.css`. That file is plain
CSS and is the single source of truth.

This is the first step towards dropping SASS from the design system entirely.

The Sass variables still exist and still work. They are now aliases onto
the custom properties:

```css
$black: var(--ds-colour-grey-900);
$s2: var(--ds-size-2);
```

`tokens.css` is imported by `partials/_variables.scss`, which every entry point
already imports. So if you compile the design system’s Sass, you get the custom
properties in your output automatically — no change to your build, your
`index.template.scss`, or your `optional-styles` block.

Compiled output is unchanged apart from gaining a `:root` block of properties,
and values now being written as `var()` references.

## Using the properties

Reference them directly in your own CSS:

```css
.my-component {
  color: var(--ds-colour-text);
  padding: var(--ds-size-2);
  border: var(--ds-size-small-1) solid var(--ds-colour-border);
}
```

There are two tiers. **Primitive** properties are raw palette and scale values —
`--ds-colour-blue-700`, `--ds-size-3`. **Semantic** properties describe the role
a value plays — `--ds-colour-text`, `--ds-colour-focus`,
`--ds-font-size-heading-2`.

Prefer the semantic properties. They are the ones that will gain theme-aware
values, so code written against them will pick up dark mode and any future
theming.

See [Colors]({{site.basedir}}/basics/colors) and
[Modular scale]({{site.basedir}}/basics/modular-scale) for the full list.

## What this breaks

Because the Sass variables now hold `var()` references rather than literal
values, **Sass cannot operate on them any more**.

Colour functions no longer work:

```css
/* No longer compiles */
color: darken($blueForWhite, 10%);
background: rgba($black, 0.5);
```

Neither does arithmetic:

```css
/* No longer compiles */
font-size: $s8 * $ratio;
margin: $s2 / 2;
```

Use `calc()` instead, which the design system’s own partials already do:

```css
font-size: calc(var(--ds-size-8) * 1.25);
margin: calc(var(--ds-size-2) / 2);
```

For colour manipulation, either add the variant you need to `tokens.css` as a
new property, or use `color-mix()`.

If you hit either of these in a consuming project, it is worth asking whether
the value belongs in the design system instead — the palette is meant to be
used as given rather than adjusted per project.

## Naming

Properties follow the pattern:

```text
--ds-[category]-[concept]-[variant]-[state]
```

Numbers in primitive names describe relative position, not a measurement. The
value behind `--ds-size-3` or `--ds-colour-blue-700` may change without the
property being renamed.

## What happens next

1. **Consumers move onto the custom properties.** This is the step this change
   exists to unblock. Nothing needs to happen all at once — see
   [Migrating to CSS custom properties]({{site.basedir}}/basics/migrating-to-css-custom-properties)
   for a step-by-step guide.
2. **The design system’s own partials move onto the semantic properties.** They
   currently still use the Sass variables, which resolve to the primitives.
   This is what will let `.ds-dark` become a short list of property overrides
   rather than a rule per component.
3. **Sass is removed.** Once nothing depends on the variables, the partials
   become plain CSS and `node-sass` goes away with them.

{% note 'Known rough edges' %}

The tiers are not perfectly applied yet. The design system’s partials still
reference primitives via the Sass variables rather than using the semantic
properties, and spacing has no semantic layer at all — use the `--ds-size-*`
scales directly for margins, padding and gaps.

This is deliberate. Getting a complete, correctly-named set of properties
published matters more right now than having the design system’s own internals
use them perfectly.

{% endnote %}
