#!/usr/bin/env bash
export DEBUG="false"
export CSRF_COOKIE_NAME="{{csrf_cookie_name}}"
export SESSION_COOKIE_NAME="{{session_cookie_name}}"
export VENV_DIR="{{venv_dir}}"
export HTTPS_ENABLED="{{ssl_on}}"
# a hack for python 3 and boto
# https://github.com/travis-ci/travis-ci/issues/5246
export BOTO_CONFIG="/tmp/bogus"
