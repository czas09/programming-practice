#   Python Standard Library: Built-in Objects

//  Built-in functions, constants, data types and exceptions.

- - - - -

##  1 Introduction

- - - - -

##  2 Built-in functions | 内置函数

Python 标准库的内置函数有 68 个：
`abs(x)` - math
`all(iterable)`
`any(iterable)`
`ascii(object)`
`bin(x)`
`class bool([x])`
`class bytearray([source[, encoding[, errors]]])`
`class bytes([source[, encoding[, errors]]])`
`callable(object)`
`chr(i)`
`@classmethod()`
`compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)`
`class complex([real[, imag]])`
`delattr(object, name)`
`class dict(**kwarg)`
`class dict(mapping, **kwarg)`
`class dict(iterable, **kwarg)`
`dir([object])`
`divmod(a, b)`
`enumerate(iterable, start=0)`
`eval(expression, globals=None, local=None)`
`exec(object[, globals[, locals]])`
`filter(function, iterable)`
`class float([x])`
`format(value[, format_spec])`
`class frozenset([iterable])`
`getattr(object, name[, default])`
`globals()`
`hasattr(object, name)`
`hash(object)`
`help([object])`
`hex(x)`
`id(object)`
`input([prompt])`
`class int(x=0)`
`class int(x, base=10)`
`isinstance(object, classinfo)`
`issubclass(class, classinfo)`
`iter(object[, sentinel])`
`len(s)`
`class list([iterable])`
`locals()`
`map(function, iterable, ...)`
`max(iterable, *[, key, default])`
`max(arg1, arg2, *args[, key])`
`memoryview(obj)`
`min(iterable, *[, key, default])`
`min(arg1, arg2, *args[, key])`
`next(iterable[, default])`
`classobject`
`oct(x)`
`open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)`
`ord(c)`
`pow(x, y[, z])`
`print(*objects, sep='', end='\n', file=sys.stdout, flush=False)`
`class property(fget=None, fset=None, fdel=None, doc=None)`
`range(stop)`
`range(start, stop[, step])`
`repr(object)`
`reversed(seq)`
`round(number[, ndigits])`
`class set([iterable])`
`setattr(object, name, value)`
`class slice(stop)`
`class slice(start, stop[, step])`
`sorted(iterable, *, jey=None, reverse=False)`
`@staticmethod()`
`class str(object='')`
`class str(object=b'', encoding='utf-8', errors='strict')`
`sum(iterable[, start])`
`super([type[, object-or-type]])`
`tuple([iterable])`
`class type(object)`
`class type(name, bases dict)`
`vars([object])`
`zip(*iterables)`
`__import__(name, globals=None, locals=None, fromlist=(), level=0)`

- - - - -

##  3 Built-in constants | 内置常量

Python 内置常量有 6 个：
`False`
`True`
`None`
`NotImplemented`
`Ellipsis`
`__debug__`

### 3.1 Constants added by the `site` module

`quit(code=None)`
`exit(code=None)`
`copyright`
`credits`
`license`

- - - - -

##  4 Built-in Types | 内置类型

numerics, sequences, mappings, classes, instances and exceptions
数值、序列、映射、类、实例和异常

### 4.1 Truth value testing

### 4.2 Boolean operations: `and`, `or`, `not`

### 4.3 Comparisons

### 4.4 Numeric types: `int`, `float`, `complex`

4.4.1 Bitwise operations on interger types
4.4.2 Additional methods on integer types
    `int.bit_length()`
    `int.to_bytes(length, byteorder, *, signed=False)`
    `classmethod int.from_bytes(bytes, byteorder, *, signed=False)`
4.4.3 Additional method on float
    `float.as_integer_ratio()`
    `float.is_integer()`
    `float.hex()`
    `classmethod float.fromhex()`
4.4.4 Hashing of numeric types

### 4.5 Iterator types

`container.__iter__()`
`iterator.__iter__()`
`iterator.__next__()`

4.5.1 Generator types

### 4.6 Sequence types: `list`, `tuple`, `range`

4.6.1 Common sequence operations
4.6.2 Immutable sequence types
4.6.3 Mutable sequence types
4.6.4 Lists
    `class list([iterable])`
    `sort(*, key=None, reverse=False)`
4.6.5 Tuples
    `class tuple([iterable])`
4.6.6 Ranges
    `class range(stop)`
    `class range(start, stop[, step])`

### 4.7 Text sequence type: `str`

`class str(object="")`
`class str(object=b'', encoding="uft-8", errors="strict")`

