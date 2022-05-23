#!/usr/bin/env bash
TESTS=./tests

rm -rf ./build
mkdir ./build

all_pass=true
for test_file in "$TESTS"/*.micro; do
    python ./test_scanner.py "$test_file" > ./build/"$(basename "$test_file" .micro).out"
    diff --strip-trailing-cr "$TESTS"/"$(basename "$test_file" .micro).out"  ./build/"$(basename "$test_file" .micro).out"
    if [[ $? -ne 0 ]]; then
        all_pass=false
    fi
done

if [ "$all_pass" = true ]; then
    echo "ALL PASS!!!"
fi
