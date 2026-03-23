# Progress: Activity Books GitHub Pages

## Session: 2026-03-24
- [x] Removed full-repo ZIP generation due to size constraints (>2GB).
- [x] Updated `deploy.yml` to only generate and release category-wise ZIPs.
- [x] Redesigned `index.html` with a minimalist dark theme and breadcrumb navigation.
- [x] Implemented conditional download logic for individual files:
    - Files < 20MB: Direct download from GitHub Pages/CDN.
    - Files >= 20MB: Download from `raw.githubusercontent.com`.
- [x] Removed "Full Library" download button from UI.
- [x] Regenerated `metadata.json` to include file sizes.
- [ ] Next: Push changes and verify deployment.
