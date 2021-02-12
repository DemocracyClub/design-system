---
title: Page layout demo
permalink: /layout-demo/index.html
layout: layouts/bare.njk
---

<header class="ds-header">
  <a class="ds-skip-link" href="#main">skip to content</a>
  <a class="ds-header-home" href="/">
    <img src="{{site.basedir}}/images/logo.svg" alt="Democracy Club home" />
  </a>
  <nav>
    <ul>
      <li>
        <a href="#">Home</a>
      </li>
      <li>
        <a aria-current="page" href="#">About</a>
      </li>
      <li>
        <a href="#">Our work</a>
      </li>
      <li>
        <a href="#">Quests</a>
      </li>
      <li>
        <a href="#">Blog</a>
      </li>
      <li>
        <a href="#">Contact</a>
      </li>
      <li>
        <a href="#">Donate</a>
      </li>
    </ul>
  </nav>
</header>
<main id="main" tabindex="-1" class="ds-stack">
  <h1>Democracy Club page layout demo</h1>
  <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Dignissimos pariatur iusto officia necessitatibus distinctio nemo perspiciatis placeat illo facilis enim soluta et accusamus sunt ipsa fugit earum, voluptas assumenda aspernatur.</p>
  <p>Distinctio iure explicabo quaerat repudiandae, nulla officia corporis! Eaque sapiente excepturi quas, nostrum cumque nisi. Quis eligendi necessitatibus, fugit voluptatem a, voluptatibus praesentium fugiat, nostrum doloremque eum est ratione provident.</p>
  <h2>A subheading</h2>
  <p>Dignissimos asperiores sequi soluta, nemo voluptatum molestias repudiandae sunt mollitia placeat magnam sapiente inventore optio iure corporis facere laboriosam dolorem nisi nobis amet minima modi, adipisci tempora voluptatibus? Id, perspiciatis.</p>
</main>
<footer class="ds-footer">
  <div class="ds-block-centered ds-text-centered ds-stack">
    <div class="ds-cluster-center">
      <ul>
        <li>
          <a href="/">Home</a>
        </li>
        <li>
          <a aria-current="true" href=".path/to/about">About</a>
        </li>
        <li>
          <a href="/path/to/">Our work</a>
        </li>
        <li>
          <a href="#">Quests</a>
        </li>
        <li>
          <a href="#">Blog</a>
        </li>
        <li>
          <a href="#">Contact</a>
        </li>
        <li>
          <a href="#">Donate</a>
        </li>
      </ul>
    </div>
    <div class="ds-copyright ds-text-centered">
      <a href="https://democracyclub.org.uk/">
        <img src="{{site.basedir}}/images/logo_white_text.svg" alt="Democracy Club Home" />
      </a>
      <p>Copyright © 2021 Democracy Club</p>
      <p>Community Interest Company</p>
      <p>Company No: <a href="https://beta.companieshouse.gov.uk/company/09461226">09461226</a></p>
    </div>
  </div>
</footer>