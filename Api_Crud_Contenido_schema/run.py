import os 
from decouple import config 

#Leer el puertp de archivo .env
port = config('API_PORT')

#Ejecutar el servidor de desarrollo de Django
os.system(f'python manage.py runserver {port}')