doc:
	cd docs && pipenv run $(MAKE) html

test: pep8
	pipenv run python -m pytest --cov=mpl_axes_aligner --cov-report=term-missing -v tests/

test-ci: pep8
	pipenv run python -m pytest --cov=mpl_axes_aligner --cov-report=xml tests/

pep8:
	pipenv run python -m pytest --pep8 -v mpl_axes_aligner/

publish: dist
	pipenv run twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

publish-test: dist
	pipenv run twine upload --repository-url https://test.pypi.org/legacy/ dist/*

dist: clean-pub
	pipenv run python setup.py sdist bdist_wheel

clean-pub:
	rm -rf build dist .egg mpl_axes_aligner.egg-info
