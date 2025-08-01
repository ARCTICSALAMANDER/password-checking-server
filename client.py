import requests

server_url = "http://localhost:5000"

def check_server_health():
    try:
        response = requests.get(f"{server_url}/health", timeout=2)
        if response.status_code == 200:
            print("Server is running and available")
            return True
        else:
            print(f"Server responded with status: {response.status_code}")
            return False
    except requests.ConnectionError:
        print("Server connection failed - is it running?")
        return False
    except requests.RequestException as e:
        print(f"Error checking server health: {e}")
        return False

def main():
    if not check_server_health():
        return

    print("Enter password to check (or 'exit' to quit):")
    while True:
        password = input()
            
        try:
            response = requests.post(
                f"{server_url}/check-password",
                json={"password": password},
                timeout=5
            )
            
            if response.status_code == 200:
                result = response.json()
                if result.get("success"):
                    print("Password is correct!")  
                else: 
                    print("Password is incorrect!")
            else:
                print(f"Server error: {response.status_code}")
                
        except requests.exceptions.Timeout:
            print("Request timed out")
        except requests.exceptions.ConnectionError:
            print("Connection to server lost")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()