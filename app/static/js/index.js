document.addEventListener("DOMContentLoaded", function(event) {
  var slideContainer = document.querySelector(".slide-container");
  var slides = document.querySelectorAll(".slide");
  var slideWidth = slides[0].offsetWidth;
  var currentSlide = 0;

  var prevButton = document.querySelector(".prev-button");
  var nextButton = document.querySelector(".next-button");

  prevButton.addEventListener("click", function() {
    currentSlide = (currentSlide - 1 + slides.length) % slides.length;
    slideContainer.style.transform = "translateX(-" + currentSlide * slideWidth + "px)";
  });

  nextButton.addEventListener("click", function() {
    currentSlide = (currentSlide + 1) % slides.length;
    slideContainer.style.transform = "translateX(-" + currentSlide * slideWidth + "px)";
  });
});


