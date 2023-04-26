import logging
from imports.config import install_folder as app_folder
import os


class Logger:

    def __init__(self, log_level, log_file_path, persistent_file_path):
        self.logger = logging.getLogger(log_file_path.name)
        self.logger.setLevel(log_level)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',
                                      datefmt='%A, %B %d, %Y | %I:%M:%S %p')

        file_handler = logging.FileHandler(str(log_file_path))
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        persistent_handler = logging.FileHandler(str(persistent_file_path))
        persistent_handler.setLevel(log_level)
        persistent_handler.setFormatter(formatter)

        self.log_file_path = str(log_file_path)
        self.persistent_path = str(persistent_file_path)

    def log_error(self, error_message):
        self.logger.error(error_message)

    def log_warning(self, warning_message):
        self.logger.warning(warning_message)

    def log_info(self, info_message):
        self.logger.info(info_message)

    def log_debug(self, debug_message):
        self.logger.debug(debug_message)

    def read_log_file_last20(self, log_file_path):
        with open(log_file_path, 'r') as log_file:
            log_records = log_file.readlines()
            last_20_lines = [x for x in log_records[-20:]]
            return ''.join(last_20_lines)

    def read_log_file(self, log_file_path, log_level=None):
        with open(log_file_path, 'r') as log_file:
            log_records = log_file.readlines()
            if log_level:
                log_records = [
                    r for r in log_records if r.startswith(log_level)]
            return ''.join(log_records)

    def clear_log(self):
        self.add_to_persistent_log()
        with open(self.log_file_path, 'r+') as file:
            file.truncate(0)

    def add_to_persistent_log(self):
        with open(self.log_file_path, 'r') as source:
            s = source.read()
            with open(self.persistent_path, 'a') as destination:
                destination.write('\n')
                destination.write(s)
                destination.write('\n')


def create_logger():
    log_path = app_folder / 'logs' / 'log.log'
    log_path_pers = app_folder / 'logs' / 'log.log'
    # Attempt to create logger, will create folders if not done already
    try:
        log_object = Logger('INFO',log_path, log_path_pers)
    except FileNotFoundError:
        os.system(f'mkdir {app_folder}/logs')
        os.system(f'mkdir {app_folder}/config')
        log_object = Logger('INFO',log_path, log_path_pers)
    return log_object


logs = create_logger()
