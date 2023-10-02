# Kubernetes exercises

Example Voting App:
https://github.com/PXL-Systems-Expert/example-voting-app.git

## Secrets

1. Delete the db, result, and worker Deployments to update the Secrets management.
1. Create a Secrets resource to externalize certain configurations of the vote Pods:
   - Name the Secrets "db".
   - The Secrets should manage the following data:
     - name: voting
     - password: mypassword
     - user: voting
1. Update the Deployment of the vote Pods to link the Secrets as environment variables:
   - The name of the environment variable for "name" should be POSTGRESQL_DATABASE.
   - The name of the environment variable for "password" should be POSTGRESQL_PASSWORD.
   - The name of the environment variable for "user" should be POSTGRESQL_USERNAME.
