document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("a").forEach(link => {
        link.addEventListener("click", function (event) {
            const targetId = this.getAttribute("href").substring(1); // Get the target section's ID
            const targetElement = document.getElementById(targetId); // Find the element

            if (targetElement) {
                event.preventDefault(); // Prevent default link behavior
                targetElement.scrollIntoView({ behavior: "smooth" });
            }
        });
    });
});
