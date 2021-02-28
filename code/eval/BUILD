load("@python_deps//:requirements.bzl", "requirement")

py_binary(
  name = "code_eval_service",
  srcs = ["code_eval_service.py"],
  deps = [
    "//code/eval/proto:code_eval_python_grpc",
    "//code/eval/proto:code_eval_python_proto",
    requirement("absl-py"),
    requirement("docker"),
    requirement("grpcio"),
  ]
)