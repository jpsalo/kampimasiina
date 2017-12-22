# kampimasiina
Kampi tutkimusprojektin koodit

Tämä on tutkimushankketta varten rakennetut koodit

`mkvirtualenv kampimasiina`
or
`mkvirtualenv --python=python3 kampimasiina`

`workon kampimasiina`

`cd web`

`python -m pip install <PACKAGE>`

`python -m pip install -r requirements.txt`

`python -m pip freeze > requirements.txt`

# Make migrations
`python ./manage.py migrate`

# Create admin user
`python manage.py createsuperuser`

# Run
`gunicorn crank.wsgi:application --env DEVELOPMENT=true`

`deactivate`

# Install Heroku

# Add Heroku remote
`heroku git:remote -a kampi`

`git subtree push --prefix web heroku master`
