#!/usr/bin/env python3
"""
سكريبت لتحميل المقطع الصوتي من SoundCloud وتحويله إلى نص باستخدام Whisper
"""

import subprocess
import sys
import os
from pathlib import Path

def install_requirements():
    """تثبيت المتطلبات اللازمة"""
    print("جارٍ تثبيت المتطلبات...")
    packages = [
        "openai-whisper",
        "yt-dlp",
        "ffmpeg-python"
    ]
    
    for package in packages:
        try:
            __import__(package.replace("-", "_"))
            print(f"✓ {package} مثبت بالفعل")
        except ImportError:
            print(f"جارٍ تثبيت {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def download_audio(url, output_dir="audio_files"):
    """تحميل المقطع الصوتي من SoundCloud"""
    print(f"\nجارٍ تحميل المقطع من: {url}")
    
    # إنشاء مجلد للصوتيات
    Path(output_dir).mkdir(exist_ok=True)
    
    output_path = os.path.join(output_dir, "audio.%(ext)s")
    
    try:
        # استخدام yt-dlp لتحميل المقطع
        cmd = [
            "yt-dlp",
            "-x",  # استخراج الصوت فقط
            "--audio-format", "mp3",
            "--audio-quality", "0",  # أفضل جودة
            "-o", output_path,
            url
        ]
        
        subprocess.run(cmd, check=True)
        
        # العثور على الملف المحمل
        audio_files = list(Path(output_dir).glob("audio.*"))
        if audio_files:
            audio_file = str(audio_files[0])
            print(f"✓ تم التحميل بنجاح: {audio_file}")
            return audio_file
        else:
            raise FileNotFoundError("لم يتم العثور على الملف المحمل")
            
    except subprocess.CalledProcessError as e:
        print(f"خطأ في التحميل: {e}")
        print("\nتأكد من تثبيت yt-dlp:")
        print("pip install yt-dlp")
        return None
    except Exception as e:
        print(f"حدث خطأ: {e}")
        return None

def transcribe_audio(audio_file, model="base", language="ar"):
    """تحويل الصوت إلى نص باستخدام Whisper"""
    print(f"\nجارٍ تحويل الصوت إلى نص باستخدام نموذج {model}...")
    
    try:
        import whisper
        
        # تحميل النموذج
        print("جارٍ تحميل نموذج Whisper...")
        model_obj = whisper.load_model(model)
        
        # تحويل الصوت إلى نص
        print("جارٍ معالجة الملف الصوتي...")
        result = model_obj.transcribe(
            audio_file,
            language=language,
            task="transcribe"
        )
        
        # حفظ النص
        transcript_file = audio_file.replace(os.path.splitext(audio_file)[1], "_transcript.txt")
        with open(transcript_file, "w", encoding="utf-8") as f:
            f.write(result["text"])
        
        print(f"✓ تم حفظ النص في: {transcript_file}")
        
        # حفظ النص مع التوقيتات
        transcript_with_timestamps = audio_file.replace(os.path.splitext(audio_file)[1], "_transcript_timestamps.txt")
        with open(transcript_with_timestamps, "w", encoding="utf-8") as f:
            for segment in result["segments"]:
                start = segment["start"]
                end = segment["end"]
                text = segment["text"]
                f.write(f"[{int(start//60)}:{int(start%60):02d} - {int(end//60)}:{int(end%60):02d}] {text}\n")
        
        print(f"✓ تم حفظ النص مع التوقيتات في: {transcript_with_timestamps}")
        
        return result["text"], transcript_file
        
    except ImportError:
        print("خطأ: لم يتم العثور على مكتبة whisper")
        print("قم بتثبيتها باستخدام: pip install openai-whisper")
        return None, None
    except Exception as e:
        print(f"حدث خطأ في التحويل: {e}")
        return None, None

def main():
    """الدالة الرئيسية"""
    url = "https://on.soundcloud.com/dR1HYTSpUFEP74u1xN"
    
    print("=" * 60)
    print("تحويل المقطع الصوتي من SoundCloud إلى نص")
    print("=" * 60)
    
    # تثبيت المتطلبات
    install_requirements()
    
    # تحميل المقطع
    audio_file = download_audio(url)
    if not audio_file:
        print("\nفشل تحميل المقطع. يرجى التحقق من الرابط والاتصال بالإنترنت.")
        return
    
    # تحويل الصوت إلى نص
    transcript, transcript_file = transcribe_audio(audio_file, model="base", language="ar")
    
    if transcript:
        print("\n" + "=" * 60)
        print("تم التحويل بنجاح!")
        print("=" * 60)
        print(f"\nالنص الأولي (أول 500 حرف):")
        print("-" * 60)
        print(transcript[:500] + "...")
        print("-" * 60)
        print(f"\nيمكنك العثور على النص الكامل في: {transcript_file}")
    else:
        print("\nفشل تحويل الصوت إلى نص.")

if __name__ == "__main__":
    main()

