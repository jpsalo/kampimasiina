# kampimasiina
Kampi tutkimusprojektin koodit

Tämä on tutkimushankketta varten rakennetut koodit

`workon env1`
`cd web`
`python -m pip install <PACKAGE>`
`python -m pip freeze > requirements.txt`
`gunicorn crank.wsgi:application --env DEVELOPMENT=true`

`git subtree push --prefix web heroku master`
