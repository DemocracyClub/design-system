---
title: Composing content
---

By combining [Stacks]({{site.basedir}}/components/stack), [Grids]({{site.basedir}}/components/grid), and the various components, you can quickly compose responsive layouts like the following “kitchen sink” example.

{% ds-example %}

<div class="site-resizer">
    <div class="ds-stack">
      <h1>Lorem ipsum dolor sit amet</h1>
      <p>Iure explicabo quasi tempore <a href="#">tempora deserunt quaerat</a> dignissimos obcaecati placeat dolor. Nihil! Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quo iure alias ipsum porro ut eaque corrupti, voluptatibus exercitationem iste consequatur?</p>
      <ul>
        <li>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Illum consequatur, rem perferendis sunt distinctio ut corrupti expedita sapiente voluptatem neque? Ratione velit illum delectus laboriosam quas expedita ex, repellendus non?</li>
        <li>Impedit praesentium ipsam, itaque perspiciatis, voluptatibus ducimus nesciunt facilis nobis nam labore illo minus explicabo natus quo eaque voluptas, dolorum quam architecto sunt! Deserunt, similique quis aliquid ex eaque reprehenderit.</li>
        <li>Veritatis rerum hic numquam quibusdam eos. Vel magni provident ea? Molestias laborum quos a expedita voluptas dolor ad, officia doloribus ullam illum, atque pariatur, consequatur error? Libero, numquam? Minima, fugit.</li>
        <li>Dolor distinctio, iusto labore ullam ducimus non praesentium et. Consequatur quisquam odio alias neque sequi modi sit? Ab facere culpa, odit nisi nam dolores repellat facilis ex consequuntur dignissimos molestias.</li>
        <li>Facilis, fuga totam reiciendis error magnam vitae cupiditate. Aut debitis ipsa cupiditate, quae laudantium repudiandae asperiores nisi. Fuga sunt, suscipit, dolor dolores asperiores labore aliquam eveniet ea aut aliquid molestiae!</li>
      </ul>
      <p>Assumenda aliquam sunt exercitationem distinctio adipisci provident id natus commodi quibusdam odit itaque amet, veritatis perspiciatis et <a href="#">ullam labore iste</a>. Ab nobis cupiditate mollitia optio, obcaecati maxime nam molestiae. Nesciunt, fugiat quas!</p>
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
      <dl class="ds-descriptions">
        <div>
          <dt>Facebook</dt>
          <dd><a href="https://www.facebook.com/shaunbaileyuk">www.facebook.com/shaunbaileyuk</a></dd>
        </div>
        <div>
          <dt>Homepage</dt>
          <div>
            <dd><a href="https://shaunbailey.uk/">https://shaunbailey.uk</a></dd>
          </div>
        </div>
        <div>
          <dt>Instagram</dt>
          <dd><a href="https://www.instagram.com/shaunbaileyam/">https://www.instagram.com/shaunbaileyam</a></dd>
        </div>
        <div>
          <dt>Email</dt>
          <dd>shaunbailey@shaunbailey.co.uk</dd>
        </div>
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
      <div>
      <div class="ds-date">
        <div class="ds-field">
          <label for="id_date-date_0">Day</label>
          <input type="number" name="day_0" value="12" required="" id="id_date-date_0">
        </div>
        <div class="ds-field">
          <label for="id_date-date_1">Month</label>
          <input type="number" name="month_1" value="12" required="" id="id_date-date_1">
        </div>
        <div class="ds-field">
          <label for="id_date-date_2">Year</label>
          <input type="number" name="year_2" value="2025" required="" id="id_date-date_2">
        </div>
      </div>
      </div>
  </div>
</div>

{% endds-example %}
