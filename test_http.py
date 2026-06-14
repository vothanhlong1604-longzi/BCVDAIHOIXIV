import http.server
import socketserver
import threading
import time
from playwright.sync_api import sync_playwright

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

def run_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

threading.Thread(target=run_server, daemon=True).start()
time.sleep(1)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.on("console", lambda msg: print(f"Browser Console: {msg.text}"))
    page.goto("http://localhost:8000/index.html")
    page.wait_for_timeout(2000)
    print("Clicking fab...")
    page.evaluate("""
        () => {
            const fab = document.getElementById('apple-ai-fab');
            if(fab) fab.click();
        }
    """)
    page.wait_for_timeout(2000)
    print("Checking audio...")
    page.evaluate("""
        () => {
            const url = `https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=vi&q=test`;
            const audio = new Audio(url);
            audio.onended = () => console.log('Audio Ended (Success)');
            audio.onerror = () => console.log('Audio Error (Failed)');
            audio.play().catch(e => console.log('Audio Play Blocked: ' + e));
        }
    """)
    page.wait_for_timeout(3000)
    browser.close()
