# ShopRatingApp
App to Rate Shops

# creating a virtual environment
sudo apt install python3.8-venv
python3 -m venv ./venv/


# installing the required modules
pip install -r requrements.txt

# use venv for virtual environment
source /venv/Scripts/activate

# Start Webserver
python3 manage.py runserver

# migrate db
python3 manage.py migrate

# create migration scripts etc
python3 manage.py makemigrations rating_app

# create superuser
python3 manage.py createsuperuser
