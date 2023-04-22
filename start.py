from settings_storage import JsonStorage, FirstTimeAppStart
from launch_browser import BrowserLauncher
from imports.config import settings_json

FirstTimeAppStart(settings_json).start()

settings = JsonStorage(settings_json)
BrowserLauncher(settings.data['browser_choice'], settings_json).launch_search()
