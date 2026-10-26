# Kabir Mehta — Product Designer

A fictional, 15-page product design portfolio built with Next.js static export, Tailwind CSS, Framer Motion and MDX. The supplied identity, companies, testimonials, contact information and outcomes are clearly marked as demo content. All interface illustrations are original SVG artwork; no real client screens or stock photos are used.

Live: https://imrzaveri-beep.github.io/kabir-mehta-portfolio/

## Run locally

Use Node 24 LTS (Node 22.12+ also supported).

```sh
npm ci
npm run dev
```

Open http://127.0.0.1:5176/kabir-mehta-portfolio/ . To preview the production export:

```sh
npm run build
npm run preview
```

The preview command serves static files from `out/`. It is a local development utility, not an application backend. Stop it with Ctrl+C when finished.

## Pages and editing

- `app/page.jsx`: home route; `app/[...slug]/page.jsx`: all other static routes and metadata.
- `components/pages.jsx`: page layouts and content sections.
- `components/interactive.jsx`: theme, menu, quick navigation, filters, copy-email, contact form and print controls.
- `app/globals.css`: Tailwind import, theme tokens, responsive layouts, reduced motion and resume print styles.
- `content/cases/*.mdx`: four complete fictional case studies.
- `content/articles/*.mdx`: four original demo article excerpts.
- `lib/data.js`: shared content, prices, contact/social links, canonical site URL and integration placeholders.
- `public/`: original logo, favicon, SVG mockups, nine playground shots, per-case Open Graph PNGs, local fonts and downloadable CV.
- `scripts/`: reproducible visual/CV generators and the local static preview server. The asset generator downloads official Google Fonts. Python CV generation requires ReportLab; normal npm builds use the already generated assets and need no Python.

The pages are Home, About, Work, PayKaro, GreenCart, MedNest, Yatra Lite, Services, Process, Playground, Writing, Resume, Testimonials, Contact and Privacy. There is also a custom 404, sitemap and robots file.

## Contact and integration setup

Edit `config` in `lib/data.js`:

- `formspreeId`: empty by default because no client endpoint was supplied. Create a form in your own Formspree account, configure its recipient, and put only the public form ID here. No account credential or private API key is needed. Rebuild and test with your own consented sample after activation. The form already supports success/failure states for Formspree.
- With an empty Formspree ID, a validated form prepares a `mailto:` enquiry. The visitor opens the draft and sends it in their email app. WhatsApp opens an encoded draft; it does not send automatically. No enquiries are stored by this website.
- `email`, `phone`, `calendly` and `socials`: replace fictional details before real use.
- `ga4MeasurementId`: intentionally inactive placeholder. No tracking script is loaded. Add the actual GA4 integration and appropriate privacy/consent treatment in a future update if wanted.
- Writing links currently explore the related topic on Medium. No published article URLs were supplied, so these are explicitly demo concepts rather than fabricated author publication claims. Replace links in `components/pages.jsx` when real articles are available.

Theme preference is the only localStorage value (`km-theme`). The contact form is not persisted.

## Deploy

The GitHub Actions workflow in `.github/workflows/deploy.yml` builds on pushes to `main` or manual dispatch, uploads `out/`, then deploys to GitHub Pages. Set repository Pages source to **GitHub Actions** if it is not already configured. The Mr Developer delivery worker performs publication for this request.

`next.config.mjs` uses `output: 'export'`, `basePath: '/kabir-mehta-portfolio'` and `trailingSlash: true`. Keep the base path in `lib/data.js` in sync. For a future custom domain, update `SITE`, base paths, metadata and workflow/domain settings together. No custom domain has been configured.

The project-level `robots.txt` lives at `/kabir-mehta-portfolio/robots.txt`. Crawlers look for an origin-level robots file; that requires control of the account's root GitHub Pages site or a custom domain. The sitemap and canonical metadata are already present.

## Accessibility and validation

- Keyboard-accessible navigation, native dialog, visible focus, skip link, labeled fields, live status, image descriptions and reduced motion support.
- Cmd/Ctrl+K opens quick navigation; Tab/arrows select links, Enter opens and Escape closes with focus returned to the trigger.
- All 15 pages inspected in the browser at 1440px and 360px: no horizontal overflow, missing image alt attributes or broken images; one H1 and distinct titles.
- Theme persistence, mobile navigation, filters, palette, FAQ, copy-email and enquiry validation/draft lifecycle exercised.
- PDF generated, text checked and page render visually inspected. Static export resource links checked for missing files.
- `npm run build`, `git diff --check`, and production `npm audit` pass; audit reports zero known vulnerabilities at delivery time.
- Lighthouse scores and scope are recorded in DELIVERY.md. Scores vary with device, network, browser and hosting.

The supplied company names and all metrics are fictional demo narratives, not endorsements. PayKaro's 41% to 79% change is accurately shown as **38 percentage points**. Yatra Lite's 1.2-second number describes its fictional case study; it is not a measured speed claim for this website.

## Asset credits

Client supplied `public/logo.svg`; favicon and Open Graph assets use that mark. SVG illustrations are original for this project. Space Grotesk, Inter and JetBrains Mono are self-hosted official Google Fonts Latin WOFF2 subsets, with their SIL Open Font License texts in `public/fonts/`. System fallbacks cover symbols outside the Latin subset. Uploaded brief/reference files are excluded from publication.
