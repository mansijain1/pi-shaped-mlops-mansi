# pi-shaped-mlops-mansi


# Iris Flower Classification API (Flask + Docker)

A **production-ready machine learning API** built with **Flask**, **Scikit-learn**, and **Docker**, serving predictions for the classic *Iris Flower Dataset*.  
This project demonstrates the full pipeline: data preparation → model training → API deployment → containerization.

---

## Project Overview

### Objective
To build and deploy a **RESTful API** that serves predictions from a trained Scikit-learn model using the Iris dataset.

### Dataset
**Iris Dataset** (built-in from `scikit-learn`)

- **Samples:** 150  
- **Features:**  
  - Sepal length  
  - Sepal width  
  - Petal length  
  - Petal width  
- **Target Classes:**  
  - Setosa (0)  
  - Versicolor (1)  
  - Virginica (2)

---


##  Setup & Installation

### 1. Clone the repository
```bash
git clone git@github.com:mansijain1/pi-shaped-mlops-mansi.git
cd pi-shaped-mlops-mansi
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Training:
```bash
python model/train_model.py
```

### 5. Run API locally
```bash
python app.py
```

### 6. Test the API
```bash
curl http://127.0.0.1:5000/health
```

### 7. Prediction Request
```bash
curl -X POST http://127.0.0.1:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

## Dockerize and Run the Application

You can containerize the Flask API using **Docker** to make deployment seamless and consistent across environments.

---

### Build Docker Image
Run the following command in your project root directory (where the `Dockerfile` is located):

```bash
docker build -t iris-ml-api .
```

### Run Docker Container

Once the image is built, start a container using:

```bash
docker run -p 5000:5000 iris-ml-api
```

##  Core Concept Questions & Answers

### 1. What is the difference between model training and model deployment?
- **Model Training:**  
  This is the process of feeding data into a machine learning algorithm so it can learn patterns and relationships. The result of training is a **trained model file** that can make predictions.
- **Model Deployment:**  
  Once trained, the model is integrated into an application (like a Flask API) so it can serve real-time predictions for new data. Deployment makes the model accessible to end-users or other systems.

---

### 2. Why do we save trained models using `joblib` or `pickle`?
- Training a model can take time and computational resources.  
- By saving the model to disk using `joblib` or `pickle`, we can:
  - Avoid retraining the model every time we restart the application.
  - Quickly load the pre-trained model into memory at runtime.
- **`joblib`** is often preferred for Scikit-learn models because it efficiently handles large NumPy arrays.

---

### 3. What are the advantages of serving ML models through REST APIs?
- **Accessibility:** Models can be accessed over the web by any client (mobile apps, web apps, etc.).
- **Scalability:** REST APIs can handle multiple simultaneous requests.
- **Interoperability:** Uses standard HTTP and JSON, which are language-agnostic.
- **Reusability:** One model can serve many applications without duplication.

---

### 4. Explain the purpose of each HTTP method (`GET`, `POST`) used in your API.
- **GET:**  
  Used to retrieve information from the server.  
  Example: `/health` or `/` endpoint to check server status or view API info.
- **POST:**  
  Used to send data to the server (e.g., input features) and receive predictions in response.  
  Example: `/predict` endpoint where you send feature values for classification.

---

### 5. What is Docker, and why is containerization important for ML deployment?
- **Docker** is a platform that packages your application and all its dependencies into a **container** — a lightweight, isolated environment.  
- **Importance:**
  - Eliminates “works on my machine” issues.
  - Ensures consistent behavior across different environments.
  - Simplifies deployment and scaling.
  - Enables reproducibility for ML experiments and APIs.

---

### 6. How does Docker ensure consistency across different environments (dev, staging, production)?
- Docker containers include everything the app needs (OS libraries, Python version, dependencies).  
- Since each environment runs the **same image**, the behavior remains consistent, regardless of the host system.
- The same container image can be run locally, on cloud servers, or in Kubernetes clusters without modification.

---

### 7. What is the role of `requirements.txt` in Python projects and Docker containers?
- Lists all Python packages and their specific versions needed for the project.  
- When building a Docker image, `pip install -r requirements.txt` ensures all dependencies are installed exactly as required.  
- This guarantees **reproducibility** and **dependency management** across environments.

---

### 8. Why do we expose ports in Docker containers?
- Containers are isolated by default.  
- **Exposing a port** (e.g., `EXPOSE 5000`) tells Docker which port the application inside the container listens on.  
- When you run `docker run -p 5000:5000`, it maps the container’s internal port (5000) to your local machine’s port (5000), making the API accessible externally.

---

### 9. How would you scale your API to handle 1000 requests per second?
Possible strategies:
1. **Use a production WSGI server** like Gunicorn or uWSGI instead of Flask’s built-in server.  
2. **Horizontal scaling:** Run multiple container instances and load-balance requests using tools like **NGINX** or **Kubernetes**.  
3. **Caching:** Cache frequent or repeated predictions to reduce computation.  
4. **Asynchronous processing:** Use message queues (RabbitMQ, Celery) for heavy workloads.  
5. **Autoscaling:** Configure auto-scaling in cloud platforms (AWS ECS, Google Cloud Run, etc.).

---

### 10. What are some security considerations when deploying ML models as APIs?
- **Input Validation:** Validate and sanitize incoming data to prevent injection attacks.  
- **Authentication & Authorization:** Protect APIs with API keys, OAuth, or JWT tokens.  
- **Rate Limiting:** Prevent abuse or denial-of-service attacks by limiting requests per user.  
- **HTTPS:** Encrypt communication to protect sensitive data in transit.  
- **Model Privacy:** Avoid leaking model internals (e.g., weights, structure) through responses.  
- **Logging & Monitoring:** Keep track of API usage and unusual behavior.

