# Todo App - Course Project

Aplicación principal del curso (Project) desarrollada para **DevOps with Kubernetes 2026**.

## Funcionamiento
Servidor HTTP ligero en Python que escucha en el puerto definido por la variable de entorno `PORT` (por defecto `3000`).
Al inicializarse, muestra exactamente en consola:
```text
Server started in port 3000
```

## Ejecución Local con Docker
```bash
docker build -t todo-app:1.2 .
docker run -p 3000:3000 --rm todo-app:1.2
```

## Despliegue en Kubernetes (k3d)

### 1. Importar imagen local a k3d
```bash
k3d image import todo-app:1.2 -c k3s-default
```

### 2. Despliegue declarativo (Ejercicio 1.4)
```bash
kubectl apply -f manifests/deployment.yaml
```

### 3. Verificar pods y logs
```bash
kubectl get pods -l app=todo-app
kubectl logs -f -l app=todo-app
```