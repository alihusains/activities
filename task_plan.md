# Task Plan: Activity Books GitHub Pages

## Phase 1: Research & Setup (Research Mode)
- [ ] Research specific GitHub Action for "latest" release tagging.
- [ ] Identify a high-quality Serif font from Google Fonts for the "Editorial" look.
- [ ] Define the exact JSON schema for `metadata.json`.

## Phase 2: Metadata Generation (Implementation)
- [ ] Create `generate_metadata.py` to walk the directory and build `metadata.json`.
- [ ] Test the script locally to ensure it handles nested directories and spaces in filenames.

## Phase 3: GitHub Actions Workflow (Infrastructure)
- [ ] Create `.github/workflows/deploy.yml`.
- [ ] Step 1: Generate metadata.
- [ ] Step 2: Zip the entire directory structure into `activity-books-full.zip`.
- [ ] Step 3: Use a Release action to upload the zip to a `latest` release tag.
- [ ] Step 4: Build/Deploy the frontend to GitHub Pages.

## Phase 4: Frontend Development (Design & Code)
- [ ] Set up basic HTML/Tailwind structure.
- [ ] Implement the "Editorial" design (Serif fonts, clean layout).
- [ ] Fetch `metadata.json` and render the file browser.
- [ ] Add the "Download All" button pointing to the Release URL.
- [ ] Add the "Iltemase Dua" footer.

## Phase 5: Verification & Launch
- [ ] Push to GitHub and verify Actions run successfully.
- [ ] Check the created Release for the zip file.
- [ ] Verify the GitHub Pages site renders correctly and links work.
