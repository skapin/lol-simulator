#!/bin/bash
set -e

cd /usr/src/app/

case "$1" in
    prod)
        echo "---> Starting in PRODUCTION mode"
        cd /usr/src/app/
        exec /usr/local/bin/gunicorn server_app:app -w 5 -b :9009
        ;;
    dev)
        echo "---> Starting in DEV mode"
        cd /usr/src/app/
        export FLASK_DEBUG=1
        echo "---> Start EXEC"
        FLASK_APP=server_app.py flask run --port 9009  --with-threads --host '0.0.0.0'
        echo "---> END"
        ;;
    worker)
        cd /usr/src/app/
        exec celery -A tasks worker -B --loglevel=DEBUG -l debug
        ;;
    sleep)
        echo "---> Starting Sleep "
        while true; do
            sleep 60
            echo "zZz"
        done
        ;;
    *)
        echo "Please specify argument (prod|dev) [ARGS..]";
        exit 1;
        ;;
esac

exit 0;
