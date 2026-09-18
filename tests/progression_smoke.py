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
    first=page.evaluate("BANK[0].id")
    page.evaluate("(id)=>{const s=getStat(state.sentenceStats,id);s.seen=1;s.correct=1;s.totalMs=5000;s.successSessions=1;s.spacedWins=0;s.mastery=calcMastery(s)}",first)
    early=page.evaluate("(id)=>getStat(state.sentenceStats,id).mastery",first)
    page.evaluate("(id)=>{const s=getStat(state.sentenceStats,id);s.seen=8;s.correct=8;s.totalMs=32000;s.successSessions=5;s.spacedWins=3;s.mastery=calcMastery(s)}",first)
    mature=page.evaluate("(id)=>getStat(state.sentenceStats,id).mastery",first)
    assert early < 85
    assert mature >= 85
    assert page.evaluate("(id)=>distractorIds(BANK.find(x=>x.id===id)).length",first)==0
    print("earlyMastery="+str(early))
    print("matureMastery="+str(mature))
    print("distractors=0")
    print("pageErrors="+str(errors))
    assert not errors
    browser.close()
