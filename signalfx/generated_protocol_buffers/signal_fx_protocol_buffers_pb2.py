# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: signal_fx_protocol_buffers.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='signal_fx_protocol_buffers.proto',
  package='com.signalfx.metrics.protobuf',
  serialized_pb='\n signal_fx_protocol_buffers.proto\x12\x1d\x63om.signalfx.metrics.protobuf\"@\n\x05\x44\x61tum\x12\x10\n\x08strValue\x18\x01 \x01(\t\x12\x13\n\x0b\x64oubleValue\x18\x02 \x01(\x01\x12\x10\n\x08intValue\x18\x03 \x01(\x03\"\'\n\tDimension\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xf0\x01\n\tDataPoint\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x0e\n\x06metric\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12\x33\n\x05value\x18\x04 \x01(\x0b\x32$.com.signalfx.metrics.protobuf.Datum\x12=\n\nmetricType\x18\x05 \x01(\x0e\x32).com.signalfx.metrics.protobuf.MetricType\x12<\n\ndimensions\x18\x06 \x03(\x0b\x32(.com.signalfx.metrics.protobuf.Dimension\"V\n\x16\x44\x61taPointUploadMessage\x12<\n\ndatapoints\x18\x01 \x03(\x0b\x32(.com.signalfx.metrics.protobuf.DataPoint\"T\n\nPointValue\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12\x33\n\x05value\x18\x04 \x01(\x0b\x32$.com.signalfx.metrics.protobuf.Datum*F\n\nMetricType\x12\t\n\x05GAUGE\x10\x00\x12\x0b\n\x07\x43OUNTER\x10\x01\x12\x08\n\x04\x45NUM\x10\x02\x12\x16\n\x12\x43UMULATIVE_COUNTER\x10\x03')

_METRICTYPE = _descriptor.EnumDescriptor(
  name='MetricType',
  full_name='com.signalfx.metrics.protobuf.MetricType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GAUGE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COUNTER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENUM', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUMULATIVE_COUNTER', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=591,
  serialized_end=661,
)

MetricType = enum_type_wrapper.EnumTypeWrapper(_METRICTYPE)
GAUGE = 0
COUNTER = 1
ENUM = 2
CUMULATIVE_COUNTER = 3



_DATUM = _descriptor.Descriptor(
  name='Datum',
  full_name='com.signalfx.metrics.protobuf.Datum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='strValue', full_name='com.signalfx.metrics.protobuf.Datum.strValue', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='doubleValue', full_name='com.signalfx.metrics.protobuf.Datum.doubleValue', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='intValue', full_name='com.signalfx.metrics.protobuf.Datum.intValue', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=67,
  serialized_end=131,
)


_DIMENSION = _descriptor.Descriptor(
  name='Dimension',
  full_name='com.signalfx.metrics.protobuf.Dimension',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.signalfx.metrics.protobuf.Dimension.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.signalfx.metrics.protobuf.Dimension.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=133,
  serialized_end=172,
)


_DATAPOINT = _descriptor.Descriptor(
  name='DataPoint',
  full_name='com.signalfx.metrics.protobuf.DataPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='com.signalfx.metrics.protobuf.DataPoint.source', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metric', full_name='com.signalfx.metrics.protobuf.DataPoint.metric', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='com.signalfx.metrics.protobuf.DataPoint.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.signalfx.metrics.protobuf.DataPoint.value', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metricType', full_name='com.signalfx.metrics.protobuf.DataPoint.metricType', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dimensions', full_name='com.signalfx.metrics.protobuf.DataPoint.dimensions', index=5,
      number=6, type=11, cpp_type=10, label=3,
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
  serialized_start=175,
  serialized_end=415,
)


_DATAPOINTUPLOADMESSAGE = _descriptor.Descriptor(
  name='DataPointUploadMessage',
  full_name='com.signalfx.metrics.protobuf.DataPointUploadMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='datapoints', full_name='com.signalfx.metrics.protobuf.DataPointUploadMessage.datapoints', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=417,
  serialized_end=503,
)


_POINTVALUE = _descriptor.Descriptor(
  name='PointValue',
  full_name='com.signalfx.metrics.protobuf.PointValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='com.signalfx.metrics.protobuf.PointValue.timestamp', index=0,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.signalfx.metrics.protobuf.PointValue.value', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=505,
  serialized_end=589,
)

_DATAPOINT.fields_by_name['value'].message_type = _DATUM
_DATAPOINT.fields_by_name['metricType'].enum_type = _METRICTYPE
_DATAPOINT.fields_by_name['dimensions'].message_type = _DIMENSION
_DATAPOINTUPLOADMESSAGE.fields_by_name['datapoints'].message_type = _DATAPOINT
_POINTVALUE.fields_by_name['value'].message_type = _DATUM
DESCRIPTOR.message_types_by_name['Datum'] = _DATUM
DESCRIPTOR.message_types_by_name['Dimension'] = _DIMENSION
DESCRIPTOR.message_types_by_name['DataPoint'] = _DATAPOINT
DESCRIPTOR.message_types_by_name['DataPointUploadMessage'] = _DATAPOINTUPLOADMESSAGE
DESCRIPTOR.message_types_by_name['PointValue'] = _POINTVALUE

class Datum(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DATUM

  # @@protoc_insertion_point(class_scope:com.signalfx.metrics.protobuf.Datum)

class Dimension(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DIMENSION

  # @@protoc_insertion_point(class_scope:com.signalfx.metrics.protobuf.Dimension)

class DataPoint(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DATAPOINT

  # @@protoc_insertion_point(class_scope:com.signalfx.metrics.protobuf.DataPoint)

class DataPointUploadMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DATAPOINTUPLOADMESSAGE

  # @@protoc_insertion_point(class_scope:com.signalfx.metrics.protobuf.DataPointUploadMessage)

class PointValue(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _POINTVALUE

  # @@protoc_insertion_point(class_scope:com.signalfx.metrics.protobuf.PointValue)


# @@protoc_insertion_point(module_scope)
