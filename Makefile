build:
	docker-compose build

run_all:
	docker-compose up --build

run_all_daemon:
	docker-compose up --build -d

test:
	docker-compose run backend pytest

lint:
	docker-compose run backend pylint --load-plugins pylint_django --django-settings-module=loft_temperature_feed_challenge.settings /app/loft_temperature_feed_* --recursive=y

format:
	docker-compose run backend black .

clean:
	rm -rf __pycache__

.PHONY: run run_daemon test lint clean
