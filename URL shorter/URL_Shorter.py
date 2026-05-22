import requests

def shorten_url(long_url):
    api_url = f"https://tinyurl.com/api-create.php?url={long_url}"
    
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.text
    else:
        return "Error shortening URL"

# User input
url = input("Enter a long URL: ")

short_url = shorten_url(url)

print("Shortened URL:", short_url)