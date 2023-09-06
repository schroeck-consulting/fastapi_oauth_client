test:
	pytest --workers auto tests --no-coverage-upload

test-with-typeguard:
	pytest --workers auto --typeguard-packages=mvv.auth.fastapi tests --no-coverage-upload

coverage:
	pytest --workers auto --cov-config=.coveragerc --cov=mvv.auth.fastapi --cov-report=term-missing --cov-report=xml --junitxml=junit/test-results.xml tests

mypy: FORCE
	mypy -p mvv.auth.fastapi --exclude "snowflake|csv_to_pandera_schema|progressbar|pandas"

bandit:
	bandit -r mvv.auth.fastapi -r -c .bandit

flake8:
	flake8 --config .flake8 mvv

pylint:
	pylint --fail-under=8  mvv

safety:
	pip-audit

build:
	python setup.py bdist_wheel sdist

publish:
	python3 -m twine upload --repository gitea dist/*
