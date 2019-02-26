default: run

init:
	pipenv install

init-d:
	pipenv install -d

loaddata: migrate
	pipenv run python manage.py loaddata kidcorral/person/fixtures/initial_data.json

makemigrations:
	pipenv run python manage.py makemigrations

migrate: makemigrations
	pipenv run python manage.py migrate

su:
	pipenv run python manage.py createsuperuser

run-app:
	pipenv run python manage.py runserver

run-test:
	pipenv run python manage.py test

r: run-app
run: init r
t: run-test
test: init-d run-test
