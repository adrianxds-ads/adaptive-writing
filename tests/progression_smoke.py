import sys
sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright
errors=[]
with sync_playwright() as p:
    browser=p.chromium.launch(channel="msedge",headless=True)
    page=browser.new_page(viewport={"width":390,"height":844})
    page.on("pageerror",lambda e: errors.append(str(e)))
    page.goto("http://127.0.0.1:9140",wait_until="networkidle")
    page.evaluate("localStorage.clear()")
    page.reload(wait_until="networkidle")
    assert page.evaluate("BANK.length")==300
    first=page.evaluate("BANK[0].id")
    page.evaluate("(id)=>{const s=getStat(state.sentenceStats,id);s.seen=2;s.correct=2;s.mastery=45}",first)
    distractors=page.evaluate("(id)=>distractorIds(BANK.find(x=>x.id===id)).length",first)
    assert distractors==1
    page.evaluate("(id)=>{const s=getStat(state.sentenceStats,id);s.mastery=70}",first)
    distractors2=page.evaluate("(id)=>distractorIds(BANK.find(x=>x.id===id)).length",first)
    assert distractors2==2
    page.evaluate("state=freshState();save()")
    page.click("#startBtn")
    for q in range(15):
        ids=page.evaluate("current.chunkIds")
        for cid in ids:
            page.click('.chunk[data-id="'+cid+'"]')
        if q<14:
            page.wait_for_function("(n)=>session && session.index===n",arg=q+1,timeout=3000)
    page.wait_for_selector("#endScreen:not(.hidden)",timeout=4000)
    assert page.inner_text("#endScore")=="15/15"
    print("bank=300")
    print("distractors=1->2 by mastery")
    print("score="+page.inner_text("#endScore"))
    print("pageErrors="+str(errors))
    assert not errors
    browser.close()
