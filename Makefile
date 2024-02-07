Makefile:
ifneq (,$(wildcard ./.env))
	include .env
	export
	ENV_FILE_PARAM = --env-file .env
endif

build:
	docker compose up --build -d --remove-orphans

up:
	docker compose up -d

up-v:
	docker compose up

down:
	docker compose down

down-v:
	docker compose down -v

status:
	docker ps -a

show-logs:
	docker compose logs

restart:
	docker compose restart

prune:
	docker system prune

remove-images:
	@read -p "WARNING: This will remove all Docker images. Are you sure you want to continue? (y/N) " confirm; \
	if [ "$$confirm" = "y" ] || [ "$$confirm" = "Y" ]; then \
		docker rmi -f $$(docker images -a -q); \
	else \
		echo "Operation canceled."; \
	fi

stop-container:
	@read -p "Enter the container ID to stop: " container_id; \
	if [ -n "$$container_id" ]; then \
		docker stop $$container_id; \
	else \
		echo "Container ID is required."; \
	fi

remove-container:
	@read -p "Enter the container ID to remove: " container_id; \
	if [ -n "$$container_id" ]; then \
		docker rm $$container_id; \
	else \
		echo "Container ID is required."; \
	fi

