load("@rules_foreign_cc//foreign_cc:defs.bzl", "configure_make")

exports_files(["python_bin"])

filegroup(
    name = "all", 
    srcs = glob(["**"]),
)

configure_make(
    name = "python3",
    args = ["-j $(nproc)"],
    configure_options = [
        "CFLAGS='-Dredacted=\"redacted\"'",
        "--with-openssl=$EXT_BUILD_DEPS/openssl",
        "--enable-optimizations",
    ],
    env = select({
        "@platforms//os:macos": {"AR": ""},
        "//conditions:default": {},
    }),
    features = select({
        "@platforms//os:macos": ["-headerpad"],
        "//conditions:default": {},
    }),
    install_prefix = "py_install",
    lib_source = "@python3_interpreter//:all",
    out_binaries = [
        "python3.9",
    ],
    out_data_dirs = ["lib"],
    deps = [
        "@openssl",
    ],
    visibility = ["//visibility:public"],
)

filegroup(
    name = "python3_bin",
    srcs = [":python3"],
    output_group = "python3.9",
    visibility = ["//visibility:public"],
)
