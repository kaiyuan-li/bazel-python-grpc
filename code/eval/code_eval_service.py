'''
A python server to evaluate code that's passed in through gRPC
'''

import docker
import grpc

from absl import logging

from code.eval.proto import code_eval_pb2
from code.eval.proto import code_eval_pb2_grpc


class CodeEvalService(code_eval_pb2_grpc.CodeEvalService):
  def Eval(req: code_eval_pb2.CodeEvalRequest):
    return code_eval_pb2.CodeEvalResponse(stdout=req.code)


def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  code_eval_pb2.add_CodeEvalService_to_server(
    CodeEvalService(), server
  )
  server.add_insecure_port('[::]:31415')
  server.start()
  logging.info('server started')
  server.wait_for_termination()

if __name__ == '__main__':
  client = docker.from_env()
  containers_list = client.containers.list()
  print(f'containers_list: {containers_list}')

  serve()