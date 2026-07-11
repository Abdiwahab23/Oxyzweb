const modalHTML = `
  <!-- Distributor Modal -->
  <div id="distributorModal" class="modal-overlay">
    <div class="modal-content">
      <button class="modal-close" onclick="closeDistributorModal()">&times;</button>
      
      <div class="modal-header">
        <div style="font-size: 11px; font-weight: 700; letter-spacing: 1px; color: var(--text-muted); text-transform: uppercase; margin-bottom: 8px;">HEALTH & WELLNESS</div>
        <h3 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 8px;">Become a Distributor</h3>
        <p style="font-size: 14px; color: var(--text-body); margin-bottom: 24px;">Tell us about your business &mdash; we'll follow up with territory availability and terms.</p>
      </div>

      <form class="distributor-form" onsubmit="sendDistributorToWhatsApp(event)">
        <div class="form-group">
          <label>FULL NAME</label>
          <input type="text" id="distName" placeholder="Your name" required />
        </div>
        <div class="form-group">
          <label>EMAIL ADDRESS</label>
          <input type="email" id="distEmail" placeholder="Your email address" required />
        </div>
        <div class="form-group">
          <label>PHONE NUMBER</label>
          <input type="tel" id="distPhone" placeholder="Your phone number" required />
        </div>
        <div class="form-group">
          <label>COMPANY</label>
          <input type="text" id="distCompany" placeholder="Company or clinic name" required />
        </div>
        <div class="form-group">
          <label>COUNTRY / TERRITORY</label>
          <select id="countrySelect" required>
            <option value="" disabled selected>Select your market</option>
            <option value="iraq">Iraq</option>
            <option value="saudi-arabia">Saudi Arabia</option>
            <option value="uae">United Arab Emirates</option>
            <option value="qatar">Qatar</option>
            <option value="kuwait">Kuwait</option>
            <option value="oman">Oman</option>
            <option value="bahrain">Bahrain</option>
            <option value="malaysia">Malaysia</option>
            <option value="singapore">Singapore</option>
            <option value="usa">USA</option>
            <option value="other">Other</option>
          </select>
        </div>
        <div class="form-group">
          <label>PARTNERSHIP INTEREST</label>
          <select id="distInterest" required>
            <option value="" disabled selected>Select one</option>
            <option value="distributor">Distributor</option>
            <option value="pharmaceutical">Pharmaceutical Partner</option>
            <option value="scientific">Scientific Office</option>
            <option value="investor">Healthcare Investor</option>
          </select>
        </div>
        <div class="form-group">
          <label>MESSAGE</label>
          <textarea id="distMessage" placeholder="Tell us about your business and goals" rows="4" required></textarea>
        </div>
        <button type="submit" class="btn btn-primary" style="width: 100%; background-color: var(--gold); border-color: var(--gold);">Submit Partnership Request</button>
      </form>
    </div>
  </div>
`;

document.addEventListener("DOMContentLoaded", () => {
    document.body.insertAdjacentHTML('beforeend', modalHTML);
    
    // Add event listener for closing on outside click after it's injected
    const distModal = document.getElementById('distributorModal');
    if (distModal) {
      distModal.addEventListener('click', function(e) {
        if (e.target === this) {
          closeDistributorModal();
        }
      });
    }
});

window.sendDistributorToWhatsApp = function(e) {
  e.preventDefault();
  const name = document.getElementById('distName').value;
  const email = document.getElementById('distEmail').value;
  const phone = document.getElementById('distPhone').value;
  const company = document.getElementById('distCompany').value;
  const countrySelect = document.getElementById('countrySelect');
  const countryText = countrySelect.options[countrySelect.selectedIndex].text;
  const interestSelect = document.getElementById('distInterest');
  const interestText = interestSelect.options[interestSelect.selectedIndex].text;
  const message = document.getElementById('distMessage').value;
  const waMessage = `*New Partnership Request* 🤝\n-----------------------------------\n*Name:* ${name}\n*Email:* ${email}\n*Phone:* ${phone}\n*Company:* ${company}\n*Country:* ${countryText}\n*Interest:* ${interestText}\n\n*Message:*\n${message}\n-----------------------------------`;
  const waUrl = `https://wa.me/6586163762?text=${encodeURIComponent(waMessage)}`;
  window.open(waUrl, '_blank');
  closeDistributorModal();
};

window.openDistributorModal = function(countryCode) {
  if(countryCode) { document.getElementById('countrySelect').value = countryCode; }
  document.getElementById('distributorModal').classList.add('active');
};

window.closeDistributorModal = function() {
  document.getElementById('distributorModal').classList.remove('active');
};
