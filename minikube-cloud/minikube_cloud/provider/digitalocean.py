import logging
import time
import sys

import digitalocean

logger = logging.getLogger(__name__)

def setup(config, credentials, user_data):
    droplet = digitalocean.Droplet(
            token=credentials['token'],
            name=config['name'],
            region=config['region'], # Amster
            image=config['image'], # Ubuntu 16.04 x64
            size_slug=config['size'],  # 4GB
            ssh_keys=[int(config['ssh_id'])], #Automatic conversion
            user_data= user_data,
            backups=False
        )
    try:
        droplet.create()
    except digitalocean.DataReadError as err:
        logger.info("Droplet creation failed.")
        logger.fatal("Error : %s", err)
        sys.exit(1)

    actions = droplet.get_actions()
    for action in actions:
        action.load()
        # Once it shows complete, droplet is up and running
        state =  action.status
        print (state)

    while True:
        if state == 'completed':
            logger.info("Droplet is active")
            break
        logger.info("Waiting for 2 sec. Droplet not ready yet.")
        time.sleep(2)
        actions = droplet.get_actions()
        for action in actions:
            action.load()
            # Once it shows complete, droplet is up and running
            state =  action.status
    logger.info("Droplet id is: %s", droplet.id)

    logger.info("Wating for 20 seconds for host to be up")
    time.sleep(20)
    # Todo: Need to find a better way to know,
    # when load will return ip address instead of 20 second sleep
    load = droplet.load()
    ndroplet = digitalocean.Droplet(load.id, credentials['token'])
    logger.info("ip address for vm is: %s", load.ip_address)
    logger.info("For ssh: ssh root@%s", load.ip_address)
    logger.info("Use: scp root@%s:~/.kube/config config", load.ip_address)


def test(config, credentials, user_data):
    logger.info("Able to spin-up vms in digitalocean")
