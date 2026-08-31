#!/bin/sh
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$script_dir"

{
    date -u '+UTC: %Y-%m-%dT%H:%M:%SZ'
    uname -mrs
    sw_vers
    clang --version
    objdump --version
} > environment.txt

{
    echo 'clang -S -O0 examples.c -o examples-O0.s'
    echo 'clang -S -O2 examples.c -o examples-O2.s'
    echo 'clang -c -O2 examples.c -o examples-O2.o'
    echo 'objdump -d examples-O2.o'
    echo 'clang -c handwritten_add_naive.s -o handwritten_add_naive.o'
    echo 'clang handwritten_add_naive.o test_handwritten.c -o handwritten-naive-demo'
    echo 'clang -c handwritten_add.s -o handwritten_add.o'
    echo 'clang handwritten_add.o test_handwritten.c -o handwritten-demo'
    echo './handwritten-demo'
} > commands.txt

clang -S -O0 examples.c -o examples-O0.s
clang -S -O2 examples.c -o examples-O2.s
clang -c -O2 examples.c -o examples-O2.o
objdump -d examples-O2.o > examples-O2-objdump.txt

clang -c handwritten_add_naive.s -o handwritten_add_naive.o
if clang handwritten_add_naive.o test_handwritten.c -o handwritten-naive-demo > link-failure.txt 2>&1; then
    echo 'ERROR: the intentionally naive symbol unexpectedly linked' >> link-failure.txt
    exit 1
fi

clang -c handwritten_add.s -o handwritten_add.o
clang handwritten_add.o test_handwritten.c -o handwritten-demo
./handwritten-demo > run-output.txt
objdump -d handwritten_add.o > handwritten-objdump.txt

shasum -a 256 examples.c examples-O0.s examples-O2.s examples-O2.o \
    handwritten_add_naive.s handwritten_add.s handwritten_add.o \
    test_handwritten.c handwritten-demo > sha256.txt
