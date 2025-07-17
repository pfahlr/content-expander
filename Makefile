CONTAINER_HANDLER=podman
COMPOSE_FILE=docker-compose.dev.yaml
DB_CONTAINER=webcontmgr-db
DB_VOLUME=webcontmgr-db-vol

db-container-up:
	@echo "📦 Brining up database container..."
	$(CONTAINER_HANDLER) compose --file=$(COMPOSE_FILE) up --build $(DB_CONTAINER)
	@echo "✅ Done!"

db-container-down:
	@echo "🛑 shutting down database"
	$(CONTAINER_HANDLER) compose  --file=$(COMPOSE_FILE) down $(DB_CONTAINER)
	@echo "💤 Done!"

db-container-nuke:
	@echo "shutting down content manager/expander database"
	$(MAKE) db-container-down
	@echo "☢️ Nuking container and volume"
	$(CONTAINER_HANDLER) container rm -f $(DB_CONTAINER)
	$(CONTAINER_HANDLER) volume rm -f content-expander_$(DB_VOLUME)
	@echo "📦 Rebuilding..."
	$(MAKE) db-container-up
	@echo "✅ Done!"
