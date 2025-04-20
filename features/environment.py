from playwright.sync_api import sync_playwright
from features.logger import setup_logger
import logging


def before_all(context):
    setup_logger()
    logging.info("Test Execution started")
    playwright1= sync_playwright().start()
    browser = playwright1.chromium.launch(headless=True,  args=[
            "--disable-blink-features=AutomationControlled",
            "--window-size=1920,1080",
        ],
        slow_mo=50  # يساعد في الانتظار بين الأوامر
    )

    page = browser.new_page(viewport={"width": 1920, "height": 1080},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.89 Safari/537.36"
   )

    context.playwright = playwright1
    context.browser = browser
    context.page = page

def after_all(context):
    logging.info("Test execution completed.")
    context.page.close()
    context.browser.close()
    context.playwright.stop()