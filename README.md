# 📊 BI Platform – Sales Analytics Dashboard

A full-stack Business Intelligence (BI) platform built using Django REST Framework and React to visualize sales data.

This project provides a backend API to serve aggregated sales data and a frontend dashboard to display the data using charts.

---

## 🚀 Tech Stack

Backend:
- Python 3.x
- Django
- Django REST Framework
- SQLite (default database)

Frontend:
- React
- Axios
- Chart.js
- React-Chartjs-2

---

## 📁 Project Structure

bi_platform/
│
├── db.sqlite3
├── manage.py
├── requirements.txt
│
├── bi_platform/          # Django project settings
│
├── api/                  # Django app (API layer)
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│
└── README.md

Frontend (separate folder):
dashboard/
│
├── package.json
├── src/
│   ├── App.js
│   └── ...
│
└── node_modules/

---

# ⚙️ Backend Setup (Django)

## 1️⃣ Create Virtual Environment (Recommended)

python -m venv venv

Activate:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

---

## 2️⃣ Install Dependencies

pip install -r requirements.txt

If installing manually:

pip install django djangorestframework

---

## 3️⃣ Run Migrations

python manage.py migrate

---

## 4️⃣ Run Django Server

python manage.py runserver

Backend will run at:

http://127.0.0.1:8000/

API Endpoint Example:

http://127.0.0.1:8000/api/sales/

---

# ⚛️ Frontend Setup (React Dashboard)

## 1️⃣ Install Node.js

Download from:
https://nodejs.org

---

## 2️⃣ Create React App

npx create-react-app dashboard
cd dashboard

---

## 3️⃣ Install Required Libraries

npm install axios chart.js react-chartjs-2

---

## 4️⃣ Replace src/App.js with:

import { useEffect, useState } from "react";
import axios from "axios";
import { Bar } from "react-chartjs-2";

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/sales/")
      .then(res => setData(res.data));
  }, []);

  const chartData = {
    labels: data.map(d => d.product__name),
    datasets: [{ 
      label: "Sales", 
      data: data.map(d => d.total_sales) 
    }]
  };

  return <Bar data={chartData} />;
}

export default App;

---

## 5️⃣ Run React App

npm start

Frontend will run at:

http://localhost:3000/

---

# 📊 How It Works

1. Django backend exposes a REST API.
2. The API returns aggregated sales data.
3. React frontend fetches data using Axios.
4. Chart.js displays the data in a bar chart.
5. Dashboard updates dynamically from API.

---

# 🎯 Features

- RESTful API for sales analytics
- Data aggregation using Django ORM
- React-based interactive dashboard
- Real-time chart visualization
- Clean backend–frontend separation

---

# 📌 Future Improvements

- Add authentication (JWT)
- Add filters (date range, category)
- Add multiple chart types
- Deploy using Docker
- Use PostgreSQL instead of SQLite

---

# 👩‍💻 Author

Sudeepthi Rao  
Full Stack & Data Analytics Enthusiast
