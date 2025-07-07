import json
from tasks.scrape_users import scrape_users

PORTAL_URL = "http://localhost:8000/test-login.html"


PORTAL_USERNAME = "srujanaontela@gmail.com"
PORTAL_PASSWORD = "1234"

if __name__ == "__main__":
    print("[1] Scrape Users")
    print("[2] Add User")
    print("[3] Remove User")
    choice = input("Choose: ")

    if choice == "1":
        result = scrape_users(PORTAL_URL, PORTAL_USERNAME, PORTAL_PASSWORD)
        print(json.dumps(result, indent=2))  # ✅ This prints the JSON



