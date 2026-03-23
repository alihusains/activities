# Findings: Activity Books GitHub Pages

## Project Goals
- Create a high-quality GitHub Pages site to browse and download activity books (PDFs).
- Automate zipping and releasing the entire directory structure on every push.
- Provide "Download All" (latest zip) and individual file/directory downloads.
- Custom footer: "Iltemase Dua".

## Technical Strategy
- **Frontend**: Single Page Application (SPA) using React or pure HTML/JS + Tailwind CSS for a "Refined/Editorial" look.
- **Metadata**: A CI script (Python or Node.js) will run on every push to generate a `metadata.json` file. This JSON will map the directory structure and file sizes/types.
- **GitHub Actions**:
  - `generate-metadata`: Scans directories and writes `metadata.json`.
  - `create-release`: Zips the whole repo (excluding hidden files/GH actions) and creates/updates a "latest" release using a tag like `v-latest`.
  - `deploy-pages`: Builds the frontend and deploys it to `gh-pages` branch.
- **Aesthetic Direction**: "Editorial Minimalist"
  - Large serif typography for headings.
  - High-contrast monochromatic palette with a single soft accent color (e.g., #fdfcf0 background).
  - Clean card-based or list-based layout for directories.
  - PDF icons and preview thumbnails if possible.

## Directory Structure Analysis
- `4-7 years/`
- `8-12 years/`
- `8-16 years/`
- `Quran/`
- `Timelines-14/`
- Standalone PDFs: `Aimmatiy_Adult_Upload_AA39-v1_May2020.pdf`, `Hadith-Kisaa-Worksheet.pdf`, etc.

## Challenges & Solutions
- **Dynamic Content**: GitHub Pages is static. **Solution**: The `metadata.json` generated at build time serves as our "database".
- **Download Directory**: Browsers can't download folders. **Solution**: The GH Action will also create individual zips for each top-level directory and attach them to the release, or we point the "Download Directory" button to a script-generated zip path if hosted on LFS/Assets. Better yet, point to the GitHub Release assets which are permanent URLs.
