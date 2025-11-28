#!/bin/bash
# سكريبت للتحقق من حالة التحويل

cd /Users/ahmedkraiz/Desktop/Text

if [ -f audio_files/audio_transcript.txt ]; then
    echo "✓ تم الانتهاء من التحويل!"
    echo ""
    echo "عدد الكلمات:"
    wc -w audio_files/audio_transcript.txt
    echo ""
    echo "أول 1000 حرف:"
    head -c 1000 audio_files/audio_transcript.txt
    echo ""
else
    echo "لا يزال قيد المعالجة..."
    echo "آخر 10 أسطر من السجل:"
    tail -10 transcribe.log 2>/dev/null || echo "لا يوجد سجل بعد"
    
    if pgrep -f "transcribe_simple.py" > /dev/null; then
        echo ""
        echo "✓ العملية لا تزال تعمل"
    else
        echo ""
        echo "⚠ العملية توقفت - تحقق من transcribe.log للأخطاء"
    fi
fi

