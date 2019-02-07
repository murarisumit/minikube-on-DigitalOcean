# minikube-on-DigitalOcean

### Pre-req 

- Install `doctl`

```
cd ~
wget https://github.com/digitalocean/doctl/releases/download/v1.12.2/doctl-1.12.2-linux-amd64.tar.gz
tar xf ~/doctl-1.12.2-linux-amd64.tar.gz
sudo mv ~/doctl /usr/local/bin
```

- Initialize your `doctl`.

```
doctl auth init
```

- You will be prompted to enter the DigitalOcean access token that you generated in the DigitalOcean control panel.

```
DigitalOcean access token: your_DO_token
```
After entering your token, you will receive confirmation that the credentials were accepted. If the token doesn't validate, make sure you copied and pasted it correctly.

```
Validating token: OK
```

This will create the necessary directory structure and configuration file to store your credentials.

### Installation

```
python setup.py install
```

or

```
pip install minikube-cloud
```

Move config and credentials file at `~/.config/minikube-cloud/config.ini` and `~/.config/minikube-cloud/credentials.ini`

Run `minikube-cloud` with specific profile:

```
minikube-cloud --profile prod
```

- Start using kubernetes.

* Wait for instance to provision, then ssh into instance and get kubeconfig file from `/root/.kube/config`.

- Verify the node.

```
kubectl get nodes
```
