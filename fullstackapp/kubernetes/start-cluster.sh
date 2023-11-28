#!/bin/bash

k3d cluster create mycluster --api-port 6550 -p "9090:80@loadbalancer" --agents 1
kubectl apply -f .