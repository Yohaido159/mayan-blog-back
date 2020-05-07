
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_pro.settings')

app = get_wsgi_application()

os.system("python manage.py migrate")
os.system("python manage.py runserver")
