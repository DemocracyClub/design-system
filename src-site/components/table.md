---
title: Table
---

Data tables must be accessible. Each must have a `<caption>` element. It is permissable to use a heading element _inside_ the `<caption>` so screen reader users can navigate to it using heading shortcuts. If you do use a heading element inside the `<caption>` you should longer introduce the table with an heading.

<div class="ds-scope">
  <table class="ds-table">
    <caption><h2>Basic table with column headers</th></caption>
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

## Row headers

You can use either column headers (`<th>` in the above example), row headers (`<th>` with `scope="row"` on each row’s first child) or both.

<div class="ds-scope">
  <table class="ds-table">
    <caption><h2>Basic table with column headers</th></caption>
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