#!/bin/bash

python /code/manage.py migrate # --settings=code.settings.production            # Apply database migrations
python /code/manage.py collectstatic --noinput # --settings=code.settings.production  # Collect static files

#Prepare log files and start outputting logs to stdout
# touch /logs/gunicorn.log
# touch /logs/access.log
# tail -n 0 -f /logs/*.log &
# Start Gunicorn processes
echo Starting Gunicorn.
#
exec gunicorn core.wsgi -b :8000

#exec gunicorn core.wsgi:application \
#    --bind 0.0.0.0:8000 \
#    --workers 3 \
#    --timeout 3600 \
#    --log-level=info \
#    #--log-file=/logs/gunicorn.log \
#    #--access-logfile=/logs/access.log \
"$@"
