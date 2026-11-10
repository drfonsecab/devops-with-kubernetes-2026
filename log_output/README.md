# Log Output Application

Aplicación de registro en tiempo real desarrollada para el curso **DevOps with Kubernetes 2026**.

## Funcionamiento
Al arrancar, genera un identificador único aleatorio (`UUIDv4`) en memoria y cada 5 segundos imprime en consola la marca de tiempo en formato ISO 8601 UTC junto al UUID:
```text
2026-11-10T12:15:17.705Z: 8523ecb1-c716-4cb6-a044-b9e83bb98e43
```

## Ejecución Local con Docker
```bash
docker build -t log-output:1.1 .
docker run --rm log-output:1.1
```

## Despliegue en Kubernetes (k3d)

### 1. Importar imagen local a k3d
```bash
k3d image import log-output:1.1 -c k3s-default
```

### 2. Despliegue declarativo (Ejercicio 1.3)
```bash
kubectl apply -f manifests/deployment.yaml
```

### 3. Verificar pods y logs
```bash
kubectl get pods -l app=log-output
kubectl logs -f -l app=log-output
```