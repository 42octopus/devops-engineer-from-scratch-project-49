# Makefile
install:
	uv sync

build:
	uv build --out-dir dist

package-install:
	uv tool install dist/*.whl --force-reinstall

brain-games:
	uv run brain-games

lint:
	uv run ruff check brain_games


.PHONY: install build package-install brain-games

