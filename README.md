# 🛎️ Guest Feedback Dashboard (Django REST API)

A simple API for collecting and managing guest feedback, built with Django and Django REST Framework. This project simulates part of a hospitality platform like Bolt Farm Treehouse, including webhook-style automation logic.

## 🚀 Features

- Guests can submit feedback (name, rating, message)
- Admin dashboard for managing entries
- API to view and create feedback
- Webhook-style simulation on new entry
- Clean, reusable code using Django + DRF

## 📸 API Endpoints

| Method | Endpoint            | Description              |
|--------|---------------------|--------------------------|
| GET    | `/api/feedback/`    | List all feedback        |
| POST   | `/api/feedback/`    | Submit new feedback      |

## 📦 Tech Stack

- Python 3.x
- Django
- Django REST Framework
- SQLite (default DB)

## 🧑‍💻 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/Kelvyn2012/feedback_project.git
   cd feedback_project
