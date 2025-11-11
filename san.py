import webbrowser
import time
import os

def open_chrome_tabs():
    # URLs to open
    urls = [
        "https://chat.openai.com/",
        "https://www.livechat.com/typing-speed-test/"
    ]

    # Try to open Chrome specifically (works on Windows, macOS, Linux)
    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",             # Windows default
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",      # macOS
        r"/usr/bin/google-chrome",                                            # Linux
        r"/usr/bin/chromium-browser"
    ]

    chrome_path = None
    for path in chrome_paths:
        if os.path.exists(path):
            chrome_path = path
            break

    if chrome_path:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        browser = webbrowser.get('chrome')
    else:
        print("⚠️ Chrome not found — using default browser.")
        browser = webbrowser.get()

    # Open each site in a new tab
    for i, url in enumerate(urls):
        if i == 0:
            browser.open(url, new=1)  # open first site in new window
        else:
            time.sleep(1)
            browser.open_new_tab(url)  # open others in new tabs

    print("✅ Chrome opened with ChatGPT and Typing Speed Test!")

if __name__ == "__main__":
    open_chrome_tabs()
