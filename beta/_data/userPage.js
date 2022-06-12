$('.dp').hover(function(){
    $(this).find('.hide').slideDown(200);
  }, function() {
    
  });

const slides = document.querySelectorAll(".galeryPictures img");
const dots = document.querySelector(".demo");
const captionText = document.querySelector(".caption");

  function openModal() {
    document.querySelector(".myModal").style.display = "block";
  }
  
  function closeModal() {
    document.querySelector(".myModal").style.display = "none";
  }
  
  var slideIndex = 1;
  showSlides(slideIndex);
  
  function plusSlides(n) {
    showSlides(slideIndex += n);
  }
  
  function currentSlide(n) {
    showSlides(slideIndex = n);
  }
  
  function showSlides(n) {
    var i;

    if (n >= slides.length) {slideIndex = 1; n=1;}
    if (n < 1) {slideIndex = slides.length;n=slides.length-1;}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    slides[n].style.display = "initial";

  }

  // var cip = $(".video").hover( hoverVideo, hideVideo );

  // function hoverVideo(e) {  
  //     $('video', this).get(0).play(); 
  // }
  
  // function hideVideo(e) {
  //     $('video', this).get(0).pause(); 
      
  // }