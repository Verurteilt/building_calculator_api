#!/bin/bash

NAME="building_calculator_api"                              #Name of the application (*)
DJANGODIR=/opt/building_calculator_api/building_calculator_api             # Django project directory (*)
SOCKFILE=/opt/building_calculator_api/building_calculator_api/run/gunicorn.sock        # we will communicate using this unix socket (*)
USER=ubuntu                                        # the user to run as (*)
GROUP=ubuntu                                     # the group to run as (*)
NUM_WORKERS=1                                     # how many worker processes should Gunicorn spawn (*)
DJANGO_SETTINGS_MODULE=building_calculator_api.settings             # which settings file should Django use (*)
DJANGO_WSGI_MODULE=building_calculator_api.wsgi                     # WSGI module name (*)

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
pyenv activate building_calculator_api
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /opt/building_calculator_api/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=unix:$SOCKFILE