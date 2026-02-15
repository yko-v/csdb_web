document.addEventListener("DOMContentLoaded", function () {

    const modal = document.getElementById("imgModal");
    const modalImg = document.getElementById("modalImage");
    const closeBtn = document.querySelector(".close");

    document.querySelectorAll(".chart-img").forEach(img => {
        img.addEventListener("click", function () {
            modal.style.display = "block";
            modalImg.src = this.src;
        });
    });

    closeBtn.addEventListener("click", function () {
        modal.style.display = "none";
    });

    // Закрытие по клику вне картинки
    modal.addEventListener("click", function (e) {
        if (e.target === modal) {
            modal.style.display = "none";
        }
    });

});

