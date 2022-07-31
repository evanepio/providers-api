run:
	. .venv/bin/activate; uvicorn providers.main:app --reload

virtual-env:
	python -m venv .venv
	. .venv/bin/activate; pip install --upgrade pip
	. .venv/bin/activate; pip install -r requirements/dev.txt

lint:
	. .venv/bin/activate; flake8 .
	. .venv/bin/activate; isort . --check-only
	. .venv/bin/activate; black . --check

clean:
	find . | grep -E '(__pycache__|\.pyc|\.pyo$$)' | xargs rm -rf

destroy:
	rm -rf .venv