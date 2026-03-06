import requests
import time
import random

# --- CONFIGURATION ---
EMAIL = "23raybak@ninestiles.org.uk"
PASS = "Student57788"

LOGIN_URL = "https://auth.app.senecalearning.com/api/login"
PROGRESS_URL = "https://api.senecalearning.com/api/progress"

def start_bot():
    print("--- Seneca Termux Automator ---")
    
    # 1. AUTHENTICATION
    auth_payload = {"email": EMAIL, "password": PASS}
    try:
        print(f"[*] Attempting login for {EMAIL}...")
        auth_res = requests.post(LOGIN_URL, json=auth_payload)
        
        if auth_res.status_code != 200:
            print(f"[-] Login Failed. Status: {auth_res.status_code}")
            print(f"[-] Response: {auth_res.text}")
            return
        
        token = auth_res.json().get("token")
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        print("[+] Login Successful!")

        # 2. ASSIGNMENT INFO
        print("\nGet these from the Seneca URL (courseId=...&sectionId=...)")
        course_id = input("Enter Course ID: ").strip()
        section_id = input("Enter Section ID: ").strip()

        # 3. COMPLETION DATA
        # study_time is in seconds (300s = 5 mins)
        study_time = random.randint(350, 650) 
        
        progress_data = {
            "courseId": course_id,
            "sectionId": section_id,
            "stats": {
                "correct": random.randint(10, 12),
                "incorrect": 0,
                "total": 12
            },
            "sessionTime": study_time
        }

        print(f"\n[*] Simulating {study_time // 60} minutes of study time...")
        print("[*] Waiting 10 seconds to sync with server...")
        time.sleep(10)

        # 4. SUBMIT
        response = requests.post(PROGRESS_URL, headers=headers, json=progress_data)
        
        if response.status_code in [200, 204]:
            print("\n[+++] SUCCESS: Assignment marked as complete!")
            print("[!] Refresh your Seneca page to see the progress.")
        else:
            print(f"[-] Error {response.status_code}: {response.text}")

    except Exception as e:
        print(f"[!] Critical Error: {e}")

if __name__ == "__main__":
    start_bot()
