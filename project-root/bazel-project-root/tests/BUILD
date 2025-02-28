load("@rules_python//python:defs.bzl", "py_test")

# Define unit tests
py_test(
    name = "test_math_utils",
    srcs = ["test_math_utils.py"],
    deps = [
        "//src:math_utils",
        "@pip_deps//pytest",
    ],
)
py_test(
    name="test_string_utils",
    srcs=["test_string_utils.py"],
    deps=[
        "//src:string_utils"
        ],
)
