#!/bin/bash

manage='python manage.py'

if [ "$1" = '-h' ] || [ "$1" = '--help' ] || [ "$1" = 'help' ]; then
  echo "Runs common django scripts, so you don't neet to memorize their weird syntax."
  echo "Usage:     ./run.sh \$command \$arg"
  echo "           defaults to start if no command given."
  echo "Commands:"
  echo "start      start the server at 127.0.0.1:8000 or at \$arg"
  echo "update     updates migrations"
  echo "migrate    updates, then run migrations"
fi

# Runs the damn dev server
if [ $# -eq 0 ]; then
  $manage runserver

# Runs the server at given address
elif [ "$1" = 'start' ]; then
  $manage runserver $2

# Update migrations
elif [ "$1" = 'update' ]; then
  $manage makemigrations school

# Migrations
# also fucking updates migrations because that's usually what you want
elif [ "$1" = 'migrate' ]; then
  ./$(basename $0) update
  $manage migrate

# Setup admin
elif [ "$1" = 'setup' ]; then
  $manage createsuperuser
fi