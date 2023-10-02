# Kubernetes exercises

Example Voting App:
https://github.com/PXL-Systems-Expert/example-voting-app.git

## StorageClass

1. Create a StorageClass.
1. Create a PersistentVolumeClaim to utilize that StorageClass, setting a storage capacity of 10Gi.
1. Update the database Deployment to link the previously created PersistentVolumeClaim.
