const { chromium } = require('playwright');

// Strategy: load regia.lt, intercept ALL network requests when typing,
// find the select/click API endpoint after dropdown click
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1600, height: 900 });

  const allRequests = [];
  page.on('request', req => {
    const url = req.url();
    if (!url.includes('.png') && !url.includes('.jpg') && !url.includes('.css') && !url.includes('.js') && !url.includes('tile') && !url.includes('MapServer')) {
      allRequests.push({ method: req.method(), url: url.substring(0, 150) });
    }
  });

  const allResponses = [];
  page.on('response', async resp => {
    const url = resp.url();
    if (url.includes('Regia2') || url.includes('regia') || url.includes('geocod') || url.includes('adres')) {
      try {
        const body = await resp.text();
        allResponses.push({ url: url.substring(0, 120), body: body.substring(0, 300) });
      } catch {}
    }
  });

  console.log('Loading regia.lt...');
  await page.goto('https://www.regia.lt', { waitUntil: 'domcontentloaded', timeout: 40000 });
  await page.waitForTimeout(9000);

  // Type slowly
  await page.focus('#_easyui_textbox_input1');
  for (const char of 'Kakliniš') {
    await page.keyboard.type(char, { delay: 250 });
    await page.waitForTimeout(100);
  }
  await page.waitForTimeout(4000);

  console.log('All Regia API responses:', JSON.stringify(allResponses, null, 2));

  const items = await page.$$eval('.textbox-panel li', els =>
    els.map(e => ({ text: e.innerText.trim(), html: e.outerHTML.substring(0,200) })).filter(e => e.text)
  );
  console.log('Dropdown items:', JSON.stringify(items.slice(0,3)));
  await page.screenshot({ path: 'nuotraukos/regia-debug.png' });

  // If items visible - click and monitor what API is called
  if (items.length > 0) {
    // Reset response tracking
    const selectResp = [];
    page.on('response', async resp => {
      const url = resp.url();
      try { selectResp.push({ url, body: (await resp.text()).substring(0,300) }); } catch {}
    });

    await page.evaluate(() => {
      const li = document.querySelector('.textbox-panel li');
      if (li) li.click();
    });
    await page.waitForTimeout(5000);
    console.log('After click responses:', JSON.stringify(selectResp.slice(0,5), null, 2));
    await page.screenshot({ path: 'nuotraukos/regia-clicked.png' });
  }

  console.log('\nAll non-asset requests:', allRequests.slice(-20).map(r => `${r.method} ${r.url}`).join('\n'));

  await browser.close();
})();