4.7.1 String methods
    `str.capitalize()`
    `str.casefold()`
    `str.center(width[, fillchar])`
    `str.count(sub[, start[, end]])`
    `str.encode(encoding="utf-8", errors="strict")`
    `str.endswith(suffix[, start[, end]])`
    `str.expandtabs(tabsize=8)`
    `str.find(sub[, start[, end]])`
    `str.format(*args, **kwargs)`
    `str.format_map(mapping)`
    `str.index(sub[, start[, end]])`
    `str.isalnum()`
    `str.isalpha()`
    `str.isdecimal()`
    `str.isdigit()`
    `str.isidentifier()`
    `str.islower()`
    `str.isnumeric()`
    `str.isprintable()`
    `str.isspace()`
    `str.istitle()`
    `str.isupper()`
    `str.join(iterable)`
    `str.ljust(width[, fillchar])`
    `str.lower()`
    `str.lstrip([chars])`
    `static str.maketrans(x[, y[, z]])`
    `str.partition(sep)`
    `str.replace(old, new[, count])`
    `str.rfind(sub[, start[, end]])`
    `str.rindex(sub[, start[, end]])`
    `str.rjust(width[, fillchar])`
    `str.rpartition(sep)`
    `str.rsplit(sep=None, maxsplit=-1)`
    `str.rstrip([chars])`
    `str.split(sep=None, maxsplit=-1)`
    `str.splitlines([keepends])`
    `str.startswith(prefix[, start[, end]])`
    `str.strip([chars])`
    `str.swapcase()`
    `str.title()`
    `str.translate()`
    `str.upper()`
    `str.zfill(width)`
4.7.2 `printf`-style string formatting

### 4.8 Binary sequence types: `bytes`, `bytearray`, `memoryview`

4.8.1 Bytes objects
    `class bytes([source[, encoding[, errors]]])`
        `hex()`
4.8.2 Bytearray objects
    `class bytearray([source[, encoding[, errors]]])`
    `classmethod fromhex(string)`
        `hex()`
4.8.3 Bytes and bytearray operations
    `bytes.count(sub[, start[, end]])`
    `bytearray.count(sub[, start[, end]])`    
    `bytes.decode(encoding="utf-8", errors="strict")`
    `bytearray.decode(encoding="utf-8", errors="strict")`    
    `bytes.endswith(suffix[, start[, end]])`
    `bytearray.endswith(suffix[, start[, end]])`    
    `bytes.find(sub[, start[, end]])`
    `bytearray.find(sub[, start[, end]])`    
    `bytes.index(sub[, start[, end]])`
    `bytearray.index(sub[, start[, end]])`    
    `bytes.join(iterable)`
    `bytearray.join(iterable)`    
    `static bytes.maketrans(x[, y[, z]])`
    `static bytearray.maketrans(x[, y[, z]])`    
    `bytes.partition(sep)`
    `bytearray.partition(sep)`    
    `bytes.replace(old, new[, count])`
    `bytearray.replace(old, new[, count])`    
    `bytes.rfind(sub[, start[, end]])`
    `bytearray.rfind(sub[, start[, end]])`    
    `bytes.rindex(sub[, start[, end]])`
    `bytearray.rindex(sub[, start[, end]])`    
    `bytes.rpartition(sep)`
    `bytearray.rpartition(sep)`    
    `bytes.startswith(prefix[, start[, end]])`
    `bytearrayes.startswith(prefix[, start[, end]])`    
    `bytes.translate()`
    `bytearray.translate()`
    `bytes.center(width[, fillbyte])`
    `bytearray.center(width[, fillbyte])`    
    `bytes.ljust(width[, fillbyte])`
    `bytearray.ljust(width[, fillbyte])`    
    `bytes.lstrip([chars])`
    `bytearray.lstrip([chars])`    
    `bytes.rjust(width[, fillbyte])`
    `bytearray.rjust(width[, fillbyte])`    
    `bytes.rsplit(sep=None, maxsplit=-1)`
    `bytearray.rsplit(sep=None, maxsplit=-1)`    
    `bytes.rstrip([chars])`
    `bytearray.rstrip([chars])`    
    `bytes.split(sep=None, maxsplit=-1)`
    `bytearrayes.split(sep=None, maxsplit=-1)`    
    `bytes.strip([chars])`
    `bytearray.strip([chars])`
    `bytes.capitalize()`
    `bytearray.capitalize()`    
    `bytes.expandtabs(tabsize=8)`
    `bytearray.expandtabs(tabsize=8)`    
    `bytes.isalnum()`
    `bytearray.isalnum()`    
    `bytes.isalpha()`
    `bytearray.isalpha()`    
    `bytes.isdigit()`
    `bytearray.isdigit()`    
    `bytes.islower()`
    `bytearray.islower()`    
    `bytes.isspace()`
    `bytearray.isspace()`    
    `bytes.istitle()`
    `bytearray.istitle()`    
    `bytes.isupper()`
    `bytearray.isupper()`    
    `bytes.lower()`
    `bytearray.lower()`    
    `bytes.splitlines([keepends=False])`
    `bytearray.splitlines([keepends=False])`    
    `bytes.swapcase()`
    `bytearray.swapcase()`    
    `bytes.title()`
    `bytearray.title()`    
    `bytes.upper()`
    `bytearray.upper()`    
    `bytes.zfill(width)`
    `bytearray.zfill(width)`
