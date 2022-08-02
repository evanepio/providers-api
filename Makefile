VENV_BIN = .venv/bin

run:
	$(VENV_BIN)/uvicorn providers.main:app --reload

virtual-env:
	python -m venv .venv
	$(VENV_BIN)/pip install --upgrade pip
	$(VENV_BIN)/pip install -r requirements/dev.txt

lint:
	$(VENV_BIN)/flake8 .
	$(VENV_BIN)/isort . --check-only
	$(VENV_BIN)/black . --check

clean:
	find . | grep -E '(__pycache__|\.pyc|\.pyo$$)' | xargs rm -rf

destroy:
	rm -rf .venv