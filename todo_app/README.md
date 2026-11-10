# Todo App - Course Project

Aplicación principal del curso (Project) desarrollada para **DevOps with Kubernetes 2026**.

## Funcionamiento
Servidor HTTP ligero en Python que escucha en el puerto definido por la variable de entorno `PORT` (por defecto `3000`).
Al inicializarse, muestra exactamente en consola:
```text
Server started in port 3000
```

## Ejecución con Docker
```bash
docker build -t todo-app:1.2 .
docker run -p 3000:3000 --rm todo-app:1.2
```

## Despliegue en Kubernetes (k3d)
```bash
# Importar imagen al clúster k3d
k3d image import todo-app:1.2 -c k3s-default

# Despliegue imperativo (Ejercicio 1.2)
kubectl create deployment todo-app-dep --image=todo-app:1.2

# Verificar logs
kubectl logs -l app=todo-app-dep
```