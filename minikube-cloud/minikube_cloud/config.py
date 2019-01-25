import configparser
import logging
import os
import sys

from pprint import pprint

logger = logging.getLogger(__name__)

def get_config(profile):
    '''
    Read the config for droplet.
    Default config location is: ~/.config/minikube-cloud/config.
    Default creds location  is: ~/.config/minikube-cloud/credentials.
    Custom config file location can be set by DOCTL_CONFIG environment variable.

    return: config and credentials
    '''
    home_dir = os.getenv('HOME')
    config = credentials = configparser.ConfigParser()

    config.read(os.path.join(home_dir, ".config", "minikube-cloud", "config.ini"))
    credentials.read(os.path.join(home_dir, ".config", "minikube-cloud", "credentials.ini"))
    # If no profile set read from default profile

    if profile not in config:
        logger.error("Profile " + profile + " is not present for config")
        logger.error("Set profile in ~/.config/minikube-cloud/config")
        sys.exit(1)
        return ""

    if profile not in credentials:
        logger.error("Profile " + profile + " is not present for credentials")
        logger.error("Set profile in ~/.config/minikube-cloud/credentials")
        sys.exit(1)
        return ""

    return config[profile], credentials[profile]


