import json
from logs.create_logger import logs


class JsonStorage:
    def __init__(self, json_file_name):
        self.json_file = json_file_name
        self.data = self.read_json()

    def read_json(self):
        try:
            with open(self.json_file, 'r') as file:
                data = json.load(file)
                return data
        except Exception as e:
            logs.log_error(e)
            # Create file if it does not exist
            with open(self.json_file, 'w') as file:
                json.dump({}, file)
                return {}

    def add_to_json(self, key, value):
        if key in self.data:
            # raise KeyError('Key Already Exists in Dictionary')
            logs.log_warning('This will overwrite existing choices')
            logs.log_info(f'Changed {key} to {value}')
            self.data.update({key: value})
        else:
            self.data[key] = value
        with open(self.json_file, 'w') as file:
            json.dump(self.data, file, indent=4)
            logs.log_info(self.data)
            logs.log_info(f'Added {key} and {value}')

    def add_sites_to_site_list(self, key, value):
        data = self.read_json()
        try:
            # Read site list, add new site, then update JSON
            site_list = data['site_list']
            site_list[key] = value
            self.add_to_json('site_list', site_list)
        except Exception as e:
            # If site_list is empty
            logs.log_info('Site List Does Not Exist')
            logs.log_error(e)
            self.add_to_json('site_list', {key: value})

    def remove_site_from_site_list(self, site_key):
        data = self.read_json()
        try:
            site_list = data['site_list']
            del site_list[site_key]
            self.add_to_json('site_list', site_list)
        except Exception as e:
            logs.log_error(e)
            print(e)


class FirstTimeAppStart:

    def __init__(self, json_filename='settings.json'):
        self.json_filename = json_filename
        self.browser_selection = None
        # Try to read browser choice from JsonStorage
        # if none exists, one will be added

    def start(self):
        # Try to read browser choice from JsonStorage
        # if none exists, one will be added

        try:
            browser_choice = JsonStorage(self.json_filename).read_json()[
                'browser_choice']
            logs.log_info(f"Browser Selected: {browser_choice}")
        except Exception as e:
            logs.log_error(e)
            browser_choice = None

            self.browser_selection = browser_choice
            select = self.get_user_input_browser()
            self.select_your_browser(select)

        self.site_setup()

    def get_user_input_browser(self):

        text = 'Please Select a Browser of your choice using the numbers:'
        browser_text = '\n1 = Chrome\n2 = Firefox\n3 = Opera GX\n4 = Safari'
        selection = None
        print(text + browser_text)

        invalid_input_warning = 'Invalid Option Selected'
        while True:
            try:
                selection = int(input())
            except ValueError:
                print(invalid_input_warning)
                continue
            else:
                if selection in [1, 2, 3, 4]:
                    break
                else:
                    print(invalid_input_warning)
        # Return used for testing
        return selection

    def select_your_browser(self, selection_from_input):

        browsers = {
            '1': 'chrome',
            '2': 'firefox',
            '3': 'gx',
            '4': 'safari'
        }

        self.browser_selection = browsers[str(selection_from_input)]
        JsonStorage(self.json_filename).add_to_json(
            'browser_choice', self.browser_selection)

        # The return will only be used for tests
        return self.browser_selection

    def does_site_list_exist(self):
        try:
            site_list = JsonStorage(self.json_filename).read_json()[
                'site_list']
            logs.log_info(f"Sites Selected: {site_list}")
            return site_list
        except Exception as e:
            logs.log_error(e)
            return None

    def site_setup(self):
        sites = self.does_site_list_exist()

        if not sites:
            print('Input the websites that you would like to use for default search.')
            print('Example: "stackoverflow.com" then enter')
            print('Add as many as you want, then type \'x\' then enter to proceed.')

            while True:
                # Collect input and break if 'X'
                website_from_user = input()
                if website_from_user in ['x', 'X', '', ' ']:
                    print('Setup Complete. Command now usable instantly.')
                    break

                website_key = website_from_user.split('.')[0]
                # logs.log_info(website_from_user_list)
                JsonStorage(self.json_filename).add_sites_to_site_list(website_key,
                                                                       website_from_user)
