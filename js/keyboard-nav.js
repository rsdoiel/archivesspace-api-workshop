document.onkeydown = function(e) {
    switch (e.keyCode) {
        case 37:
            document.querySelectorAll("a[title='Previous slide']")[0].click();
            break;
        case 39:
            document.querySelectorAll("a[title='Next slide']")[0].click();
            break;
        case 72:
        case 83:
            document.querySelectorAll("a[title='Return to start of presentation']")[0].click();
            break;
    }
};