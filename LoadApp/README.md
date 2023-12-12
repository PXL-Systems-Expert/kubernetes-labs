k3d cluster create my-cluster --servers 2 --agents 2 --api-port 0.0.0.0:6443 --port 0.0.0.0:8080:80@loadbalancer --port 0.0.0.0:8443:443@loadbalancer

kubectl apply -f application/php-apache.yaml

maak een HorizontalPodAutoscaler aan

kubectl autoscale deployment php-apache --cpu-percent=50 --min=1 --max=10

check de status

kubectl get horizontalpodautoscaler
kubectl get hpa
kubectl top pod php-apache-...

run dit in eerste terminal start een tijdelijke busybox container die het endpoint blijft consumen

kubectl run -i --tty load-generator --rm --image=busybox --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://php-apache; done"

check hpa status in de 2de terminal hogere CPU load zou snel moeten duidelijk worden meer replica's worden gestart

kubectl get hpa php-apache --watch

check actual state van de deployment

kubectl get deployment php-apache

stop de load
<CTRL>+C in 2de terminal busybox terminal

check status

kubectl get hpa php-apache --watch
kubectl get deployment php-apache --watch
