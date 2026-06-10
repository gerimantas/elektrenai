# -*- coding: utf-8 -*-
import tempfile, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from pathlib import Path
from playwright.sync_api import sync_playwright

OUTPUT = Path(tempfile.gettempdir()) / "elektrenai"
OUTPUT.mkdir(exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page(viewport={"width": 1600, "height": 900})

    # Login
    page.goto("https://www.geoportal.lt/map/", timeout=90000, wait_until="domcontentloaded")
    page.get_by_role("button", name="Prisijungti").first.click()
    page.wait_for_timeout(2000)
    page.fill("input[type='text']", "Gerimantas")
    page.fill("input[type='password']", "Nntchn*61*87")
    page.get_by_role("button", name="prisijungti").click()
    page.wait_for_load_state("load", timeout=60000)
    page.wait_for_selector("canvas, .ol-viewport", timeout=60000)
    page.wait_for_timeout(4000)
    print("Map loaded")

    # Strategy: use geoportal URL with cadastre layer + LKS94 coords for Sabaliskes area
    # Elektrėnai center LKS94: ~541500, 6072000
    # Navigate with zoom to that area and enable RC kadastras layer
    page.goto(
        "https://www.geoportal.lt/map/#zoom=13&coordinate=541500,6072000&crs=3346&layers=rc_kadastro_zemelapis:1",
        timeout=90000, wait_until="domcontentloaded"
    )
    page.wait_for_selector("canvas, .ol-viewport", timeout=60000)
    page.wait_for_timeout(5000)
    page.screenshot(path=str(OUTPUT / "50_zoom_elektrenai.png"))
    print("Screenshot: 50_zoom_elektrenai.png")

    # Try "Žemėlapio turinys" → enable RC kadastras layer manually
    page.get_by_text("Žemėlapio turinys").first.click()
    page.wait_for_timeout(2000)
    page.screenshot(path=str(OUTPUT / "51_layers_panel.png"))
    print("Screenshot: 51_layers_panel.png")

    # Dump layer panel content
    texts = page.evaluate("""() => {
        return Array.from(document.querySelectorAll('*'))
            .filter(el => el.offsetParent !== null && el.children.length === 0 && el.innerText?.trim().length > 0)
            .map(el => ({tag: el.tagName, text: el.innerText.trim().slice(0,80), id: el.id, cls: el.className?.slice(0,60)}))
            .slice(0, 100);
    }""")
    print("LAYER PANEL CONTENT:")
    for t in texts:
        print(t)

    browser.close()
