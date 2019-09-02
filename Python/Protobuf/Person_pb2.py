# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Person.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='Person.proto',
    package='Test',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=_b(
        '\n\x0cPerson.proto\x12\x04Test\"5\n\x06Person\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x0b\n\x03\x41ge\x18\x02 \x01(\x05\x12\x10\n\x08Marriage\x18\x03 \x01(\x08\x62\x06proto3')
)

_PERSON = _descriptor.Descriptor(
    name='Person',
    full_name='Test.Person',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='Name', full_name='Test.Person.Name', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='Age', full_name='Test.Person.Age', index=1,
            number=2, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='Marriage', full_name='Test.Person.Marriage', index=2,
            number=3, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
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
    serialized_start=22,
    serialized_end=75,
)

DESCRIPTOR.message_types_by_name['Person'] = _PERSON
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), {
    'DESCRIPTOR': _PERSON,
    '__module__': 'Person_pb2'
    # @@protoc_insertion_point(class_scope:Test.Person)
})
_sym_db.RegisterMessage(Person)

# @@protoc_insertion_point(module_scope)
