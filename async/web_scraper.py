import asyncio
import aiohttp
from bs4 import BeautifulSoup
import time

async def fetch_url(session, url):
    """Fetch a single URL asynchronously"""
    try:
        async with session.get(url) as response:
            return await response.text()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

async def parse_content(html):
    """Parse HTML content to extract useful information"""
    if not html:
        return None
    soup = BeautifulSoup(html, 'html.parser')
    # Example: Extract all paragraph texts
    return [p.text for p in soup.find_all('p')]

async def scrape_websites(urls):
    """Scrape multiple websites concurrently"""
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            # Create tasks for fetching and parsing
            task = asyncio.create_task(fetch_url(session, url))
            tasks.append(task)
        
        # Wait for all fetch tasks to complete
        html_contents = await asyncio.gather(*tasks)
        
        # Parse all HTML contents
        parse_tasks = [parse_content(html) for html in html_contents]
        results = await asyncio.gather(*parse_tasks)
        
        return results

async def main():
    # Example URLs to scrape
    urls = [
        'https://example.com',
        'https://python.org',
        'https://github.com'
    ]
    
    start_time = time.time()
    results = await scrape_websites(urls)
    end_time = time.time()
    
    print(f"Scraped {len(urls)} websites in {end_time - start_time:.2f} seconds")
    for url, result in zip(urls, results):
        if result:
            print(f"\nContent from {url}:")
            print(f"Found {len(result)} paragraphs")
            print("First paragraph:", result[0][:100] if result else "No content")

if __name__ == "__main__":
    asyncio.run(main()) 