#!/usr/bin/env bash

case "$OSTYPE" in
    msys*)    python=python ;;
    cygwin*)  python=python ;;
    *)        python=python3 ;;
esac

cd ../
echo "from yacut import db; \
     db.create_all(); \
     URLMap.query.delete(); \
     URLMap_object = URLMap(original='https://example.com/', short='example'); db.session.add(URLMap_object); db.session.commit()" | flask shell >/dev/null 2>&1
cd -
