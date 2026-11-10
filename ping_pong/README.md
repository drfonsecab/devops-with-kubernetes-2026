# Ping-Pong Application

Aplicación auxiliar para el curso **DevOps with Kubernetes 2026**.

## Funcionamiento
Mantiene un contador en memoria que inicia en 0. Con cada solicitud `GET /pingpong`, responde con `pong <contador>` e incrementa el valor en 1.

## Despliegue en Kubernetes (k3d)
```bash
docker build -t ping-pong:1.9 .
k3d image import ping-pong:1.9 -c k3s-default
kubectl apply -f manifests/
```