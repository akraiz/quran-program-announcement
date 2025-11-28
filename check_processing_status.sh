#!/bin/bash
# سكريبت للتحقق من حالة المعالجة

cd /Users/ahmedkraiz/Desktop/Text

echo "=== حالة المعالجة ==="
echo ""

# التحقق من العملية
if pgrep -f "process_all_audio.py" > /dev/null; then
    echo "✓ العملية تعمل حالياً"
    ps aux | grep -i "process_all_audio\|whisper" | grep -v grep | head -2
else
    echo "⚠ لا توجد عملية نشطة"
fi

echo ""
echo "=== الملفات المعالجة ==="
if [ -d "ملخصات_الصوتيات/transcripts" ]; then
    count=$(ls -1 "ملخصات_الصوتيات/transcripts"/*.txt 2>/dev/null | wc -l)
    echo "عدد الملفات المعالجة: $count"
    ls -lh "ملخصات_الصوتيات/transcripts"/*.txt 2>/dev/null | tail -5
else
    echo "المجلد غير موجود بعد"
fi

echo ""
echo "=== الملفات المتبقية ==="
total=$(ls -1 audio_files/*.{mp3,m4a} 2>/dev/null | wc -l)
processed=$(ls -1 "ملخصات_الصوتيات/transcripts"/*.txt 2>/dev/null | wc -l)
remaining=$((total - processed))
echo "المتبقي: $remaining من $total"

