chrome.browserAction.onClicked.addListener(function(tab) {
    // No tabs or host permissions needed!
    var url = window.location.href;
    console.log(url);
  });