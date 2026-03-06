import requests
import time
import random
import getpass

# API Endpoints
LOGIN_URL = "https://auth.app.senecalearning.com/api/login"
PROGRESS_URL = "https://api.senecalearning.com/api/progress"

def start_bot():
    print("--- Seneca Termux Automator ---")
    email = input("Email: ")
    password = getpass.getpass("Password (hidden): ")

    # 1. AUTHENTICATION
    auth_payload = {"email": email, "password": password}
    try:
        auth_res = requests.post(LOGIN_URL, json=auth_payload)
        if auth_res.status_code != 200:
            print("[-] Login Failed. Check your email/password.")
            return
        
        # Extract the token
        token = auth_res.json().get("token")
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        print("[+] Login Successful!")

        # 2. COURSE CONFIG
        course_id = input("Enter Course ID: ")
        section_id = input("Enter Section ID: ")

        # 3. COMPLETION SIGNAL
        # sessionTime is in seconds. We use a human-like range.
        study_time = random.randint(300, 600) 
        
        progress_data = {
            "courseId": course_id,
            "sectionId": section_id,
            "stats": {
                "correct": random.randint(8, 12),
                "incorrect": random.randint(0, 2),
                "total": 12
            },
            "sessionTime": study_time
        }

        print(f"[*] Simulating {study_time // 60} minutes of study...")
        time.sleep(5) # Short wait before sending

        response = requests.post(PROGRESS_URL, headers=headers, json=progress_data)
        
        if response.status_code in [200, 204]:
            print("[+++] SUCCESS: Assignment marked as complete!")
        else:
            print(f"[-] Error {response.status_code}: {response.text}")

    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    start_bot()
