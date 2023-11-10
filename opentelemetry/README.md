k3d cluster create mycluster --port 80:80@loadbalancer --api-port 6443
k3d cluster create mycluster --servers 1 --agents 2 --port 80:80@loadbalancer --api-port 6443

helm install my-otel-demo open-telemetry/opentelemetry-demo

kubectl apply -f .\ingress.yaml

http://otel-demo.local.gd/
http://otel-demo.local.gd/grafana
http://otel-demo.local.gd/feature
http://otel-demo.local.gd/loadgen/
http://otel-demo.local.gd/jaeger/ui

kubectl port-forward svc/my-otel-demo-otelcol 4318:4318

k3d cluster delete mycluster