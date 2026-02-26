# Makefile
install:
	uv sync

build:
	uv build --out-dir dist

package-install:
	uv tool install dist/*.whl --force-reinstall

brain-games:
	uv run brain-games

.PHONY: install build package-install brain-games

