#!/usr/bin/env python3
"""سكريبت بسيط لتحويل الصوت إلى نص"""
import whisper
import sys

print("جارٍ تحميل نموذج Whisper (base)...")
print("هذا قد يستغرق دقيقة أو دقيقتين...")
model = whisper.load_model("base")

print("\n✓ تم تحميل النموذج")
print("جارٍ تحويل الصوت إلى نص...")
print("(هذا قد يستغرق 10-15 دقيقة للمقطع الذي مدته 53 دقيقة)")

audio_file = "audio_files/audio.mp3"
result = model.transcribe(audio_file, language="ar", verbose=True)

# حفظ النص
output_file = "audio_files/audio_transcript.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(result["text"])

print(f"\n✓ تم الحفظ في: {output_file}")
print(f"\nأول 500 حرف من النص:")
print("-" * 60)
print(result["text"][:500])

