#!/usr/bin/env python3
"""Rewrite every domain reference in this site from config/site.json.

Usage: python3 tools/set-domain.py [site-root]
Reads the "domain" value from <site-root>/config/site.json and updates:
  CNAME, sitemap.xml, robots.txt, site.webmanifest, and the absolute
  URLs (canonical, og:url, og:image, twitter:image, JSON-LD) in every
  top-level .html page. Internal navigation uses relative links and is
  never touched.
"""
import json
import re
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
cfg = json.loads((root / "config" / "site.json").read_text(encoding="utf-8"))
new_domain = cfg["domain"].strip()
new_base = f"https://{new_domain}/"

# Find the current domain from CNAME so the script works after any change.
cname_path = root / "CNAME"
old_domain = cname_path.read_text(encoding="utf-8").strip() if cname_path.exists() else ""
if not old_domain or old_domain == new_domain:
    print(f"Domain already set to {new_domain}; nothing to rewrite.")
    if old_domain != new_domain:
        cname_path.write_text(new_domain + "\n", encoding="utf-8")
    sys.exit(0)

targets = [cname_path, root / "sitemap.xml", root / "robots.txt", root / "site.webmanifest"]
targets += sorted(root.glob("*.html"))
changed = []
for path in targets:
    if not path.exists():
        continue
    text = path.read_text(encoding="utf-8")
    updated = text.replace(f"https://{old_domain}", f"https://{new_domain}").replace(old_domain, new_domain)
    if updated != text:
        path.write_text(updated, encoding="utf-8")
        changed.append(path.name)
cname_path.write_text(new_domain + "\n", encoding="utf-8")
print(f"Domain changed from {old_domain} to {new_domain} in: {', '.join(changed) or 'CNAME only'}")
print(f"Base URL is now {new_base}")
