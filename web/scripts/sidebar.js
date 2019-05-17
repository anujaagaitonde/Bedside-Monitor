
function toggleSidenav()
{
    navSize = document.getElementById("mySidenav").style.width;
    if((navSize == "0px") || (navSize == 0))
    {
        openNav ();
    }
    else
    {
        closeNav();
    }
    return;
}

function openNav()
{
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    return;
}

function closeNav()
{
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
    return;
}
