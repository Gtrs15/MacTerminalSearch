# MacTerminalSearch

MacTerminalSearch is a tool that enables google search functionality directly from your terminal.  
Type your entire search without leaving your editor/terminal.



## Requirements

Python3




# Installation



Run the following commands.


Step 1: Clone app to directory:


	git clone https://github.com/Gtrs15/MacTerminalSearch.git /Users/Shared/.MacTerminalSearch


Step 2: Add alias to zshrc file:

You can replace the ```~/.zshrc``` with ```~/.bashrc``` if you use bash as your default shell. 

Any alias can be used if you are already using ```ts``` for something else, or if you  prefer a different one.


	echo 'alias ts="python3 /Users/Shared/.MacTerminalSearch/start.py"' >> ~/.zshrc







## Usage 

Use the command ```ts``` (or the custom alias) to search with site contraints of only websites added by the user.  

Use the options shown below to make changes after initial setup.  



## Options

```-g``` Do a normal google search and not limit search to site list.

Example usage: ```ts -g python selenium documentation```

```-d <SITE_KEY>``` : delete a website from the site list (don't include .com)

Example usage: ```ts -d stackoverflow``` (can also use any non-blank string to check site_list)

```-a <SITE_URL>``` : add a site to the site list (Do not need https or WWW in URL)

Example usage: ```ts -a stackoverflow.com```

```--update``` : Remove MacTerminalSearch and then install the most recent version.

```--uninstall``` : Remove MacTerminalSearch and all config files.


