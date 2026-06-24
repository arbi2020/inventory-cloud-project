# 📦 Inventory Management System (Cloud Project)

A full-stack **Inventory Web Application** built with **Flask, MongoDB, Docker, and Kubernetes (Oracle Kubernetes Engine - OKE)**.

This project demonstrates containerization, orchestration, cloud deployment, and managed database integration.

---

## 🚀 Features

* 📊 Dashboard with product statistics
* 🔍 Search products by name
* 🎯 Filter products by category
* ➕ Add products (CRUD operations)
* 🗄️ MongoDB database integration
* 🐳 Docker containerized application
* ☸️ Kubernetes deployment on Oracle Cloud (OKE)
* 🌐 Public access through LoadBalancer

---

## 🏗️ Architecture

Browser → Flask Web App → MongoDB → Kubernetes Service → LoadBalancer → Internet

### Cloud Deployment

* Flask runs inside Kubernetes Pods
* MongoDB runs either:

  * Inside Kubernetes Cluster (`mongo.yaml`)
  * MongoDB Atlas (recommended)
* Kubernetes Service exposes the application through a LoadBalancer

![Project Diagram](images/project_architecture.png)

---

## 📂 Project Structure

```text
inventory-cloud-project/
│
├── app/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   └── requirements.txt
│
├── k8s/
│   ├── web.yaml
│   └── mongo.yaml
│
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Technologies Used

* Python 3
* Flask
* MongoDB
* PyMongo
* Docker
* Kubernetes (Oracle Kubernetes Engine - OKE)
* Oracle Container Registry (OCIR)
* MongoDB Atlas

---

## 🔧 Environment Variables

### Local / Kubernetes Deployment

```bash
MONGO_URI=mongodb://mongo:27017/
```

### MongoDB Atlas Deployment

```bash
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/catalogue
```

---

## 🐳 Run Locally (Docker)

### Build Docker Image

```bash
docker build -t catalogue-web:1.0 .
```

### Run Container

```bash
docker run -p 5000:5000 \
-e MONGO_URI=mongodb://mongo:27017/ \
catalogue-web:1.0
```

### Access Application

```text
http://localhost:5000
```

---

## ☸️ Kubernetes Deployment (Oracle OKE)

### 1. Push Image to OCIR

```bash
docker tag catalogue-web:1.0 \
ca-toronto-1.ocir.io/<namespace>/catalogue-web:1.0

docker push \
ca-toronto-1.ocir.io/<namespace>/catalogue-web:1.0
```

### 2. Deploy Resources

```bash
kubectl apply -f k8s/mongo.yaml
kubectl apply -f k8s/web.yaml
```

### 3. Verify Deployment

```bash
kubectl get pods
kubectl get svc
```

### 4. Get Public URL

Check the External IP:

```bash
kubectl get svc
```

Example:

```text
http://40.233.123.166/
```

---

## ☁️ MongoDB Atlas (DBaaS)

Instead of running MongoDB inside Kubernetes:

1. Create a MongoDB Atlas Cluster
2. Create a Database User
3. Configure Network Access
4. Copy the Connection String
5. Replace the environment variable

```bash
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/catalogue
```

---

## 🧠 Learning Objectives

* Docker Containerization
* Kubernetes Orchestration
* Oracle Cloud Deployment (OKE)
* MongoDB Atlas Integration
* Container Registry Management (OCIR)
* Cloud-Native Application Deployment
* Microservices Architecture Concepts

---

## ⚠️ Common Issues

### ❌ MongoDB Authentication Error

Possible causes:

* Incorrect username or password
* User not created in Atlas
* Invalid cluster URL

### ❌ Image Pull Error

Possible causes:

* Missing OCIR secret
* Incorrect image path
* Registry authentication issue

### ❌ Pod Restart Loop

Possible causes:

* Incorrect `MONGO_URI`
* MongoDB service unavailable
* Network connectivity issues

---

## 👨‍💻 Authors

* Larbi Teraoui
* Omar Aoun

---

## 📜 License

Educational Project – Cloud Computing & DevOps Training

---

## 🔗 GitHub Repository

https://github.com/arbi2020/inventory-cloud-project
