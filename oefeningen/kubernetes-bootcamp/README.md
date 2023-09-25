# Oefeningen

Selectie oefeningen uit Kubernetes-bootcamp:
https://kubernetes-bootcamp.wikitops.io

Voting App repo:
https://github.com/wikitops/example-voting-app

## Orchestration

1. Create a namespace called voting-app
2. Update one node with the key/value label: type=database
3. Update another node with the key/value label: type=queue
4. Ensure each nodes are correctly configured

## Pods

1. Deploy each containers of the Voting App in a single Pod called voting-app in his dedicated namespace created in the previous module.
2. Ensure the Pods are up and running
3. Check the logs of each Pods

## ReplicaSet

1. Delete the Pods created in the previous module exercise
2. Create a ReplicaSet to replicate the worker Pod to 1
3. Ensure the Pod is replicate to 1 and it is up and running
4. Scale the worker Pods to 3 in command line
5. Ensure the worker Pod is the only Pods replicate to 3 and it is up and running

## Deployments

1. Delete the ReplicaSet deployed in the previous module exercise
2. Develop the Deployment yaml file to deploy the Voting App microservices.
3. Update the vote Deployment to attach two environment variables:
   - Name the first OPTION_A, her value has to be CATS
   - Name the second OPTION_B, her value has to be DOGS
6. Update the db, result and worker Deployment to attach three environment variables:
   - Name the first POSTGRES_NAME, her value has to be "voting"
   - Name the second POSTGRES_USER, her value has to be "voting"
   - Name the third POSTGRES_PASSWORD, her value has to be "password"
7. Ensure each Pods are up and running

## Services

1. Manage the access of each part of the Voting App based on those conditions :
2. The PostgreSQL database Deployment must only be access from the Kubernetes cluster on port 5432.
3. The Redis queue Deployment must only be access from the Kubernetes cluster on port 6379.
4. The vote and result Deployment must be publicly access on port 8080.
5. The worker Pods must not be exposed.
6. Try to access the vote web site
7. Try to access the result web site

## ConfigMaps

1. Delete the vote Deployment to be able to manage the environment variable with a ConfigMaps
2. Create a ConfigMaps resource to externalize some part of the vote Pods :
3. Name the ConfigMaps vote
4. The ConfigMaps must manage those data:
   - option_a: "CATS"
   - option_b: "DOGS"
5. Update the Deployment of the vote Pods to attach the ConfigMaps as environment variables:
   - The name of the option_a environment variable has to be OPTION_A
   - The name of the option_b environment variable has to be OPTION_B

## Secrets

1. Delete the db, result and worker Deployment to be able to update the Secrets management
2. Create a Secrets resource to externalize some part of the vote Pods:
   - Named the Secrets db
   - The Secrets must manage those data:
     - name: voting
     - password: mypassword
     - user: voting
3. Update the Deployment of the vote Pods to attach the Secrets as environment variables:
   - The name of the name environment variable has to be POSTGRESQL_DATABASE
   - The name of the password environment variable has to be POSTGRESQL_PASSWORD
   - The name of the user environment variable has to be POSTGRESQL_USERNAME

## Volumes

1. On the node labelized type=database, create this directory: ~/data/votingapp/07_volumes/database/data
2. Create a PersistentVolume based on that local directory previously created. The storage capacity of this volume has to be 10Gi.
3. Create the PersistentVolumeClaim to consume the PersistentVolume previously created. Manage this object to claim only 5Gi of the PersistentVolume.
4. Attach the volume to the database Pods

## StorageClass

1. Create a StorageClass based on a cloud provider. (AWS, Azure, GCP)
2. Create a PersistentVolumeClaim to consume that StorageClass and create a storage object capacity of 10Gi.
3. Update the database Deployment to attach the previous PersistentVolumeClaim created.

## Routes

1. Expose the vote Services as an Ingress controller.
2. Expose the result Services as an Ingress controller.
3. Ensure that you accessed both services externally.
