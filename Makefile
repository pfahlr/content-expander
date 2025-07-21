.PHONY: sops-encrypt sops-start-env db-up db-down db-nuke run-fastapi run-vite 
CONTAINER_HANDLER=podman
COMPOSE_FILE=docker-compose.dev.yaml
DB_CONTAINER=webcontmgr-db
DB_VOLUME=webcontmgr-db-vol

sops-encrypt:
	@echo "Encrypting the .env file"
	sops -e --in-place ./.env

sops-decrypt:
	@echo "Decrypting into session"
	sops exec-env ./.env /usr/bin/bash

db-up:
	@echo "📦 Brining up database container..."
	$(CONTAINER_HANDLER) compose --file=$(COMPOSE_FILE) up --build $(DB_CONTAINER)
	@echo "✅ Done!"

db-down:
	@echo "🛑 shutting down database"
	$(CONTAINER_HANDLER) compose  --file=$(COMPOSE_FILE) down $(DB_CONTAINER)
	@echo "💤 Done!"

db-nuke:
	#@echo "are you sure you want to nuke the database? (Y/n)?"
	#@read ans
	#@echo $ans
	#if [ "$${ans:-N}" = "y" ] || [ "$${ans:-N}"  = "Y" ]; then
	@echo "shutting down content manager/expander database"
	$(MAKE) db-down
	@echo "☢️ Nuking container and volume"
	$(LAUNCH_WITH_SECRETS) $(CONTAINER_HANDLER) container rm -f $(DB_CONTAINER)
	$(LAUNCH_WITH_SECRETS) $(CONTAINER_HANDLER) volume rm -f content-expander_$(DB_VOLUME)
	@echo "📦 Rebuilding..."
	$(MAKE) db-container-up
	@echo "✅ Done!"
	#fi
	#@echo "Done!"

run-fastapi-dev:
	#source backend/fastapi/venv/bin/activate
	@cd backend/fastapi && ./entrypoint.sh

run-vite-dev:
	@echo "Loading ReactJS Frontent Dev Server"
	@./frontend/entrypoint.sh