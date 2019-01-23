import configparser
import logging
import os
import sys

from pprint import pprint

logger = logging.getLogger(__name__)

def get_config(profile='default'):
    '''
    Read the config for droplet.
    Default location would be ~/.config/cloud-minikube/config.
    Custom config file location can be set by DOCTL_CONFIG environment variable.
    '''
    home_dir = os.getenv('HOME')
    config = configparser.ConfigParser()
    config.read(os.path.join(home_dir, ".config", "cloud-minikube", "config.ini"))
    # If no profile set read from default profile

    if profile not in config:
        logger.error("Profile " + profile + " is not present")
        logger.info("Set profile in ~/.config/cloud-minikube/config")
        sys.exit(1)
        return ""
    else:
        return config[profile]



