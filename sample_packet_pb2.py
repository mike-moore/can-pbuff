# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sample_packet.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sample_packet.proto',
  package='',
  serialized_pb='\n\x13sample_packet.proto\";\n\x08WayPoint\x12\x0f\n\x07Heading\x18\x01 \x02(\x02\x12\x10\n\x08\x44istance\x18\x02 \x02(\x02\x12\x0c\n\x04Name\x18\x03 \x02(\t\"-\n\x10IdValuePairFloat\x12\n\n\x02Id\x18\x01 \x02(\r\x12\r\n\x05Value\x18\x02 \x01(\x02\"U\n\rCommandPacket\x12\x1e\n\x0bWayPointCmd\x18\x01 \x01(\x0b\x32\t.WayPoint\x12$\n\tRoverCmds\x18\x02 \x03(\x0b\x32\x11.IdValuePairFloat\"\x84\x01\n\x0fTelemetryPacket\x12\x17\n\x0fMeasuredHeading\x18\x01 \x02(\x02\x12\x18\n\x10MeasuredDistance\x18\x02 \x02(\x02\x12&\n\x0bRoverStatus\x18\x03 \x03(\x0b\x32\x11.IdValuePairFloat\x12\x16\n\x0e\x41\x63tiveWayPoint\x18\x04 \x01(\t')




_WAYPOINT = _descriptor.Descriptor(
  name='WayPoint',
  full_name='WayPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Heading', full_name='WayPoint.Heading', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Distance', full_name='WayPoint.Distance', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Name', full_name='WayPoint.Name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=23,
  serialized_end=82,
)


_IDVALUEPAIRFLOAT = _descriptor.Descriptor(
  name='IdValuePairFloat',
  full_name='IdValuePairFloat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id', full_name='IdValuePairFloat.Id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Value', full_name='IdValuePairFloat.Value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=84,
  serialized_end=129,
)


_COMMANDPACKET = _descriptor.Descriptor(
  name='CommandPacket',
  full_name='CommandPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='WayPointCmd', full_name='CommandPacket.WayPointCmd', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RoverCmds', full_name='CommandPacket.RoverCmds', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=131,
  serialized_end=216,
)


_TELEMETRYPACKET = _descriptor.Descriptor(
  name='TelemetryPacket',
  full_name='TelemetryPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='MeasuredHeading', full_name='TelemetryPacket.MeasuredHeading', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MeasuredDistance', full_name='TelemetryPacket.MeasuredDistance', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RoverStatus', full_name='TelemetryPacket.RoverStatus', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ActiveWayPoint', full_name='TelemetryPacket.ActiveWayPoint', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=219,
  serialized_end=351,
)

_COMMANDPACKET.fields_by_name['WayPointCmd'].message_type = _WAYPOINT
_COMMANDPACKET.fields_by_name['RoverCmds'].message_type = _IDVALUEPAIRFLOAT
_TELEMETRYPACKET.fields_by_name['RoverStatus'].message_type = _IDVALUEPAIRFLOAT
DESCRIPTOR.message_types_by_name['WayPoint'] = _WAYPOINT
DESCRIPTOR.message_types_by_name['IdValuePairFloat'] = _IDVALUEPAIRFLOAT
DESCRIPTOR.message_types_by_name['CommandPacket'] = _COMMANDPACKET
DESCRIPTOR.message_types_by_name['TelemetryPacket'] = _TELEMETRYPACKET

class WayPoint(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WAYPOINT

  # @@protoc_insertion_point(class_scope:WayPoint)

class IdValuePairFloat(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _IDVALUEPAIRFLOAT

  # @@protoc_insertion_point(class_scope:IdValuePairFloat)

class CommandPacket(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COMMANDPACKET

  # @@protoc_insertion_point(class_scope:CommandPacket)

class TelemetryPacket(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TELEMETRYPACKET

  # @@protoc_insertion_point(class_scope:TelemetryPacket)


# @@protoc_insertion_point(module_scope)
