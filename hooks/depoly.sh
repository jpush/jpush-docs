#!/bin/bash

echo `date`

DOC_DIR=$(cd `dirname $0`;cd ..; pwd)
VENV_PATH=$DOC_DIR/venv

source $DOC_DIR/hooks/hooksrc

# Run directly without params OR within python webhooks script
if [[ $# -eq 0 || $DEPOLY_BRANCH == $1 ]]; then
    echo "Depoly JPush Docs Branch $DEPOLY_BRANCH"

    cd $DOC_DIR

    git fetch
    diff=`git diff $DEPOLY_BRANCH $REMOTE_REPO_MAME/$DEPOLY_BRANCH`

    if [ -n "$diff" ]; then
        echo "Something Changed"

        git checkout $DEPOLY_BRANCH
        git merge $REMOTE_REPO_MAME/$DEPOLY_BRANCH

        source $VENV_PATH/bin/activate
        mkdocs build
        echo "Building documentation..."
        deactivate
    else
        echo "Nothing Changed"
    fi
else
    echo "DEPOLY_BRANCH #${DEPOLY_BRANCH} and Event Branch #${1} are Not Match"
fi
