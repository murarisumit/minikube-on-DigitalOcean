import configparser
import logging
import os
import sys

from pprint import pprint

logger = logging.getLogger(__name__)

def get_configs_path():
    '''
    Get the config files path

    Reads if MINIKUBE_CLOUD_CONFIG environment variable to set to get configs directory

    Default config location is: $HOME/.config/minikube-cloud/config.ini.
    Default creds location  is: $HOME/.config/minikube-cloud/credentials.ini.
    '''
    if 'MINIKUBE_CLOUD_CONFIG' in os.environ:
        config_dir = os.environ['MINIKUBE_CLOUD_CONFIG']
    else:
        home_dir = os.getenv('HOME')
        config_dir = os.path.join(home_dir, '.config', 'minikube-cloud')

    config_file = os.path.join(config_dir, 'config.ini')
    credential_file = os.path.join(config_dir, 'credentials.ini')
    return config_file, credential_file


def get_config(profile):
    '''
    Read the config for droplet.
    Default config location is: $HOME/.config/minikube-cloud/config.
    Default creds location  is: $HOME/.config/minikube-cloud/credentials.

    Return: config and credentials for given profile
    '''
    config_file, creds_file = get_configs_path()
    home_dir = os.getenv('HOME')
    config = credentials = configparser.ConfigParser()

    config.read(config_file)
    credentials.read(creds_file)

    if profile not in config:
        logger.fatal("Profile " + profile + " is not present for config")
        sys.exit(1)
        return ""

    if profile not in credentials:
        logger.fatal("Profile " + profile + " is not present for credentials")
        sys.exit(1)
        return ""

    return config[profile], credentials[profile]
