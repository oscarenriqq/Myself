document.querySelector("tbody tr").addEventListener("click", function(e) {
    const url = e.target.parentNode.getAttribute("url")
    window.open(url, "_blank")
})