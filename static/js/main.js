document.querySelector("tbody tr").addEventListener("click", function(e) {
    const url = e.target.parentNode.getAttribute("url")
    if (url)
        window.open(url, "_blank")
})