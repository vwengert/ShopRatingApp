# ShopRatingApp
App to Rate Shops

# installing the required modules
sudo pip install -r requrements.txt

# use venv for virtual environment
source /venv/Scripts/activate

# Start Webserver
python3 manage.py runserver

# migrate db
python3 manage.py migrate

# create db
python3 manage.py makemigration rating_app

# create superuser
python3 manage.py createsuperuser
