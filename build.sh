set -o errexit


# Dependencies Installation
pip install -r requirements.txt


# Static Files Creation
python manage.py collectstatic


# Database Migration
python makemigrations base
python makemigrations
python manage.py migrate