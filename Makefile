help:
	@echo "  env         create a development environment using venv"
	@echo "  deps        install dependencies using pip"
	@echo "  test        run all your tests using unittest"
	@echo "  clean       remove unwanted files like .pyc's"

requirements: .requirements.txt

.requirements.txt: requirements.txt
	$(shell . .venv/bin/activate && pip install -r requirements.txt)

.PHONY: run
run:
	$(shell . .venv/bin/activate && python3 wsgi.py)

.PHONY: test
test:
	python3 -m unittest discover

.PHONY: deploy
deploy:
	$(shell . ./deploy.sh)

.PHONY: clean
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
