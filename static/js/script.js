// Other Scripts
function scrollToTop() {
    window.scrollTo(0, 0);
}

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

// JQuery Scripts
$(document).ready(function() {
    document.getElementById('login-next-url').value = window.location.pathname;
    document.getElementById('signup-next-url').value = window.location.pathname;
    document.getElementById('logout-anchor').href = "/logout/?next="+window.location.pathname;

    $("#modal_confirm_password_signup").on('input', function() {
        if (this.value === document.getElementById('modal_password_signup').value) {
            document.getElementById('signup-submit-button').disabled = false
        } else {
            document.getElementById('signup-submit-button').disabled = true
        }
    });
    
    $(window).scroll(function() {
        var topPosition = $(window).scrollTop();
        var windowHeight = $(window).height();

        if(topPosition > windowHeight/2) {
            $("#scroll-to-top").css("display", "block");
        } else {
            $("#scroll-to-top").css("display", "none");
        }
    });
})