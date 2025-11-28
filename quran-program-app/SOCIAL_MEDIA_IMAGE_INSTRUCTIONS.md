# Social Media Image Setup Instructions

## Quick Setup (Recommended)

I've added all the meta tags to your HTML file. Now you need to create and upload the Open Graph image.

### Option 1: Use Online Service (Easiest)

1. Go to https://www.canva.com/ or https://www.figma.com/
2. Create a new design with dimensions: **1200 x 630 pixels**
3. Design your image with:
   - Title: "برنامج مدارسة سورة الفاتحة"
   - Subtitle: "وتصحيح تلاوتها"
   - Description: "رحلة روحية عميقة نحو فهم السبع المثاني"
   - Use your brand colors (green #0a5d61, gold #eab308)
4. Export as PNG
5. Name it `og-image.png`
6. Upload it to your Vercel project root

### Option 2: Screenshot the Generator

1. Open `og-image-generator.html` in your browser
2. Take a screenshot at exactly 1200x630 pixels
3. Save as `og-image.png`
4. Upload to your project

### Option 3: Use Vercel OG Image Generator

You can use Vercel's built-in OG image generator by creating an API route, but the simplest is to just upload a static image.

## Upload the Image

1. Add `og-image.png` to your project root (same folder as `quran_program_announcement.html`)
2. Commit and push to GitHub:
   ```bash
   git add og-image.png
   git commit -m "Add social media preview image"
   git push
   ```
3. Vercel will automatically deploy it

## Test Your Social Media Preview

After deploying:

1. **Facebook Debugger**: https://developers.facebook.com/tools/debug/
   - Enter: `https://quran-program.vercel.app/`
   - Click "Scrape Again" to refresh

2. **Twitter Card Validator**: https://cards-dev.twitter.com/validator
   - Enter: `https://quran-program.vercel.app/`

3. **LinkedIn Post Inspector**: https://www.linkedin.com/post-inspector/
   - Enter: `https://quran-program.vercel.app/`

## Current Status

✅ Meta tags added to HTML
⏳ Image needs to be created and uploaded
⏳ After upload, test with the validators above

## Image Specifications

- **Size**: 1200 x 630 pixels (1.91:1 ratio)
- **Format**: PNG or JPG
- **File size**: Under 8MB (recommended: under 1MB)
- **File name**: `og-image.png` (must match the meta tag)

