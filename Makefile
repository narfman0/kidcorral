default: run

collectstatic:
	pipenv run python manage.py collectstatic --noinput

deploy-gcp: collectstatic
	pipenv lock -r > requirements.txt
	gcloud app deploy -q app.yaml

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

run-app-public:
	pipenv run python manage.py runserver 0.0.0.0:8000

run-test:
	pipenv run python manage.py test

r: run-app
rp: run-app-public
run: init r
run-public: init rp
t: run-test
test: init-d run-test
