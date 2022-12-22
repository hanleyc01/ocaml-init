# ocaml-init

Simple initialization script that sets up a small OCaml project 
using dune, made for how I like it. I really don't like how "heavy"
initialization of a project is with dune, much preferring something
minimal like Rust's cargo: so here's something very similar.

# Outline of Files Outputted

1. dune-project

```
(lang dune 3.6)
```

2. .ocamlformat
```
profile = janestreet
version = 0.24.1
```

3. bin/main.ml 
```ml 
let () = print_endline "Hello, world!"
```

4. bin/dune 
```
(executable
  (name main)
  (libraries))
```

5. Makefile
```
test: bin/main.ml
	dune build --profile=release && _build/default/bin/main.exe test.txt
```

# Potential Note

ocaml-init does an initial call to `dune build`, so if that messes with anything just change the script
