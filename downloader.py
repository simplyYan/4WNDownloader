import os
import requests

def download_file(file_name):
    # Base URL of the GitHub repository
    base_url = "https://raw.githubusercontent.com/simplyYan/4WNDownloader/main/files/"
    
    # Full URL of the file
    file_url = f"{base_url}{file_name}"
    
    # Local path to save the file
    local_path = os.path.join(os.getcwd(), file_name)
    
    try:
        # Request to check if the file exists
        response = requests.get(file_url, stream=True)
        if response.status_code == 200:
            print(f"Downloading file '{file_name}'...")
            with open(local_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"File '{file_name}' downloaded successfully!")
        else:
            print(f"File '{file_name}' not found in the repository.")
    except Exception as e:
        print(f"An error occurred while trying to download the file: {e}")

def main():
    print("=== 4WN Downloader ===")
    file_name = input("Enter the name of the file you want to download (including extension): ").strip()
    
    if file_name:
        download_file(file_name)
    else:
        print("File name cannot be empty.")

if __name__ == "__main__":
    main()
