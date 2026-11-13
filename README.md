# ZINNIASHARK 회사 웹사이트

기존 Astro 정적 사이트이며 공개 주소는 https://zinniashark.com/ 입니다. `npm run build`는 ignored `dist/`를 생성합니다. 원격 소스 반영과 실제 호스팅 배포 완료는 별도로 확인합니다.

## 앱 개인정보처리방침 연결

- 공식 원문은 제품 사이트에서 플랫폼별로 관리합니다. 회사 웹사이트 방침과 앱의 처리 범위는 구분합니다.
- Windows: https://dpnzdy.github.io/adequora-writer/app-privacy.html — 시행일 2026-11-01 유지.
- Android: https://dpnzdy.github.io/adequora-writer/android-app-privacy.html — 시행일 2026-11-13.
- 공통 주소는 `src/data/adequora-writer.ts`의 privacy/androidPrivacy, 진입점은 `Layout.astro`, `ProductResources.astro`, 한·영 privacy 페이지입니다.
- Android 정책 공개가 Google Play 앱 출시나 심사 승인을 뜻하지 않도록 표시합니다. 기존 Windows 다운로드와 공개 이력을 정책 추가만으로 변경하지 않습니다.

## 검증

```powershell
npm run build
npm run preview -- --host 127.0.0.1 --port 4174
python scripts/qa-privacy.py
```

기존 Playwright·Microsoft Edge 환경에서 한·영 정책/지원/제품 페이지를 320·390·768·1440px로 확인합니다. 결과·캡처는 ignored `.qa/privacy/`에 저장합니다. 메일을 보내거나 문의 정보를 제출하지 않습니다.
