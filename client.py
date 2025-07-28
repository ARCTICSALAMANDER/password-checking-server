import requests

SERVER_URL = "http://localhost:5000/check-password"

def main():
    try:
        responce = requests.get("http://localhost:5000/health", timeout=5)
        if responce.status_code == 200:
            print("Server is running and available")
    except requests.ConnectionError:
        print("Server connection failed")

    while True:
        password = input()
        try:
            responce = requests.post(SERVER_URL, json={"password": password}, timeout=10)
            if responce.status_code == 200:
                result = responce.json()
                if result.get("success"):
                    print("password is correct")
                else:
                    print("password incorrect")
            elif responce.status_code == 400:
                print("Invalid data")
            else:
                print(f"Error: {responce.status_code}")
        except requests.exceptions.Timeout:
            print("Time limit exceeded")
        except requests.exceptions.ConnectionError:
            print("Server is not available")
        except requests.exceptions.RequestException as e:
            print(f"Error occured: {e}")

if __name__ == "__main__":
    main()