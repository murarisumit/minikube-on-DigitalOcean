import os
import logging
import sys

from jinja2 import Template
import oyaml as yaml

from . import config
from . import parser
from .provider import digitalocean
from .provider import aws

logger = logging.getLogger(__name__)

PROVIDER_MAP = {
        'digitalocean' : digitalocean.setup,
        'aws' : aws.stub,
    }

def get_user_data(template_path, kubectl_version, minikube_version):
    user_data_file = open(template_path, 'r')
    user_data = "#cloud-config\n\n"

    cloud_config = {}
    cloud_config['runcmd'] = []
    for line in user_data_file:
        cloud_config['runcmd'].append(line)

    user_data += yaml.dump(cloud_config, default_flow_style=False)
    return Template(user_data).render(
            kubectl_version=kubectl_version,
            minikube_version=minikube_version
            )

def setup_logging(verbose):
    if verbose:
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    else:
        FORMAT = '%(message)s'
        logging.basicConfig(
                stream=sys.stdout,
                level=logging.INFO,
                format=FORMAT
            )

def main():
    args = parser.get_argparser()
    user_cfg, credentials = config.get_config(args.profile)

    setup_logging(args.verbose)

    base_path = os.path.dirname(__file__)
    base_template_path = os.path.join(base_path, 'templates')
    template_path = os.path.join(base_template_path, 'ubuntu.j2')

    user_data = get_user_data(
        template_path,
        user_cfg['kubectl_version'],
        user_cfg['minikube_version'],
        )
    provider = PROVIDER_MAP[args.cloud]
    provider(user_cfg, credentials, user_data)


if __name__ == "__main__":
    main()
