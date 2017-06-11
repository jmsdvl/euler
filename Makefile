clean:
	find . | grep -E "(__pycache__|\.pyo|\.pyc)" | xargs rm -rf
