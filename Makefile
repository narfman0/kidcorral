default: init run

init:
	pipenv install

init-d:
	pipenv install -d

makemigrations:
	pipenv run python manage.py makemigrations

migrate: makemigrations
	pipenv run python manage.py migrate

su:
	pipenv run python manage.py createsuperuser

run:
	pipenv run python manage.py runserver
