# AGENT.md

This document serves as the single source of truth for AI agents (and human contributors) interacting with, maintaining, or modernizing this repository.

---

## 1. Project Overview & Identity

- **Owner**: Xuyang Kang (Senior SRE-SWE at Google - Agentic AI SRE & Ads SRE; ex-DoorDash, ex-ExaWizards, ex-Indeed; MSc University of Edinburgh / University of York, BSc Nankai University).
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
│   ├── index.html      # JEIP & JEQP Dividend Monitor (monthly payout stats, history & TradingView charts)
│   └── index_dev.html  # Development version of the market console
├── py/
│   └── index.html      # In-browser Python REPL running on Brython
└── *.svg, *.png, *.jpg # Asset logos (Google, DoorDash, Edinburgh, York, Nankai, QR code, etc.)
```

---

## 3. Technology Stack & Architectural Principles

1. **Zero-Build Static Architecture**:
   - Built with vanilla HTML5, CSS3, and modern client-side JavaScript.
   - Pure HTML/CSS for `index.html` — **do not add JavaScript or build steps** to the homepage.
   - Changes committed to `master` take effect immediately on GitHub Pages.
   - Do not introduce heavy frontend frameworks (e.g., React, Vue, Next.js) unless explicitly requested.

2. **Distinctive Visual Aesthetic**:
   - The homepage uses the **Virgil** font (`Virgil.woff2`, Excalidraw-like font) to cultivate a friendly, clean, and authentic developer persona.
   - Content presentation is structured around semantic tags (`<header>`, `<main>`, `<section>`, `<footer>`) and responsive, CSS Grid card-based layouts.

3. **Autonomous Sub-Applications**:
   - `/market`: JEIP & JEQP Dividend Monitor (clean sans-serif dashboard, high-density monthly distribution tracker and TradingView widgets).
   - `/py`: Client-side Python REPL powered by Brython.
   - `/resume` & `/resume.html`: Dual redirection handlers pointing directly to `/resume.pdf`.

---

## 4. Agent Operational Rules & Conventions

### 4.1. Inviolable Constraints
- **Preserve `CNAME`**: Never delete or alter `CNAME` (`xuyang.me`). Removing it will break the custom domain mapping.
- **Maintain Direct Static Serving**: Keep asset paths relative and ensure directory indexes (`/resume/`, `/market/`, `/py/`) resolve correctly without requiring a custom routing server.
- **Avoid Breaking Sub-tools**: Do not touch or modify the embedded scripts in `/market` or `/py` unless specifically requested.

### 4.2. Specific Design & Content Preferences
- **Languages Section**: **Must always use country flag emojis** via HTML entities (`&#x1F1EC;&#x1F1E7; &#x1F1E8;&#x1F1F3; &#x1F1EF;&#x1F1F5;` for 🇬🇧 🇨🇳 🇯🇵) styled with `.emoji`. **Never replace them with text language labels** (e.g. "English · 中文 · 日本語").
- **Education Section**: Keep education items unified **without graduation years** (e.g., `MSc in HPC and DS`, `MSc in Computer Science`, `BSc in Computer Science`).
- **Semantic HTML**: Maintain clean semantic HTML (`<header>`, `<main>`, `<section>`, `<footer>`) with descriptive headings and accessibility attributes (`aria-label`, `rel="noopener noreferrer"`).
- **Design Tokens**: Style via CSS custom properties (`--bg-color`, `--card-bg`, `--text-primary`, `--border-color`, etc.) defined in `:root`.
- **Card Spacing**: Use CSS Grid `gap` (e.g., `gap: 20px`) for card layouts; avoid adding `margin: 20px` directly onto grid cards to prevent doubled spacing.
- **Responsiveness**: Mobile breakpoint is `@media (max-width: 600px)`:
  - Force cards into single column (`grid-template-columns: 1fr`).
  - Keep QR code size manageable (e.g., `width: 150px`).
- **Typography**: Respect Virgil font pairing with fallback to `sans-serif`.
- **SEO & Social Cards**: Keep OpenGraph (`og:title`, `og:description`, `og:url`, `og:image`) and canonical links updated.

---

## 5. Common Maintenance Workflows

### Updating Work Experience or Education
- Edit `index.html` within the `<section id="experience">` or `<section id="education">`.
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
