import os
import logging
import sys
import time

import digitalocean
from jinja2 import Template
import oyaml as yaml

import config

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

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

def create_vm(config, user_data):

    TOKEN = os.environ.get('DOTOKEN')
    droplet = digitalocean.Droplet(
            token=TOKEN,
            name=config['name'],
            region=config['region'], # Amster
            image=config['image'], # Ubuntu 16.04 x64
            size_slug=config['size'],  # 4GB
            # ssh_keys=[config['ssh_id']], #Automatic conversion
            ssh_keys=[22432270], #Automatic conversion
            user_data= user_data,
            backups=False
        )

    droplet.create()
    actions = droplet.get_actions()
    for action in actions:
        action.load()
        # Once it shows complete, droplet is up and running
        state =  action.status
        print (state)

    while True:
        if state == 'completed':
            print ("Droplet is active")
            print (state)
            break
        print ("Waiting for 2 sec. Dropet not ready yet.")
        time.sleep(2)
        actions = droplet.get_actions()
        for action in actions:
            action.load()
            # Once it shows complete, droplet is up and running
            state =  action.status

def main():
    base_path = sys.path[0]
    base_template_path = os.path.join(base_path, 'templates')
    template_path = os.path.join(base_template_path, 'ubuntu.j2')

    user_cfg = config.get_config()

    user_data = get_user_data(
        template_path,
        user_cfg['kubectl_version'],
        user_cfg['minikube_version'],
        )

    # create_vm(user_cfg, user_data)


if __name__ == "__main__":
    main()
