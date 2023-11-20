# Import the required libraries
from playwright.async_api import async_playwright
import asyncio
import time
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import re

# Define the URL to scrape
url = "https://www.complex.management/legal/documents/STSMA-S:1"


async def scrape(url):
    """Scrape the URL."""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Navigate to the URL
        await page.goto(url)

        # Wait for the page to load
        await page.wait_for_load_state("networkidle")

        # Get the page content
        content = await page.content()

        # Close the browser
        await browser.close()

        # Create a BeautifulSoup object
        soup = BeautifulSoup(content, "html.parser")

        # Find the table of contents
        toc = soup.find_all("div", class_="tab-content")

        # Find all the panels
        panels = toc[0].find_all("mat-expansion-panel")

        # Loop through the panels
        for panel in panels:
            # Find the panel title
            title = panel.find("span", class_="index-button ng-star-inserted")

            # Find the panel content
            content = panel.find("div", class_="mat-expansion-panel-content")

            # Find all the links
            links = content.find_all("a")

            # Print the title
            print(title.text)

            # Print the links
            for link in links:
                print(link.text)

            # Print a new line
            print("\n")


if __name__ == "__main__":
    asyncio.run(scrape(url))
