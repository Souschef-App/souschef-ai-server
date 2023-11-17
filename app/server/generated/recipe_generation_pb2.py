# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: recipe_generation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17recipe_generation.proto\"-\n\x16RecipeBreakdownRequest\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\"7\n\x10RetryTaskRequest\x12\x13\n\x04task\x18\x01 \x01(\x0b\x32\x05.Task\x12\x0e\n\x06prompt\x18\x02 \x01(\t\":\n\nIngredient\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x02\x12\x0c\n\x04unit\x18\x03 \x01(\t\"-\n\x0bKitchenware\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x05\"\xb9\x01\n\x04Task\x12\x0c\n\x04uuid\x18\x01 \x01(\x0c\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x12\n\ndifficulty\x18\x04 \x01(\x05\x12\x10\n\x08\x64uration\x18\x05 \x01(\x05\x12 \n\x0bingredients\x18\x06 \x03(\x0b\x32\x0b.Ingredient\x12!\n\x0bkitchenware\x18\x07 \x03(\x0b\x32\x0c.Kitchenware\x12\x14\n\x0c\x64\x65pendencies\x18\x08 \x03(\x0c\",\n\x14RecipeBreakdownReply\x12\x14\n\x05tasks\x18\x01 \x03(\x0b\x32\x05.Task\",\n\x15RetryTaskRequestReply\x12\x13\n\x04task\x18\x01 \x01(\x0b\x32\x05.Task2\xde\x01\n\x10RecipeGeneration\x12\x46\n\x12getRecipeBreakDown\x12\x17.RecipeBreakdownRequest\x1a\x15.RecipeBreakdownReply\"\x00\x12H\n\x14retryRecipeBreakDown\x12\x17.RecipeBreakdownRequest\x1a\x15.RecipeBreakdownReply\"\x00\x12\x38\n\tretryTask\x12\x11.RetryTaskRequest\x1a\x16.RetryTaskRequestReply\"\x00\x42-\xaa\x02*souschef.server.Services.SubtaskGenerationb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'recipe_generation_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002*souschef.server.Services.SubtaskGeneration'
  _globals['_RECIPEBREAKDOWNREQUEST']._serialized_start=27
  _globals['_RECIPEBREAKDOWNREQUEST']._serialized_end=72
  _globals['_RETRYTASKREQUEST']._serialized_start=74
  _globals['_RETRYTASKREQUEST']._serialized_end=129
  _globals['_INGREDIENT']._serialized_start=131
  _globals['_INGREDIENT']._serialized_end=189
  _globals['_KITCHENWARE']._serialized_start=191
  _globals['_KITCHENWARE']._serialized_end=236
  _globals['_TASK']._serialized_start=239
  _globals['_TASK']._serialized_end=424
  _globals['_RECIPEBREAKDOWNREPLY']._serialized_start=426
  _globals['_RECIPEBREAKDOWNREPLY']._serialized_end=470
  _globals['_RETRYTASKREQUESTREPLY']._serialized_start=472
  _globals['_RETRYTASKREQUESTREPLY']._serialized_end=516
  _globals['_RECIPEGENERATION']._serialized_start=519
  _globals['_RECIPEGENERATION']._serialized_end=741
# @@protoc_insertion_point(module_scope)
