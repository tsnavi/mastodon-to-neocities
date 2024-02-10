# mastodon-to-neocities
A method for importing your Mastodon feed into your Neocities site via .rss (workaround for Neocities' CSP restricting direct linking to external .rss)

# Requirements
- [Neocities Account](https://neocities.org/)
- Mastodon Feed (your mastodon URL plus .rss appended eg: https://indieweb.social/@tsxyz.rss)
- Ruby installed https://www.ruby-lang.org/en/downloads/
- Neocities CLI setup (Ruby needed to run this CLI) - First time, after Ruby is installed, run 'gem neocities install' in CMD. Then run just 'neocities' and it will ask you to authenticate with your username and password. Then you can run the script in this repo (for more info: https://neocities.org/cli)

# Method
- Ensure you have the above requirements (remember to authenticate after installing Neocities via Ruby)
- Edit rssfetch.py to suit
  - Mastodon feed url
  - local .rss filename
  - Location of current feed for deletion
  - Upload destination in your Neocities folders
- Setup your html to parse the .rss feed (see index.html or https://tsxyz.neocities.org/micro)
- Run rssfetch.py
- If successful, schedule rssfetch.py to run in Task Scheduler

# Todo:
Local method of reducing down .rss feed to 'x most recent toots' - Save server space and threadwork, if a page is only displaying the 4 most recent toots, therefore doesn't need to download the whole feed. See: https://tsxyz.neocities.org homepage
