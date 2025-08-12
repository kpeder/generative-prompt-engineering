ARGS :=  --location us-central1 --project-id kped-ai-w00t


.PHONY: help
help:
	@echo 'make <target>'
	@echo ''
	@echo 'Targets:'
	@echo '    help       Show this help'
	@echo ''
	@echo '    build      Build the package'
	@echo '    clean      Remove build and test files'
	@echo '    pre-commit Run pre-commit checks'
	@echo '    test       Run unit tests'
	@echo ''


.PHONY: build
build:
	@uv build


.PHONY: clean
clean:
	@rm -rf dist


.PHONY: pre-commit
pre-commit:
	@uv run pre-commit run -a


.PHONY: test
test:
	@uv run pytest -vv --cov ${ARGS}
