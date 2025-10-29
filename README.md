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