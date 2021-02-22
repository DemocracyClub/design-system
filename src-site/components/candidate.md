---
title: Candidate
---

Use the Candidate component for summarizing key information about a political candidate.

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

Each Candidate in the list of Candidates from the previous example uses the following markup. Do not place any more content than the (linked) candidate name and party affiliation for Candidates in a list.

```html
<div class="ds-candidate">
  <div class="ds-candidate-body ds-stack-smallest">
    <h3 class="ds-candidate-name ds-h5">
      <a href="path/to/candidate">Candidate name</a>
    </h3>
    <div class="ds-h6">Candidate party</div>
  </div>
  <div class="ds-candidate-image">
    <img src="/path/to/candidate/image" alt="">
  </div>
</div>
```

## Markup variants

* Choose a heading level that is appropriate for the context. In the above example, `<h3>` assumes the Candidate instance belongs to a section headed with an `<h2>`.
* Alternative text is not necessary for the image, since the name and party affiliation already suffice in terms of pertinent info.
* For standalone Candidate components (not included alongside others in a list) use a `<div>` for the outer `class="ds-candidate"` element. It is permissable to use longform content in a standalone content, in place of the party name. Note the use of increase spacing by replacing `ds-stack-smallest` with `ds-stack-smaller`. Also note the removal of the link around the candidate name since a standalone Candidate is intended for the candidate page itself.

```html
<div class="ds-candidate">
  <div class="ds-candidate-body ds-stack-smaller">
    <h2 class="ds-candidate-name ds-h3">
      Candidate name
    </h2>
    <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Libero, suscipit fugit veritatis impedit, distinctio sint commodi labore porro ipsum, a officiis nesciunt aspernatur consequatur. Atque ab eligendi maxime rerum consequatur.<p>
  </div>
  <div class="ds-candidate-image">
    <img src="/path/to/candidate/image" alt="">
  </div>
</div>
```

### Standalone Candidate

<div class="ds-scope">
  <div class="ds-candidate">
    <div class="ds-candidate-body ds-stack-smaller">
      <h2 class="ds-candidate-name ds-h3">
        Candidate name
      </h2>
      <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Libero, suscipit fugit veritatis impedit, distinctio sint commodi labore porro ipsum, a officiis nesciunt aspernatur consequatur. Atque ab eligendi maxime rerum consequatur.<p>
    </div>
    <div class="ds-candidate-image">
      <img src="{{site.basedir}}/images/candidate_example.jpg" alt="">
    </div>
  </div>
</div>

## Dark theme

Invoke the dark theme on any component by applying `class="ds-dark"` to a container element.

<div class="ds-scope">
  <div class="site-resizer ds-dark">
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
