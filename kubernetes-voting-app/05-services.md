# Kubernetes exercises

Example Voting App:
https://github.com/PXL-Systems-Expert/example-voting-app.git

## Services

1. Manage the access for each component of the Voting App based on the following conditions:
  - The PostgreSQL database Deployment should only be accessible from within the Kubernetes cluster on port 5432.
  - The Redis queue Deployment should only be accessible from within the Kubernetes cluster on port 6379.
  - The vote and result Deployments should be publicly accessible on port 8080.
  - The worker Pods should not be exposed.
1. Attempt to access the vote website.
1. Attempt to access the result website.
