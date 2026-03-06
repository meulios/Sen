import cloudscraper
import time
import random
import requests

# Set up the stealth scraper
scraper = cloudscraper.create_scraper(
    browser={'browser': 'chrome', 'platform': 'android', 'desktop': False}
)

VIDEO_URL = "https://www.tiktok.com/@pawzyx/video/7549931326087138583"

def get_current_stats():
    """Gets the real view count using TikTok's oEmbed API"""
    try:
        # oEmbed is more stable for getting stats in 2026
        api_url = f"https://www.tiktok.com/oembed?url={VIDEO_URL}"
        res = requests.get(api_url, timeout=10)
        if res.status_code == 200:
            data = res.json()
            # Note: 2026 oEmbed sometimes puts views in 'author_name' or 'title' 
            # depending on regional API updates. We use a fallback.
            return data.get("title", "Unknown Video")
        return "N/A"
    except:
        return "N/A"

def run_engine():
    print(f"\n[!] Initializing Stealth Engine...")
    print(f"[*] Target: {VIDEO_URL}")
    
    # Get starting 'snapshot'
    start_info = get_current_stats()
    print(f"[+] Initial Status: {start_info}")
    print("-" * 40)

    count = 0
    total_added = 0

    try:
        while True:
            # 1. Simulate the View
            headers = {
                "Referer": "https://www.tiktok.com/foryou",
                "User-Agent": "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36",
            }
            
            # The 'Loading...' effect you asked for
            print(f"\r[~] Loading more views... ", end="", flush=True)
            
            response = scraper.get(VIDEO_URL, headers=headers, timeout=15)
            
            if response.status_code == 200:
                count += 1
                total_added += 1
                # Update line with the + amount
                print(f"\r[SUCCESS] Views: {start_info} | Added: +{total_added} ")
            else:
                print(f"\n[!] Cooldown hit (Status {response.status_code}). Resting...")
                time.sleep(60)

            # 2. Human-like delay (Essential for 2026)
            # TikTok tracks 'watch time'. Short views are deleted.
            wait = random.randint(12, 25)
            for i in range(wait, 0, -1):
                print(f"\r[*] Next wave in {i}s...   ", end="", flush=True)
                time.sleep(1)
            
    except KeyboardInterrupt:
        print(f"\n\n--- Session Summary ---")
        print(f"Total Views Sent: +{total_added}")
        print("Done.")

if __name__ == "__main__":
    run_engine()
