# Jenkins set-up
## port forwarding
8880 -> 80 op traefik
8443 -> 443 op traefik
800x -> nodeports 3000x op de agent nodes
volume aanpassen!

```rm -r -fo jenkins_data
mkdir jenkins_data
```

## create cluster with k3d config file
### bash
```
CLUSTER_NAME="my-ci-cluster"
k3d cluster create --config ./k3d-config.yaml
kubectl cluster-info
kubectl taint node k3d-$CLUSTER_NAME-server-0 node-role.kubernetes.io/master:NoSchedule
kubectl taint node k3d-$CLUSTER_NAME-server-1 node-role.kubernetes.io/master:NoSchedule
```
### Powershell
```
k3d cluster create --config .\k3d-config.yaml
$clustername = "my-ci-cluster"
kubectl cluster-info
kubectl taint node k3d-$clustername-server-0 node-role.kubernetes.io/master:NoSchedule
kubectl taint node k3d-$clustername-server-1 node-role.kubernetes.io/master:NoSchedule
```

## separate namespace
```
kubectl create namespace devops-tools
```

## opzetten service account
ClusterRole en ServiceAccount: jenkins-admin

permissies voor alle cluster components

```
kubectl apply -f service-account.yaml
```

## set up PV en PVC
```
kubectl create -f volume.yaml
```

## set up deployment
jenkins:latest
```
kubectl create -f deployment.yaml
```

## check status
```
kubectl get deployments --namespace devops-tools
kubectl get pods --namespace devops-tools
```

## set up service voor jenkins
## UI accessible op nodeport 30000
```
kubectl create -f service.yaml
```

## checks
```
kubectl get nodes -o wide
kubectl get services --namespace devops-tools
kubectl get pods --namespace devops-tools -o wide
```

## get jenkins passwd

### bash
```
JENKINS_POD=`kubectl get pods --namespace devops-tools -o wide -o jsonpath="{.items[0].metadata.name}"`
kubectl logs --namespace devops-tools $JENKINS_POD
```
### Powershell
```
$jenkinspod = $(kubectl get pods --namespace devops-tools -o wide | Select-String jenkins-..........-.....).Matches.Value
kubectl logs --namespace devops-tools $jenkinspod
kubectl exec -it $jenkinspod cat /var/jenkins_home/secrets/initialAdminPassword -n devops-tools
```

browse naar http://localhost:8000

## alternatief
```
kubectl port-forward service/jenkins-service 6420:8080 --namespace devops-tools
```
browse naar localhost:6420

## store Dockerhub credentials als secret
### bash
```
DOCKER_SERVER="https://index.docker.io/v1/"
DOCKER_USER="tomcoolpxl"
DOCKER_PASS="password"
DOCKER_MAIL="tom.cool@pxl.be"
kubectl create secret docker-registry dockercred --docker-server=$DOCKER_SERVER --docker-username=$DOCKER_USER --docker-password=$DOCKER_PASS --docker-email=$DOCKER_MAIL --namespace devops-tools
```

### Powershell
```
$dockerserver = 'https://index.docker.io/v1/'
$dockerusername = 'tomcoolpxl'
$dockerpassword = 'password'
$dockeremail = 'tom.cool@pxl.be'
kubectl create secret docker-registry dockercred --docker-server=$dockerserver --docker-username=$dockerusername --docker-password=$dockerpassword --docker-email=$dockeremail --namespace devops-tools
```