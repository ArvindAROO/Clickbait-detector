chrome.browserAction.setIcon({
    path: {
        48: "icon_48.png"
    }
});
function hello() {
    chrome.tabs.query({
        active: true,
        lastFocusedWindow: true
    }, tabs => {
        let url = tabs[0].url;
        // use `url` here inside the callback because it's asynchronous!

        // alert('hello ' + url); 
        function callback() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    result = xhr.responseText;
                    
                    alert(result)
                }
            }
        };
        
        //the request format will be "http://127.0.0.1:5000/url?query=https://example.com"
        // where query is the url to be checked
        var xhr = new XMLHttpRequest();
        requestUrl = "http://127.0.0.1:5000/url?query=" + url 
        xhr.open("GET", requestUrl, true);
        xhr.onreadystatechange = callback;
        xhr.send();
    });
    
}
  
document.getElementById('button').addEventListener('click', hello); // activate only on click