###################################################################################
# This Makefile is used for installing dependencies, running the dev server and   #
# running tests.                                                                  #
###################################################################################

# Run 'make help' if there is no specified target. -> i.e. 'make'
.DEFAULT_GOAL := help

# Print a small manual on how this Makefile can be used
help:
	@echo "usage:"
	@echo "   make <target>"
	@echo "targets:"
	@echo "   install        Install project dependencies and git pre-commit hooks"
	@echo "   run            Run development server at http://localhost:5000"
	@echo "   test           Run all available tests of the project"
	@echo "   help           List usage and available targets"

# Installs project dependencies and git pre-commit hooks.
install:
	pipenv install

# Runs the development server which will be served at http://localhost:5001
run:
	pipenv run flask run

# Runs all tests of the project
test:
	pipenv run pytest --cov=src --cov-report=html --cov-report=term --cov-branch test/
