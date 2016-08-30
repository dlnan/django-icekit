#!/bin/bash

# Run tests.

cat <<EOF
# `whoami`@`hostname`:$PWD$ runtests.sh $@
EOF

set -e

export BASE_SETTINGS_MODULE=test
export PGDATABASE=test_icekit
export REUSE_DB=1
export SETUP_POSTGRES_FORCE=1
export SRC_PGDATABASE="$ICEKIT_DIR/initial_data.sql"

unset WAITLOCK_ENABLED

python "$ICEKIT_DIR/bin/manage.py" test --noinput --verbosity=2 "${@:-icekit}"
