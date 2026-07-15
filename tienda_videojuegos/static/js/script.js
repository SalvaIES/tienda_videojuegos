document.addEventListener("DOMContentLoaded", function() {
    const btn = document.getElementById("toggle-theme");
    const html = document.documentElement;

    const savedTheme = localStorage.getItem("theme");
    if (savedTheme) {
        html.setAttribute("data-bs-theme", savedTheme);
    }

    btn.addEventListener("click", function() {
        const current = html.getAttribute("data-bs-theme");
        const next = current === "dark" ? "light" : "dark";
        html.setAttribute("data-bs-theme", next);
        localStorage.setItem("theme", next);
    });
});