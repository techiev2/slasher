/**
 * Slasher login view JS handles.
 */

var $;

$(document).ready(function () {
    "use strict";
    var obj = {};
    (function () {
        obj.elems = {
            loginUname: $("#slasher_uname"),
            loginPass: $("#slasher_upass"),
            loginSubmit: $("#slasher_login")
        };
        obj.fns = {
            postLogin: function () {
                $.ajax({
                    type: 'post',
                    url: window.location.href,
                    data: {
                        username: obj.elems.loginUname.val(),
                        password: obj.elems.loginPass.val()
                    },
                    success: function (data) {
                        if (data.status === 'success') {
                            window.location.href = '/';
                        }
                    }
                });
            }
        };
    }());

    obj.elems.loginUname.focus();

    obj.elems.loginUname.on("blur", function () {

        var elem = $(this),
            val = elem.val();
        $.ajax({
            type: 'post',
            url: '/suggest/',
            data: {
                sugg: val,
                type: 'username'
            },
            success: function (data) {
                if (data.status === "failure") {
                    obj.elems.loginUname.addClass("clearfix error");
                }
            }
        });

    });

    obj.elems.loginPass.on("keyup", function (evt) {
        if (evt.keyCode === 13) {
            obj.fns.postLogin();
        }
    });

    obj.elems.loginSubmit.on("click", function () {
        obj.fns.postLogin();
    });

});
