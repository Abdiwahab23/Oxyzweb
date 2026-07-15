# OXYZ Health & Wellness - Developer Guide

Welcome to the OXYZ Health & Wellness repository! This guide is intended for developers taking over or contributing to the project. It outlines the technology stack, architecture, and instructions for how the project is built.

## Technology Stack

This project is built using a **pure Vanilla stack** to maximize performance, keep the codebase lightweight, and avoid unnecessary dependencies. 

* **HTML**: HTML5
* **CSS**: Vanilla CSS3 (Custom Properties/Variables, Grid, Flexbox)
* **JavaScript**: Vanilla ES6 JavaScript (No frameworks like React, Vue, or jQuery)
* **Hosting / Deployment**: GitHub Pages (Note the `.nojekyll` file, which tells GitHub Pages to bypass Jekyll processing and serve the static files exactly as they are).

## Project Architecture & Structure

Since there is no bundler (like Webpack or Vite), everything is linked directly in the HTML. 

### Component Reusability (JavaScript Injection)
To avoid duplicating the Navigation Bar and Footer across multiple HTML pages, we use JavaScript to inject these components. 
* `<div id="nav-placeholder"></div>` is replaced by the HTML inside `js/nav.js`.
* `<div id="footer-placeholder"></div>` is replaced by the HTML inside `js/footer.js`.

### Directory Layout

```text
├── css/                  # All stylesheets
│   ├── style.css         # Main entry point (imports the other files)
│   ├── variables.css     # CSS Custom Properties (Colors, Fonts, Spacing)
│   ├── layout.css        # Structural CSS (Navbar, Hero, Grid containers)
│   └── components.css    # UI elements (Cards, Buttons, Modals, Galleries)
│
├── js/                   # JavaScript files
│   ├── script.js         # Core logic (Scroll animations, DOM manipulation)
│   ├── nav.js            # Navbar HTML template and mobile menu logic
│   ├── footer.js         # Footer HTML template
│   └── modal.js          # Logic for Lightbox/Modals
│
├── [Asset Folders]       # Images, Videos, and specific page assets
│   ├── images/           # Global icons, logos, videos
│   ├── Bioseries/        # Assets for the bioseries.html page
│   ├── Products/         # Product imagery
│   ├── StemCell/         # Assets for oxyz-cell.html
│   └── ...               
│
└── *.html                # Main Pages
    ├── index.html        # Homepage
    ├── bioseries.html    # BioSeries Products Page
    ├── oxyz-cell.html    # Stem Cell Therapy Page
    ├── training.html     # Training & Consultation Page
    ├── about.html        # About Us Page
    └── contact.html      # Contact Us Page
```

## Styling Guide

The styling relies heavily on CSS Custom Properties (CSS variables) defined in `css/variables.css`. When adding new components, always use these variables to maintain brand consistency:

* **Primary Colors:** `var(--primary)`, `var(--primary-dark)`, `var(--gold)`
* **Neutral Colors:** `var(--white)`, `var(--bg-light)`, `var(--text-dark)`, `var(--text-body)`, `var(--text-muted)`
* **Spacing & Shadows:** `var(--radius)`, `var(--shadow)`, `var(--transition)`

### Buttons
Buttons use base `.btn` classes combined with variants.
* `.btn-primary` (Green background)
* `.btn-gold` (Gold background)
* `.btn-outline` (White text/border - use ONLY on dark backgrounds)
* `.btn-outline-primary` (Green text/border - use on white backgrounds/cards)

## How to Run the Project Locally

Because it's a static site, there is no `npm install` or build step required. 

However, because we use ES6 modules and JavaScript to fetch/inject components (like the nav and footer), you **cannot** just double-click the `.html` files (this will trigger a CORS policy error in your browser).

You must run a local web server. You can do this using any of the following methods:

**Method 1: VS Code Live Server (Recommended)**
1. Install the "Live Server" extension in VS Code.
2. Right-click on `index.html` and select "Open with Live Server".

**Method 2: Python**
If you have Python installed, open your terminal in the project root and run:
`python -m http.server 8000`
Then go to `http://localhost:8000` in your browser.

**Method 3: Node.js (http-server)**
If you have Node installed:
`npx http-server`

## Making Changes & Deployment

1. Make your changes locally and verify them on your local server.
2. Ensure you haven't broken the mobile responsiveness. Check both desktop and mobile views.
3. Commit your changes and push to the `main` branch. 
4. Since the site is hosted on GitHub Pages, pushing to `main` will automatically trigger a deployment, and the live site will update shortly after.
