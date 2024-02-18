install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

quick-install:
	poetry install
	poetry build
	poetry publish --dry-run

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint


