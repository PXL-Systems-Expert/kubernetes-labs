# Kubernetes exercises

Example Voting App:
https://github.com/PXL-Systems-Expert/example-voting-app.git

## Volumes

1. On the node labeled type=database, create this directory: ~/data/votingapp/07_volumes/database/data.
1. Create a PersistentVolume using the local directory created previously. The storage capacity for this volume should be 10Gi.
1. Create a PersistentVolumeClaim to utilize the PersistentVolume created earlier. Configure this object to claim only 5Gi of the PersistentVolume.
1. Attach the volume to the database Pods.
