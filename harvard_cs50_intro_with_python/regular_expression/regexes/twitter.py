#collect username from url
import re
url = input("URL: ").strip()

username = url.removeprefix("https://twitter.com/", "")
print(f"Username: {username}")

