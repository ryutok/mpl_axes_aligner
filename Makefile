doc:
	cd docs && $(MAKE) html

test: flake8
	python -m pytest --cov=mpl_axes_aligner --cov-report=term-missing -v tests/

test-ci: flake8
	python -m pytest --cov=mpl_axes_aligner --cov-report=xml tests/

flake8:
	python -m pytest --flake8 mpl_axes_aligner/

publish: dist
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

publish-test: dist
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

dist: clean-pub
	python setup.py sdist bdist_wheel

clean-pub:
	rm -rf build dist .egg mpl_axes_aligner.egg-info
