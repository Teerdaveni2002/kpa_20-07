KPA Backend - Inspection Management APIs

This repository contains the backend APIs for the KPA Inspection Management System. Built using **Django** and **Django REST Framework**, this project powers functionalities like inspection form submission, filtering, and login using mobile number.

---

## 📦 Technologies Used

- Python 3.x
- Django 4.x
- Django REST Framework
- PostgreSQL

---

## 📁 Project Structure

kpa_20-07/
├── authentication/ # Login and user authentication
├── Bogie_checksheet/ # Bogie inspection form APIs
├── wheel_form/ # Wheel form inspection APIs
├── kpa_project/ # Main Django project settings
├── manage.py # Django entry point
├── requirements.txt # Python dependencies
└── README.md # Project info



## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/Teerdaveni2002/kpa_20-07.git
cd kpa_20-07
2. Set up virtual environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Configure Database
Make sure PostgreSQL is running, then update settings.py with your DB credentials.

python
Copy
Edit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
5. Run Migrations & Server
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
📬 API Features
✅ Login via mobile number and password

✅ Submit inspection forms

✅ Retrieve inspection data with filters

✅ API-based authentication

📮 Sample API Endpoints
Method	Endpoint	Description
POST	/api/login/	Login with mobile number
POST	/api/bogie/form/	Submit bogie form (http://127.0.0.1:8000/bogie/bogie-checksheet/)
[GET	/api/bogie/form/?param=value](http://127.0.0.1:8000/wheel/filter/?submitted_date)	Filter bogie data
POST	/api/wheel/form/	Submit wheel form(http://127.0.0.1:8000/wheel/wheel/)

🤝 Contributing
Feel free to raise issues or submit pull requests. This is a learning project, so any contributions are appreciated!

📄 License
This project is licensed under the MIT License.

👩‍💻 Author
Teerdaveni Gedela
GitHub: @Teerdaveni2002
