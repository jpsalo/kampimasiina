#!/bin/sh

# Dump data into csv
# https://stackoverflow.com/a/39534852/7010222
# https://stackoverflow.com/questions/39457549/heroku-django-dumpdata/39534852#comment81138914_39534852
heroku run --app kampi python manage.py dumpdata motivation --natural-foreign -- | jq '[.[] | {mturk: .fields."mturk", experiment_type: .fields."experiment_type", earnings: .fields."earnings"}]' > questionnaires.json
./node_modules/.bin/json2csv -i questionnaires.json > questionnaires.csv
