# Public website coverage — November 21, 2026

Compared the organization's current public repository inventory with the canonical website at https://simplemindsstudios.com/.

## Findings and changes

- 22 public organization repositories; all were present in the project directory before this change.
- 13 public repositories lacked a direct homepage link. All 22 now have a card in the homepage collection, alongside Hart, in Motion.
- Brad Devowe's **The Anonymous Family** and Bart Salazar's **STILL HERE — A Tree of Memory** were already live and linked near the bottom of the homepage. They are now featured immediately after the opening section, with an opening-screen link and a desktop navigation link.
- The header's **All projects** link now remains visible on phones. Previously the navigation links disappeared below 900px.
- The family-history section has its own display layer above the decorative background.
- The Aurelia & Wayfinder room now links to the public research directory rather than displaying an inactive preparation notice.
- One reviewed catalog generates both the homepage collection and the static searchable directory during the build. GitHub Pages checks that the catalog includes every current public organization repository before publishing.
- The previously public Fractalnomia overview remains on the homepage. Its source repository and research files remain private and are excluded from the public catalog.

## Repository comparison

“Linked” includes a public presentation or the repository itself for studio documentation. The homepage “before” column refers to direct links in the prior index, not links reachable through the full directory.

| Public repository | Public title | Homepage before | Homepage now | Directory now |
| --- | --- | --- | --- | --- |
| `the-anonymous-family` | The Anonymous Family | Linked | Linked | Linked |
| `still-here` | STILL HERE — A Tree of Memory | Linked | Linked | Linked |
| `RomanMAST` | LensBridge | Linked | Linked | Linked |
| `project-voyager-iii` | Voyager III | No direct link | Linked | Linked |
| `project-wayfinder` | Project Wayfinder | No direct link | Linked | Linked |
| `project-aurelia` | Project Aurelia | No direct link | Linked | Linked |
| `witness-multiple` | WITNESS / MULTIPLE | No direct link | Linked | Linked |
| `the-moving-frame` | The Moving Frame | No direct link | Linked | Linked |
| `lincd-public` | Linc(d) | Linked | Linked | Linked |
| `spineflow-tiny-showcase` | SpineFlow Tiny | Linked | Linked | Linked |
| `mi-tech-bros` | MI Tech Bros | No direct link | Linked | Linked |
| `the-hart-protocol` | The Hart Protocol | Linked | Linked | Linked |
| `Low-Visibility-Lookbooks` | Low Visibility — Lookbooks | No direct link | Linked | Linked |
| `low-visibility-brand-bible` | Low Visibility — Brand Bible | Linked | Linked | Linked |
| `glam-confession` | Glam Confession | Linked | Linked | Linked |
| `thinking-clearer` | Thinking Clearer with Lincoln | Linked | Linked | Linked |
| `best-human-moment` | The Human Room | No direct link | Linked | Linked |
| `public-website.github.io` | Atlas Museum | No direct link | Linked | Linked |
| `simplemindsstudios.github.io` | Simple Minds Studios website | Linked | Linked | Linked |
| `sms-standards` | SMS Standards | No direct link | Linked | Linked |
| `agent-skills` | Agent Skills — Linc(d) prototype | No direct link | Linked | Linked |
| `.github` | Organization profile & attribution | No direct link | Linked | Linked |

## Validation

- Live GitHub public-inventory comparison: all 22 public repositories represented.
- All 23 catalog destinations returned HTTP 200 during this audit.
- Root-domain and GitHub Pages project-path builds passed.
- Homepage JavaScript syntax check passed.
- Browser confirmed 23 catalog-backed homepage cards and both family-history exhibits before the rooms.
- Phone layouts at 390px and 320px: persistent All projects link, no horizontal document overflow.
- Directory search for Brad returned his exhibit; category and project anchors are stable.
- No private repository content, email configuration, or DNS records were changed.
