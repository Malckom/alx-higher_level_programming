json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
Serialize obj as a JSON formatted stream to fp (a .write()-supporting file-like object) using this conversion table.

If skipkeys is true (default: False), then dict keys that are not of a basic type (str, int, float, bool, None) will be skipped instead of raising a TypeError.

The json module always produces str objects, not bytes objects. Therefore, fp.write() must support str input.

If ensure_ascii is true (the default), the output is guaranteed to have all incoming non-ASCII characters escaped. If ensure_ascii is false, these characters will be output as-is.

If check_circular is false (default: True), then the circular reference check for container types will be skipped and a circular reference will result in a RecursionError (or worse).

If allow_nan is false (default: True), then it will be a ValueError to serialize out of range float values (nan, inf, -inf) in strict compliance of the JSON specification. If allow_nan is true, their JavaScript equivalents (NaN, Infinity, -Infinity) will be used.

If indent is a non-negative integer or string, then JSON array elements and object members will be pretty-printed with that indent level. An indent level of 0, negative, or "" will only insert newlines. None (the default) selects the most compact representation. Using a positive integer indent indents that many spaces per level. If indent is a string (such as "\t"), that string is used to indent each level.

Changed in version 3.2: Allow strings for indent in addition to integers.

If specified, separators should be an (item_separator, key_separator) tuple. The default is (', ', ': ') if indent is None and (',', ': ') otherwise. To get the most compact JSON representation, you should specify (',', ':') to eliminate whitespace.

Changed in version 3.4: Use (',', ': ') as default if indent is not None.

If specified, default should be a function that gets called for objects that can’t otherwise be serialized. It should return a JSON encodable version of the object or raise a TypeError. If not specified, TypeError is raised.

If sort_keys is true (default: False), then the output of dictionaries will be sorted by key.

To use a custom JSONEncoder subclass (e.g. one that overrides the default() method to serialize additional types), specify it with the cls kwarg; otherwise JSONEncoder is used.

Changed in version 3.6: All optional parameters are now keyword-only.

Note Unlike pickle and marshal, JSON is not a framed protocol, so trying to serialize multiple objects with repeated calls to dump() using the same fp will result in an invalid JSON file.
json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
Serialize obj to a JSON formatted str using this conversion table. The arguments have the same meaning as in dump().

Note Keys in key/value pairs of JSON are always of the type str. When a dictionary is converted into JSON, all the keys of the dictionary are coerced to strings. As a result of this, if a dictionary is converted into JSON and then back into a dictionary, the dictionary may not equal the original one. That is, loads(dumps(x)) != x if x has non-string keys.
json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
Deserialize fp (a .read()-supporting text file or binary file containing a JSON document) to a Python object using this conversion table.

object_hook is an optional function that will be called with the result of any object literal decoded (a dict). The return value of object_hook will be used instead of the dict. This feature can be used to implement custom decoders (e.g. JSON-RPC class hinting).

object_pairs_hook is an optional function that will be called with the result of any object literal decoded with an ordered list of pairs. The return value of object_pairs_hook will be used instead of the dict. This feature can be used to implement custom decoders. If object_hook is also defined, the object_pairs_hook takes priority.

Changed in version 3.1: Added support for object_pairs_hook.

parse_float, if specified, will be called with the string of every JSON float to be decoded. By default, this is equivalent to float(num_str). This can be used to use another datatype or parser for JSON floats (e.g. decimal.Decimal).

parse_int, if specified, will be called with the string of every JSON int to be decoded. By default, this is equivalent to int(num_str). This can be used to use another datatype or parser for JSON integers (e.g. float).

Changed in version 3.11: The default parse_int of int() now limits the maximum length of the integer string via the interpreter’s integer string conversion length limitation to help avoid denial of service attacks.

parse_constant, if specified, will be called with one of the following strings: '-Infinity', 'Infinity', 'NaN'. This can be used to raise an exception if invalid JSON numbers are encountered.

Changed in version 3.1: parse_constant doesn’t get called on ‘null’, ‘true’, ‘false’ anymore.

To use a custom JSONDecoder subclass, specify it with the cls kwarg; otherwise JSONDecoder is used. Additional keyword arguments will be passed to the constructor of the class.

If the data being deserialized is not a valid JSON document, a JSONDecodeError will be raised.

Changed in version 3.6: All optional parameters are now keyword-only.

Changed in version 3.6: fp can now be a binary file. The input encoding should be UTF-8, UTF-16 or UTF-32.

json.loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
Deserialize s (a str, bytes or bytearray instance containing a JSON document) to a Python object using this conversion table.

The other arguments have the same meaning as in load().

If the data being deserialized is not a valid JSON document, a JSONDecodeError will be raised.

Changed in version 3.6: s can now be of type bytes or bytearray. The input encoding should be UTF-8, UTF-16 or UTF-32.

Changed in version 3.9: The keyword argument encoding has been removed.

Encoders and Decoders
class json.JSONDecoder(*, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, strict=True, object_pairs_hook=None)
Simple JSON decoder.

Performs the following translations in decoding by default:

JSON

Python

object

dict

array

list

string

str

number (int)

int

number (real)

float

true

True

false

False

null

None

It also understands NaN, Infinity, and -Infinity as their corresponding float values, which is outside the JSON spec.

object_hook, if specified, will be called with the result of every JSON object decoded and its return value will be used in place of the given dict. This can be used to provide custom deserializations (e.g. to support JSON-RPC class hinting).

object_pairs_hook, if specified will be called with the result of every JSON object decoded with an ordered list of pairs. The return value of object_pairs_hook will be used instead of the dict. This feature can be used to implement custom decoders. If object_hook is also defined, the object_pairs_hook takes priority.


