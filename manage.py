"""
StudyBuddy Management Script

This script is the main entry point for managing the StudyBuddy Django project.
It sets up project settings and handles command-line execution.

Usage:
    python manage.py <management_command>

For more information on available management commands, refer to the Django documentation:
https://docs.djangoproject.com/en/stable/ref/django-admin/
"""
import os
import sys
from django.core.management import execute_from_command_line


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studybuddy.settings')
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
