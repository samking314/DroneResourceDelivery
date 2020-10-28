.PHONY: docs test

help:
	@echo "  env         create a development environment using virtualenv"
	@echo "  deps        install dependencies using pip"
	@echo "  test        run all your tests using py.test"
# 	@echo "  clean       remove unwanted files like .pyc's"

env:
	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
	python get-pip.py && \
	rm -rf get-pip.py && \
	pip install virtualenv && \
	virtualenv env && \
	. env/bin/activate && \
	make deps

deps:
	pip install -r requirements.txt

# clean:
# 	python manage.py clean

test:
	python -m unittest discover