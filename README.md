# bazel-hermetic-python
Yet another attempt to have a more hermetic python with bazel

## goal

Build our own python interpreter in a clean fashion and be able to use pip to install packages.
## must read blog/github

* https://thethoughtfulkoala.com/posts/2020/05/16/bazel-hermetic-python.html - pro: enable pip usage; cons: use SSL from the system. if your CI does not have it, or your fellow dev does not want to alter its host SSL config, this is not great.
* https://github.com/kku1993/bazel-hermetic-python : same, but covers also docker images.
* https://github.com/jvolkman/bazel-nix-python-example - insightful. pro: use nix-build. Cons: use nix-build. 
* https://github.com/gearoid-murphy/bazel_hermetic_python + https://github.com/gearoid-murphy/bazel_hermetic_python_demo - a nice approach using rules_foreign_cc. I ended up making my own simplified, flatten version of this. 

## tryout

We have a simple helloworld using pip packages, and doing a TLS query:
```
❯ bazel run //:helloworld
INFO: Analyzed target //:helloworld (0 packages loaded, 0 targets configured).
INFO: Found 1 target...
Target //:helloworld up-to-date:
  bazel-bin/helloworld
INFO: Elapsed time: 0.211s, Critical Path: 0.00s
INFO: 1 process: 1 internal.
INFO: Build completed successfully, 1 total action
INFO: Build completed successfully, 1 total action
3.9.10 (main, Feb 27 2022, 00:07:43) 
[Clang 13.0.0 (clang-1300.0.29.30)]
Hello world
TLS seems OK
```

