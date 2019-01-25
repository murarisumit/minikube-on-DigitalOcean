DROPLET_NAME=sumit

istio:
	echo $(DO_SSH_ID)
	./minikube.sh $(DROPLET_NAME) $(DO_SSH_ID)

ls:
	doctl compute droplet ls

copy-config:
	mv -f kubeconfig ~/.kube/istio-kubeconfig/config

delete:
	doctl compute droplet delete $(DROPLET_NAME)
