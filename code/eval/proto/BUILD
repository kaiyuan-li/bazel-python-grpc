load("@rules_proto//proto:defs.bzl", "proto_library")
load("@rules_proto_grpc//python:defs.bzl", "python_grpc_library")

proto_library(
    name = "code_eval_proto",
    srcs = ["code_eval.proto"],
    visibility = ["//visibility:public"],
)

python_grpc_library(
  name = "code_eval_python_grpc",
  protos = [":code_eval_proto"],
  visibility = ["//visibility:public"],
)