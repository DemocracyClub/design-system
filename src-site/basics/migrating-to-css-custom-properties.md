---
title: Migrating to CSS custom properties
---

A step-by-step guide for moving a consuming project off the design system’s Sass
variables and onto its CSS custom properties.

This page is written to be worked through by a person or handed to an automated
agent as its instructions. It assumes the project has some local Sass of its own
that uses the design system — component styles, overrides, page-specific rules.

For what changed and why, see
[CSS custom properties]({{site.basedir}}/basics/css-custom-properties).

## Before you start

**Do not remove your Sass build.** The design system’s component styles are
still Sass. You still compile `index.template.scss` exactly as you do today, and
the custom properties arrive in your compiled CSS automatically because
`tokens.css` is imported by `partials/_variables.scss`. Removing the Sass
compilation step is a *later* piece of work, and not part of this.

## Do it in two phases

Phase 1 is mechanical and safe. Phase 2 requires judgement. Do not interleave
them — you lose the ability to tell a mistake from an intended change.

| | Phase 1 | Phase 2 |
|---|---|---|
| What | Replace `$var` with the exact property it aliases | Replace primitives with semantic properties |
| Judgement | None — use the table below | Yes — depends on what the value *means* |
| Visual result | **Must be pixel-identical** | Should be identical, but verify |
| Benefit | Removes the Sass dependency | Makes the project themeable |

## Phase 1: the mechanical swap

Replace every design system Sass variable with the custom property it aliases.

```css
/* Before */
.my-thing {
  color: $black;
  padding: $s2;
  border-bottom: $ss2 solid $blueForWhite;
}

/* After */
.my-thing {
  color: var(--ds-colour-grey-900);
  padding: var(--ds-size-2);
  border-bottom: var(--ds-size-small-2) solid var(--ds-colour-blue-700);
}
```

### The complete mapping

This is the whole set. There are no others. If you find a `$variable` from the
design system that is not in this table, follow **Report it upstream** below
rather than guessing.

| Sass variable | CSS custom property |
|---|---|
| `$darkBlack` | `--ds-colour-grey-950` |
| `$black` | `--ds-colour-grey-900` |
| `$blackOpacity` | `--ds-colour-grey-900-alpha` |
| `$white` | `--ds-colour-white` |
| `$whiteOpacity` | `--ds-colour-white-alpha` |
| `$pinkForWhite` | `--ds-colour-pink-700` |
| `$blueForWhite` | `--ds-colour-blue-700` |
| `$blueForBlack` | `--ds-colour-blue-400` |
| `$blueLight` | `--ds-colour-blue-100` |
| `$greenForWhite` | `--ds-colour-green-700` |
| `$greenForBlack` | `--ds-colour-green-400` |
| `$redForWhite` | `--ds-colour-red-700` |
| `$redForBlack` | `--ds-colour-red-400` |
| `$redForBlueLight` | `--ds-colour-red-700` |
| `$amber` | `--ds-colour-amber-400` |
| `$s1` … `$s8` | `--ds-size-1` … `--ds-size-8` |
| `$ss1` … `$ss8` | `--ds-size-small-1` … `--ds-size-small-8` |
| `$increment-small-scale` | `--ds-size-small-1` |
| `$familyMain` | `--ds-font-family-main` |
| `$familyBody` | `--ds-font-family-body` |
| `$lineHeight` | `--ds-line-height-default` |
| `$lineHeightTight` | `--ds-line-height-tight` |
| `$measure` | `--ds-width-measure` |
| `$measureReduced` | `--ds-width-measure-reduced` |
| `$measureHalf` | `--ds-width-measure-half` |
| `$measureThird` | `--ds-width-measure-third` |
| `$cardShadow` | `--ds-shadow-card` |

`$ratio` is the only exception: it is a bare number (`1.25`), not a length, and
has no custom property. Use the literal `1.25` in `calc()`.

### Two things that will not compile

**Colour functions.** Sass cannot operate on a `var()` reference.

```css
/* Was fine, now fails */
background: rgba($black, 0.5);
border-color: darken($blueForWhite, 10%);
```

This is a **stop-and-report** case. See below.

**Arithmetic.** Same reason.

```css
/* Was fine, now fails */
font-size: $s8 * $ratio;
margin: $s2 / 2;
```

Move the arithmetic into CSS:

```css
font-size: calc(var(--ds-size-8) * 1.25);
margin: calc(var(--ds-size-2) / 2);
```

If the arithmetic is producing a *new scale step* rather than a one-off, that is
also worth reporting upstream — the scale may need extending for everyone.

{% warning 'Mistakes here fail silently' %}

A mistyped Sass variable was a build error. A mistyped custom property is not.

```css
color: var(--ds-colour-blck);   /* compiles fine, renders wrong */
```

An undefined `var()` makes the property invalid at computed-value time, so the
element falls back to its inherited or initial value instead of erroring. Your
build will pass and the page will look subtly wrong.

This is why the verification step below is not optional, and why it has to check
rendered output rather than just that the build succeeded.

{% endwarning %}

## Phase 2: move onto semantic properties

Phase 1 leaves the project using *primitive* properties — raw palette and scale
values. Phase 2 replaces them with properties that describe the value’s **role**.

