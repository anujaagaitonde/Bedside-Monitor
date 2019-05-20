function toggleStar() {
    if (document.getElementById("star").classList.contains("unstarred"))
    {
        document.getElementById("star").classList.remove("unstarred");
        document.getElementById("star").classList.add("starred");
    }
    else
    {
        document.getElementById("star").classList.remove("starred");
        document.getElementById("star").classList.add("unstarred");
    }

    return;
}