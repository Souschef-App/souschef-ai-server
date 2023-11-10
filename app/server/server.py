from concurrent import futures

import grpc
import helloworld_pb2
import helloworld_pb2_grpc

class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message="Hello, %s!" % request.name)

class Server:
     def __init__(self):
        self.port = "50051"
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), self.server)
        self.server.add_insecure_port("[::]:" + self.port)