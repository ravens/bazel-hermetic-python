load("@rules_foreign_cc//foreign_cc:defs.bzl", "configure_make")

filegroup(
    name = "all", 
    srcs = glob(["**"]),
)

configure_make(
    name = "openssl",
    args = ["-j $(nproc)"],
    configure_command = "config",
    configure_in_place = True,
    configure_options = [
        "no-comp",
        "no-idea",
        "no-weak-ssl-ciphers",
        "no-shared",
    ],
    env = select({
        "@platforms//os:macos": {
            "AR": "",
        },
        "//conditions:default": {
        },
    }),
    lib_source = "@openssl//:all",
    out_static_libs = [
        "libssl.a",
        "libcrypto.a",
    ],
    targets = [
        "build_libs",
        "install_dev",
    ],
    visibility = ["//visibility:public"],
)