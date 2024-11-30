import requests
import json

# Function to start a new session and retrieve session_id
def start_session(first_name, last_name):
    url = 'https://hackdiversity.xyz/api/start-session'
    payload = {
        'firstName': first_name,
        'lastName': last_name
    }
    
    try:
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            session_data = response.json()
            session_id = session_data.get('session_id')
            if session_id:
                print(f'Session started successfully! Session ID: {session_id}')
                return session_id
            else:
                print('Error: Session ID not found in the response')
        else:
            print(f'Error starting session: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error starting session: {e}')
    return None
def main():
    # Step 1: Start a session and get session_id
    first_name = 'Obianuju'  # Replace with your first name
    last_name = 'Enekebe'     # Replace with your last name
    session_id = start_session(first_name, last_name)
    print(session_id)
if __name__ == '__main__':
    main()