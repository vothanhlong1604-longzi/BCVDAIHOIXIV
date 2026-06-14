import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

with open("src/ai-copilot.v2.js", "r", encoding="utf-8") as f:
    content = f.read()

start_str = "function startInteraction() {\n    if (currentState !== 'IDLE') return;"

unlock_code = """
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

replacement = start_str + "\n" + unlock_code

content = content.replace(start_str, replacement)

with open("src/ai-copilot.v2.js", "w", encoding="utf-8") as f:
    f.write(content)

print("Injected audio unlock logic!")
