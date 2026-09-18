import sys
sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright
errors=[]
with sync_playwright() as p:
    browser=p.chromium.launch(channel="msedge",headless=True)
    page=browser.new_page(viewport={"width":390,"height":844})
    page.on("pageerror",lambda e: errors.append(str(e)))
    page.goto("http://127.0.0.1:9142",wait_until="networkidle")
    page.evaluate("localStorage.clear()")
    page.reload(wait_until="networkidle")
    assert page.evaluate("BANK.length")==300
    page.click("#startBtn")
    page.wait_for_selector("#gameScreen:not(.hidden)")
    assert page.locator("#prompt").count()==0
    slots=page.locator(".slotNum")
    assert slots.count()==len(page.evaluate("current.chunkIds"))
    assert [slots.nth(i).inner_text() for i in range(slots.count())]==[str(i+1) for i in range(slots.count())]
    texts=page.locator(".chunk").all_inner_texts()
    assert all(t==t.lower() for t in texts)
    assert page.locator("#soundBtn").count()==1
    assert page.locator("#exitBtn").count()==1
    page.click("#exitBtn")
    page.wait_for_selector("#startScreen:not(.hidden)")
    page.click("#startBtn")
    for q in range(15):
        ids=page.evaluate("current.chunkIds")
        for cid in ids:
            page.click('.chunk[data-id="'+cid+'"]')
        if q<14:
            page.wait_for_function("(n)=>session && session.index===n",arg=q+1,timeout=3000)
    page.wait_for_selector("#endScreen:not(.hidden)",timeout=4000)
    assert page.inner_text("#endScore")=="15/15"
    assert page.locator("#reviewBtn").is_disabled()
    print("bank=300")
    print("lowercase=true")
    print("numberedSlots=true")
    print("exitToMenu=true")
    print("score="+page.inner_text("#endScore"))
    print("pageErrors="+str(errors))
    assert not errors
    browser.close()
