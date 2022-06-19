venv:
	brew install pyenv node
	pyenv install 3.8.13 --skip-existing
	python -m pip install --upgrade pip
	pyenv virtualenv 3.8.13 stealth_venv
	pyenv local stealth_venv

deps:
	pip install -r requirements.txt
	npm install chrome-remote-interface

docker:
	docker build -t sst:0.0.1 .

