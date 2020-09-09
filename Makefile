SHELL := /bin/bash

help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

install:
	pipenv install

activate:
	pipenv shell

test:
	python manage.py test

run:
	python manage.py runserver

migration:
	python manage.py makemigrations

migrate:
	python manage.py migrate

superuser:
	docker-compose exec qife_api python manage.py createsuperuser

heroku:
	git push heroku master

up:
	docker-compose up -d

provision:
	docker-compose exec qife_api python manage.py makemigrations
	docker-compose exec qife_api python manage.py migrate

logs:
	docker-compose logs -f

logs-api:
	docker-compose logs -f qife_api

logs-celery:
	docker-compose logs -f celery

logs-mysql:
	docker-compose logs -f mysql

logs-redis:
	docker-compose logs -f redis

shell-db:
	docker-compose exec db mysql -uroot -p

shell-api:
	docker-compose exec qife_api python manage.py shell

down:
	docker-compose down