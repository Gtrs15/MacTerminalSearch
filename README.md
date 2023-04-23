# MacTerminalSearch

MacTerminalSearch is a tool that enables google search functionality directly from your terminal.  
Type your entire search without leaving your editor/terminal.


## Installation

The app can be installed from the .dmg file.  
If you would prefer to clone it, here are the instructions:
Run the following command.

	git clone https://github.com/Gtrs15/MacTerminalSearch.git /Users/Shared/.MacTerminalSearch

Once complete, add an alias to your .zshrc or .bashrc file for quicker execution of the app.

Example: ```alias ts="python3 /Users/Shared/.MacTerminalSearch/start.py"```

Any alias can be used if you are already using ```ts``` for something else.  


## Options

```-g``` Used to do a normal google search and not limit search to site list.

Example usage: ```ts -g python selenium documentation```

```-d <SITE_KEY>``` : delete a website from the site list (don't include .com)

Example usage: ```ts -d stackoverflow``` (can also use any non-blank string to check site_list)

```-a <SITE_URL>``` : add a site to the site list (Do not need https or WWW in URL)

Example usage: ```ts -a stackoverflow.com```

```--update``` : Remove MacTerminalSearch and then install the most recent version.

```--uninstall``` : Remove MacTerminalSearch and all config files.


