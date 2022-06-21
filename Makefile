pre-build:
brew install gcc openssl readline sqlite3 xz zlib
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/johnsmith/.zshrc
brew install pyenv
brew install pyenv-virtualenv
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.zshrc
pyenv install 3.9.4 --skip-existing
pyenv global 3.9.4
brew install node



venv-init:
pyenv install 3.9.4 --skip-existing
-pyenv uninstall -f stealth_venv
-pyenv virtualenv 3.9.4 stealth_venv
-pyenv local stealth_venv



deps:
python -m pip install --upgrade pip
pip install --upgrade pip-tools
pip install -r requirements.txt
npm install chrome-remote-interface



full-build: pre-build venv-init deps
