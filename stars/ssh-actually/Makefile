# SSH, Actually — an instance of *, Actually. Build and verification targets.
# The build engine is the `star-actually` package (a dependency); this repo is
# content (nodes/) + config (site.yaml).

.PHONY: install lint typecheck test verify validate build serve clean

install:
	uv sync --all-groups
	uv run pre-commit install

lint:
	uv run ruff format --check tests
	uv run ruff check tests

typecheck:
	uv run mypy tests

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