4.8.4 `printf`-style bytes formatting
4.8.5 Memory views
    `class memoryview(obj)`
        `__eq__(exporter)`
        `tobytes()`
        `hex()`
        `tolist()`
        `release()`
        `cast(format[, shape])`
        `obj`
        `nbytes`
        `readonly`
        `format`
        `itemsize`
        `ndim`
        `shape`
        `strides`
        `suboffsets`
        `c_contiguous`
        `f_contiguous`
        `contiguous`

### 4.9 Set types: `set`, `frozenset`

`class set([iterable])`
`class frozenset([iterable])`
    `len(s)`
    `x in s`
    `x not in s`
    `isdisjoint(other)`
    `issubset(other)`, `set <= other`, `set < other`
    `issuperset(other)`, `set >= other`, `set > other`
    `union(*others)`, `set | other | ...`
    `intersection(*others)`, `set & other & ...`
    `difference(*others)`, `set - other - ...`
    `symmetric_difference(other)`, `set ^ other`
    `copy()`
    `update(*others)`, `set |= other | ...`
    `intersection_update(*others)`, `set &= other = ...`
    `difference_update(*others)`, `set -= other | ...`
    `symmetric_dofference_update(other)`, `set ^= other`
    `add(elem)`
    `remove(elem)`
    `discard(elem)`
    `pop()`
    `clear()`

### 4.10 Mapping types: `dict`

`class dict(**kwarg)`
`class dict(mapping, **kwarg)`
`class dict(iterable, **kwarg)`
    `len(d)`
    `d[key]`
    `d[key] = value`
    `del d[key]`
    `key in d`
    `key not in d`
    `iter(d)`
    `clear()`
    `copy()`
    `classmethod fromkeys(seq[, value])`
    `get(key[, default])`
    `items()`
    `keys()`
    `pop(key[, default])`
    `popitem()`
    `setdefault(key[, default])`
    `update([other])`
    `values()`

4.10.1 Dictionary view objects
    `len(dictview)`
    `iter(dictview)`
    `x in dictview`

### 4.11 Context manager types

`contextmanager.__enter__()`
`contextmanager.__exit__(exc_type, exc_val, exc_tb)`

### 4.12 Other built-in types

4.12.1 Modules
4.12.2 Classes and class instance
4.12.3 Functions
4.12.4 Methods
4.12.5 Code objects
4.12.6 Type objects
4.12.7 Null object
4.12.8 The Ellipsis object
4.12.9 The NotImplemented object
4.12.10 Boolean values
4.12.11 Internal objects

### 4.13 Special attributes

`object.__dict__`
`instance.__class__`
`class.__bases__`
`definition.__name__`
`definition.__qualname__`
`class.__mro__`
`class.mro()`
`class.__subclasses__()`

- - - - -

##  5 Built-in exceptions | 内置异常

### 5.1 Base classes

`exception BaseException`
    `args`
    `with_traceback(tb)`
`exception Exception`
`exception ArithmeticError`
`exception BufferError`
`exception LookupError`

### 5.2 Concrete exceptions

`exception AssertionError`
`exception AttributeError`
`exception EOFError`
`exception FloatingPointError`
`exception GeneratorExit`
`exception ImportError`
`exception ModuleNotFoundError`
`exception IndexError`
`exception KeyError`
`exception KeyboardInterrupt`
`exception MemoryError`
`exception NameError`
`exception NotImplementedError`
`exception OSError([arg])`
`exception OSError(errno, strerror[, filename[, winerror[, filename2]]])`
`exception OverflowError`
`exception RecursionError`
`exception ReferenceError`
`exception RuntimeError`
`exception StopIteration`
`exception StopAsyncIteration`
`exception SyntaxError`
`exception IndentationError`
`exception TabError`
`exception SystemError`
`exception SystemExit`
`exception TypeError`
`exception UnboundLocalError`
`exception UnicodeError`
    `encoding`
    `reason`
    `object`
    `start`
    `end`
`exception UnicodeEncodeError`
`exception UnicodeDecodeError`
`exception UnicodeTranslateError`
`exception ValueError`
`exception ZeroDivisionError`
`exception EnvironmentError`
`exception IOError`
`exception WindowsError`

### 5.3 Warnings

`exception Warning`
`exception UserWarning`
`exception DeprecationWarning`
`exception PendingDeprecationWarning`
`exception SyntaxWarning`
`exception RuntimeWarning`
`exception FutureWarning`
`exception ImportWarning`
`exception UnicodeWarning`
`exception BytesWarning`
`exception ResourceWarning`

### 5.4 Exception hierarchy

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
```