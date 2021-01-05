build:
	docker-compose build

run:
	docker-compose up -d

rerun: clean-docker-volumes
	docker-compose up -d

stop: clean-docker-volumes

clean-docker-volumes:
	docker-compose down -v

alembic-migrate:
	alembic upgrade head
