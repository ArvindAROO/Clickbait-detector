(function() {
    function r(e, n, t) {
        function o(i, f) {
            if (!n[i]) {
                if (!e[i]) {
                    var c = "function" == typeof require && require;
                    if (!f && c) return c(i, !0);
                    if (u) return u(i, !0);
                    var a = new Error("Cannot find module '" + i + "'");
                    throw a.code = "MODULE_NOT_FOUND", a
                }
                var p = n[i] = {
                    exports: {}
                };
                e[i][0].call(p.exports, function(r) {
                    var n = e[i][1][r];
                    return o(n || r)
                }, p, p.exports, r, e, n, t)
            }
            return n[i].exports
        }
        for (var u = "function" == typeof require && require, i = 0; i < t.length; i++) o(t[i]);
        return o
    }
    return r
})()({
    1: [function(require, module, exports) {

    }, {}],
    2: [function(require, module, exports) {
        const fs = require('fs')

        /////
        chrome.tabs.query({
            active: true,
            lastFocusedWindow: true
        }, tabs => {
            let url = tabs[0].url;
            // use `url` here inside the callback because it's asynchronous!

            fs.writeFile('C:/Users/91807/Desktop/Project/Hallothon_2021/self/Output.txt', url, (err) => {
                if (err) alert("err");
                alert("success")
            })
        });
        ///////////
    }, {
        "fs": 1
    }]
}, {}, [2]);