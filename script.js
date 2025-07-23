$(document).ready(function () {
  $('.slider').slick({
    infinite: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 3000,         // ⏱ Slides change every 3 seconds
    speed: 600,                  // ⏩ Transition takes 0.6 seconds
    arrows: true,
    prevArrow: '<button class="slick-prev">&#8592;</button>',
    nextArrow: '<button class="slick-next">&#8594;</button>',
    pauseOnHover: true,
    cssEase: 'ease-in-out',
    responsive: [
      {
        breakpoint: 768,
        settings: {
          arrows: false,
          dots: true
        }
      }
    ]
  });
});

document.addEventListener('DOMContentLoaded', function () {
  const serviceBoxes = document.querySelectorAll('.service-box');

  serviceBoxes.forEach(box => {
    const imageContainer = box.querySelector('.image-container');
    const description = imageContainer.querySelector('.service-description');

    imageContainer.addEventListener('mouseenter', () => {
      description.style.bottom = '0';
    });

    imageContainer.addEventListener('mouseleave', () => {
      description.style.bottom = '-100%';
    });
  });
});

  document.addEventListener('DOMContentLoaded', function() {
    var viewMoreLink = document.getElementById('viewMoreLink');
    var diseaseList = document.getElementById('diseaseList');
    if (viewMoreLink) {
      viewMoreLink.addEventListener('click', function(e) {
        e.preventDefault();
        if (diseaseList.style.display === 'none') {
          diseaseList.style.display = 'flex';
          viewMoreLink.textContent = 'Hide List';
        } else {
          diseaseList.style.display = 'none';
          viewMoreLink.textContent = 'View More';
        }
      });
    }
  });

  // hamburger.js

document.addEventListener('DOMContentLoaded', function () {
  const hamburger = document.getElementById('hamburger-menu');
  const navLinks = document.getElementById('navLinks');

  hamburger.addEventListener('click', function (e) {
    e.stopPropagation();
    navLinks.classList.toggle('open');
  });

  document.addEventListener('click', function (e) {
    if (!navLinks.contains(e.target) && !hamburger.contains(e.target)) {
      navLinks.classList.remove('open');
    }
  });

  // Close on nav item click
  document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('open');
    });
  });
});
