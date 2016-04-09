#!/bin/sh
export VIRTUAL_ENV="/home/felix/venv_34_pandas"
export PATH="$VIRTUAL_ENV/bin:$PATH"
unset PYTHON_HOME
exec "${@:-$SHELL}"
