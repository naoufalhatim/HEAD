# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from blender_api_msgs/Viseme.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy

class Viseme(genpy.Message):
  _md5sum = "d32d126f54c4095d488da702ed7cd41d"
  _type = "blender_api_msgs/Viseme"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """string name
time start
duration duration
float32 rampin
float32 rampout
float32 magnitude
"""
  __slots__ = ['name','start','duration','rampin','rampout','magnitude']
  _slot_types = ['string','time','duration','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       name,start,duration,rampin,rampout,magnitude

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Viseme, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.name is None:
        self.name = ''
      if self.start is None:
        self.start = genpy.Time()
      if self.duration is None:
        self.duration = genpy.Duration()
      if self.rampin is None:
        self.rampin = 0.
      if self.rampout is None:
        self.rampout = 0.
      if self.magnitude is None:
        self.magnitude = 0.
    else:
      self.name = ''
      self.start = genpy.Time()
      self.duration = genpy.Duration()
      self.rampin = 0.
      self.rampout = 0.
      self.magnitude = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2I2i3f.pack(_x.start.secs, _x.start.nsecs, _x.duration.secs, _x.duration.nsecs, _x.rampin, _x.rampout, _x.magnitude))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.start is None:
        self.start = genpy.Time()
      if self.duration is None:
        self.duration = genpy.Duration()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.name = str[start:end].decode('utf-8')
      else:
        self.name = str[start:end]
      _x = self
      start = end
      end += 28
      (_x.start.secs, _x.start.nsecs, _x.duration.secs, _x.duration.nsecs, _x.rampin, _x.rampout, _x.magnitude,) = _struct_2I2i3f.unpack(str[start:end])
      self.start.canon()
      self.duration.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2I2i3f.pack(_x.start.secs, _x.start.nsecs, _x.duration.secs, _x.duration.nsecs, _x.rampin, _x.rampout, _x.magnitude))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.start is None:
        self.start = genpy.Time()
      if self.duration is None:
        self.duration = genpy.Duration()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.name = str[start:end].decode('utf-8')
      else:
        self.name = str[start:end]
      _x = self
      start = end
      end += 28
      (_x.start.secs, _x.start.nsecs, _x.duration.secs, _x.duration.nsecs, _x.rampin, _x.rampout, _x.magnitude,) = _struct_2I2i3f.unpack(str[start:end])
      self.start.canon()
      self.duration.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2I2i3f = struct.Struct("<2I2i3f")