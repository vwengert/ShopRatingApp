#!/bin/bash
cd /home/pi/ShopRatingApp
source venv/bin/activate
nohup python manage.py runserver 0.0.0.0:8000
