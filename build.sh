set -o errexit


# Dependencies Installation
pip install -r requirements.txt


# Static Files Creation
python manage.py collectstatic


# Database Migration
python manage.py makemigrations base
python manage.py makemigrations
python manage.py migrate