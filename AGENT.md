# AGENT.md

This document serves as the single source of truth for AI agents (and human contributors) interacting with, maintaining, or modernizing this repository.

---

## 1. Project Overview & Identity

- **Owner**: Xuyang Kang (Senior SRE-SWE at Google; ex-DoorDash, ex-ExaWizards, ex-Indeed; MSc University of Edinburgh / University of York, BSc Nankai University).
- **Primary Domain**: [https://xuyang.me](https://xuyang.me)
- **Deployment Platform**: GitHub Pages (`xuyangkang/xuyangkang.github.io`), served directly from the root of the `master` branch.
- **Repository Purpose**: Personal portfolio, resume gateway, and showcase for developer experiments.

---

## 2. Repository Layout

```text
.
├── AGENT.md            # AI agent instructions, guidelines, and context (this file)
├── README.md           # Repository overview and local preview guide
├── .gitignore          # Ignore rules for OS artifacts, editor configs, and temp files
├── CNAME               # Custom domain configuration (xuyang.me)
├── index.html          # Main homepage (profile, experience, education, booking)
├── Virgil.woff2        # Custom font providing the signature hand-drawn / sketch aesthetic
├── resume.pdf          # Latest PDF resume
├── resume.html         # HTTP-equiv & JS redirect to /resume.pdf
├── resume/
│   └── index.html      # Directory index redirect to /resume.pdf
├── market/
│   ├── index.html      # "炼金控制台" (multi-asset TradingView dashboard with auto-cycle)
│   └── index_dev.html  # Development version of the market console
├── py/
│   └── index.html      # In-browser Python REPL running on Brython
└── *.svg, *.png, *.jpg # Asset logos (Google, DoorDash, Edinburgh, York, Nankai, QR code, etc.)
```

---

## 3. Technology Stack & Architectural Principles

1. **Zero-Build Static Architecture**:
   - Built with vanilla HTML5, CSS3, and modern client-side JavaScript.
   - No build step, bundler, or package manager required. Changes committed to `master` take effect immediately on GitHub Pages.
   - Do not introduce heavy frontend frameworks (e.g., React, Vue, Next.js) unless explicitly requested.

2. **Distinctive Visual Aesthetic**:
   - The homepage uses the **Virgil** font (`Virgil.woff2`, Excalidraw-like font) to cultivate a friendly, clean, and authentic developer persona.
   - Content presentation is structured around responsive, card-based layouts.

3. **Autonomous Sub-Applications**:
   - `/market`: Standalone TradingView embed displaying BTC, SP500, USDJPY, and Gold with automated tab-switching.
   - `/py`: Client-side Python REPL powered by Brython.
   - `/resume` & `/resume.html`: Dual redirection handlers pointing directly to `/resume.pdf`.

---

## 4. Agent Operational Rules & Conventions

### 4.1. Inviolable Constraints
- **Preserve `CNAME`**: Never delete or alter `CNAME` (`xuyang.me`). Removing it will break the custom domain mapping.
- **Maintain Direct Static Serving**: Keep asset paths relative and ensure directory indexes (`/resume/`, `/market/`, `/py/`) resolve correctly without requiring a custom routing server.
- **Avoid Breaking Sub-tools**: Do not touch or modify the embedded scripts in `/market` or `/py` unless specifically requested.

### 4.2. Coding & Design Standards
- **Design Tokens**: When enhancing styles, prefer CSS custom properties (`--color-bg`, `--color-card`, `--color-text`, etc.) to facilitate clean maintenance and theming.
- **Typography**: When adding or updating text, respect the Virgil font pairing. Fall back gracefully to `sans-serif` or modern system fonts.
- **Responsiveness**: Always verify changes on mobile viewports (`max-width: 600px`). Ensure cards and icon-text combinations wrap cleanly.
- **Asset Handling**: Maintain SVG vector quality for logos where possible. Ensure all image assets retain proper aspect ratios.
- **SEO & Social Cards**: Keep OpenGraph (`og:title`, `og:description`), Twitter Card metadata, and canonical links synchronized with `https://xuyang.me`.

---

## 5. Common Maintenance Workflows

### Updating Work Experience or Education
- Edit `index.html` within the `.container` or education card sections.
- Keep bullet points action- and impact-oriented.
- Follow the existing `.icon-text` structure (logo image + title/time span).

### Updating Resume
- Overwrite `resume.pdf` with the new document.
- Verify that `resume.html` and `resume/index.html` continue to redirect properly.

### Local Previewing
Since this is a pure static site, run any lightweight local server from the repository root:
```bash
# Python 3
python -m http.server 8000

# Node (npx)
npx serve .
```
Open `http://localhost:8000` to preview.
