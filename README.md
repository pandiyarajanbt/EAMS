# EAMS - Employee Attendance Management System

EAMS is a smart, AI-powered Employee Attendance Management System developed using Python, Django, and Machine Learning.  
It simplifies attendance tracking using facial recognition and provides real-time insights for HR and organizational efficiency.

## 🚀 Features

- Face recognition-based attendance system
- Real-time employee check-in/check-out tracking
- Admin panel for attendance monitoring
- Employee profile and role management
- Machine Learning-powered face verification
- Secure login and authentication
- Scalable and modular backend architecture

## 🛠 Tech Stack

- **Backend:** Python, Django
- **Machine Learning:** face-recognition, OpenCV, TensorFlow/Keras
- **Database:** PostgreSQL / SQLite (development)
- **APIs:** Django REST Framework
- **Authentication:** Django Auth
- **Deployment:** Gunicorn, Nginx, Docker (optional)

## 👨‍💻 Developed By

EAMS is proudly developed and maintained by:

- **Pandiyarajan** – Solo Developer (Python, Django, Machine Learning)

I built this project independently as part of my vision to create powerful, AI-integrated tools for business workflows.  
However, **this project is open-source and open to collaboration**.

> 💬 **Want to contribute?** I'm inviting developers to join the journey — whether you're into backend, frontend, ML, or DevOps, feel free to fork, contribute, or raise issues!

## 📦 Installation & Setup

Follow these steps to run the project locally:

```bash
# Clone the repository
git clone https://github.com/pandiyarajanbt/EAMS.git
cd eams

# Create a virtual environment
python -m venv env
source env/bin/activate      # For Linux/macOS
env\Scripts\activate         # For Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create a superuser (admin)
python manage.py createsuperuser

# Start the development server
python manage.py runserver
