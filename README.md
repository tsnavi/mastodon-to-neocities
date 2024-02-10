# mastodon-to-neocities
A method for importing your Mastodon feed into your Neocities site via .rss (workaround for Neocities' CSP restricting direct linking to external .rss)

# Why?
Mastodon is a great method for microblogging. Since I'm using my website to document my experiences with web development, I felt that importing my toots, where I would post about my website changes, would be a suitable way of [documenting my processes](https://indieweb.org/documentation) - less formal, and more frequent.
However, free-tier Neocities understandably doesn't allow a lot of external resources to be called, so to display a Mastodon feed on your page you need to first download it and upload it to your site. That is a pain in the arse to do manually each time you toot.
This tool automates that process, and also shows you how to display the .rss in your html (using javascript to parse rss into html elements of your choosing)

# Requirements
- [Neocities Account](https://neocities.org/)
- Mastodon Feed (your mastodon URL plus .rss appended eg: https://indieweb.social/@tsxyz.rss)
- Ruby installed https://www.ruby-lang.org/en/downloads/
- Neocities CLI setup (Ruby needed to run this CLI) - First time, after Ruby is installed, run 'gem neocities install' in CMD. Then run just 'neocities' and it will ask you to authenticate with your username and password. After that you can run the script in this repo (for more info: https://neocities.org/cli)

# Method
- **IMPORTANT**: This script asks Neocities to **DELETE** a file. Make sure you read the comments of, and make edits to, the py script before running. To be on the safe side, [download a backup of your site first](https://neocities.org/site_files/download)!
- Ensure you have the above requirements (remember to authenticate after installing Neocities)
- Edit rssfetch.py to suit
  - Mastodon feed url
  - local .rss filename
  - Location of current rss feed for deletion
  - Upload destination in your Neocities folders
- Setup your html to parse the .rss feed (see [index.html](https://github.com/tsnavi/mastodon-to-neocities/blob/main/index.html), [tsnavi/js-rss-reader](https://github.com/tsnavi/js-rss-reader) or [a live example on my site](https://tsxyz.neocities.org/micro)).
- Run rssfetch.py
- (Optional, Windows) Once successful schedule rssfetch.py to run in Task Scheduler - you have to ask it to run python, with arg of "rssfetch.py" and file location of the folder containing rssfetch.py
  - ![image](https://github.com/tsnavi/mastodon-to-neocities/assets/145156860/ab832590-06c5-4a5d-a51c-86a1298896fa)


# Todo:
Local method of reducing down .rss feed to 'x most recent toots' - Save server space and threadwork, if a page is only displaying the 4 most recent toots, therefore doesn't need to download the whole feed. See: https://tsxyz.neocities.org homepage
