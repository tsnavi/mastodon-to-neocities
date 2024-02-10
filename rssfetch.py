import requests
import os
from datetime import datetime

# Download Mastodon feed and save as RSS file locally
def download_mastodon_feed(url, filename):
    try:
        print(f"Downloading Mastodon feed from URL: {url}")
        response = requests.get(url)
        print(f"Response status code: {response.status_code}")
        if response.status_code == 200:
            # Save the response content as RSS file
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded Mastodon feed and saved as {filename}")
            # Log file information
            file_info = os.stat(filename)
            print(f"File size: {file_info.st_size} bytes")
            print(f"Last modified: {datetime.fromtimestamp(file_info.st_mtime)}")
            return True
        else:
            print(f"Failed to download Mastodon feed. Status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"Error downloading Mastodon feed: {e}")
        return False


# Upload file to Neocities
def upload_to_neocities(filename):
    try:
        # If file already exists, you must delete it. Maybe there's a better way using 'push', but I don't understand it at the moment so I'm using this method.
        # Make sure this argument matches the folder structure where you want your .rss to live
        # IMPORTANT: This will delete files in your folders if configured wrong
        os.system(f'neocities delete micro/{filename}')
        
        # Upload rss file
        # The Neocities CLI uses -d to define "directory" - IE: it won't find work if you write "upload micro/feed.rss", but the delete function does
        upload_command = f'neocities upload -d micro {filename}'
        os.system(upload_command)
        print(f"Uploaded {filename} to Neocities")
    except Exception as e:
        print(f"Error uploading file to Neocities: {e}")

def main():
    # EDIT THIS to your own Feed URL
    mastodon_feed_url = 'https://indieweb.social/@tsxyz.rss'
    
    # EDIT THIS to your desired .rss local and uploaded filename
    filename = 'mastodon_feed.rss'

    # Download Mastodon feed
    if download_mastodon_feed(mastodon_feed_url, filename):
        # Upload RSS file to Neocities
        upload_to_neocities(filename)

if __name__ == "__main__":
    main()
