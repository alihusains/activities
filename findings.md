# Findings: Activity Books GitHub Pages

## Project Goals
- Create a high-quality GitHub Pages site to browse and download activity books (PDFs).
- Automate zipping and releasing the entire directory structure on every push.
- Provide "Download All" (latest zip) and individual file/directory downloads.

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
- **Download Directory**: Browsers can't download folders. **Solution**: The GH Action generates individual ZIP archives for each top-level category and uploads them to the "latest" release. The frontend dynamically links the "Download Folder" button to these release assets.
- **Large File Handling**: Files >20MB are served via `raw.githubusercontent.com`, while smaller files use the standard GitHub Pages CDN for better performance.

## Visual Identity
- **Theme**: Dark Mode (Glassmorphism)
- **Typography**: Bebas Neue (Headings), Plus Jakarta Sans (Body)
- **Previews**: PDF.js renders the first page of each document directly in the browser as a preview thumbnail.
