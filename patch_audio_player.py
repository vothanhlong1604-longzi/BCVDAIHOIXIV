import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

with open("src/ai-copilot.v2.js", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Modify the unlock code to initialize the global audio player
unlock_code_old = """
    // iOS/Mobile Audio Unlock workaround
    if (!window.__audioUnlocked) {
        window.__audioUnlocked = true;
        try {
            const unlockAudio = new Audio("data:audio/mp3;base64,//OExAAAAANIAAAAAExBTUUzLjEwMKqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq");
            unlockAudio.play().catch(()=>{});
            
            const unlockSpeech = new SpeechSynthesisUtterance('');
            unlockSpeech.volume = 0;
            window.speechSynthesis.speak(unlockSpeech);
        } catch (e) {}
    }
"""

unlock_code_new = """
    // iOS/Mobile Audio Unlock workaround
    if (!window.__audioUnlocked) {
        window.__audioUnlocked = true;
        try {
            // Khởi tạo một global audio player duy nhất để tái sử dụng (Bắt buộc cho Safari/iOS)
            window.__ttsAudioPlayer = new Audio("data:audio/mp3;base64,//OExAAAAANIAAAAAExBTUUzLjEwMKqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq");
            window.__ttsAudioPlayer.play().catch(()=>{});
            
            const unlockSpeech = new SpeechSynthesisUtterance('');
            unlockSpeech.volume = 0;
            window.speechSynthesis.speak(unlockSpeech);
        } catch (e) {}
    }
"""
content = content.replace(unlock_code_old, unlock_code_new)

# 2. Modify the fallback block to reuse window.__ttsAudioPlayer instead of creating a new Audio()
fallback_block_old = """         console.warn("Không tìm được giọng Web Speech vi-VN. Kích hoạt Google Translate TTS API dự phòng.");
         
         // Nếu có preload từ trước thì tái sử dụng để phát ngay lập tức
         let audio;
         if (window.__nextAudioPreload && window.__nextAudioPreload.dataset.chunkIndex == currentChunk) {
             audio = window.__nextAudioPreload;
         } else {
             const url = `https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=vi&q=${encodeURIComponent(chunkText)}`;
             audio = new Audio(url);
         }
         
         currentAudio = audio;
         audio.onended = () => {
             currentChunk++;
             playNextChunk();
         };
         audio.onerror = () => {
             console.error("Lỗi mạng khi tải Google TTS API");
             currentChunk++;
             playNextChunk();
         };
         audio.play().catch(e => {
             console.error("Audio blocked by browser:", e);
             currentChunk++;
             playNextChunk();
         });
         
         // Preload audio cho chunk tiếp theo để loại bỏ hoàn toàn độ trễ mạng
         if (currentChunk + 1 < chunks.length) {
             const nextText = chunks[currentChunk + 1].trim();
             if (nextText) {
                 const nextUrl = `https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=vi&q=${encodeURIComponent(nextText)}`;
                 const nextAudio = new Audio(nextUrl);
                 nextAudio.preload = 'auto';
                 nextAudio.dataset.chunkIndex = currentChunk + 1;
                 window.__nextAudioPreload = nextAudio;
             }
         }
      }"""

fallback_block_new = """         console.warn("Không tìm được giọng Web Speech vi-VN. Kích hoạt Google Translate TTS API dự phòng.");
         
         const url = `https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=vi&q=${encodeURIComponent(chunkText)}`;
         
         // Bắt buộc phải tái sử dụng global audio player đã được unlock bằng User Gesture trên Safari/iOS
         let audio = window.__ttsAudioPlayer || new Audio();
         audio.src = url;
         
         currentAudio = audio;
         audio.onended = () => {
             currentChunk++;
             playNextChunk();
         };
         audio.onerror = () => {
             console.error("Lỗi mạng khi tải Google TTS API");
             currentChunk++;
             playNextChunk();
         };
         audio.play().catch(e => {
             console.error("Audio blocked by browser:", e);
             currentChunk++;
             playNextChunk();
         });
      }"""

if fallback_block_old in content:
    content = content.replace(fallback_block_old, fallback_block_new)
    with open("src/ai-copilot.v2.js", "w", encoding="utf-8") as f:
        f.write(content)
    print("Patched audio player!")
else:
    print("Fallback block not found! Cannot patch.")
