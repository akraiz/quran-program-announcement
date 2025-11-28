#!/usr/bin/env python3
"""
سكريبت لمعالجة جميع الملفات الصوتية وتحويلها إلى نصوص وملخصات
"""

import os
import whisper
from pathlib import Path
import json
from datetime import datetime

def get_audio_files(audio_dir="audio_files"):
    """الحصول على قائمة بجميع الملفات الصوتية"""
    audio_extensions = ['.mp3', '.m4a', '.wav', '.opus', '.flac']
    audio_files = []
    
    for file in Path(audio_dir).iterdir():
        if file.suffix.lower() in audio_extensions and file.is_file():
            # تجنب الملفات المكررة (مثل .m4a و .mp3 لنفس الملف)
            base_name = file.stem
            if not any(f.stem == base_name and f != file for f in Path(audio_dir).iterdir() 
                      if f.suffix.lower() in audio_extensions):
                audio_files.append(file)
    
    return sorted(audio_files)

def transcribe_audio(audio_file, model="base", language="ar"):
    """تحويل الصوت إلى نص"""
    print(f"\n{'='*60}")
    print(f"جارٍ معالجة: {audio_file.name}")
    print(f"{'='*60}")
    
    try:
        # تحميل النموذج
        print("جارٍ تحميل نموذج Whisper...")
        model_obj = whisper.load_model(model)
        
        # تحويل الصوت إلى نص
        print("جارٍ معالجة الملف الصوتي...")
        result = model_obj.transcribe(
            str(audio_file),
            language=language,
            task="transcribe",
            verbose=True
        )
        
        return result
        
    except Exception as e:
        print(f"حدث خطأ في التحويل: {e}")
        return None

def save_transcript(audio_file, result, output_dir="transcripts"):
    """حفظ النص"""
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)
    
    transcript_file = output_dir / f"{audio_file.stem}_transcript.txt"
    
    with open(transcript_file, "w", encoding="utf-8") as f:
        f.write(result["text"])
    
    print(f"✓ تم حفظ النص في: {transcript_file}")
    
    # حفظ مع التوقيتات
    transcript_timestamps = output_dir / f"{audio_file.stem}_transcript_timestamps.txt"
    with open(transcript_timestamps, "w", encoding="utf-8") as f:
        for segment in result["segments"]:
            start = segment["start"]
            end = segment["end"]
            text = segment["text"]
            f.write(f"[{int(start//60)}:{int(start%60):02d} - {int(end//60)}:{int(end%60):02d}] {text}\n")
    
    return transcript_file

def create_summary(transcript_text, title):
    """إنشاء ملخص ذكي للنص"""
    # هذا سيكون ملخص بسيط - يمكن تحسينه لاحقاً
    words = transcript_text.split()
    word_count = len(words)
    
    # أول 500 كلمة كملخص أولي
    preview = ' '.join(words[:500])
    
    summary = {
        "title": title,
        "word_count": word_count,
        "preview": preview,
        "full_text": transcript_text
    }
    
    return summary

def process_all_files(audio_dir="audio_files", output_base="ملخصات_الصوتيات"):
    """معالجة جميع الملفات الصوتية"""
    audio_files = get_audio_files(audio_dir)
    
    if not audio_files:
        print("لم يتم العثور على ملفات صوتية!")
        return
    
    print(f"\nتم العثور على {len(audio_files)} ملف صوتي:")
    for i, f in enumerate(audio_files, 1):
        size_mb = f.stat().st_size / (1024 * 1024)
        print(f"  {i}. {f.name} ({size_mb:.1f} MB)")
    
    # إنشاء مجلدات الإخراج
    transcripts_dir = Path(output_base) / "transcripts"
    summaries_dir = Path(output_base) / "summaries"
    transcripts_dir.mkdir(parents=True, exist_ok=True)
    summaries_dir.mkdir(parents=True, exist_ok=True)
    
    results = []
    
    for audio_file in audio_files:
        try:
            # تحويل إلى نص
            result = transcribe_audio(audio_file, model="base", language="ar")
            
            if result:
                # حفظ النص
                transcript_file = save_transcript(audio_file, result, transcripts_dir)
                
                # إنشاء ملخص
                summary = create_summary(result["text"], audio_file.stem)
                
                # حفظ الملخص
                summary_file = summaries_dir / f"{audio_file.stem}_summary.json"
                with open(summary_file, "w", encoding="utf-8") as f:
                    json.dump(summary, f, ensure_ascii=False, indent=2)
                
                results.append({
                    "file": audio_file.name,
                    "transcript": str(transcript_file),
                    "summary": str(summary_file),
                    "word_count": summary["word_count"]
                })
                
                print(f"✓ تمت معالجة {audio_file.name} بنجاح!")
            else:
                print(f"✗ فشلت معالجة {audio_file.name}")
                
        except Exception as e:
            print(f"✗ خطأ في معالجة {audio_file.name}: {e}")
            continue
    
    # حفظ تقرير بجميع النتائج
    report_file = Path(output_base) / "processing_report.json"
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump({
            "processed_at": datetime.now().isoformat(),
            "total_files": len(audio_files),
            "successful": len(results),
            "results": results
        }, f, ensure_ascii=False, indent=2)
    
    print(f"\n{'='*60}")
    print(f"تمت معالجة {len(results)} من {len(audio_files)} ملف")
    print(f"التقارير محفوظة في: {output_base}")
    print(f"{'='*60}")

if __name__ == "__main__":
    process_all_files()

