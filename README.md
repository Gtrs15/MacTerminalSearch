# MacTerminalSearch

MacTerminalSearch is a tool that enables google search functionality directly from your terminal.  
Type your entire search without leaving your editor/terminal.



## Requirements

Python3




# Installation


## Easy Install


[The app can be installed from the zip file contained in the release.](https://github.com/Gtrs15/MacTerminalSearch/releases/tag/Initial_Release)

Download the file named "run_installation.zip"

Unzip the .app file contained inside

Run the .app file

After you run the .app file, you can launch any new instance of terminal and use the command ```ts``` to use the app.

## Manual Install


If you would prefer to manually install, here are the instructions:

Run the following commands.

Clone app to directory:

	git clone https://github.com/Gtrs15/MacTerminalSearch.git /Users/Shared/.MacTerminalSearch

Add alias to zshrc file:

	echo 'alias ts="python3 /Users/Shared/.MacTerminalSearch/start.py"' >> ~/.zshrc

Lastly, make a folder for the config file

	mkdir /Users/Shared/.MacTerminalSearch/config_files

You can replace the ```~/.zshrc``` with ```~/.bashrc``` if you use bash as your default shell. 

Any alias can be used if you are already using ```ts``` for something else, or if you  prefer a different one.





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


