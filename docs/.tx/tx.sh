#!/usr/bin/env bash
# Script to exchange translation files between repo and Transifex via Travis CI.
# It relies on $TXTOKEN and $GHTOKEN being set as env vars for the given repo
# in Travis CI.

git_setup() {
  git config --global user.email "bot+travis@transifex.com"
  git config --global user.name "Transifex Bot (Travis CI)"
}

commit_translation_files() {
  echo "checkout"
  git checkout -b transifex
  echo "add"
  git add source/_locale/*.po
  echo "commit"
  git commit -m "Translation update from Transifex" -m "[ci skip]"
}

push_translation_files() {
  echo "git remote"
  git remote add origin-travis https://${GHTOKEN}@github.com/$TRAVIS_REPO_SLUG.git > /dev/null 2>&1
  echo "git push"
  git push -f --set-upstream origin-travis transifex
}

tx_init() {
  echo "[https://www.transifex.com]
hostname = https://www.transifex.com
username = api
password = $TXTOKEN
token =" > ~/.transifexrc
}

update_translations() {
  make gettext
  rm .tx/config
  sphinx-intl create-txconfig
  sphinx-intl update-txconfig-resources --transifex-project-name tradssat
}

tx_push() {
  # Only run once, and only on $TX_BRANCH branch
  echo $TRAVIS_JOB_NUMBER | grep "\.1$"
  if [ $? -eq 0 ] && [ $TRAVIS_BRANCH == $TX_BRANCH ]
    then
      tx_init
      update_translations
      tx push --source --no-interactive
  fi
}

tx_pull() {
  # Only run once, and only for $TX_TAG tag
  echo $TRAVIS_JOB_NUMBER | grep "\.1$"
  if [ $? -eq 0 ] # && [ $TRAVIS_TAG == $TX_TAG ]
    then
      echo "pulling"
      tx_init
      tx pull --all --force
      FRESH_TRANSLATIONS=$(git diff-index --name-only HEAD --)
      echo $FRESH_TRANSLATIONS
      if [ -n "$FRESH_TRANSLATIONS" ]
        then
          echo "pushing"
          git_setup
          commit_translation_files
          push_translation_files
      fi
  fi
}

# Check arg passed to script and call appropriate function
case $@ in
  push) tx_push ;;
  pull) tx_pull ;;
  *) echo "Either 'push' or 'pull' should be passed as an argument to tx.sh." ;;
esac