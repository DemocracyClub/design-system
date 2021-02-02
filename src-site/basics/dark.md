---
title: Dark theme
---

For sections of a page that should use the dark theme, simply wrap them in an element with the `ds-dark` class:

```html
<div class="ds-dark">
  <!-- dark themed elements and components -->
</div>
```

<div class="ds-scope">
  <div class="ds-dark ds-stack" style="padding: 3rem">
    <h2>Dark section</h2>
    <p>Lorem ipsum dolor sit amet consectetur, <a href="#">adipisicing elit</a>. Totam consequuntur distinctio, eaque laborum id nemo nisi atque quis provident doloribus? Aperiam modi recusandae veritatis perspiciatis illum iste explicabo necessitatibus velit?</p>
    <h2>Sample blockquote:</h2>
    <blockquote>
      Very clear, simple, comprehensive. It’s a wonderful voting tool and it definitely influenced positively my decision to vote. Thank you for providing such informative and easy-to-follow pre-voting platform.
    </blockquote>
    <div class="ds-grid">
      <div class="ds-card">
        <div class="ds-card-body ds-stack">
          <h3><a href="#" class="ds-card-link">Card 1</a></h3>
          <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quas, quae eos laboriosam vero aliquid quam soluta ad officiis quia omnis molestiae optio dolore nesciunt tempora? Dolor doloremque illum quasi exercitationem?<p>
        </div>
      </div>
      <div class="ds-card">
        <div class="ds-card-body ds-stack">
          <h3><a href="#" class="ds-card-link">Card 2</a></h3>
          <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo qui delectus eos sapiente. Necessitatibus quis ratione praesentium esse culpa accusantium est, tempore qui deleniti molestias fugit doloremque debitis tempora illum.</p>
        </div>
      </div>
      <div class="ds-card">
        <div class="ds-card-body ds-stack">
          <h3><a href="#" class="ds-card-link">Card 3</a></h3>
          <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse laboriosam recusandae illo non accusamus vero cupiditate aspernatur incidunt nostrum, commodi quos dicta ducimus quidem debitis et reiciendis dolores minima velit.</p>
        </div>
      </div>
    </div>
    <p>Iure explicabo quasi tempore <a href="#">tempora deserunt quaerat</a> dignissimos obcaecati placeat dolor. Nihil! Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quo iure alias ipsum porro ut eaque corrupti, voluptatibus exercitationem iste consequatur?</p>
    <div class="ds-table">
      <table>
        <caption>Basic table with column and row headers</caption>
        <tr>
          <th>Column 1</th>
          <th>Column 2</th>
          <th>Column 3</th>
        </tr>
        <tr>
          <th scope="row">Row 1 / row header</th>
          <td>Row 1 / cell 2</td>
          <td>Row 1 / cell 3</td>
        </tr>
        <tr>
          <th scope="row">Row 2 / row header</th>
          <td>Row 2 / cell 2</td>
          <td>Row 2 / cell 3</td>
        </tr>
        <tr>
          <th scope="row">Row 3 / row header</th>
          <td>Row 3 / cell 2</td>
          <td>Row 3 / cell 3</td>
        </tr>
      </table>
    </div>
    <h2>Description list:</h2>
    <dl>
      <dt>Lorem ipsum dolor sit amet</dt>
      <dd>Consectetur adipisicing elit. Doloribus enim pariatur nihil id reprehenderit iste voluptatum atque natus beatae debitis inventore cumque quibusdam.</dd>
      <dt>Doloribus enim pariatur</dt>
      <dd>Maxime incidunt modi harum? Ipsa ipsum dignissimos repudiandae rerum, recusandae rem accusantium quod omnis minus soluta veniam possimus laudantium dolorum.</dd>
      <dt>Possimus laudantium dolorum</dt>
      <dd>Autem perspiciatis laudantium velit magni, repudiandae dolores laboriosam expedita ipsum officia obcaecati, dolor soluta.</dd>
    </dl>
    <form>
      <div class="ds-field">
        <label for="username">
          Username
          <small>Or enter your email address</small>
        </label>
        <input type="text" id="username">
      </div>
      <div class="ds-field">
        <label for="password">
          Password
        </label>
        <input type="password" id="password">
      </div>
      <div class="ds-field">
        <button class="ds-button" type="submit">Log in</button>
      </div>
    </form>
  </div>
</div>