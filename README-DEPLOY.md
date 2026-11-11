# OwnVoice Studio site: deploy guide

This folder is a complete static website, GitHub Pages compatible, built as
OwnVoice Studio's PRIMARY public website. It is a full product site served
from the .tech domain itself. It is not a redirect, not a parked page, and
not a pointer to a product hosted elsewhere. Keep it that way: every page,
price, and contact route lives here.

## The domain lives in one place

- `config/site.json` holds the single `domain` value (lead candidate:
  ownvoice.tech).
- If the purchased name differs, edit that one value, then run:

  `python3 tools/set-domain.py .`

  The script rewrites CNAME, sitemap.xml, robots.txt, site.webmanifest,
  and every canonical, Open Graph, and JSON-LD URL in the HTML pages.
  Internal navigation is relative and never needs editing.

## Deploy steps once the domain is purchased

1. Confirm the final name in `config/site.json` and run the set-domain
   script above. Read CNAME back: it must contain the bare domain only,
   one line, no https prefix.
2. Create a GitHub repository for this site (or a dedicated branch) and
   push this folder's contents as the site root. The `.nojekyll` file is
   already in place.
3. In the repository, open Settings, then Pages. Set the source to the
   publishing branch and root folder. Set the custom domain to the exact
   value in CNAME, and tick Enforce HTTPS once the certificate is issued.
4. At the registrar where the .tech name was bought, set DNS:
   - Apex (the bare domain): four A records to GitHub Pages:
     185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153.
     Add the matching AAAA records if IPv6 is wanted:
     2606:50c0:8000::153, 2606:50c0:8001::153, 2606:50c0:8002::153,
     2606:50c0:8003::153.
   - www: one CNAME record pointing to the GitHub Pages host name for the
     repository (the `<owner>.github.io` name shown in Pages settings).
5. Wait for DNS to propagate, then verify live, in this order:
   - The bare domain loads the home page over HTTPS with a valid
     certificate, and www resolves to the same site.
   - Every page in sitemap.xml returns 200: home, process, pricing,
     about, contact, privacy, terms.
   - A bad path returns the custom 404 page.
   - View source on the home page: the canonical URL is the live domain.
6. Fund compliance hold: the site must STAY live and working on the .tech
   domain as OwnVoice Studio's primary website through evaluation and,
   on an award, for 24 months after payment (No Excuses Fund Terms,
   section 2.6). Do not replace it with a redirect or a holding page at
   any point in that window. Renew the domain on time; a lapsed
   registration breaks compliance and the site at once.
7. Optional after go-live: submit sitemap.xml in Google Search Console
   for the new domain property.

## Fullest use of the domain (empire benefit checklist)

- Email on the domain: once DNS is live, the registrar or Zoho route can
  add studio addresses on the .tech domain later. NOTE: the published
  contact email of record today is contact@onikanglobal.com. Do not
  change any published contact address until Frank rules on it, and if it
  ever changes, update config/site.json and every page in the same pass.
- Subdomains stay available for studio tools later (for example an intake
  or review subdomain) without touching the primary site.
- Keep this site as the canonical link for OwnVoice Studio in store
  listings, the Papermark deck, and grant applications, so every surface
  points at the primary site on the .tech domain.

## QC record for this build (2026-11-11)

- Zero em dashes across the whole tree (grep proof in the build report).
- All internal links resolve to files in this folder (script checked).
- Pricing arithmetic checked: 5h = $1,400 (minimum), 7h = $1,800
  (typical), 10h = $2,400, 12.5h reaches the $2,900 maximum.
- Copy uses facts of record only: pricing, consent first intake,
  pronunciation review loop, masters owned outright, Ghost Narrator
  heritage line, contact@onikanglobal.com, (917) 727-6096, Pennsylvania.
