# tasks/manage_users.py

from browser.playwright_wrapper import Browser

def add_user(portal_url, username, password, user_info):
    browser = Browser(headless=False)
    browser.start()
    browser.login(portal_url, username, password)

    # Example navigation to add user page
    browser.page.click("text=Add User")
    browser.page.fill("input[name='name']", user_info["name"])
    browser.page.fill("input[name='email']", user_info["email"])
    browser.page.select_option("select[name='role']", user_info["role"])
    browser.page.click("button[type='submit']")

    browser.page.wait_for_timeout(3000)
    browser.close()

def remove_user(portal_url, username, password, email_to_remove):
    browser = Browser(headless=False)
    browser.start()
    browser.login(portal_url, username, password)

    browser.page.fill("input[placeholder='Search']", email_to_remove)
    browser.page.click("text=Delete")
    browser.page.click("text=Confirm")

    browser.page.wait_for_timeout(3000)
    browser.close()
