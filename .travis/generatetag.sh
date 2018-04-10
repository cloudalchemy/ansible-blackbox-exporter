#!/bin/bash

# Some basic variables
GIT_MAIL="paulfantom@gmail.com"
GIT_USER="paulfantom"
ORGANIZATION="cloudalchemy"
PROJECT="ansible-blackbox-exporter"

# Git config
git config --global user.email "${GIT_MAIL}"
git config --global user.name "${GIT_USER}"
GIT_URL=$(git config --get remote.origin.url)
GIT_URL=${GIT_URL#*//}

# Auto tagger
# Test if current commit is already tagged
git tag --points-at
[[ $(git tag --points-at) ]] && exit 0

GIT_TAG=$([[ "$TRAVIS_COMMIT_MESSAGE" =~ ("Merge pull request".*\[feature\].*) ]] && git semver --next-minor || git semver --next-patch )
echo "$TRAVIS_COMMIT_MESSAGE"
echo $GIT_TAG
git tag $GIT_TAG -a -m "Generated tag from TravisCI for build $TRAVIS_BUILD_NUMBER"
git push https://${GH_TOKEN}:@${GIT_URL} --tags || exit 0

# Auto changelog
docker run -it --rm -v "$(pwd)":/usr/local/src/your-app ferrarimarco/github-changelog-generator \
               -u "${ORGANIZATION}" -p "${PROJECT}" --token ${GH_TOKEN} \
               --release-url "https://galaxy.ansible.com/${ORGANIZATION}/${PROJECT}" \
               --unreleased-label "**Upcoming**" --no-compare-link

git add CHANGELOG.md
git commit -m '[ci skip] new changelog'
git push https://${GH_TOKEN}:@${GIT_URL} || exit 0
