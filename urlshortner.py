import pyshorteners

url = input("Enter URL: ")

# auto-fix missing https
if not url.startswith("http"):
    url = "https://" + url

try:
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)

    print("Short URL:", short_url)

except Exception as e:
    print("Error:", e)