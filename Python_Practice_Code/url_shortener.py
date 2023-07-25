import hashlib

def shorten_url(long_url):
    # Create a hash of the long URL using MD5
    hash_object = hashlib.md5(long_url.encode())
    hash_hex = hash_object.hexdigest()
    
    # Take the first 8 characters of the hash as the short URL
    short_url = hash_hex[:8]
    
    return short_url

def url_shortener():
    print("URL Shortener")
    long_url = input("Enter the long URL: ")
    short_url = shorten_url(long_url)
    print(f"Short URL: https://short.url/{short_url}")

if __name__ == "__main__":
    url_shortener()
