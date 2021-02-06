.PHONY: make_requirements

make_requirements:
	poetry export -f requirements.txt -o requirements.txt