help:
	@echo "  env         create a development environment using venv"
	@echo "  deps        install dependencies using pip"
	@echo "  test        run all your tests using unittest"
	@echo "  clean       remove unwanted files like .pyc's"

requirements: .requirements.txt

.requirements.txt: requirements.txt
	. .venv/bin/activate && pip install -r requirements.txt

.PHONY: run
run:
	. .venv/bin/activate && python3 wsgi.py

test:
	python -m unittest discover

.PHONY: deploy
deploy:
	. ./deploy.sh

.PHONY: clean
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
