
virtual-env:
	python -m venv .venv
	. .venv/bin/activate; pip install -r requirements/dev.txt

destroy:
	rm -rf .venv