# ShopRatingApp
App to Rate Shops

# creating a virtual environment
sudo apt install python3.8-venv
python3 -m venv ./venv/
source /venv/Scripts/activate

# installing the required modules
source /venv/Scripts/activate
pip install -r requirements.txt
or
pip install django django-bootstrap4

# Start Webserver
source /venv/Scripts/activate
python3 manage.py runserver

# migrate db
source /venv/Scripts/activate
python3 manage.py migrate

# create migration scripts etc
source /venv/Scripts/activate
python3 manage.py makemigrations rating_app

# create superuser
source /venv/Scripts/activate
python3 manage.py createsuperuser
