# Deployment Guide - Quran Program Announcement

## Step 1: Create GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the **+** icon in the top right corner
3. Select **New repository**
4. Repository name: `quran-program-announcement` (or any name you prefer)
5. Set it to **Public** (or Private if you prefer)
6. **DO NOT** initialize with README, .gitignore, or license (we already have these)
7. Click **Create repository**

## Step 2: Push Code to GitHub

After creating the repository, GitHub will show you commands. Use these:

```bash
cd /Users/ahmedkraiz/Desktop/Text
git remote add origin https://github.com/YOUR_USERNAME/quran-program-announcement.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

## Step 3: Deploy to Vercel

### Option A: Using Vercel Website (Recommended)

1. Go to [vercel.com](https://vercel.com) and sign in (use GitHub to sign in)
2. Click **Add New Project**
3. Import your GitHub repository: `quran-program-announcement`
4. Vercel will auto-detect the settings:
   - Framework Preset: **Other**
   - Root Directory: `./` (leave as is)
5. Click **Deploy**
6. Wait for deployment to complete (usually 1-2 minutes)
7. Your site will be live at: `https://your-project-name.vercel.app`

### Option B: Using Vercel CLI

If you prefer command line:

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
cd /Users/ahmedkraiz/Desktop/Text
vercel

# Follow the prompts:
# - Set up and deploy? Yes
# - Which scope? (select your account)
# - Link to existing project? No
# - Project name? quran-program-announcement
# - Directory? ./
# - Override settings? No
```

## Step 4: Custom Domain (Optional)

1. In Vercel dashboard, go to your project
2. Click **Settings** → **Domains**
3. Add your custom domain
4. Follow DNS configuration instructions

## Troubleshooting

- If the page doesn't load, check that `quran_program_announcement.html` is in the root directory
- Make sure all external resources (fonts, icons) are accessible
- Check Vercel deployment logs for any errors

## Updating the Site

After making changes:

```bash
cd /Users/ahmedkraiz/Desktop/Text
git add .
git commit -m "Update: description of changes"
git push
```

Vercel will automatically redeploy when you push to GitHub!

