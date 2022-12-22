#!/usr/bin/env python
import os

def write_dune():
    f = open("dune-project", 'w')
    f.write('(lang dune 3.6)')
    f.close()

def write_bin():
    os.system('mkdir bin')
    f0 = open("bin/main.ml", 'w')
    f0.write('let () = print_endline "Hello, World!"')
    f0.close()
    f1 = open("bin/dune", "w")
    f1.write('(executable\n  (name main)\n  (libraries))')
    f1.close()

def write_ocamlformat():
    f = open(".ocamlformat", 'w')
    f.write('profile = janestreet\nversion = 0.24.1')
    f.close()

def emit_prebuild():
    os.system("dune build")

def write_makefile():
    f = open("Makefile", 'w')
    f.write('test: bin/main.ml\n\tdune build --profile=release && _build/default/bin/main.exe test.txt')
    f.close()

if __name__ == '__main__':
    write_dune()
    write_bin()
    write_ocamlformat()
    emit_prebuild()
    write_makefile()
