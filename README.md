# DevOps with Kubernetes 2026 (MOOC.fi)

Este repositorio contiene las soluciones y proyectos del curso **[DevOps with Kubernetes 2026](https://devopswithkubernetes.com/)** impartido por la **Universidad de Helsinki (MOOC.fi)**.

- **Estudiante / Usuario de GitHub:** [@drfonsecab](https://github.com/drfonsecab)
- **Repositorio:** [devops-with-kubernetes-2026](https://github.com/drfonsecab/devops-with-kubernetes-2026)
- **Visibilidad:** Público (acceso directo para el evaluador @mattiluukkainen).

---

## 📁 Estructura del Repositorio

El repositorio sigue un esquema modular donde cada aplicación o componente se desarrolla en su propio directorio independiente:

`	ext
.
├── .gitignore
├── README.md                      # Índice maestro de ejercicios y entregas
├── log_output/                    # Aplicación 'Log Output' (generador/lector de hashes)
│   ├── manifests/                 # Manifiestos de Kubernetes (Deployment, Service, etc.)
│   ├── src/                       # Código fuente de la aplicación
│   ├── Dockerfile
│   └── README.md                  # Instrucciones para ejecutar y probar la aplicación
├── todo_app/                      # Aplicación principal del curso 'Todo App' (Project)
│   ├── manifests/
│   ├── src/
│   ├── Dockerfile
│   └── README.md
└── ping_pong/                     # Aplicación 'Ping-Pong' (contador de solicitudes)
    ├── manifests/
    ├── src/
    ├── Dockerfile
    └── README.md
`

> **Nota:** Cada carpeta de aplicación contiene su propio README.md con las instrucciones específicas para construir la imagen Docker, desplegar los manifiestos en el clúster (k3d/GKE) y verificar su funcionamiento.

---

## ⚡ Regla Crítica de Entregas y Enlaces

> ⚠️ **IMPORTANTE (Regla de evaluación del MOOC):**
> Los enlaces a los ejercicios completados en este README.md **NO** deben apuntar a la rama main, sino directamente a la carpeta de la aplicación dentro del **GitHub Release / Tag** correspondiente al ejercicio.
>
> **Formato requerido:**
> https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/<tag>/<directorio-de-la-app>
>
> *Ejemplo:* https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/1.1/log_output

---

## 🔁 Flujo de Trabajo por Ejercicio

Cada vez que se complete un ejercicio:

1. **Desarrollar y probar:** Realizar los cambios de código y/o manifiestos en la carpeta de la aplicación correspondiente (ej. /log_output).
2. **Commit y Push:** Confirmar los cambios y subirlos a la rama principal:
   `ash
   git add .
   git commit -m "feat(1.1): complete exercise 1.1 log output app"
   git push origin main
   `
3. **Crear GitHub Release / Tag:** Generar un Release con el tag coincidiendo exactamente con el número de ejercicio (ej. 1.1):
   - Con GitHub CLI:
     `ash
     gh release create 1.1 --title "1.1" --notes "Solución para el ejercicio 1.1"
     `
   - O vía web en GitHub en la sección **Releases -> Draft a new release** (Tag: 1.1, Title: 1.1).
4. **Actualizar el índice:** Editar este README.md raíz enlazando el ejercicio al tag recién creado:
   `markdown
   | 1.1 | Getting started | /log_output | [Ver entrega (Tag 1.1)](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/1.1/log_output) | ✅ Completado |
   `
5. **Commit y Push final del README:**
   `ash
   git add README.md
   git commit -m "docs: link exercise 1.1 in README"
   git push origin main
   `

---

## 📚 Índice de Ejercicios por Capítulo

### Chapter 2: Kubernetes basics

| Ejercicio | Descripción / Tema | Aplicación | Enlace a Release / Tag | Estado |
| :---: | :--- | :--- | :--- | :---: |
| **1.1** | First deploy (Log Output) | /log_output | [Solución (Tag 1.1)](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/1.1/log_output) | ✅ Completado |
| **1.2** | Project v0.1 (Todo App) | /todo_app | [Solución (Tag 1.2)](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/1.2/todo_app) | ✅ Completado |
| **1.3** | Declarative approach | /log_output | [Solución (Tag 1.3)](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/1.3/log_output) | ✅ Completado |
| **1.4** | Project v0.2 | /todo_app | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/1.4/todo_app) | ⏳ Pendiente |
| **1.5** | Project v0.3 | /todo_app | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/1.5/todo_app) | ⏳ Pendiente |
| **1.6** | Project v0.4 | /todo_app | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/1.6/todo_app) | ⏳ Pendiente |
| **1.7** | External access with Ingress | /log_output | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/1.7/log_output) | ⏳ Pendiente |
| **1.8** | Project v0.5 | /todo_app | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/1.8/todo_app) | ⏳ Pendiente |
| **1.9** | More services (Ping-Pong) | /ping_pong | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/1.9/ping_pong) | ⏳ Pendiente |
| **1.10** | Split log output | /log_output | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/1.10/log_output) | ⏳ Pendiente |
| **1.11** | Persisting data / Volumes | /log_output | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/1.11/log_output) | ⏳ Pendiente |
| **1.12** | Project v0.6 | /todo_app | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/1.12/todo_app) | ⏳ Pendiente |
| **1.13** | Project v0.7 | /todo_app | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/1.13/todo_app) | ⏳ Pendiente |

