#!/usr/bin/env bash
TEST_RESULT=./tests/output
for test_file in ./tests/input/*; do
    output=$(python test_symbol_table.py ${test_file})
    target="${TEST_RESULT}/$(basename ${test_file} .micro)".out
    echo "$output" | diff --strip-trailing-cr "$target" -
    if [[ $? -ne 0 ]]; then
        echo "Fail Test: ${test_file}"
        exit
    fi
done

echo "ALL PASS!!!"
