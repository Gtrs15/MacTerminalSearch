import sys
import webbrowser
from settings_storage import JsonStorage
from logs.create_logger import logs
from imports.config import help_message
from imports.install import ProgramInstallation


class BrowserLauncher:

    def __init__(self, browser_selection, json_settings_file):
        self.json_settings_file = json_settings_file

        # Mac paths tested on 4/1/2023
        # Working
        self.browser_list = {
            "chrome": "open -a /Applications/Google\ Chrome.app %s",
            "firefox": "open -a /Applications/Firefox.app %s",
            "gx": "open -a /Applications/Opera\ GX.app %s",
            "safari": "open -a /Applications/Safari.app %s"
        }

        self.browser_selection = browser_selection

        # Set self.browser_path to the selection of the self.os list
        # then Select from returned list (based on OS) using browser_selection index
        self.browser_path = self.browser_list[self.browser_selection]

        self.websites = [value for value in JsonStorage(self.json_settings_file).data['site_list'].values()]

        self.url = 'https://www.google.com/search?q='

        self.flag = self.check_first_flag()
        self.change_settings = None

    @staticmethod
    def check_first_flag():
        try:
            return sys.argv[1]
        except IndexError as e:
            logs.log_error(e)
            # If no args were passed, defaults to -h (help) flag
            return '-h'

    # Create site specific search string
    def site_specific_search(self):
        sites = ' ( '
        for index, website_url in enumerate(self.websites):
            sites += 'site:' + website_url
            if index == len(self.websites) - 1:
                sites += ' )'
            else:
                sites += ' OR '
        return sites

    # Return the args passed in CLI as a string
    def get_search_from_args(self):

        if self.flag[0] == '-':
            return " ".join(sys.argv[2:])
        else:
            return " ".join(sys.argv[1:])

    # Combine url, search query, and site specs
    def create_search_url(self, site_specs):
        # If option flag detected, evaluate and return the result
        if self.flag[0] == '-':
            return self.first_arg_evaluator()
        # If no option, return the url and search_query, and site_specifications
        else:
            return self.url + self.get_search_from_args() + site_specs

    def first_arg_evaluator(self):
        settings = JsonStorage(self.json_settings_file)

        # Google search only, no site constraint
        if self.flag == '-g':
            return self.url + self.get_search_from_args()
        else:
            # All non '-g' flags will change settings
            self.change_settings = True

        # Add a website to the site_list
        if self.flag == '-a':
            try:
                site_to_add = sys.argv[2]
                settings.add_sites_to_site_list(site_to_add.split('.')[0], site_to_add)
                site_list = settings.read_json()['site_list']
                print(f'New List:')
                print([(f'{site_list[x]}') for x in site_list])
            except:
                print('Invalid Site Addition')

        # Delete a website from site_list
        if self.flag == '-d':
            site_index = sys.argv[2]
            settings.remove_site_from_site_list(site_index.split('.')[0])
            print(f'Deleted {site_index} from site_list.\nNew List:')
            site_list = settings.read_json()['site_list']
            print(*[x for x in site_list])
            
        # Show Help Message
        if self.flag == '-h':
            print(help_message)
            site_list = settings.read_json()['site_list']
            print('Current Site List:')
            print(*[x for x in site_list.keys()])

        # Update App
        if self.flag == '--update':
            print('MacTerminalSearch will now update.')
            ProgramInstallation().update()
            print('Update Complete')

        # Uninstall App
        if self.flag == '--uninstall':
            print('MacTerminalSearch will now uninstall. Thank you for using my app.')
            ProgramInstallation().uninstall()
            print('Removal Complete')

    # Run the program
    def launch_search(self):
        search_specs = self.site_specific_search()
        search_url = self.create_search_url(search_specs)
        # Open Browser only if settings were unchanged
        if not self.change_settings:
            webbrowser.get(self.browser_path).open(search_url)



