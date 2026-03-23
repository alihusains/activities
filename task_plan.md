# Task Plan: Activity Books GitHub Pages

## Phase 1: Research & Setup (Research Mode)
- [ ] Research specific GitHub Action for "latest" release tagging.
- [ ] Identify a high-quality Serif font from Google Fonts for the "Editorial" look.
- [ ] Define the exact JSON schema for `metadata.json`.

## Phase 2: Metadata Generation (Implementation)
- [ ] Create `generate_metadata.py` to walk the directory and build `metadata.json`.
- [ ] Test the script locally to ensure it handles nested directories and spaces in filenames.

## Phase 3: GitHub Actions Workflow (Infrastructure)
- [x] Create `.github/workflows/deploy.yml`.
- [x] Step 1: Generate metadata.
- [x] Step 2: Create individual zips for each top-level category.
- [x] Step 3: Use a Release action to upload category zips to a `latest` release tag.
- [x] Step 4: Build/Deploy the frontend to GitHub Pages.

## Phase 4: Frontend Development (Design & Code)
- [x] Set up basic HTML/Tailwind structure.
- [x] Implement the "Editorial" design (Serif fonts, clean layout).
- [x] Fetch `metadata.json` and render the file browser.
- [x] Implement conditional download logic (CDN vs Raw based on size).
- [x] Add the "Iltemase Dua" footer.

## Phase 5: Verification & Launch
- [ ] Push to GitHub and verify Actions run successfully.
- [ ] Check the created Release for the zip file.
- [ ] Verify the GitHub Pages site renders correctly and links work.
