const footerHTML = `
    <footer class="footer">
      <div class="footer-grid">
        <div class="footer-col">
          <img src="images/Logo%202.png" alt="OXYZ Health & Wellness" class="footer-logo">
          <p>Advancing regenerative medicine by combining scientific innovation
            with personalized wellness solutions.</p>
          <div class="social-links">
            <a href="https://www.facebook.com/OXYZHealthInternational"><i class="fab fa-facebook-f"></i></a>
            <a href="https://www.instagram.com/oxyz.bioseries?igsh=YjFvcmp1c2VwdjQ5"><i class="fab fa-instagram"></i></a>
            <a href="https://international.oxyzhealth.com"><i class="fas fa-globe"></i></a>
          </div>
        </div>
        <div class="footer-col">
          <h4>Quick Links</h4>
          <ul class="footer-links">
            <li><a href="index.html">Home</a></li>
            <li><a href="bioseries.html">BioSeries</a></li>
            <li><a href="oxyz-cell.html">Stem Cell</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Explore</h4>
          <ul class="footer-links">
            <li><a href="training.html">Training & Consultation</a></li>
            <li><a href="about.html">About Us</a></li>
            <li><a href="contact.html">Contact Us</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Contact Us</h4>
          <ul class="footer-links">
            <li class="footer-contact-item">
              <a href="mailto:global@oxyzhealth.com" class="footer-contact-link">
                <i class="far fa-envelope" class="footer-contact-icon"></i>
                global@oxyzhealth.com
              </a>
            </li>
            <li class="footer-contact-item">
              <a href="tel:+6586163762" class="footer-contact-link">
                <i class="fas fa-phone-alt" class="footer-contact-icon"></i>
                +65 8616 3762
              </a>
            </li>
            <li class="footer-contact-item">
              <i class="fas fa-map-marker-alt" class="footer-contact-icon"></i>
              USA | Singapore | Malaysia
            </li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 OXYZ Health & Wellness. All Rights Reserved.</p>
      </div>
    </footer>
`;

document.addEventListener("DOMContentLoaded", () => {
    const footerPlaceholder = document.getElementById("footer-placeholder");
    if (footerPlaceholder) {
        footerPlaceholder.innerHTML = footerHTML;
    }
});
