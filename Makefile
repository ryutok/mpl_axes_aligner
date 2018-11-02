doc:
	cd docs && pipenv run $(MAKE) html

test:
	pipenv run python -m pytest --cov=mpl_axes_aligner --cov-report=term-missing -v tests/

test-ci:
	pipenv run python -m pytest --cov=mpl_axes_aligner --cov-report=xml tests/

publish:
	pipenv run python setup.py sdist bdist_wheel
	pipenv run twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
	rm -rf build dist .egg mpl_axes_aligner.egg-info
