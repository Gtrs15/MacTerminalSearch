from pathlib import Path

home_dir = Path().home()

install_folder = Path('/Users/Shared/.MacTerminalSearch')
app_folder = home_dir / 'PycharmProjects' / 'MacTerminalSearch' # For development

settings_json = install_folder / 'config_files' / 'search_config.json'
settings_json_development = app_folder / 'config_files' / 'search_config.json'

help_message = f'''
Welcome to terminalSearch

  Usage Options:
-------------------------------------  
  ts OR ts -h: Show this help message

  ts -g <SEARCH TEXT HERE> : Search google without using specific sites
    Example: ts -g what is the vs code keyboard shortcut to open git graph

  ts -d <SITE_KEY> : delete a website from the site list (don't include .com)
    Example: ts -d stackoverflow (can also use any non-blank string to check site_list)

  ts -a <SITE_URL>: add a site to the site list (Do not need https or WWW in URL)
    Example: ts -a stackoverflow.com

  ts --update : This will remove and then re-install the MacTerminalSearch App
  
  ts --uninstall : This will remove the MacTerminalSearch App and all config files
'''
