"""Read-only browser QA for app-policy discovery; never sends mail or submits data."""
from pathlib import Path
import argparse
import json
from playwright.sync_api import sync_playwright

parser=argparse.ArgumentParser()
parser.add_argument('--base',default='http://127.0.0.1:4174/')
args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
output=root/'.qa/privacy'
output.mkdir(parents=True,exist_ok=True)
android='https://dpnzdy.github.io/ZinniaSharkNote/android-app-privacy.html'
windows='https://dpnzdy.github.io/ZinniaSharkNote/app-privacy.html'
reports=[]
with sync_playwright() as p:
    browser=p.chromium.launch(channel='msedge',headless=True)
    page=browser.new_page(device_scale_factor=1)
    errors=[]
    page.on('pageerror',lambda e:errors.append(str(e)))
    for width in [1440,768,390,320]:
        page.set_viewport_size({'width':width,'height':1000})
        for route in ['privacy/','ko/privacy/','support/','ko/support/','products/adequora-writer/','ko/products/adequora-writer/']:
            response=page.goto(args.base.rstrip('/')+'/'+route,wait_until='networkidle')
            assert response.status==200,(width,route)
            assert page.locator('h1').count()==1,route
            assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),(width,route,'overflow')
            assert page.locator(f'footer a[href="{android}"]').count()==1,route
            assert page.locator(f'footer a[href="{windows}"]').count()==1,route
            if route in ['privacy/','ko/privacy/']:
                panel=page.locator('.app-policy-links')
                assert panel.locator(f'a[href="{android}"]').count()==1
                assert panel.locator(f'a[href="{windows}"]').count()==1
                assert '2026' in panel.inner_text()
                if width in [1440,390]:
                    page.screenshot(path=str(output/f'{route.replace("/","-")}{width}.png'),full_page=True)
            reports.append({'route':route,'width':width,'status':'PASS'})
    assert not errors,errors
    browser.close()
(output/'report.json').write_text(json.dumps({'checks':reports,'consoleErrors':errors},indent=2),encoding='utf-8')
print(f'PASS: {len(reports)} responsive privacy-link checks; no mail sent.')
