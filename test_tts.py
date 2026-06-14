from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.on("console", lambda msg: print(f"Console: {msg.text}"))
    page.goto("data:text/html,<!DOCTYPE html><html><head><meta name=\"referrer\" content=\"no-referrer\"></head><body><h1>Testing TTS</h1><button id='btn'>Play</button><script>document.getElementById('btn').onclick = () => { const a = new Audio('https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=vi&q=test'); a.onended = () => console.log('SUCCESS'); a.onerror = () => console.log('ERROR'); a.play().catch(e => console.log('BLOCKED ' + e)); }</script></body></html>")
    page.wait_for_timeout(1000)
    page.click("#btn")
    page.wait_for_timeout(3000)
    browser.close()