---

### Chapter 3: More building blocks

| Ejercicio | Descripción / Tema | Aplicación | Enlace a Release / Tag | Estado |
| :---: | :--- | :--- | :--- | :---: |
| **2.1** | Connecting pods | /log_output & /ping_pong | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/2.1/log_output) | ⏳ Pendiente |
| **2.2** | Project v0.8 | /todo_app | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/2.2/todo_app) | ⏳ Pendiente |
| **2.3** | Routing with Ingress | /log_output & /ping_pong | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/2.3/log_output) | ⏳ Pendiente |
| **2.4** | Project v0.9 | /todo_app | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/2.4/todo_app) | ⏳ Pendiente |
| **2.5** | Documentation & setup | Documentación | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/2.5/) | ⏳ Pendiente |
| **2.6** | State storage / ConfigMaps | /log_output | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/2.6/log_output) | ⏳ Pendiente |
| **2.7** | Stateful applications / PostgreSQL | /ping_pong | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/2.7/ping_pong) | ⏳ Pendiente |
| **2.8** | Project v1.0 | /todo_app | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/2.8/todo_app) | ⏳ Pendiente |
| **2.9** | Daily reminder / CronJob | /todo_app | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/2.9/todo_app) | ⏳ Pendiente |
| **2.10** | Project v1.1 | /todo_app | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/2.10/todo_app) | ⏳ Pendiente |

---

### Chapter 4: To the cloud

| Ejercicio | Descripción / Tema | Aplicación | Enlace a Release / Tag | Estado |
| :---: | :--- | :--- | :--- | :---: |
| **3.1** | Cloud deployment (GKE) | /log_output & /ping_pong | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/3.1/log_output) | ⏳ Pendiente |
| **3.2** | Automated deployment for project | /todo_app | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/3.2/todo_app) | ⏳ Pendiente |
| **3.3** | Dynamic environments (Branch namespaces) | Manifiestos / CI | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/3.3/) | ⏳ Pendiente |
| **3.4** | Automated cleanup of namespaces | CI/CD | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/3.4/) | ⏳ Pendiente |
| **3.5** | DBaaS vs DIY Comparison | Documentación | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/3.5/) | ⏳ Pendiente |
| **3.6** | Resource limits & requests | /log_output / /todo_app | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/3.6/todo_app) | ⏳ Pendiente |
| **3.7** | Cloud PVC persistence | /todo_app | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/3.7/todo_app) | ⏳ Pendiente |
| **3.8** | Horizontal Pod Autoscaler (HPA) | /todo_app | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/3.8/todo_app) | ⏳ Pendiente |
| **3.9** | Resource optimization | Manifiestos | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/3.9/) | ⏳ Pendiente |
| **3.10** | Project v1.2 | /todo_app | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/3.10/todo_app) | ⏳ Pendiente |

---

### Chapter 5: GitOps and friends

| Ejercicio | Descripción / Tema | Aplicación | Enlace a Release / Tag | Estado |
| :---: | :--- | :--- | :--- | :---: |
| **4.1** | Readiness & Liveness probes | /log_output & /ping_pong | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/4.1/log_output) | ⏳ Pendiente |
| **4.2** | Project health checks | /todo_app | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/4.2/todo_app) | ⏳ Pendiente |
| **4.3** | Prometheus & monitoring | Monitoreo | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/4.3/) | ⏳ Pendiente |
| **4.4** | Progressive delivery (Canary) | /todo_app | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/4.4/todo_app) | ⏳ Pendiente |
| **4.5** | Project v1.3 | /todo_app | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/4.5/todo_app) | ⏳ Pendiente |
| **4.6** | Event-driven architecture (NATS) | Microservicios | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/4.6/) | ⏳ Pendiente |
| **4.7** | GitOps with Flux / ArgoCD | GitOps | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/4.7/) | ⏳ Pendiente |
| **4.8** | Project v2.0 (Full GitOps) | /todo_app | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/4.8/todo_app) | ⏳ Pendiente |

---

### Chapter 6: Under the hood

| Ejercicio | Descripción / Tema | Aplicación | Enlace a Release / Tag | Estado |
| :---: | :--- | :--- | :--- | :---: |
| **5.1** | Rollout strategies | Manifiestos | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/5.1/) | ⏳ Pendiente |
| **5.2** | Project v2.1 | /todo_app | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/5.2/todo_app) | ⏳ Pendiente |
| **5.3** | Service mesh | Malla de servicios | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/5.3/) | ⏳ Pendiente |
| **5.4** | Project v2.2 | /todo_app | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/5.4/todo_app) | ⏳ Pendiente |
| **5.5** | Custom Resource Definitions (CRDs) | Controladores / CRD | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/5.5/) | ⏳ Pendiente |
| **5.6** | Project v2.3 | /todo_app | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/5.6/todo_app) | ⏳ Pendiente |
| **5.7** | Kubernetes Network Policies | Seguridad | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/5.7/) | ⏳ Pendiente |
| **5.8** | Project final submission | General | [Pendiente](https://github.com/drfonsecab/devops-with-kubernetes-2026/tree/5.8/) | ⏳ Pendiente |