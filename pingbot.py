import requests
import time

def main():
    server_url = "http://localhost:5000/health"
    while True:
        try:
            response = requests.get(server_url, timeout=5)
            result = response.json()
            if result.get("status") == "ok" and response.status_code == 200:
                print("Server is ok and running")
            else:
                print("Something happened to the server, check")
        except:
            print("SERVER FAILED")
        time.sleep(480)


if __name__ == "__main__":
    main()