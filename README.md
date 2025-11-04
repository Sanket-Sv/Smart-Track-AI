# 🚌 SmartTrack AI – Real-Time Intelligent Public Transport Tracking System  

![GitHub Repo stars](https://img.shields.io/github/stars/Sanket-Sv/Smart-Track-AI?style=flat&color=gold)
![GitHub forks](https://img.shields.io/github/forks/Sanket-Sv/Smart-Track-AI?style=flat)
![GitHub last commit](https://img.shields.io/github/last-commit/Sanket-Sv/Smart-Track-AI)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-2.3-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🧭 Overview

**SmartTrack AI** is a real-time AI-based bus tracking and management system.  
It integrates **IoT + AI** to provide live GPS tracking, ETA prediction, route optimization, and demand forecasting — making public transport **smarter, faster, and more efficient**.

---

## 🚀 Key Features

### 🧑‍🤝‍🧑 User Features
- 🗺️ **Live Bus Tracking** – Real-time bus movement on an interactive Leaflet map  
- ⏱️ **ETA Prediction** – AI predicts arrival time using traffic & route data  
- 📍 **Search Bus & Stops** – Find nearest bus and upcoming arrival  
- 🔐 **User Login & Signup** – Secure passenger authentication  

### 🧑‍💼 Admin Features
- 📊 **Admin Dashboard** – Manage buses, drivers, and routes  
- ⚙️ **Data-Driven Insights** – AI-powered route optimization  
- 📈 **Demand Forecasting & Delay Alerts** – Real-time analytics dashboard  

---

## 🧠 Tech Stack

| Layer | Technology Used |
|-------|------------------|
| **Frontend** | HTML5, CSS3, JavaScript, Leaflet.js, AOS.js |
| **Backend** | Flask (Python), Flask-CORS |
| **Database** | SQLite3 |
| **Machine Learning** | scikit-learn, pandas, numpy, joblib |
| **Deployment** | Render (Backend), Netlify (Frontend) |

---

## 📂 Project Structure

```bash
SmartTrack-AI/
├── backend/
│   ├── app.py                  # Flask backend server
│   ├── models/                 # Trained ML models
│   ├── routes/                 # Bus route data
│   ├── utils/                  # Helper modules
│   └── requirements.txt
│
├── frontend/
│   ├── index.html              # Home page
│   ├── live_map.html           # Real-time map page
│   ├── admin_dashboard.html    # Admin dashboard
│   ├── assets/
│   │   ├── css/style.css
│   │   ├── js/ (map.js, api.js, etc.)
│   │   └── images/
│
├── database/
│   ├── buses.db
│   ├── bus_live_data.csv
│   └── trip_history.csv
│
├── ml_training/
│   ├── train_eta_model.ipynb
│   ├── train_demand_model.ipynb
│   ├── data_preprocessing.py
│   └── model_evaluation.py
│
└── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Sanket-Sv/Smart-Track-AI.git
cd Smart-Track-AI
```

### 2️⃣ Backend Setup

```bash
cd backend
pip install -r requirements.txt
python app.py
```

✅ Flask API runs at:
👉 `http://127.0.0.1:5000`

### 3️⃣ Frontend Setup

```bash
cd ../frontend
python -m http.server 5500
```

✅ Frontend runs at:
👉 `http://127.0.0.1:5500/index.html`

---

## 🌍 API Endpoints

| Endpoint                 | Method | Description                |
| ------------------------ | ------ | -------------------------- |
| `/api/location/<bus_id>` | GET    | Get real-time bus location |
| `/api/eta`               | POST   | Predict ETA using ML       |
| `/api/demand_forecast`   | GET    | Predict passenger demand   |
| `/api/delay_status`      | POST   | Detect route delays        |
| `/api/optimize_route`    | POST   | Suggest optimal route      |

### 🧪 Example Request

**POST** `/api/eta`

```json
{
  "bus_id": "BUS001",
  "source": "Stop A",
  "destination": "Stop B"
}
```

**Response**

```json
{
  "bus_id": "BUS001",
  "eta_minutes": 14.7
}
```

---

## ☁️ Deployment

### 🔹 Backend Deployment (Render)

1. Go to [Render.com](https://render.com)
2. Click **New + → Web Service**
3. Connect your GitHub repo
4. Set build command:

   ```bash
   pip install -r backend/requirements.txt
   ```

   Start command:

   ```bash
   python backend/app.py
   ```
5. Save and Deploy 🚀
6. Copy the deployed API URL (e.g. `https://smarttrack-backend.onrender.com`)

---

### 🔹 Frontend Deployment (Netlify)

1. Go to [Netlify](https://netlify.com)
2. Click **New site from Git** → Select your repo
3. Build command: *(leave empty)*
4. Publish directory:

   ```
   frontend
   ```
5. Deploy!
6. Update frontend JS to use your Render API base URL.

---

## 📸 Preview (Optional)

*(Add screenshots here later)*
Example:

```markdown
![Live Bus Map Screenshot](frontend/assets/images/sample_map.png)
![Admin Dashboard Screenshot](frontend/assets/images/sample_dashboard.png)
```

---

## ✨ Author

**👨‍💻 Sanket Kumar**  
📧 [sanketsv11@gmail.com](mailto:sanketsv11@gmail.com)  
🌐 [GitHub: Sanket-Sv](https://github.com/Sanket-Sv)  
💼 [LinkedIn (optional)](https://linkedin.com/in/sanket-sv)

---

## 🧾 License

This project is licensed under the **MIT License** – feel free to use and modify it with proper credit.

---

⭐ **If you find this project helpful, please star ⭐ the repository on GitHub!**

---
