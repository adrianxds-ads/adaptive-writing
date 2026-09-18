import sys
sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright
errors = []
with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=True)
    page = browser.new_page(viewport={"width": 390, "height": 844})
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.goto("http://127.0.0.1:9137", wait_until="networkidle")
    page.evaluate("localStorage.clear()")
    page.reload(wait_until="networkidle")
    assert page.evaluate("BANK.length") == 300
    assert page.evaluate("CONTENT.chunks.length") > 150
    page.click("#startBtn")
    for q in range(15):
        page.wait_for_selector("#gameScreen:not(.hidden)")
        ids = page.evaluate("current.chunkIds")
        for cid in ids:
            page.click('.chunk[data-id="' + cid + '"]')
        if q < 14:
            page.wait_for_function("(n)=>session && session.index===n", arg=q + 1, timeout=3000)
    page.wait_for_selector("#endScreen:not(.hidden)", timeout=4000)
    score = page.inner_text("#endScore")
    total = page.evaluate("state.totalAnswers")
    correct = page.evaluate("state.totalCorrect")
    print("bank=" + str(page.evaluate("BANK.length")))
    print("chunks=" + str(page.evaluate("CONTENT.chunks.length")))
    print("score=" + score)
    print("totalAnswers=" + str(total))
    print("totalCorrect=" + str(correct))
    print("pageErrors=" + str(errors))
    assert score == "15/15"
    assert total == 15 and correct == 15
    assert not errors
    browser.close()
