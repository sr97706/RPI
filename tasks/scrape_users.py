from browser.playwright_wrapper import Browser

def scrape_users(portal_url, username, password):
    browser = Browser()
    browser.login(portal_url, username, password)

    # Wait for table to load
    browser.page.wait_for_selector("table")

    rows = browser.page.query_selector_all("table tr")[1:]  # skip the header row

    users = []
    for row in rows:
        cells = row.query_selector_all("td")
        if len(cells) == 4:
            users.append({
                "name": cells[0].inner_text().strip(),
                "email": cells[1].inner_text().strip(),
                "role": cells[2].inner_text().strip(),
                "last_login": cells[3].inner_text().strip()
            })

    browser.close()
    return users