This is what makes a project themeable: when the design system gains dark mode
and other themes, semantic properties change value and primitives do not.

```css
/* Phase 1 result — correct, but says "grey 900" */
.my-thing { color: var(--ds-colour-grey-900); }

/* Phase 2 — says "this is body text" */
.my-thing { color: var(--ds-colour-text); }
```

Work out what the value *means* in each place, then pick the matching property:

| If the value is… | Use |
|---|---|
| Body or heading text | `--ds-colour-text` |
| Text on a dark background | `--ds-colour-text-inverse` |
| A link or interactive text | `--ds-colour-link` |
| A button or call to action | `--ds-colour-action` |
| A keyboard focus outline | `--ds-colour-focus` |
| The page background | `--ds-colour-background-page` |
| A form, table or filter background | `--ds-colour-background-panel` |
| A dark header or footer background | `--ds-colour-background-inverse` |
| A code block or highlight wash | `--ds-colour-background-subtle` |
| A card, form or table border | `--ds-colour-border` |
| A border on a dark background | `--ds-colour-border-inverse` |
| A success state | `--ds-colour-success` |
| An error or validation failure | `--ds-colour-error` |
| An informational state | `--ds-colour-info` |
| Body copy size | `--ds-font-size-body` |
| An `h1`–`h6` size | `--ds-font-size-heading-1` … `-6` |

Two rules that matter:

**Do not swap on value alone.** `--ds-colour-text` and `--ds-colour-border` do
not currently resolve to the same value, but even where two properties do match
today, using the wrong one couples your code to a coincidence. Pick by meaning.

**If nothing fits, leave the primitive in place** and report it. A missing
semantic role is a gap in the design system, not something to work around
locally.

Spacing has no semantic layer yet — keep using `--ds-size-*` and
`--ds-size-small-*` directly for margins, padding and gaps.

## Report it upstream

The design system is meant to be used as given. Where a project has had to
diverge, that is nearly always a signal the system is missing something — and
fixing it centrally means every other project benefits.

Raise an issue at
[github.com/DemocracyClub/design-system/issues](https://github.com/DemocracyClub/design-system/issues)
when you hit any of these:

- **A colour function on a design system colour** — `darken()`, `lighten()`,
  `rgba()`, `mix()`. The variant you are producing probably belongs in the
  palette.
- **A hardcoded colour that is close to a design system one.** Near-misses are
  usually accidental drift.
- **A local variable holding a design decision** — a spacing step, a breakpoint,
  a shadow, a font size not on the scale.
- **A semantic role with no matching property**, such as a warning or disabled
  state.
- **A new scale step**, or arithmetic that is really extending the scale.
- **A local reimplementation of something the design system already provides**,
  or a component that overrides design system styles to change its appearance.
- **Anything in this guide that turned out to be wrong or incomplete.**

Do not block on the report. Note it, apply the smallest local fix that works,
and carry on — the issue is so the gap gets closed properly later.

{% note 'What to include in the report' %}

The file and rule you found it in, what the code was doing, and what you did
instead. A three-line snippet is usually enough. The goal is that someone can
tell whether the design system needs a new property, a new component, or
nothing at all.

{% endnote %}

## Verify

Run all three. The first two catch nothing on their own.

**1. It compiles.** Necessary, not sufficient — see the warning above.

**2. No design system variables remain.** In your own Sass:

```
grep -rnE '\$(black|white|darkBlack|blackOpacity|whiteOpacity|pinkForWhite|blueForWhite|blueForBlack|blueLight|greenForWhite|greenForBlack|redForWhite|redForBlack|redForBlueLight|amber|s[1-8]|ss[1-8]|familyMain|familyBody|lineHeight|lineHeightTight|measure|cardShadow|ratio)\b' --include='*.scss' .
```

**3. Nothing moved.** This is the one that matters. Phase 1 must be pixel-
identical, so compare rendered output before and after — a screenshot diff if
the project has one, otherwise load the affected pages and compare computed
styles in devtools. Pay particular attention to anything that renders as
`transparent`, the default text colour, or an unstyled fallback: that is the
signature of a mistyped property name.

## If you are an automated agent

Follow the procedure above. These constraints are not negotiable.

1. **Only use property names that appear in this page or in `system/tokens.css`.**
   Never invent one. If the name you want does not exist, that is a
   stop-and-report case, not a naming exercise.
2. **Never change a value.** Phase 1 is a rename. If output would change
   visually, you have made a mistake.
3. **Complete phase 1 across the project before starting phase 2**, and keep
   them in separate commits so a visual regression can be bisected to one or the
   other.
4. **Do not remove or restructure the Sass build**, and do not convert the
   project’s own Sass variables, mixins or functions. Only design system
   variables are in scope.
5. **Do not tokenise local literals.** A one-off `margin: 3px` that is not a
   design decision stays as it is.
6. **When a colour function or missing property blocks you, stop on that rule**,
   apply the smallest local fix, and record it for the upstream report. Do not
   improvise a replacement value, and do not silently skip the rule.
7. **Report at the end** with: files changed, every stop-and-report case found,
   and any rule you could not migrate. An empty list is a valid answer; a
   fabricated one is not.
