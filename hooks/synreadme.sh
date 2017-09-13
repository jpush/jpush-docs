#!/bin/bash

echo `date`

DOC_DIR=$(cd `dirname $0`;cd ..; pwd)
VENV_PATH=$DOC_DIR/venv
REPOS_DIR=$DOC_DIR/repos

source $DOC_DIR/hooks/hooksrc

REPOS=(
    'jpush-api-java-client'
    'jpush-api-csharp-client'
    'jpush-api-php-client'
    'jpush-api-python-client'
    'jpush-api-nodejs-client'
    'jpush-api-ruby-client'
    'jmessage-api-java-client'
    'jmessage-api-csharp-client'
    'jmessage-api-python-client'
    'jmessage-api-php-client'
    'jsms-api-java-client'
    'jsms-api-php-client'
    'jsms-api-csharp-client'
)

repo_clone() {
    repo=$1

    cd $REPOS_DIR
    if [ ! -d $repo ]; then
        echo "$repo is Not Found, Cloning..."
        git clone https://github.com/jpush/${repo}.git
        echo "$repo Cloned"
    fi
    return 0
}
cp_readme() {
    repo=$1

    array=(${repo//-/ })
    product=${array[0]}
    language=${array[2]}

    readme_dist_dir=$DOC_DIR/zh/$product/server/sdk;
    if [ ! -d $readme_dist_dir ]; then
        echo "MKDIR a Folder to put ${product}'README"
        mkdir $readme_dist_dir
    fi

    echo "Sync ${repo}'s README to Docs..."

    repo_dir=$REPOS_DIR/$repo
    readme=$readme_dist_dir/${language}_sdk.md
    cd $repo_dir

    git pull

    cp $repo_dir/README.md $readme

    return 0
}

do_sync() {
    repo=$1

    repo_clone $repo
    if [ ! 0 -eq $? ]; then
        echo "Something Wrong when Cloning $repo, Try later"
        exit 0
    fi
    cp_readme $repo
    if [ ! 0 -eq $? ]; then
        echo "Something Wrong when Synchronizing ${repo}'README, Try later"
        exit 0
    fi
}

if [ ! -d $REPOS_DIR ]; then
    mkdir $REPOS_DIR
fi

if [ 0 -eq $# ]; then
    for repo in ${REPOS[@]}
    do
        do_sync $repo
    done
else
    do_sync $1
fi

cd $DOC_DIR
source $VENV_PATH/bin/activate
mkdocs build
echo "Building documentation..."
deactivate
