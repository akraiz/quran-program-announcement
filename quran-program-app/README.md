# Quran Program Announcement Landing Page

A beautiful, responsive landing page for the Quran Program announcement and registration.

## 📁 Project Structure

```
quran-program-app/
├── quran_program_announcement.html  # Main landing page
├── quran_program_teaser_poster.html # Teaser poster page
├── vercel.json                      # Vercel deployment configuration
├── package.json                     # Project metadata
├── og-image-generator.html          # Tool to generate social media preview image
├── og-image.svg                     # SVG version of social preview
├── DEPLOYMENT_GUIDE.md             # Deployment instructions
└── SOCIAL_MEDIA_IMAGE_INSTRUCTIONS.md # Social media setup guide
```

## 🚀 Live Site

**Production URL**: https://quran-program.vercel.app/

## 🛠️ Setup & Deployment

### Prerequisites
- Git
- GitHub account
- Vercel account (free tier works)

### Deployment Steps

1. **Deploy to Vercel**:
   - The site is connected to GitHub: `akraiz/quran-program-announcement`
   - Vercel auto-deploys on every push to `main` branch
   - No build step required (static HTML)

2. **Update Content**:
   - Edit `quran_program_announcement.html`
   - Commit and push to GitHub
   - Vercel will automatically redeploy

## 📱 Social Media Preview

To enable social media previews (Facebook, Twitter, WhatsApp):

1. Create `og-image.png` (1200x630px)
2. Use `og-image-generator.html` as a template
3. Upload to project root
4. Clear Facebook cache: https://developers.facebook.com/tools/debug/

See `SOCIAL_MEDIA_IMAGE_INSTRUCTIONS.md` for detailed steps.

## 📧 Email Integration

The registration form uses EmailJS to send registration emails.

- Service ID: `service_qc5k53g`
- Template ID: `template_nl26k4v`
- Public Key: `Cvr4J4Be4ibRxRMeF`

See `EMAIL_SETUP_INSTRUCTIONS.md` in parent directory for setup details.

## 🎨 Features

- ✅ Fully responsive design (mobile, tablet, desktop)
- ✅ RTL (Right-to-Left) Arabic support
- ✅ Beautiful Islamic-inspired design
- ✅ EmailJS form integration
- ✅ Social media meta tags (Open Graph, Twitter Cards)
- ✅ Smooth animations and transitions
- ✅ SEO optimized

## 📝 Notes

- The main HTML file is self-contained (includes all CSS and JavaScript)
- No build process required
- All external resources use CDN links
- Fonts loaded from Google Fonts (Amiri, Cairo)

## 🔗 Related Files

- Email templates and setup: See parent directory `EMAIL_*` files
- Audio processing scripts: See parent directory `*audio*.py` files

