window.onscroll = function() {headerStick()};

var header = document.getElementById("myHeader");
var sticky = header.offsetTop;

function headerStick()
{
    if((window.pageYOffset > sticky) || (window.pageYOffset <= 0))
    {
        header.classList.add("sticky");
    }
    else
    {
        header.classList.remove("sticky");
    }
}