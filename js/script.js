document.addEventListener("DOMContentLoaded", () => {

  // ========================
  // Set Active Link on Desktop
  // ========================
  // Set Active Link on Desktop
  // ========================
  const currentPathDesktop = window.location.pathname.split('/').pop() || 'index.html';
  const desktopNavItems = document.querySelectorAll('.nav-links > a:not(.btn)');
  desktopNavItems.forEach(a => {
    if (a.getAttribute('href') === currentPathDesktop) {
      a.classList.add('active');
    }
  });

  // ========================
  // Mobile Navigation Toggle

  // ========================
  const menuToggle = document.querySelector(".menu-toggle");
  const navLinks = document.querySelector(".nav-links");

  if (menuToggle && navLinks) {
    menuToggle.addEventListener("click", () => {
      navLinks.classList.toggle("active");
      document.body.classList.toggle("no-scroll");
  // Mobile Menu Header & Active State
  if (navLinks && !document.querySelector('.mobile-nav-header')) {
    const header = document.createElement('div');
    header.className = 'mobile-nav-header';
    header.innerHTML = '<div style="display: flex; align-items: center; text-decoration: none;"><img src="images/Logo.png" alt="OXYZ Health" style="height: 32px; margin-right: 12px;"><span class="logo-text" style="font-size: 15px; white-space: normal; line-height: 1.2;">OXYZ <span class="logo-text-gold">Health & Wellness</span></span></div>';
    navLinks.insertBefore(header, navLinks.firstChild);

    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    const navItems = navLinks.querySelectorAll('a:not(.btn)');
    navItems.forEach(a => {
      if (a.getAttribute('href') === currentPath) {
        a.classList.add('active-link');
      }
    });
  }
      const icon = menuToggle.querySelector("i");
      if (icon) {
        icon.classList.toggle("fa-bars");
        icon.classList.toggle("fa-times");
      }
    });
  }

  // ========================
  // Hero Slideshow

  // ========================
  const slides = document.querySelectorAll(".hero-slide");

  if (slides.length > 1) {
    let currentSlide = 0;

    setInterval(() => {
      slides[currentSlide].classList.remove("active");
      currentSlide = (currentSlide + 1) % slides.length;
      slides[currentSlide].classList.add("active");
    }, 5000); // Change image every 5 seconds
  }

  // ========================
  // Scroll Animations

  // ========================
  const animatedElements = document.querySelectorAll(".animate-on-scroll");

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
        }
      });
    },
    {
      threshold: 0.1,
      rootMargin: "0px 0px -40px 0px",
    },
  );

  animatedElements.forEach((el) => observer.observe(el));

  // ========================
  // Lightbox

  // ========================
  const lightbox = document.getElementById("imageLightbox");
  const lightboxImg = document.getElementById("lightboxImg");
  const lightboxClose = document.querySelector(".lightbox-close");
  const triggers = document.querySelectorAll(".lightbox-trigger");

  if (lightbox && lightboxImg && lightboxClose) {
    triggers.forEach((trigger) => {
      trigger.addEventListener("click", function () {
        lightbox.style.display = "block";
        lightboxImg.src = this.src;
      });
    });

    lightboxClose.addEventListener("click", () => {
      lightbox.style.display = "none";
    });

    // Close on clicking outside the image
    lightbox.addEventListener("click", (e) => {
      if (e.target !== lightboxImg) {
        lightbox.style.display = "none";
      }
    });
  }

  // ========================
  // Number Counters

  // ========================
  const counterElements = document.querySelectorAll(".counter");
  const counterObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const target = entry.target;
        const targetNumber = parseFloat(target.getAttribute('data-target'));
        const prefix = target.getAttribute('data-prefix') || '';
        const suffix = target.getAttribute('data-suffix') || '';
        let currentNumber = 0;
        
        // 90 frames = 1.5 seconds to match the progress bar CSS animation duration
        const increment = targetNumber / 90; 
        
        const updateCounter = () => {
          currentNumber += increment;
          
          if ((increment > 0 && currentNumber >= targetNumber) || (increment < 0 && currentNumber <= targetNumber)) {
            target.innerText = prefix + targetNumber + suffix;
          } else {
            target.innerText = prefix + Math.round(currentNumber) + suffix;
            requestAnimationFrame(updateCounter);
          }
        };
        
        // Short delay to match progress bar easing
        setTimeout(() => {
          updateCounter();
        }, 200);
        
        observer.unobserve(target); // Only animate once
      }
    });
  }, { threshold: 0.5 });
  
  counterElements.forEach(el => counterObserver.observe(el));
});



// Add WhatsApp floating widget
document.addEventListener("DOMContentLoaded", function() {
    const waWidget = document.createElement("a");
    waWidget.href = "https://wa.me/6586163762";
    waWidget.target = "_blank";
    waWidget.className = "wa-float";
    waWidget.innerHTML = `
        <i class="fab fa-whatsapp"></i>
        <span class="wa-tooltip">Chat with us!</span>
    `;
    document.body.appendChild(waWidget);
});
