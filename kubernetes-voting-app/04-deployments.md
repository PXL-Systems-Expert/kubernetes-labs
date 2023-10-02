# Kubernetes exercises

Example Voting App:
https://github.com/PXL-Systems-Expert/example-voting-app.git

## Deployments

1. Delete the ReplicaSet deployed in the previous module exercise.
1. Develop the Deployment YAML file to deploy the Voting App microservices.
1. Update the vote Deployment to attach two environment variables:
   - Name the first OPTION_A; its value should be CATS.
   - Name the second OPTION_B; its value should be DOGS.
1. Update the db, result, and worker Deployment to attach three environment variables:
   - Name the first POSTGRES_NAME; its value should be "voting."
   - Name the second POSTGRES_USER; its value should be "voting."
   - Name the third POSTGRES_PASSWORD; its value should be "password."
1. Ensure each Pod is up and running.
