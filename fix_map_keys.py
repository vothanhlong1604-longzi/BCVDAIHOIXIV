with open("src/ai-copilot.v2.js", "r", encoding="utf-8") as f:
    text = f.read()

import re

# We will just replace the entire STUDIO_VOICE_MAP and STUDIO_VIDEO_MAP objects
new_maps = """const STUDIO_VIDEO_MAP = {
    "lời chào": "./data/video/studio_greeting.mp4",
    "bản đồ tri thức": "./data/video/studio_mindmap.mp4",
    "đại học csnd": "./data/video/studio_csnd.mp4",
    "nghị quyết 71": "./data/video/studio_nq71.mp4",
    "đoạn trích nghị quyết": "./data/video/studio_qa1.mp4",
    "5 nội dung cơ bản": "./data/video/studio_qa2.mp4"
};
const STUDIO_VOICE_MAP = {
    "lời chào": "./data/audio/studio_greeting.mp3",
    "bản đồ tri thức": "./data/audio/studio_mindmap.mp3",
    "đại học csnd": "./data/audio/studio_csnd.mp3",
    "nghị quyết 71": "./data/audio/studio_nq71.mp3",
    "đoạn trích nghị quyết": "./data/audio/studio_qa1.mp3",
    "5 nội dung cơ bản": "./data/audio/studio_qa2.mp3"
};"""

text = re.sub(r'const STUDIO_VIDEO_MAP = \{.*?\n\};\s*const STUDIO_VOICE_MAP = \{.*?\n\};', new_maps, text, flags=re.DOTALL)

# Let's also check if my previous really_fix_intent_keys.py script accidentally mangled the playVideoAvatar calls
text = re.sub(r"playVideoAvatar\('[^']*?chA.o'", "playVideoAvatar('lời chào'", text)
text = re.sub(r"playVideoAvatar\('[^']*?ngh.< quy.t'", "playVideoAvatar('đoạn trích nghị quyết'", text)
text = re.sub(r"playVideoAvatar\('5[^']*?b.n'", "playVideoAvatar('5 nội dung cơ bản'", text)
text = re.sub(r"playVideoAvatar\('[^']*?tri th.cc'", "playVideoAvatar('bản đồ tri thức'", text)


with open("src/ai-copilot.v2.js", "w", encoding="utf-8") as f:
    f.write(text)

print("Maps fixed!")
