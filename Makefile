doc:
	cd docs && pipenv run $(MAKE) html

apidoc:
	pipenv run sphinx-apidoc -f -o docs/ mpl_axes_aligner/

test:
	pipenv run pytest --cov=mpl_axes_aligner --cov-report=term-missing -v tests/
