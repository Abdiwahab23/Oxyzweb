const navHTML = `
    <nav class="navbar scrolled">
      <a href="index.html" class="logo" style="display: flex; align-items: center; text-decoration: none;">
        <img src="images/Logo%202.png" alt="OXYZ Health & Wellness" style="height: 40px" />
        <span class="logo-text">OXYZ <span class="logo-text-gold">Health & Wellness</span></span>
      </a>
      <div class="nav-links">
        <a href="index.html">Home</a>
        <a href="bioseries.html">BioSeries</a>
        <a href="oxyz-cell.html">Stem Cell</a>
        <a href="training.html">Training &amp; Consultation</a>
        <a href="about.html">About Us</a>
        <a href="contact.html">Contact Us</a>
      </div>
      <div class="nav-right" style="display: flex; align-items: center; gap: 20px; z-index: 1000;">
        <div class="menu-toggle">
          <i class="fas fa-bars"></i>
        </div>
      </div>
    </nav>
`;

const navPlaceholder = document.getElementById("nav-placeholder");
if (navPlaceholder) {
    navPlaceholder.innerHTML = navHTML;
}
