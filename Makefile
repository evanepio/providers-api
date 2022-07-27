
virtual-env:
	python -m venv .venv
	. .venv/bin/activate; pip install -r requirements/dev.txt

format:
	. .venv/bin/activate; isort .
	. .venv/bin/activate; black .

destroy:
	rm -rf .venv