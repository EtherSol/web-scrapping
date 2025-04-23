from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)  # Turn off headless so you can see it
        context = browser.new_context(user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
        ))

        page = context.new_page()
        page.goto("https://medium.com/@vrtwise/mf-doom-and-how-he-changed-the-world-of-rap-and-alternative-hip-hop-27389f8a94d5")

        # Wait for article content to load
        page.wait_for_selector("article")

        title = page.title()
        print("Page title:", title)

        # Grab article content
        paragraphs = page.query_selector_all("article p")
        article_text = "\n\n".join([p.inner_text() for p in paragraphs])

        print("\nArticle Content Preview:\n")
        print(article_text[:1000])  # Just show the first 1000 chars

        browser.close()

if __name__ == "__main__":
    run()