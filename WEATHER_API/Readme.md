# 🌤️ Weather App

A simple and clean desktop weather application built with **Python** and **PyQt5** that fetches real-time weather data using the **OpenWeatherMap API**.

---

## 📸 Preview
<img width="221" height="263" alt="image" src="https://github.com/user-attachments/assets/5157362c-103b-458e-a370-513a022a9649" />


---

## ✨ Features

- 🔍 Search weather by city name
- 🌡️ Displays temperature in both **°C** and **°F**
- 😊 Shows a **weather emoji** based on conditions
- 📝 Displays a **weather description** (e.g., Overcast clouds)
- ⚠️ Handles errors gracefully (invalid city, network issues, bad API key, etc.)

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.10+ | Core language |
| PyQt5 | GUI framework |
| Requests | HTTP requests to the API |
| OpenWeatherMap API | Weather data source |

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.10+ installed, then install the required libraries:

```bash
pip install PyQt5 requests
```

### API Key Setup

1. Go to [https://openweathermap.org/](https://openweathermap.org/) and create a free account.
2. Navigate to **API Keys** in your profile and copy your key.
3. Replace the `api_key` value in `weather_app.py`:

```python
api_key = "your_api_key_here"
```

### Run the App

```bash
python weather_app.py
```

---

## 🗂️ Project Structure

```
weather-app/
│
├── weather_app.py        # Main application file
└── README.md             # Project documentation
```

---

## 🌦️ Weather Emoji Guide

| Condition | Emoji |
|---|---|
| Thunderstorm | ⛈️ |
| Drizzle | 🌦️ |
| Rain | 🌧️ |
| Snow | ❄️ |
| Atmosphere (fog, mist) | 🌫️ |
| Clear sky | ☀️ |
| Cloudy | ☁️ |
| Unknown | ❓ |

---

## ⚠️ Error Handling

The app gracefully handles the following errors:

- **400** – Bad Request / City not found
- **401** – Unauthorized / Invalid API key
- **403** – Forbidden / Access denied
- **404** – City not found
- **500 / 502 / 503 / 504** – Server-side errors
- **Connection Error** – No internet connection
- **Timeout** – Server took too long to respond

---

## 📌 Known Issues / Notes

- The API currently returns temperature with `units=metric`, so the raw `temp` value is already in °C. The line `temperature_c = temperature_k - 273.15` in `display_weather()` is unused — the label correctly displays the metric value.
- The stylesheet in `InitUI()` is missing a closing `}` for `#description_label` — this may cause minor styling inconsistencies.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [OpenWeatherMap](https://openweathermap.org/) for the free weather API
- [PyQt5](https://pypi.org/project/PyQt5/) for the GUI framework
