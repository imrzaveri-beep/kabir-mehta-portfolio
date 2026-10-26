# Delivery report: Kabir Mehta – Product Designer

## Summary
I built a complete 15-page portfolio with a dark visual style, a saved light theme and layouts for desktop and mobile. It includes four detailed product stories, original interface mockups, a nine-shot visual playground and a downloadable demo CV. The site uses the supplied logo and clearly identifies all fictional experience, testimonials and metrics. Contact enquiries work through email and WhatsApp drafts, with Formspree support ready for your form ID.

## What was built
- Home with availability, hero, selected work, services, quotes, article links and contact CTA.
- About with original illustrated avatar, story, skills, tools and experience timeline.
- Work index with All, Fintech, Health, Commerce and Travel filters.
- PayKaro case study with research, decisions, results, gallery and learnings.
- GreenCart case study with research, decisions, results, gallery and learnings.
- MedNest case study with research, decisions, results, gallery and learnings.
- Yatra Lite case study with research, decisions, results, gallery and learnings.
- Services with four priced packages, monthly retainer and six FAQs.
- Process with five steps and deliverables.
- Playground with nine original visual experiments.
- Writing with four original demo excerpts and related Medium topic links.
- Resume with web layout, printable styling and a real downloadable PDF.
- Testimonials with all six supplied demo quotes.
- Contact with validated form, email copy, WhatsApp, Calendly, phone, city map and social links.
- Privacy policy describing actual form, theme and third-party link behavior.
- Mobile menu, Cmd/Ctrl+K navigation, theme persistence, desktop cursor, motion effects and reduced-motion support.
- Unique titles/descriptions, per-case Open Graph images, favicon, sitemap, robots file and custom 404.
- GitHub Pages deployment workflow and editing/setup documentation.

## How to see it
Live preview: https://imrzaveri-beep.github.io/kabir-mehta-portfolio/ . GitHub Pages may take a few minutes after publication. Source: https://github.com/imrzaveri-beep/kabir-mehta-portfolio . Locally, run `npm ci`, `npm run build`, then `npm run preview`, and open http://127.0.0.1:5176/kabir-mehta-portfolio/ .

## Questions for you
- None.

## What we need from you
- For direct email delivery through Formspree, supply your public form ID and verified recipient; put the ID in `lib/data.js` under `config.formspreeId`. Email and WhatsApp drafts already work without it.
- Before using this demo as a real portfolio, replace fictional contact details, availability, social/Calendly profiles and career/project/testimonial claims in `lib/data.js`, `components/pages.jsx` and the MDX files. Replace or regenerate the demo CV too.
- Supply actual published article URLs to replace the clearly marked Medium topic links in `components/pages.jsx`.
- If you want analytics, provide your GA4 measurement ID for a later integration. The placeholder in `lib/data.js` is inactive and no tracking script runs.
- A custom domain is optional. `kabirmehta.design` has not been purchased or connected; this delivery uses GitHub Pages.

## Please check
- Review desktop and mobile layouts, all four project stories, prices, downloadable CV and contact details. Added case-study narrative, roles, teams, timelines and article excerpts are realistic fictional demo content.
- All supplied identities, testimonials and metrics are labeled fictional. Company names do not imply actual employment or endorsements.
- PayKaro's 41% to 79% increase is shown as 38 percentage points. Yatra Lite's 1.2-second figure is a supplied fictional product outcome, not this portfolio's measured load time.
- Email drafts require a configured email app and a final Send action. WhatsApp opens a draft for review. No real enquiry was sent during testing, and live Formspree delivery cannot be tested without your endpoint.
- Four writing links open related Medium topics because no real article URLs were supplied.
- The sitemap and project robots file are included. GitHub Pages project hosting does not give this repository control of the origin's root `/robots.txt`.

## Suggestions
- Replace demo material with approved real case-study evidence and testimonials before sharing as a professional identity.
- Connect your own Formspree form and run one real delivery test.
- Add published writing links and a verified current CV.
- Connect a purchased domain when ready.

## Bugs fixed
- Fixed mobile hero words joining when a desktop line break was hidden.
- Replaced oversized font files with official Latin WOFF2 subsets and explicit variable weights.
- Added an accessible name to the quick-navigation dialog and normalized active navigation paths.
- Cleared stale contact drafts when form fields change; incomplete forms cannot create a draft.
- Ensured assets and PDF links include the GitHub Pages repository base path.

## Technical notes
Next.js static export, React, Tailwind CSS, Framer Motion and MDX. No database, accounts or application backend. Dependency versions are pinned with a lockfile; GitHub Actions uses Node 24 LTS. Content is in `components/`, `lib/data.js` and `content/`; assets are in `public/`. No secrets or environment variables are required. Uploaded briefs, build output and dependencies are excluded from Git.

Production build and static resource-link checks pass. All 15 content routes were checked in the browser at 1440px and 360px with no page overflow, broken images, missing image descriptions or browser errors. Interactive checks covered theme persistence, mobile menu, palette and Escape focus, filters, FAQs, copy-email, required fields and email/WhatsApp draft handling. The one-page PDF was rendered and visually checked. Production dependency audit reported zero known vulnerabilities on 26 October 2026.

Lighthouse 13.5.0 in Chromium 156, measured through Chrome DevTools on 26 October 2026: local mobile homepage Accessibility **100**, Best Practices **100**, SEO **92**, Performance **80**. The separate mobile Contact accessibility audit also scored **100**. Homepage slow-4G simulation measured FCP 1.1s, LCP 5.3s, TBT 20ms and CLS 0. These are measured page-specific scores, not a claim that every route was scored. Local preview is an uncompressed static server; public hosting may differ. SEO's robots warning comes from the origin-root robots URL on the local server; the repository-level file and sitemap are exported. The requested 95+ accessibility target is met on both measured pages.
