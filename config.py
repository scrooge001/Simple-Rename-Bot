from os import environ

API_ID = int(environ.get("API_ID", ""))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
ADMIN = int(environ.get("ADMIN", ""))          
CAPTION = environ.get("CAPTION", "<a href='t.me/adgmovies'>\n{file_name}\n\n┏━━━━•❅•°•❈•°•❅•━━━━┓\n💥★ ADG MOVIES™ ★💥\n┗━━━━•❅•°•❈•°•❅•━━━━┛</a>")

# for thumbnail ( back end is MrMKN brain 😉)
DOWNLOAD_LOCATION = "./DOWNLOADS"

