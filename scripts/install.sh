mkvirtualenv ui-experimental-platform-api
ln -s `pwd`/scripts/virtualenv/* $VIRTUAL_ENV/$VIRTUALENVWRAPPER_ENV_BIN_DIR
pip install -r requirements.txt
pip install -r requirements_dev.txt
deactivate
workon ui-experimental-platform-api
