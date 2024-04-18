#!/usr/bin/env bash

set -eu -o pipefail

cd examples/02_crowsnest

PRG="crowsnest.py"
for FILE in solution*.py; do
    echo "==> ${FILE} <==" 
    cp "$FILE" "$PRG"
    make test
done

cd ../..

echo "Done."
