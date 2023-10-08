#!/bin/bash
k3d cluster create --api-port 6550 -p "8081:80@loadbalancer" --agents 1
