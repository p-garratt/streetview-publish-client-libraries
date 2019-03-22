# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/streetview/publish_v1/proto/resources.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/streetview/publish_v1/proto/resources.proto',
  package='google.streetview.publish.v1',
  syntax='proto3',
  serialized_options=_b('\n(com.google.geo.ugc.streetview.publish.v1B\032StreetViewPublishResourcesZCgoogle.golang.org/genproto/googleapis/streetview/publish/v1;publish'),
  serialized_pb=_b('\n2google/streetview/publish_v1/proto/resources.proto\x12\x1cgoogle.streetview.publish.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x18google/type/latlng.proto\"\x1f\n\tUploadRef\x12\x12\n\nupload_url\x18\x01 \x01(\t\"\x15\n\x07PhotoId\x12\n\n\x02id\x18\x01 \x01(\t\"%\n\x05Level\x12\x0e\n\x06number\x18\x01 \x01(\x01\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xbe\x01\n\x04Pose\x12)\n\x0clat_lng_pair\x18\x01 \x01(\x0b\x32\x13.google.type.LatLng\x12\x10\n\x08\x61ltitude\x18\x02 \x01(\x01\x12\x0f\n\x07heading\x18\x03 \x01(\x01\x12\r\n\x05pitch\x18\x04 \x01(\x01\x12\x0c\n\x04roll\x18\x05 \x01(\x01\x12\x32\n\x05level\x18\x07 \x01(\x0b\x32#.google.streetview.publish.v1.Level\x12\x17\n\x0f\x61\x63\x63uracy_meters\x18\t \x01(\x02\">\n\x05Place\x12\x10\n\x08place_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\rlanguage_code\x18\x03 \x01(\t\"C\n\nConnection\x12\x35\n\x06target\x18\x01 \x01(\x0b\x32%.google.streetview.publish.v1.PhotoId\"\xd8\x06\n\x05Photo\x12\x37\n\x08photo_id\x18\x01 \x01(\x0b\x32%.google.streetview.publish.v1.PhotoId\x12\x41\n\x10upload_reference\x18\x02 \x01(\x0b\x32\'.google.streetview.publish.v1.UploadRef\x12\x14\n\x0c\x64ownload_url\x18\x03 \x01(\t\x12\x15\n\rthumbnail_url\x18\t \x01(\t\x12\x12\n\nshare_link\x18\x0b \x01(\t\x12\x30\n\x04pose\x18\x04 \x01(\x0b\x32\".google.streetview.publish.v1.Pose\x12=\n\x0b\x63onnections\x18\x05 \x03(\x0b\x32(.google.streetview.publish.v1.Connection\x12\x30\n\x0c\x63\x61pture_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x06places\x18\x07 \x03(\x0b\x32#.google.streetview.publish.v1.Place\x12\x12\n\nview_count\x18\n \x01(\x03\x12K\n\x0ftransfer_status\x18\x0c \x01(\x0e\x32\x32.google.streetview.publish.v1.Photo.TransferStatus\x12R\n\x13maps_publish_status\x18\r \x01(\x0e\x32\x35.google.streetview.publish.v1.Photo.MapsPublishStatus\"\xa5\x01\n\x0eTransferStatus\x12\x1b\n\x17TRANSFER_STATUS_UNKNOWN\x10\x00\x12\x15\n\x11NEVER_TRANSFERRED\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\r\n\tCOMPLETED\x10\x03\x12\x0c\n\x08REJECTED\x10\x04\x12\x0b\n\x07\x45XPIRED\x10\x05\x12\r\n\tCANCELLED\x10\x06\x12\x19\n\x15RECEIVED_VIA_TRANSFER\x10\x07\"]\n\x11MapsPublishStatus\x12#\n\x1fUNSPECIFIED_MAPS_PUBLISH_STATUS\x10\x00\x12\r\n\tPUBLISHED\x10\x01\x12\x14\n\x10REJECTED_UNKNOWN\x10\x02\x42\x8b\x01\n(com.google.geo.ugc.streetview.publish.v1B\x1aStreetViewPublishResourcesZCgoogle.golang.org/genproto/googleapis/streetview/publish/v1;publishb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_type_dot_latlng__pb2.DESCRIPTOR,])



_PHOTO_TRANSFERSTATUS = _descriptor.EnumDescriptor(
  name='TransferStatus',
  full_name='google.streetview.publish.v1.Photo.TransferStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TRANSFER_STATUS_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEVER_TRANSFERRED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECTED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPIRED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCELLED', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RECEIVED_VIA_TRANSFER', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1191,
  serialized_end=1356,
)
_sym_db.RegisterEnumDescriptor(_PHOTO_TRANSFERSTATUS)

_PHOTO_MAPSPUBLISHSTATUS = _descriptor.EnumDescriptor(
  name='MapsPublishStatus',
  full_name='google.streetview.publish.v1.Photo.MapsPublishStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED_MAPS_PUBLISH_STATUS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PUBLISHED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECTED_UNKNOWN', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1358,
  serialized_end=1451,
)
_sym_db.RegisterEnumDescriptor(_PHOTO_MAPSPUBLISHSTATUS)


_UPLOADREF = _descriptor.Descriptor(
  name='UploadRef',
  full_name='google.streetview.publish.v1.UploadRef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='upload_url', full_name='google.streetview.publish.v1.UploadRef.upload_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=173,
  serialized_end=204,
)


_PHOTOID = _descriptor.Descriptor(
  name='PhotoId',
  full_name='google.streetview.publish.v1.PhotoId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.streetview.publish.v1.PhotoId.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=206,
  serialized_end=227,
)


_LEVEL = _descriptor.Descriptor(
  name='Level',
  full_name='google.streetview.publish.v1.Level',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='google.streetview.publish.v1.Level.number', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.streetview.publish.v1.Level.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=229,
  serialized_end=266,
)


_POSE = _descriptor.Descriptor(
  name='Pose',
  full_name='google.streetview.publish.v1.Pose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lat_lng_pair', full_name='google.streetview.publish.v1.Pose.lat_lng_pair', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='google.streetview.publish.v1.Pose.altitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='heading', full_name='google.streetview.publish.v1.Pose.heading', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pitch', full_name='google.streetview.publish.v1.Pose.pitch', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roll', full_name='google.streetview.publish.v1.Pose.roll', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='google.streetview.publish.v1.Pose.level', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accuracy_meters', full_name='google.streetview.publish.v1.Pose.accuracy_meters', index=6,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=269,
  serialized_end=459,
)


_PLACE = _descriptor.Descriptor(
  name='Place',
  full_name='google.streetview.publish.v1.Place',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='place_id', full_name='google.streetview.publish.v1.Place.place_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.streetview.publish.v1.Place.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language_code', full_name='google.streetview.publish.v1.Place.language_code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=461,
  serialized_end=523,
)


_CONNECTION = _descriptor.Descriptor(
  name='Connection',
  full_name='google.streetview.publish.v1.Connection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='google.streetview.publish.v1.Connection.target', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=525,
  serialized_end=592,
)


_PHOTO = _descriptor.Descriptor(
  name='Photo',
  full_name='google.streetview.publish.v1.Photo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='photo_id', full_name='google.streetview.publish.v1.Photo.photo_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upload_reference', full_name='google.streetview.publish.v1.Photo.upload_reference', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='download_url', full_name='google.streetview.publish.v1.Photo.download_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='thumbnail_url', full_name='google.streetview.publish.v1.Photo.thumbnail_url', index=3,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='share_link', full_name='google.streetview.publish.v1.Photo.share_link', index=4,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pose', full_name='google.streetview.publish.v1.Photo.pose', index=5,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connections', full_name='google.streetview.publish.v1.Photo.connections', index=6,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capture_time', full_name='google.streetview.publish.v1.Photo.capture_time', index=7,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='places', full_name='google.streetview.publish.v1.Photo.places', index=8,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='view_count', full_name='google.streetview.publish.v1.Photo.view_count', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transfer_status', full_name='google.streetview.publish.v1.Photo.transfer_status', index=10,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maps_publish_status', full_name='google.streetview.publish.v1.Photo.maps_publish_status', index=11,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PHOTO_TRANSFERSTATUS,
    _PHOTO_MAPSPUBLISHSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=595,
  serialized_end=1451,
)

_POSE.fields_by_name['lat_lng_pair'].message_type = google_dot_type_dot_latlng__pb2._LATLNG
_POSE.fields_by_name['level'].message_type = _LEVEL
_CONNECTION.fields_by_name['target'].message_type = _PHOTOID
_PHOTO.fields_by_name['photo_id'].message_type = _PHOTOID
_PHOTO.fields_by_name['upload_reference'].message_type = _UPLOADREF
_PHOTO.fields_by_name['pose'].message_type = _POSE
_PHOTO.fields_by_name['connections'].message_type = _CONNECTION
_PHOTO.fields_by_name['capture_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PHOTO.fields_by_name['places'].message_type = _PLACE
_PHOTO.fields_by_name['transfer_status'].enum_type = _PHOTO_TRANSFERSTATUS
_PHOTO.fields_by_name['maps_publish_status'].enum_type = _PHOTO_MAPSPUBLISHSTATUS
_PHOTO_TRANSFERSTATUS.containing_type = _PHOTO
_PHOTO_MAPSPUBLISHSTATUS.containing_type = _PHOTO
DESCRIPTOR.message_types_by_name['UploadRef'] = _UPLOADREF
DESCRIPTOR.message_types_by_name['PhotoId'] = _PHOTOID
DESCRIPTOR.message_types_by_name['Level'] = _LEVEL
DESCRIPTOR.message_types_by_name['Pose'] = _POSE
DESCRIPTOR.message_types_by_name['Place'] = _PLACE
DESCRIPTOR.message_types_by_name['Connection'] = _CONNECTION
DESCRIPTOR.message_types_by_name['Photo'] = _PHOTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UploadRef = _reflection.GeneratedProtocolMessageType('UploadRef', (_message.Message,), dict(
  DESCRIPTOR = _UPLOADREF,
  __module__ = 'google.streetview.publish_v1.proto.resources_pb2'
  ,
  __doc__ = """Upload reference for media files.
  
  
  Attributes:
      upload_url:
          Required. An upload reference should be unique for each user.
          It follows the form: "https://streetviewpublish.googleapis.com
          /media/user/{account\_id}/photo/{upload\_reference}"
  """,
  # @@protoc_insertion_point(class_scope:google.streetview.publish.v1.UploadRef)
  ))
_sym_db.RegisterMessage(UploadRef)

PhotoId = _reflection.GeneratedProtocolMessageType('PhotoId', (_message.Message,), dict(
  DESCRIPTOR = _PHOTOID,
  __module__ = 'google.streetview.publish_v1.proto.resources_pb2'
  ,
  __doc__ = """Identifier for a [Photo][google.streetview.publish.v1.Photo].
  
  
  Attributes:
      id:
          Required. A unique identifier for a photo.
  """,
  # @@protoc_insertion_point(class_scope:google.streetview.publish.v1.PhotoId)
  ))
_sym_db.RegisterMessage(PhotoId)

Level = _reflection.GeneratedProtocolMessageType('Level', (_message.Message,), dict(
  DESCRIPTOR = _LEVEL,
  __module__ = 'google.streetview.publish_v1.proto.resources_pb2'
  ,
  __doc__ = """Level information containing level number and its corresponding name.
  
  
  Attributes:
      number:
          Floor number, used for ordering. 0 indicates the ground level,
          1 indicates the first level above ground level, -1 indicates
          the first level under ground level. Non-integer values are OK.
      name:
          Required. A name assigned to this Level, restricted to 3
          characters. Consider how the elevator buttons would be labeled
          for this level if there was an elevator.
  """,
  # @@protoc_insertion_point(class_scope:google.streetview.publish.v1.Level)
  ))
_sym_db.RegisterMessage(Level)

Pose = _reflection.GeneratedProtocolMessageType('Pose', (_message.Message,), dict(
  DESCRIPTOR = _POSE,
  __module__ = 'google.streetview.publish_v1.proto.resources_pb2'
  ,
  __doc__ = """Raw pose measurement for an entity.
  
  
  Attributes:
      lat_lng_pair:
          Latitude and longitude pair of the pose, as explained here: ht
          tps://cloud.google.com/datastore/docs/reference/rest/Shared.Ty
          pes/LatLng When creating a
          [Photo][google.streetview.publish.v1.Photo], if the latitude
          and longitude pair are not provided, the geolocation from the
          exif header is used. A latitude and longitude pair not
          provided in the photo or exif header causes the create photo
          process to fail.
      altitude:
          Altitude of the pose in meters above WGS84 ellipsoid. NaN
          indicates an unmeasured quantity.
      heading:
          Compass heading, measured at the center of the photo in
          degrees clockwise from North. Value must be >=0 and <360. NaN
          indicates an unmeasured quantity.
      pitch:
          Pitch, measured at the center of the photo in degrees. Value
          must be >=-90 and <= 90. A value of -90 means looking directly
          down, and a value of 90 means looking directly up. NaN
          indicates an unmeasured quantity.
      roll:
          Roll, measured in degrees. Value must be >= 0 and <360. A
          value of 0 means level with the horizon. NaN indicates an
          unmeasured quantity.
      level:
          Level (the floor in a building) used to configure vertical
          navigation.
      accuracy_meters:
          The estimated horizontal accuracy of this pose in meters with
          68% confidence (one standard deviation). For example, on
          Android, this value is available from this method: https://dev
          eloper.android.com/reference/android/location/Location#getAccu
          racy(). Other platforms have different methods of obtaining
          similar accuracy estimations.
  """,
  # @@protoc_insertion_point(class_scope:google.streetview.publish.v1.Pose)
  ))
_sym_db.RegisterMessage(Pose)

Place = _reflection.GeneratedProtocolMessageType('Place', (_message.Message,), dict(
  DESCRIPTOR = _PLACE,
  __module__ = 'google.streetview.publish_v1.proto.resources_pb2'
  ,
  __doc__ = """Place metadata for an entity.
  
  
  Attributes:
      place_id:
          Place identifier, as described in
          https://developers.google.com/places/place-id.
      name:
          Output-only. The name of the place, localized to the
          language\_code.
      language_code:
          Output-only. The language\_code that the name is localized
          with. This should be the language\_code specified in the
          request, but may be a fallback.
  """,
  # @@protoc_insertion_point(class_scope:google.streetview.publish.v1.Place)
  ))
_sym_db.RegisterMessage(Place)

Connection = _reflection.GeneratedProtocolMessageType('Connection', (_message.Message,), dict(
  DESCRIPTOR = _CONNECTION,
  __module__ = 'google.streetview.publish_v1.proto.resources_pb2'
  ,
  __doc__ = """A connection is the link from a source photo to a destination photo.
  
  
  Attributes:
      target:
          Required. The destination of the connection from the
          containing photo to another photo.
  """,
  # @@protoc_insertion_point(class_scope:google.streetview.publish.v1.Connection)
  ))
_sym_db.RegisterMessage(Connection)

Photo = _reflection.GeneratedProtocolMessageType('Photo', (_message.Message,), dict(
  DESCRIPTOR = _PHOTO,
  __module__ = 'google.streetview.publish_v1.proto.resources_pb2'
  ,
  __doc__ = """Photo is used to store 360 photos along with photo metadata.
  
  
  Attributes:
      photo_id:
          Required when updating a photo. Output only when creating a
          photo. Identifier for the photo, which is unique among all
          photos in Google.
      upload_reference:
          Required when creating a photo. Input only. The resource URL
          where the photo bytes are uploaded to.
      download_url:
          Output only. The download URL for the photo bytes. This field
          is set only when [GetPhotoRequest.view][google.streetview.publ
          ish.v1.GetPhotoRequest.view] is set to [PhotoView.INCLUDE\_DOW
          NLOAD\_URL][google.streetview.publish.v1.PhotoView.INCLUDE\_DO
          WNLOAD\_URL].
      thumbnail_url:
          Output only. The thumbnail URL for showing a preview of the
          given photo.
      share_link:
          Output only. The share link for the photo.
      pose:
          Pose of the photo.
      connections:
          Connections to other photos. A connection represents the link
          from this photo to another photo.
      capture_time:
          Absolute time when the photo was captured. When the photo has
          no exif timestamp, this is used to set a timestamp in the
          photo metadata.
      places:
          Places where this photo belongs.
      view_count:
          Output only. View count of the photo.
      transfer_status:
          Output only. Status of rights transfer on this photo.
      maps_publish_status:
          Output only. Status in Google Maps, whether this photo was
          published or rejected.
  """,
  # @@protoc_insertion_point(class_scope:google.streetview.publish.v1.Photo)
  ))
_sym_db.RegisterMessage(Photo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)