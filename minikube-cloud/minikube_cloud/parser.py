import argparse
import logging

from . import main
from . import version

logger = logging.getLogger(__name__)

def get_argparser():
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description='Utility to setup minikube in cloud')

    parser.add_argument(
            '-p', '--profile',
            type=str,
            default="default",
            help="minikube-cloud profile name"
        )

    parser.add_argument(
            '-n',
            '--name',
            type=str,
            help="name of the vm"
        )

    parser.add_argument(
            '-c',
            type=str,
            dest='cloud',
            choices=main.PROVIDER_MAP.keys(),
            help="name of the cloud provider"
        )

    parser.add_argument(
            '-v',
            '--verbose',
            type=str,
            help="Set verbosity on for "
        )

    parser.add_argument(
            '-V',
            '--version',
            action='version',
            version="%(prog)s " + version.__version__
        )

    args = parser.parse_args()
    logger.debug('Profile is : %s', args.profile)
    logger.debug('Name is : %s', args.name)

    return args
