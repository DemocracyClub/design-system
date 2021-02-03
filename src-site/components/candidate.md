---
title: Candidate
---

The Candidate component is a special kind of card. For all other card use cases, see the generic [Card]({{site.basedir}}/components/card). The following demo uses a [Grid]({{site.basedir}}/components/grid) as a list (`<ul>`) to display a list of cards.

<div class="ds-scope">
  <div class="site-resizer">
    <ul class="ds-grid">
      <li class="ds-candidate">
        <div class="ds-candidate-body ds-stack-smallest">
          <h3 class="ds-candidate-name ds-h5">
            <a href="path/to/candidate">Michael Rosen</a>
          </h3>
          <div class="ds-h6">Labour</div>
        </div>
        <div class="ds-candidate-image">
          <img src="{{site.basedir}}/images/candidate_example.jpg" alt="">
        </div>
      </li>
      <li class="ds-candidate">
        <div class="ds-candidate-body ds-stack-smallest">
          <h3 class="ds-candidate-name ds-h5">
            <a href="path/to/candidate">David Moreland</a>
          </h3>
          <div class="ds-h6">Independent</div>
        </div>
        <div class="ds-candidate-image">
          <img src="{{site.basedir}}/images/candidate_example_2.jpg" alt="">
        </div>
      </li>
      <li class="ds-candidate">
        <div class="ds-candidate-body ds-stack-smallest">
          <h3 class="ds-candidate-name ds-h5">
            <a href="path/to/candidate">Giles Orpen-Smellie</a>
          </h3>
          <div class="ds-h6">Conservative & Unionist Party</div>
        </div>
        <div class="ds-candidate-image">
          <img src="{{site.basedir}}/images/candidate_example_3.jpg" alt="">
        </div>
      </li>
    </ul>
  </div>
</div>

A typical Candidate uses the following markup:

```html
<li class="ds-candidate">
  <div class="ds-candidate-body ds-stack-smallest">
    <h3 class="ds-candidate-name ds-h5">
      <a href="path/to/candidate">Candidate name</a>
    </h3>
    <div class="ds-h6">Candidate party</div>
  </div>
  <div class="ds-candidate-image">
    <img src="/path/to/candidate/image" alt="">
  </div>
</li>
```

## Markup variants

* Where the Candidate instance is standalone (not alongside others) make the `class="ds-candidate"` element a `<section>`—not an `<li>`.
* Choose a heading level that is appropriate for the context. In the above example, `<h3>` assumes the Candidate instance belongs to a section headed with an `<h2>`.
* Alternative text is not necessary for the image, since the name and party affiliation already suffice in terms of pertinent info.

