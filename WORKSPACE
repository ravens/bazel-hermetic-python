load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    sha256 = "954aa89b491be4a083304a2cb838019c8b8c3720a7abb9c4cb81ac7a24230cea",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_python/releases/download/0.4.0/rules_python-0.4.0.tar.gz",
        "https://github.com/bazelbuild/rules_python/releases/download/0.4.0/rules_python-0.4.0.tar.gz",
    ],
)

RULES_FOREIGN_CC_VERSION="0.7.1"
http_archive(
    name = "rules_foreign_cc",
    sha256 = "bcd0c5f46a49b85b384906daae41d277b3dc0ff27c7c752cc51e43048a58ec83",
    strip_prefix = "rules_foreign_cc-{0}".format(RULES_FOREIGN_CC_VERSION),
    url = "https://github.com/bazelbuild/rules_foreign_cc/archive/{0}.tar.gz".format(RULES_FOREIGN_CC_VERSION),
)

load("@rules_foreign_cc//foreign_cc:repositories.bzl", "rules_foreign_cc_dependencies")
rules_foreign_cc_dependencies(register_default_tools = True)

OPENSSL_VERSION="1.1.1k"
http_archive(
    name = "openssl",
    build_file = "@//:openssl.BUILD",
    strip_prefix = "openssl-{0}".format(OPENSSL_VERSION),
    sha256 = "892a0875b9872acd04a9fde79b1f943075d5ea162415de3047c327df33fbaee5",
    urls = ["https://mirror.bazel.build/www.openssl.org/source/openssl-{0}.tar.gz".format(OPENSSL_VERSION)],
)

PYTHON_VERSION="3.9.10"
http_archive(
    name = "python3_interpreter",
    urls = ["https://www.python.org/ftp/python/{0}/Python-{0}.tar.xz".format(PYTHON_VERSION)],
    sha256 = "0a8fbfb5287ebc3a13e9baf3d54e08fa06778ffeccf6311aef821bb3a6586cc8",
    strip_prefix = "Python-{0}".format(PYTHON_VERSION),
    build_file = "@//:python.BUILD",
)

register_toolchains("//:my_py_toolchain")

# load("@rules_python//python:pip.bzl", "pip_install")

# pip_install(
#     name = "pip",
#     requirements = "//:requirements.txt",
#     # YG: does not work as we need a file under a target, and we have only the source at this stage - no python interpreter, of course.
#     # python_interpreter_target = "@python3_interpreter//:python3_bin",
# )

load("@rules_python//python:pip.bzl", "pip_parse")
pip_parse(
    name = "pip_parsed_deps",
    enable_implicit_namespace_pkgs = True,
    extra_pip_args = ["--no-cache-dir"],
    requirements_lock = "//:requirements.txt",
)
load("@pip_parsed_deps//:requirements.bzl", install_parsed_pip_deps="install_deps")
install_parsed_pip_deps()