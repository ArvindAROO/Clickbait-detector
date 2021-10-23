const fs = require('fs')
  

chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
    let url = tabs[0].url;
    // use `url` here inside the callback because it's asynchronous!
    
    fs.writeFile('C:/Users/91807/Desktop/Project/Hallothon_2021/self/Output.txt', url, (err) => {
        if (err) alert("err");
        alert("success")
    })
});