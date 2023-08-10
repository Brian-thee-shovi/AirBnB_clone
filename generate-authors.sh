#!/usr/bin/env bash

set -e

AUTHORS_DIR="$(pwd)"

set -x

cat > "${AUTHORS_DIR}/AUTHORS" <<- EOF
    $(git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf)
EOF
