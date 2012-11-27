/**
 * Slasher home view JS handles.
 */

$(document).ready(function () {
    "use strict";
    var obj = {};
    (function () {
        obj.elems = {
            searchForm: $(".navbar-search"),
            searchInput: $(".search-query")
        };
        obj.fns = {};
    }());

    obj.elems.searchForm.on("keyup", function (evt) {
        if (evt.keyCode === 13) {
            evt.preventDefault();
        } else {
            var value = obj.elems.searchInput.val();
            if (value) {
                $.ajax({
                    url: '/suggest/',
                    type: 'post',
                    data: {
                        'type': 'username',
                        'sugg': value
                    },
                    success: function (data) {
                        console.log(data);
                    }
                });
            }
        }
    });

});
