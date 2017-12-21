# kampimasiina
Kampi tutkimusprojektin koodit

Tämä on tutkimushankketta varten rakennetut koodit

`mkvirtualenv kampimasiina`
`workon kampimasiina`

`cd web`

`python -m pip install <PACKAGE>`

`python -m pip install -r requirements.txt`

`python -m pip freeze > requirements.txt`

`gunicorn crank.wsgi:application --env DEVELOPMENT=true`

`deactivate`

`git subtree push --prefix web heroku master`
