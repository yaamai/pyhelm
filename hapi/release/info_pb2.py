# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hapi/release/info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from hapi.release import status_pb2 as hapi_dot_release_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hapi/release/info.proto',
  package='hapi.release',
  syntax='proto3',
  serialized_pb=_b('\n\x17hapi/release/info.proto\x12\x0chapi.release\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19hapi/release/status.proto\"\xd5\x01\n\x04Info\x12$\n\x06status\x18\x01 \x01(\x0b\x32\x14.hapi.release.Status\x12\x32\n\x0e\x66irst_deployed\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rlast_deployed\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07\x64\x65leted\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x44\x65scription\x18\x05 \x01(\tB\tZ\x07releaseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,hapi_dot_release_dot_status__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_INFO = _descriptor.Descriptor(
  name='Info',
  full_name='hapi.release.Info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='hapi.release.Info.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='first_deployed', full_name='hapi.release.Info.first_deployed', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_deployed', full_name='hapi.release.Info.last_deployed', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deleted', full_name='hapi.release.Info.deleted', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Description', full_name='hapi.release.Info.Description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=315,
)

_INFO.fields_by_name['status'].message_type = hapi_dot_release_dot_status__pb2._STATUS
_INFO.fields_by_name['first_deployed'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_INFO.fields_by_name['last_deployed'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_INFO.fields_by_name['deleted'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Info'] = _INFO

Info = _reflection.GeneratedProtocolMessageType('Info', (_message.Message,), dict(
  DESCRIPTOR = _INFO,
  __module__ = 'hapi.release.info_pb2'
  # @@protoc_insertion_point(class_scope:hapi.release.Info)
  ))
_sym_db.RegisterMessage(Info)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\007release'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
