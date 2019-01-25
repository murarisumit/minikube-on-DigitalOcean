import logging

import digitalocean

logger = logging.getLogger(__name__)

def setup_vm(config, credentials, user_data):
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

def test(input):
    logger.info("Able to spin-up vms in digitalocean")
