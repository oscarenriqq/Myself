const trs = document.querySelectorAll("tbody tr")
trs.forEach((tr) => {
    tr.addEventListener("click", function(e) {
        const url = e.target.parentNode.getAttribute("url")
        if (url)
            window.open(url, "_blank")
    })
})

updateSizes()

//event on change screen size
window.addEventListener("resize", updateSizes)

function updateSizes() {
    const width = window.innerWidth || document.documentElement.clientWidth
    const logo = document.querySelector("a.logo")
    const h1Main = document.querySelector("main h1")

    if (width < 768) {
        logo.classList.remove("fs-1")
        logo.classList.add("fs-2")

        h1Main.classList.remove("fs-2")
        h1Main.classList.add("fs-3")
    }
    else {
        logo.classList.remove("fs-2")
        logo.classList.add("fs-1")

        h1Main.classList.remove("fs-3")
        h1Main.classList.add("fs-2")
    }
}