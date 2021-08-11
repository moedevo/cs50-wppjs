function showPage(page) {
    // Hide all other pages
    document.querySelectorAll('div').forEach(div => {
        div.style.display = 'none';
    });

    // Show requested page
    document.querySelector(`#${page}`).style.display = 'block';
}
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('button').forEach(button => {
        button.onclick = function() {
            showPage(this.dataset.page);
        };
    });
});
