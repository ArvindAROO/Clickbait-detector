function callAPI() {
    chrome.tabs.query({ //get the url of the last focused window, ie the current tab
        active: true,
        lastFocusedWindow: true
    }, tabs => {
        let url = tabs[0].url;
        function callback() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    result = xhr.responseText;
                    //alert(result);
                    document.getElementById('result').innerHTML = result;
                    var temp = document.getElementById("body").clientHeight;
                    if(temp < 300)
                        document.body.style.height = temp + 150 + 'px';
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
  
  document.getElementById('button').addEventListener('click', callAPI); // activate only on click