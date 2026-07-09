# Ho System, Actually — an instance of *, Actually. The build engine is the
# `star-actually` package (a dependency); this repo is content + config.

.PHONY: install ingest lint typecheck test verify validate build serve clean

install:
	uv sync --all-groups
	uv run pre-commit install

# Re-crawl the Ho System source into nodes/ (idempotent). Run whenever ho grows.
ingest:
	uv run python scripts/ingest.py

lint:
	uv run ruff format --check tests scripts
	uv run ruff check tests scripts

typecheck:
	uv run mypy tests scripts

test:
	uv run pytest

verify: lint typecheck test

validate:
	uv run star-actually validate

build:
	uv run star-actually build

serve: build
	uv run star-actually serve

clean:
	rm -rf dist htmlcov .pytest_cache .mypy_cache .ruff_cache
