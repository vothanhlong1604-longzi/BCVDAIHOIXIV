import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Add meta referrer tag if not exists
if '<meta name="referrer" content="no-referrer">' not in content:
    content = content.replace('<head>', '<head>\n  <meta name="referrer" content="no-referrer">')
    
with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Added no-referrer meta tag to index.html")
