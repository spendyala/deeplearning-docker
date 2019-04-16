#!/bin/bash
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

set -e

# if we are running on OSX, don't bother signing the notebooks, we are probably on a developer's laptop...
if [[ ! $(uname -r) = *'linuxkit'* ]]; then
    if [ -e /home/spendyala/project/notebooks ]; then
        TMP_XXX_SAVE=`pwd`
        # for any notebooks in the 'notebooks' sub-dir, sign them, we will "trust" them
        cd /home/spendyala/project/notebooks
        for f in *.ipynb; do
            # if there aren't any *.ipynb then '*.ipynb' is sent through the loop as $f
            if [[ -e $f ]]; then
                jupyter trust "$f"
            fi
        done
        cd $TMP_XXX_SAVE
    fi
fi

# determine if we are running lab or notebook
NOTEBOOK_MODE=${NOTEBOOK_MODE:-notebook}

if [[ ! -z "${JUPYTERHUB_API_TOKEN}" ]]; then
  # launched by JupyterHub, use single-user entrypoint
  exec /usr/local/bin/start-singleuser.sh $*
else
  . /usr/local/bin/start.sh jupyter $NOTEBOOK_MODE $*
fi
