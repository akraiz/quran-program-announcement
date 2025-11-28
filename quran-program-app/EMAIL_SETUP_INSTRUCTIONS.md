# Email Setup Instructions - Quran Program Registration Form

This guide will help you set up the email functionality for the registration form.

## Option 1: EmailJS (Recommended - No Backend Required)

### Step 1: Create EmailJS Account
1. Go to https://www.emailjs.com/
2. Sign up for a free account (free tier allows 200 emails/month)

### Step 2: Connect Your Email Service
1. Go to **Email Services** in your dashboard
2. Click **Add New Service**
3. Choose your email provider (Gmail, Outlook, Yahoo, etc.)
4. Follow the connection wizard:
   - For Gmail: You'll need to create an App Password
   - For other services: Follow their specific instructions
5. **Save your Service ID** (e.g., `service_abc123`)

### Step 3: Create Email Template
1. Go to **Email Templates** in your dashboard
2. Click **Create New Template**
3. Fill in the following:
   - **Template Name**: "Quran Program Registration"
   - **Subject**: `طلب تسجيل جديد - برنامج مدارسة سورة الفاتحة`
   - **Content** (HTML):
   ```html
   <h2 style="color: #0a5d61; font-family: Arial, sans-serif;">طلب تسجيل جديد</h2>
   <div style="font-family: Arial, sans-serif; line-height: 1.8;">
       <p><strong>الاسم الكامل:</strong> {{from_name}}</p>
       <p><strong>البريد الإلكتروني:</strong> {{from_email}}</p>
       <p><strong>رقم الهاتف:</strong> {{phone}}</p>
       <p><strong>مستوى الخبرة:</strong> {{experience}}</p>
       <p><strong>تاريخ التقديم:</strong> {{submission_date}}</p>
       <hr style="border: 1px solid #e2e8f0; margin: 20px 0;">
       <p style="white-space: pre-line;">{{message}}</p>
   </div>
   ```
4. **Save your Template ID** (e.g., `template_xyz789`)

### Step 4: Get Your Public Key
1. Go to **Account** → **General** in your dashboard
2. Find **API Keys** section
3. Copy your **Public Key** (e.g., `abcdefghijklmnop`)

### Step 5: Update the HTML File
Open `quran_program_announcement.html` and replace these values:

1. **Line ~1309**: Replace `YOUR_PUBLIC_KEY`
   ```javascript
   emailjs.init("YOUR_PUBLIC_KEY"); // Replace with your actual key
   ```

2. **Line ~1345**: Replace `YOUR_SERVICE_ID` and `YOUR_TEMPLATE_ID`
   ```javascript
   emailjs.send('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', {
   ```

3. **Line ~1346**: Replace `your-email@example.com`
   ```javascript
   to_email: 'your-email@example.com', // Replace with your actual email
   ```

### Example Configuration:
```javascript
emailjs.init("abcdefghijklmnop"); // Your Public Key

emailjs.send('service_abc123', 'template_xyz789', {
    to_email: 'info@quranprogram.com', // Your email
    // ... rest of the code
});
```

---

## Option 2: FormSpree (Alternative - Simpler Setup)

If you prefer a simpler solution without template configuration:

### Step 1: Sign Up
1. Go to https://formspree.io/
2. Sign up for a free account (50 submissions/month on free tier)

### Step 2: Create Form
1. Click **New Form**
2. Set form endpoint (e.g., `https://formspree.io/f/YOUR_FORM_ID`)
3. Add your email address

### Step 3: Update HTML
Replace the EmailJS code with FormSpree:

```javascript
document.getElementById('registrationForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const form = this;
    const formData = new FormData(form);
    formData.append('_subject', 'طلب تسجيل جديد - برنامج مدارسة سورة الفاتحة');
    
    fetch('https://formspree.io/f/YOUR_FORM_ID', {
        method: 'POST',
        body: formData,
        headers: {
            'Accept': 'application/json'
        }
    })
    .then(response => {
        if (response.ok) {
            showMessage('success', 'شكراً لك! تم إرسال طلب التسجيل بنجاح.');
            form.reset();
        } else {
            throw new Error('Network response was not ok');
        }
    })
    .catch(error => {
        showMessage('error', 'حدث خطأ أثناء إرسال الطلب.');
    });
});
```

---

## Testing

After setup:
1. Fill out the form on your website
2. Submit it
3. Check your email inbox (and spam folder)
4. You should receive the registration details

## Troubleshooting

### Emails not arriving?
- Check your spam/junk folder
- Verify all IDs are correctly entered
- Check EmailJS dashboard for error logs
- Ensure email service is properly connected

### Form not submitting?
- Open browser console (F12) to check for errors
- Verify EmailJS script is loaded
- Check network tab for API calls

## Need Help?

- EmailJS Documentation: https://www.emailjs.com/docs/
- FormSpree Documentation: https://help.formspree.io/

---

**Note**: The free tiers are perfect for testing. For production with high volume, consider upgrading.

