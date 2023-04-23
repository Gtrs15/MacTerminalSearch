import os
from imports.config import install_folder
from pathlib import Path


class ProgramInstallation:

    def __init__(self) -> None:

        # Define App Folder
        self.app_folder = install_folder
        # Define alias message
        self.alias_message = f"\"python3 {self.app_folder}/start.py\""
        # Define alias string to add to zshrc
        self.alias_to_add_to_zshrc = f'alias ts={self.alias_message}'

        # Define git repo to clone
        self.gitRepo = 'https://github.com/Gtrs15/MacTerminalSearch.git'

    def install(self):
        self.clone_repo_to_empty_folder()
        self.create_empty_folders_logs_and_config()
        self.echo_alias_to_zshrc()

    def uninstall(self):
        os.system(f'rm -rf {self.app_folder}/.git')
        os.system(f'rm -r {self.app_folder}')
        self.remove_alias_from_zshrc()

    def update(self):
        self.uninstall()
        self.install()

    def clone_repo_to_empty_folder(self):
        os.system(f'git clone {self.gitRepo} {self.app_folder}')

    def create_empty_folders_logs_and_config(self):
        # mkdir for install, might ask for user password
        os.system(f'mkdir {self.app_folder}/logs')
        os.system(f'mkdir {self.app_folder}/config')

    def echo_alias_to_zshrc(self):
        self.check_if_zshrc_exists()
        # Write alias to the zshrc file
        os.system(f'''echo '{self.alias_to_add_to_zshrc}' >> ~/.zshrc''')

    def check_if_zshrc_exists(self):
        try:
            zshrc_file = Path().home() / '.zshrc'
        except:
            os.system(f'touch {zshrc_file}')
            zshrc_file = Path().home() / '.zshrc'
        return zshrc_file

    def remove_alias_from_zshrc(self):
        zshrc_file = self.check_if_zshrc_exists()

        # Set lines to all lines of zshrc file
        with open(zshrc_file, 'r') as f:
            lines = f.readlines()

        # Iterate through lines and rewrite the file over itself
        # except for the line containing the alias
        with open(zshrc_file, 'w') as f:
            for line in lines:
                if self.alias_to_add_to_zshrc not in line:
                    f.write(line)

    def check_if_installed(self):
        pass

