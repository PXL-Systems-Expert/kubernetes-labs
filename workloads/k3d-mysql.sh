#!/bin/bash
k3d cluster create mycluster --volume $HOME/k3d-temp:/var/lib/rancher/k3s/storage@all --api-port 6550 -p "8090:80@loadbalancer" --agents 1
