#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'churchwebsite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
#     new here
    if not User.objects.filter(is_superuser=True).first():
    user = User.objects.create(
        username = 'admin',
        email = 'admin@mywebsite.com',
        is_superuser = True,
        ...
    )
    user.set_password('some password')
    user.save()


if __name__ == '__main__':
    main()
