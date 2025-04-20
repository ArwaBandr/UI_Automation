# SDAIA UI Test Automation – Search Functionality

This project provides automated UI testing for the [SDAIA](https://sdaia.gov.sa/en/default.aspx#) website’s search functionality using **Behave**, **Playwright**, and **Docker**, with scheduled execution via **Kubernetes CronJob** on **Minikube**.

---

## Features Covered

- Valid search with results
- Invalid search with no results
- Suspicious search input (e.g., symbols)
- Edge cases:
  - Long input
  - One-character input
  - Whitespace-only input

---

## Project Structure

```
UI_Automation/
│
├── features/
│   ├── search.feature
│   └── steps/
│       └── search.py
├── pages/
│   └── search_page.py
├── config.py
├── requirements.txt
├── Dockerfile
├── cronjob.yaml
└── README.md
```

---

## How to Run the Project Locally

This test suite is built with **Python**, **Behave**, and **Playwright**.  
Follow the steps below to run it locally on your machine:

### 1. Clone the project
```bash
git clone https://github.com/ArwaBandr/UI_Automation.git
cd UI_Automation
```

### 2. Create and activate a virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Playwright browsers
```bash
python -m playwright install
```

### 5. Run the tests
```bash
behave
```

---

## Run Using Docker

### 1. Build the Docker image
```bash
docker build -t my-behave-image .
```

### 2. Run the test suite inside a container
```bash
docker run my-behave-image
```

---

## Kubernetes CronJob (Minikube)

### 1. Start Minikube
```bash
minikube start
```

### 2. Load the Docker image into Minikube
```bash
minikube image load my-behave-image
```

### 3. Apply the CronJob definition
```bash
kubectl apply -f cronjob.yaml
```


### 4. View running pods
```bash
kubectl get pods
```


---

## Cron Schedule

This CronJob is scheduled to run **every hour**:
```
0 * * * *
```

---

## Author

Created by **Arwa**  
Tested using: Python, Behave, Playwright, Docker, Kubernetes (Minikube)