import requests
import time
import random

# --- YOUR ACCOUNT DETAILS ---
EMAIL = "23raybak@ninestiles.org.uk"
PASS = "Student57788"

# --- API ENDPOINTS ---
LOGIN_URL = "https://auth.app.senecalearning.com/api/login"
PROGRESS_URL = "https://api.senecalearning.com/api/progress"

def run_bot():
    # 1. Login to get your Token
    print(f"[*] Logging in as {EMAIL}...")
    try:
        auth_res = requests.post(LOGIN_URL, json={"email": EMAIL, "password": PASS})
        if auth_res.status_code != 200:
            print("[-] Login Failed! Check your password.")
            return
        
        token = auth_res.json().get("token")
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        print("[+] Login Successful. Token acquired.")

        # 2. Ask for the homework details
        # You get these from the Seneca URL (e.g. courseId=...&sectionId=...)
        course_id = input("Paste Course ID: ")
        section_id = input("Paste Section ID: ")

        # 3. Simulate "Learning" (to avoid getting banned)
        # We tell Seneca you spent between 5 and 10 minutes
        study_seconds = random.randint(300, 600) 
        
        payload = {
            "courseId": course_id,
            "sectionId": section_id,
            "stats": {
                "correct": random.randint(9, 11), # 90-100% score
                "incorrect": 0,
                "total": 11
            },
            "sessionTime": study_seconds
        }

        print(f"[*] Simulating study session ({study_seconds // 60} mins)...")
        print("[*] Please wait 10 seconds for the 'handshake'...")
        time.sleep(10) 

        # 4. Submit the work
        response = requests.post(PROGRESS_URL, headers=headers, json=payload)
        
        if response.status_code in [200, 204]:
            print("[+++] DONE! This section is now marked as complete on Seneca.")
        else:
            print(f"[-] Error: {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"[!] Critical Error: {e}")

if __name__ == "__main__":
    run_bot()
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
