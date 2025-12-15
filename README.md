

🌾 Overview

Krishi Mitra is a **Smart Agricultural Assistance System** designed to empower farmers with scientific decisions about crop cultivationand expected yield(llm), soil health, weather, market trends, and government schemes.
The platform integrates **Firebase**, **Location-based APIs**, **OpenWeather**, and **Google Maps** for a complete real-time solution.

---

### 💡 Key Features

✔ **User Authentication** – Secure login using Firebase Auth
✔ **Soil Health Analysis**

* Upload soil test report
* Automatic parsing of NPK, pH, moisture
* AI-based recommendations (trained llm model for crop suggestion with expected yieid)
* PDF Report generation
* Cloud storage — View history and trends
  ✔ **Satellite-based Irrigation Support** (optional)
  ✔ **Real-time 7-day Moisture & Rain Forecast**
  ✔ **Nearby Fertilizer Dealer Finder using Geo-location**
  ✔ **Market Price Finder (based on location)**
  ✔ **Government Schemes & Local Officer Info**
  ✔ **Crop Recommendation Model**
  ✔ **Multiple Language Support (English + Malayalam)**
  ✔ **Responsive UI — Mobile + Desktop**

---

### 🧩 Technology Stack

| Category           | Tools / Platforms                               |
| ------------------ | ----------------------------------------------- |
| Frontend           | HTML, CSS, JavaScript, TailwindCSS              |
| Backend / Database | Firebase Authentication & Firestore             |
| APIs Integrated    | OpenWeather API, Google Maps API, Overpass API  |
| File Parsing       | jsPDF (text extraction), Browser parsing        |
| Deployment         | Works on any static hosting or Firebase Hosting |

---

### 📁 Project Structure

```
Krishi_Mitra_App/
├── index.html                  <-- Landing Page / Entry Point
├── register.html               <-- User Sign Up Page
├── login.html                  <-- User Login Page
│
├── dashboard/
│   ├── index.html     <-- Central hub after successful login
│
├── features/
│   ├── testing.html      <-- "know your soil" feature
│   ├── newcalendar.html  <-- "New Calendar" feature
│   ├── news.html         <-- "News" feature
│   ├── krishi.html       <-- real time query support chat system
│      
│
└── ai_advisor/
    └── ai_advisor.html         <-- The LLM AI Advisor Page 
```

---

### 🚀 How to Run the Project

#### Option 1️⃣ — Run Locally on Your System

1️⃣ Download/Clone the entire project folder
2️⃣ Open **index.html** in any browser (Chrome recommended)
3️⃣ Allow **Location Access** for live features:

* Current weather & forecasts
* Market prices
* Fertilizer shop locator
  4️⃣ Login using your Firebase credentials
  5️⃣ Explore portal sections:
* Know Your Soil
* Crop Suggestions
* Govt. Schemes
* Daily Advisory
  ✔ Everything runs directly in browser — **No server required**

---

#### Option 2️⃣ — Host Online Using Firebase Hosting

1️⃣ Install Firebase CLI

```sh
npm install -g firebase-tools
```

2️⃣ Login to Firebase

```sh
firebase login
```

3️⃣ Initialize Firebase App

```sh
firebase init hosting
```

➡ Select the project → Set `public` as your build folder
4️⃣ Deploy

```sh
firebase deploy
```


---

### 🔑 API Keys Required

| Service             | Purpose                      | Where to put it                     |
| ------------------- | ---------------------------- | ----------------------------------- |
| Firebase            | Auth + Cloud DB              | In Firebase config in HTML pages    |
| Google Maps API Key | Lab locator                  | `<script>` tag in map-related pages |
| OpenWeather Key     | Moisture & rainfall forecast | In soil.js / weather fetch script   |

👉 Make sure API keys are enabled and unrestricted for required services.

---

### 🔐 Authentication Notes

➡ User login required for:
✔ Saving soil reports to Firestore
✔ Viewing historical trends

➡ Browsing general features can work **without login**

---

 🧪 Test Credentials (for judges)

```
User: 9368970354
Password: sachan12345
```

---

🏆 Why Krishi Mitra? 

* Solves real farmer problems with data-driven decisions
* Cloud-enabled — Farmers can track soil health over time
* Multi-language & location-based personalization
* Expandable with ML crop insights & satellite irrigation
* Practical, scalable & impactful innovation 🎯

---

 👨‍💻 Developed By

**Team — inoveda**
Guided by agricultural experts & modern technology

---

 I  also provide:
📌 **Project PPT**
📌 **Demo video script**
youtube link- https://youtu.be/nwVFI13abBk




