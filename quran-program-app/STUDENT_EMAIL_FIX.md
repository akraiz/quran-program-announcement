# Fix: Student Email Not Receiving Confirmation

## Problem
Both emails are being sent to the admin email (ctrleng.ahmed@gmail.com) instead of one to admin and one to student.

## Root Cause
The EmailJS template (`template_nl26k4v`) has a hardcoded "To Email" address in the EmailJS dashboard, which overrides the `to_email` parameter in the code.

## Solution: Two Options

### Option 1: Modify Existing Template (Recommended)

1. Go to your EmailJS dashboard: https://dashboard.emailjs.com/
2. Navigate to **Email Templates**
3. Find and edit template: `template_nl26k4v`
4. In the **Settings** tab, find the **To Email** field
5. Change it from: `ctrleng.ahmed@gmail.com` (hardcoded)
6. To: `{{to_email}}` (dynamic variable)
7. Save the template

**Note:** After this change, you'll need to update the code to use the template differently for admin vs student emails.

---

### Option 2: Create a Separate Student Template (Better Solution)

This is the recommended approach for better organization.

#### Step 1: Create New Template in EmailJS

1. Go to EmailJS dashboard → **Email Templates**
2. Click **Create New Template**
3. Template Name: `Student Confirmation Template`
4. Template ID: Copy this (e.g., `template_student_confirmation`)

#### Step 2: Configure Template

**To Email Field:** `{{to_email}}` (THIS IS CRITICAL - must be dynamic!)

**Subject:** `تأكيد تسجيلك - برنامج مدارسة سورة الفاتحة`

**Content (HTML):**
```html
<div dir="rtl" style="font-family: Arial, sans-serif; line-height: 1.8; direction: rtl;">
    <h2 style="color: #0a5d61;">شكراً لتسجيلك في برنامج مدارسة سورة الفاتحة</h2>
    
    <p>عزيزي/عزيزتي {{from_name}}،</p>
    
    <p>تم استلام طلب التسجيل الخاص بك بنجاح. سيتم التواصل معك قريباً لتأكيد التسجيل وتزويدك بكافة التفاصيل.</p>
    
    <div style="background: #f8fafc; padding: 15px; border-radius: 8px; margin: 20px 0;">
        <h3 style="color: #0a5d61; margin-top: 0;">معلومات التسجيل:</h3>
        <p><strong>الاسم الكامل:</strong> {{from_name}}</p>
        <p><strong>البريد الإلكتروني:</strong> {{from_email}}</p>
        <p><strong>رقم الهاتف:</strong> {{phone}}</p>
        <p><strong>مستوى الخبرة:</strong> {{experience}}</p>
        <p><strong>تاريخ التقديم:</strong> {{submission_date}}</p>
    </div>
    
    <p>نتمنى أن تكون هذه الرحلة مفيدة ومثمرة في فهم سورة الفاتحة وتصحيح التلاوة.</p>
    
    <p>مع تحيات،<br>فريق برنامج مدارسة سورة الفاتحة</p>
</div>
```

#### Step 3: Update the HTML Code

Once you have the new template ID, update the code in `quran_program_announcement.html`:

1. Find the student email section (around line 1447)
2. Replace `template_nl26k4v` with your new student template ID
3. Make sure `to_email: formData.email` is set correctly

---

## Quick Fix (Current Code)

For now, I've updated the code to send only ONE email to the admin (to avoid duplicates). The student email is commented out until you configure the template.

To re-enable student emails:

1. Follow Option 1 or 2 above
2. Then uncomment/re-add the student email code in the HTML file

---

## Testing

After making changes:

1. Test the form submission
2. Check your admin email (should receive 1 email)
3. Check the student's email (should receive 1 confirmation email)
4. Verify the content is correct in both

---

## Current Status

✅ **Fixed:** No more duplicate emails to admin
⏳ **Pending:** Student confirmation email (requires template configuration)

---

## Need Help?

If you need assistance setting up the template:
1. EmailJS Documentation: https://www.emailjs.com/docs/
2. Template Variables: https://www.emailjs.com/docs/user-guide/dynamic-template-data/

