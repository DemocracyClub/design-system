---
title: Table
---

Data tables must be accessible. Each must have a `<caption>` element. It is permissable to use a heading element _inside_ the `<caption>` so screen reader users can navigate to it using heading shortcuts. For the sake of avoiding redundancy, if you do use a heading element inside the `<caption>` you should longer introduce the table with a heading.

<div class="ds-scope">
  <div class="ds-table">
    <table>
      <caption><h2>Basic table with column headers</h2></caption>
      <tr>
        <th>Column 1</th>
        <th>Column 2</th>
        <th>Column 3</th>
      </tr>
      <tr>
        <td>Row 1 / cell 1</td>
        <td>Row 1 / cell 2</td>
        <td>Row 1 / cell 3</td>
      </tr>
      <tr>
        <td>Row 2 / cell 1</td>
        <td>Row 2 / cell 2</td>
        <td>Row 2 / cell 3</td>
      </tr>
      <tr>
        <td>Row 3 / cell 1</td>
        <td>Row 3 / cell 2</td>
        <td>Row 3 / cell 3</td>
      </tr>
    </table>
  </div>
</div>

```html
<div class="ds-table">
  <table>
    <caption><h2>Basic table with column headers</h2></caption>
    <tr>
      <th>Column 1</th>
      <th>Column 2</th>
      <th>Column 3</th>
    </tr>
    <!-- rows here -->
  </table>
</div>
```

## Row headers

You can use either column headers (`<th>` in the above example), row headers (`<th>` with `scope="row"` on each row’s first child) or both.

<div class="ds-scope">
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
</div>

```html
<div class="ds-table">
  <table>
    <caption>Basic table with column headers</caption>
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
```

## Responsiveness

Tables should retain their structure for comprehension. Ensuring they can be used and viewed with many columns, or in smaller viewports, the containing `class="ds-table"` element is scrollable along the horizontal axis.

<div class="ds-scope">
  <div class="ds-table">
    <table>
      <caption><h2>Basic table with column headers</h2></caption>
      <tr>
        <th>Column 1</th>
        <th>Column 2</th>
        <th>Column 3</th>
        <th>Column 4</th>
        <th>Column 5</th>
        <th>Column 6</th>
        <th>Column 7</th>
        <th>Column 8</th>
        <th>Column 9</th>
        <th>Column 10</th>
        <th>Column 11</th>
        <th>Column 12</th>
        <th>Column 13</th>
        <th>Column 14</th>
        <th>Column 15</th>
      </tr>
      <tr>
        <td>Row 1 / cell 1</td>
        <td>Row 1 / cell 2</td>
        <td>Row 1 / cell 3</td>
        <td>Row 1 / cell 4</td>
        <td>Row 1 / cell 5</td>
        <td>Row 1 / cell 6</td>
        <td>Row 1 / cell 7</td>
        <td>Row 1 / cell 8</td>
        <td>Row 1 / cell 9</td>
        <td>Row 1 / cell 10</td>
        <td>Row 1 / cell 11</td>
        <td>Row 1 / cell 12</td>
        <td>Row 1 / cell 13</td>
        <td>Row 1 / cell 14</td>
        <td>Row 1 / cell 15</td>
      </tr>
      <tr>
        <td>Row 2 / cell 1</td>
        <td>Row 3 / cell 2</td>
        <td>Row 4 / cell 3</td>
        <td>Row 5 / cell 4</td>
        <td>Row 6 / cell 5</td>
        <td>Row 7 / cell 6</td>
        <td>Row 8 / cell 7</td>
        <td>Row 9 / cell 8</td>
        <td>Row 9 / cell 9</td>
        <td>Row 9 / cell 10</td>
        <td>Row 9 / cell 11</td>
        <td>Row 9 / cell 12</td>
        <td>Row 9 / cell 13</td>
        <td>Row 9 / cell 14</td>
        <td>Row 9 / cell 15</td>
      </tr>
    </table>
  </div>
</div>