
function ready(fn) {
  'use strict';
  if (document.readyState !== 'loading') {
    fn();
  } else if (document.addEventListener) {
    document.addEventListener('DOMContentLoaded', fn);
  } else {
    document.attachEvent('onreadystatechange', function () {
      if (document.readyState !== 'loading') {
        fn();
      }
    });
  }
}

var matches = function (el, selector) {
  'use strict';
  return (
    el.matches ||
    el.matchesSelector ||
    el.msMatchesSelector ||
    el.mozMatchesSelector ||
    el.webkitMatchesSelector ||
    el.oMatchesSelector
  ).call(el, selector);
};

function parent(el, selector) {
  'use strict';
  while ((el = el.parentNode) && el !== document) {
    // See "Matches Selector" above
    if (!selector || matches(el, selector)) {
      return el;
    }
  }
}

var ds_filter = {
  init: function () {
    'use strict';
    this.filter_list = document.querySelectorAll(".ds-filterable");
    this.input = document.getElementById("ds-filter-input");
    this.input.addEventListener("input", this.handleInput.bind(this));
  },
  handleInput: function () {
    'use strict';
    var value = this.input.value;
    var weakMatch = new RegExp(value, "i");
    Array.prototype.filter.call(this.filter_list, function (filter_item) {
      var parent_group = parent(filter_item, ".ds-filterable-group");
      if (weakMatch.test(filter_item.dataset.filterText)) {
        filter_item.classList.remove("ds-filtered");
        if (parent_group !== undefined) {
            parent_group.classList.remove("ds-filtered");
        }

      } else {
        filter_item.classList.add("ds-filtered");
        // hide filterable groups if empty
        if (parent_group !== undefined) {
          if (parent_group.querySelectorAll(".ds-filterable:not(.ds-filtered)").length === 0) {
            parent_group.classList.add("ds-filtered");
          } else {
            parent_group.classList.remove("ds-filtered");
          }
        }
      }
    });
  }
}


ready(function() {
  'use strict';
  ds_filter.init();
});
