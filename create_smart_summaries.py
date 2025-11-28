#!/usr/bin/env python3
"""
سكريبت لإنشاء ملخصات ذكية من النصوص المحولة
"""

import os
from pathlib import Path
import re

def extract_key_points(text, min_length=50):
    """استخراج النقاط الرئيسية من النص"""
    # تقسيم النص إلى جمل
    sentences = re.split(r'[.!?]\s+', text)
    
    # تصفية الجمل القصيرة جداً
    meaningful_sentences = [s.strip() for s in sentences if len(s.strip()) >= min_length]
    
    return meaningful_sentences

def create_smart_summary(transcript_file, title):
    """إنشاء ملخص ذكي من ملف النص"""
    with open(transcript_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # تنظيف النص
    text = text.strip()
    
    # إحصائيات
    word_count = len(text.split())
    char_count = len(text)
    
    # استخراج النقاط الرئيسية
    key_points = extract_key_points(text)
    
    # أول 300 كلمة كملخص أولي
    words = text.split()
    preview = ' '.join(words[:300])
    
    # آخر 200 كلمة (الخلاصة)
    conclusion = ' '.join(words[-200:]) if len(words) > 200 else text
    
    # البحث عن عناوين محتملة في النص
    # (جمل تبدأ بأرقام أو كلمات مثل "أولاً"، "ثانياً"، إلخ)
    headings = []
    heading_patterns = [
        r'أول[اًا]?\s*[:.]?\s*(.+?)[.!?]',
        r'ثان[ياًا]?\s*[:.]?\s*(.+?)[.!?]',
        r'ثالث[اًا]?\s*[:.]?\s*(.+?)[.!?]',
        r'رابع[اًا]?\s*[:.]?\s*(.+?)[.!?]',
        r'خامس[اًا]?\s*[:.]?\s*(.+?)[.!?]',
        r'(\d+)[\.)]\s*(.+?)[.!?]',
    ]
    
    for pattern in heading_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        headings.extend([m if isinstance(m, str) else m[1] for m in matches[:5]])
    
    summary = {
        "title": title,
        "statistics": {
            "word_count": word_count,
            "character_count": char_count,
            "estimated_duration_minutes": word_count / 150  # متوسط 150 كلمة في الدقيقة
        },
        "preview": preview,
        "conclusion": conclusion,
        "key_points": key_points[:20],  # أول 20 نقطة رئيسية
        "headings": headings[:10] if headings else None
    }
    
    return summary

def format_summary_markdown(summary):
    """تنسيق الملخص بصيغة Markdown"""
    md = f"""# {summary['title']}

## إحصائيات
- **عدد الكلمات:** {summary['statistics']['word_count']:,}
- **عدد الأحرف:** {summary['statistics']['character_count']:,}
- **المدة المقدرة:** {summary['statistics']['estimated_duration_minutes']:.1f} دقيقة

---

## نظرة عامة

{summary['preview']}...

---

## النقاط الرئيسية

"""
    
    for i, point in enumerate(summary['key_points'][:15], 1):
        md += f"{i}. {point}\n\n"
    
    if summary['headings']:
        md += "\n## العناوين الرئيسية\n\n"
        for heading in summary['headings']:
            md += f"- {heading}\n"
        md += "\n"
    
    md += f"""
---

## الخلاصة

{summary['conclusion']}

---

*ملخص تلقائي من النص المحول*
"""
    
    return md

def process_transcripts(transcripts_dir="ملخصات_الصوتيات/transcripts", 
                       summaries_dir="ملخصات_الصوتيات/summaries"):
    """معالجة جميع ملفات النصوص وإنشاء ملخصات"""
    transcripts_path = Path(transcripts_dir)
    summaries_path = Path(summaries_dir)
    
    if not transcripts_path.exists():
        print(f"المجلد {transcripts_dir} غير موجود!")
        return
    
    transcript_files = list(transcripts_path.glob("*_transcript.txt"))
    
    if not transcript_files:
        print("لم يتم العثور على ملفات نصوص!")
        return
    
    summaries_path.mkdir(parents=True, exist_ok=True)
    
    print(f"تم العثور على {len(transcript_files)} ملف نصي")
    
    for transcript_file in transcript_files:
        try:
            title = transcript_file.stem.replace("_transcript", "")
            print(f"\nجارٍ إنشاء ملخص لـ: {title}")
            
            # إنشاء الملخص
            summary = create_smart_summary(transcript_file, title)
            
            # حفظ بصيغة Markdown
            md_file = summaries_path / f"{title}_summary.md"
            md_content = format_summary_markdown(summary)
            
            with open(md_file, "w", encoding="utf-8") as f:
                f.write(md_content)
            
            print(f"✓ تم حفظ الملخص في: {md_file}")
            
        except Exception as e:
            print(f"✗ خطأ في معالجة {transcript_file.name}: {e}")
            continue
    
    print(f"\n✓ تمت معالجة {len(transcript_files)} ملف")

if __name__ == "__main__":
    process_transcripts()

