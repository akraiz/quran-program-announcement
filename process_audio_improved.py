#!/usr/bin/env python3
"""
سكريبت محسّن لمعالجة الملفات الصوتية واحداً تلو الآخر
"""

import os
import whisper
from pathlib import Path
import json
from datetime import datetime

def get_audio_files(audio_dir="audio_files"):
    """الحصول على قائمة بجميع الملفات الصوتية (بدون تكرار)"""
    audio_extensions = ['.mp3', '.m4a', '.wav', '.opus', '.flac']
    audio_files = []
    processed_names = set()
    
    for file in sorted(Path(audio_dir).iterdir()):
        if file.suffix.lower() in audio_extensions and file.is_file():
            base_name = file.stem
            # تجنب الملفات المكررة (نأخذ .mp3 إذا كان موجوداً)
            if base_name not in processed_names:
                # إذا كان هناك .mp3 و .m4a لنفس الاسم، نأخذ .mp3 فقط
                if file.suffix.lower() == '.m4a':
                    mp3_version = file.parent / f"{base_name}.mp3"
                    if mp3_version.exists():
                        continue
                
                audio_files.append(file)
                processed_names.add(base_name)
    
    return audio_files

def is_already_processed(audio_file, transcripts_dir):
    """التحقق إذا كان الملف معالجاً بالفعل"""
    transcript_file = Path(transcripts_dir) / f"{audio_file.stem}_transcript.txt"
    return transcript_file.exists()

def transcribe_single_file(audio_file, model="base", language="ar", transcripts_dir="ملخصات_الصوتيات/transcripts"):
    """تحويل ملف صوتي واحد إلى نص"""
    print(f"\n{'='*70}")
    print(f"📁 الملف: {audio_file.name}")
    size_mb = audio_file.stat().st_size / (1024 * 1024)
    print(f"📊 الحجم: {size_mb:.1f} MB")
    print(f"{'='*70}")
    
    # التحقق إذا كان معالجاً
    if is_already_processed(audio_file, transcripts_dir):
        print(f"✓ هذا الملف معالج بالفعل - تخطي")
        return True
    
    try:
        # تحميل النموذج (مرة واحدة فقط)
        if not hasattr(transcribe_single_file, 'model'):
            print("🔄 جارٍ تحميل نموذج Whisper (base)...")
            transcribe_single_file.model = whisper.load_model(model)
            print("✓ تم تحميل النموذج")
        
        # تحويل الصوت إلى نص
        print("🔄 جارٍ تحويل الصوت إلى نص...")
        print("   (هذا قد يستغرق وقتاً حسب حجم الملف)")
        
        result = transcribe_single_file.model.transcribe(
            str(audio_file),
            language=language,
            task="transcribe",
            verbose=False  # تقليل الإخراج
        )
        
        # حفظ النص
        Path(transcripts_dir).mkdir(parents=True, exist_ok=True)
        transcript_file = Path(transcripts_dir) / f"{audio_file.stem}_transcript.txt"
        
        with open(transcript_file, "w", encoding="utf-8") as f:
            f.write(result["text"])
        
        word_count = len(result["text"].split())
        print(f"✓ تم الحفظ: {transcript_file.name}")
        print(f"  عدد الكلمات: {word_count:,}")
        
        # حفظ مع التوقيتات
        transcript_timestamps = Path(transcripts_dir) / f"{audio_file.stem}_transcript_timestamps.txt"
        with open(transcript_timestamps, "w", encoding="utf-8") as f:
            for segment in result["segments"]:
                start = segment["start"]
                end = segment["end"]
                text = segment["text"]
                f.write(f"[{int(start//60)}:{int(start%60):02d} - {int(end//60)}:{int(end%60):02d}] {text}\n")
        
        return True
        
    except Exception as e:
        print(f"✗ خطأ في معالجة {audio_file.name}: {e}")
        return False

def main():
    """الدالة الرئيسية"""
    audio_dir = "audio_files"
    transcripts_dir = "ملخصات_الصوتيات/transcripts"
    
    print("="*70)
    print("🎙️  معالجة الملفات الصوتية وتحويلها إلى نصوص")
    print("="*70)
    
    # الحصول على الملفات
    audio_files = get_audio_files(audio_dir)
    
    if not audio_files:
        print("❌ لم يتم العثور على ملفات صوتية!")
        return
    
    # استبعاد audio.mp3 لأنه معالج بالفعل
    audio_files = [f for f in audio_files if f.stem != "audio"]
    
    print(f"\n📋 تم العثور على {len(audio_files)} ملف صوتي:")
    for i, f in enumerate(audio_files, 1):
        size_mb = f.stat().st_size / (1024 * 1024)
        status = "✓" if is_already_processed(f, transcripts_dir) else "⏳"
        print(f"  {status} {i}. {f.name} ({size_mb:.1f} MB)")
    
    # معالجة كل ملف
    successful = 0
    failed = 0
    
    for i, audio_file in enumerate(audio_files, 1):
        print(f"\n[{i}/{len(audio_files)}] معالجة الملف {i} من {len(audio_files)}")
        
        if transcribe_single_file(audio_file, transcripts_dir=transcripts_dir):
            successful += 1
        else:
            failed += 1
    
    # تقرير نهائي
    print(f"\n{'='*70}")
    print("📊 التقرير النهائي:")
    print(f"  ✓ نجحت: {successful}")
    print(f"  ✗ فشلت: {failed}")
    print(f"  📁 الملفات محفوظة في: {transcripts_dir}")
    print(f"{'='*70}")
    
    print("\n💡 الخطوة التالية: تشغيل create_smart_summaries.py لإنشاء الملخصات")

if __name__ == "__main__":
    main()

