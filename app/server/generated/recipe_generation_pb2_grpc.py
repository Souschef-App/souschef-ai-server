# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import recipe_generation_pb2 as recipe__generation__pb2


class RecipeGenerationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getRecipeBreakDown = channel.unary_unary(
                '/RecipeGeneration/getRecipeBreakDown',
                request_serializer=recipe__generation__pb2.RecipeBreakdownRequest.SerializeToString,
                response_deserializer=recipe__generation__pb2.RecipeBreakdownReply.FromString,
                )
        self.retryRecipeBreakDown = channel.unary_unary(
                '/RecipeGeneration/retryRecipeBreakDown',
                request_serializer=recipe__generation__pb2.RecipeBreakdownRequest.SerializeToString,
                response_deserializer=recipe__generation__pb2.RecipeBreakdownReply.FromString,
                )
        self.retryTask = channel.unary_unary(
                '/RecipeGeneration/retryTask',
                request_serializer=recipe__generation__pb2.RetryTaskRequest.SerializeToString,
                response_deserializer=recipe__generation__pb2.RetryTaskRequestReply.FromString,
                )


class RecipeGenerationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getRecipeBreakDown(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def retryRecipeBreakDown(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def retryTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RecipeGenerationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getRecipeBreakDown': grpc.unary_unary_rpc_method_handler(
                    servicer.getRecipeBreakDown,
                    request_deserializer=recipe__generation__pb2.RecipeBreakdownRequest.FromString,
                    response_serializer=recipe__generation__pb2.RecipeBreakdownReply.SerializeToString,
            ),
            'retryRecipeBreakDown': grpc.unary_unary_rpc_method_handler(
                    servicer.retryRecipeBreakDown,
                    request_deserializer=recipe__generation__pb2.RecipeBreakdownRequest.FromString,
                    response_serializer=recipe__generation__pb2.RecipeBreakdownReply.SerializeToString,
            ),
            'retryTask': grpc.unary_unary_rpc_method_handler(
                    servicer.retryTask,
                    request_deserializer=recipe__generation__pb2.RetryTaskRequest.FromString,
                    response_serializer=recipe__generation__pb2.RetryTaskRequestReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RecipeGeneration', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RecipeGeneration(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getRecipeBreakDown(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RecipeGeneration/getRecipeBreakDown',
            recipe__generation__pb2.RecipeBreakdownRequest.SerializeToString,
            recipe__generation__pb2.RecipeBreakdownReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def retryRecipeBreakDown(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RecipeGeneration/retryRecipeBreakDown',
            recipe__generation__pb2.RecipeBreakdownRequest.SerializeToString,
            recipe__generation__pb2.RecipeBreakdownReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def retryTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RecipeGeneration/retryTask',
            recipe__generation__pb2.RetryTaskRequest.SerializeToString,
            recipe__generation__pb2.RetryTaskRequestReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
