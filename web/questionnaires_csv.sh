#!/bin/sh

# https://stackoverflow.com/a/39534852/7010222
heroku run python manage.py dumpdata motivation --natural-foreign -- | jq '[.[] | {mturk: .fields."mturk", experiment_type: .fields."experiment_type", earnings: .fields."earnings"}]' > questionnaires.json
json2csv -i questionnaires.json > questionnaires.csv
