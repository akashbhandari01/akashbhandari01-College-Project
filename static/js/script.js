$("#search-icon").click(function () {
   $(".nav").toggleClass("search");
   $(".nav").toggleClass("no-search");
   $(".search-input").toggleClass("search-active");
});
$('.menu-toggle').click(function () {
   $(".nav").toggleClass("mobile-nav");
   $(this).toggleClass("is-active");
});
let slideIndex = 0;
showSlides();

function showSlides() {
   let i;
   let slides = document.getElementsByClassName("mySlides");
   for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
   }
   slideIndex++;
   if (slideIndex > slides.length) { slideIndex = 1 }
   slides[slideIndex - 1].style.display = "block";
   setTimeout(showSlides, 2000); // Change image every 2 seconds
} 