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
    page.click("#startBtn")
    ids=page.evaluate("current.chunkIds")
    wrong=list(reversed(ids))
    if wrong==ids and len(ids)>1:
        wrong[0],wrong[1]=wrong[1],wrong[0]
    for cid in wrong:
        page.click('.chunk[data-id="'+cid+'"]')
    page.wait_for_timeout(250)
    shown=page.locator("#buildArea .built").all_inner_texts()
    expected=page.evaluate("current.chunkIds.map(id=>displayChunk(id))")
    assert shown==expected
    page.wait_for_function("()=>session.index===1",timeout=3000)
    for q in range(1,15):
        ids=page.evaluate("current.chunkIds")
        for cid in ids:
            page.click('.chunk[data-id="'+cid+'"]')
        if q<14:
            page.wait_for_function("(n)=>session && session.index===n",arg=q+1,timeout=3000)
    page.wait_for_selector("#endScreen:not(.hidden)",timeout=4000)
    assert not page.locator("#reviewBtn").is_disabled()
    page.click("#reviewBtn")
    page.wait_for_selector("#reviewScreen:not(.hidden)")
    assert page.locator(".reviewItem").count()==1
    print("correctionSnapsToCanonical=true")
    print("reviewErrors=true")
    print("pageErrors="+str(errors))
    assert not errors
    browser.close()
