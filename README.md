# kampimasiina
Tämä on tutkimushankketta varten rakennetut koodit

## Installation

### Create isolated Python environment (optional)
`mkvirtualenv kampimasiina`
or
`mkvirtualenv --python=python3 kampimasiina`

`workon kampimasiina`

Shut down virtual environment:
`deactivate`

### Install requirements
`cd web`

`python -m pip install -r requirements.txt`

### Make migrations
`python ./manage.py migrate`

### Create admin user (optional)
`python manage.py createsuperuser`

## Run
`gunicorn crank.wsgi:application --env DEVELOPMENT=true`

open http://localhost:8000

### Adding a package
`python -m pip install <PACKAGE>`

#### Update requirements:
`python -m pip freeze > requirements.txt`

## Deploy

### Install Heroku CLI
https://devcenter.heroku.com/articles/heroku-cli#download-and-install

### Log in
`heroku login`

### Add Heroku remote
`heroku git:remote -a kampi`

### Deploy the code
`git subtree push --prefix web heroku master`

## Work with the results

### Install Node and npm
https://nodejs.org/en/

#### Install json2csv
`npm install`

### Install jq
https://stedolan.github.io/jq/

### Save questionnaires into CSV file
`sh questionnaires_csv.sh`
