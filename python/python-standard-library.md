#   The Python Standard Library

- - - - -

##  1 Introduction

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
    `start`
    `stop`
    `step`

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
    `bytearray.translate    `str.translate()`()`
    
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
    `bytearray.strip([chars    `str.strip([chars])`])`
    
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
    `bytes.zfill(width)
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

### 5.2 Concrete exceptions

### 5.3 Warnings

### 5.4 Exception hierarchy

- - - - -

##  6 Text precessing services | 文本处理服务

### 6.1 `string`: Common string operations

### 6.2 `re`: Regular expression operations

### 6.3 `difflib`: Helpers for computing deltas

### 6.4 `textwrap`: Text wrapping and filling

### 6.5 `unicodedata`: Unicode database

### 6.6 `stringprep`: Internet string preparation

### 6.7 `readline`: GNU readline interface

### 6.8 `rlcompleter`: Completion function for GNU readline

- - - - -

##  7 Binary data services | 二进制数据服务

### 7.1 `struct`: Interpret bytes as packed binary data

### 7.2 `codecs`: Codec registry and base classes

- - - - -

### 8 Data types | 数据类型

### 8.1 `datetime`: Basic date and time types

### 8.2 `calendar`: General calendar-related functions

### 8.3 `collections`: Container datatypes

### 8.4 `collections.abc`: Abstract base classes for containers

### 8.5 `heapq`: Heap queue algorithm

### 8.6 `bisect`: Array bisection algorithm

### 8.7 `array`: Efficient arrays of numeric values

### 8.8 `weakref`: Weak references

### 8.9 `types`: Dynamic type creation and names for built-in types

### 8.10 `copy`: Shallow and deep copy operations

### 8.11 `pprint`: Data pretty printer

### 8.12 `reprlib`: Alternate `repr()` implementation

### 8.13 `enum`: Supprt for enumerations

- - - - -

##  9 Numeric and mathmatical modules | 数字与数学模块

### 9.1 `numbers`: Numeric abstract base classes

### 9.2 `math`: Mathematical functions

### 9.3 `cmath`: Mathematical functions for complex numbers

### 9.4 `decimal`: Decimal fixed point and floating point arithmetic

### 9.5 `fractions`: Rational numbers

### 9.6 `random`: Generate pseudo-random numbers

### 9.7 `statistics`: Mathematical statistics functions

- - - - -

##  10 Functional programming modules | 函数式编程模块
    
### 10.1 `itertools`: Functions creating iterators for efficient looping

### 10.2 `functools`: Higher-order functions and operations on callable objects

### 10.3 `operator`: Standard operators as functions

- - - - -

##  11 File and directory access | 文件与目录访问

### 11.1 `pathlib`: Object-oriented filesystem paths

### 11.2 `os.path`: Common pathname manipulations

### 11.3 `fileinput`: Iterate over lines from multiple input streams

### 11.4 `stat`: Interpreting `stat()` results

### 11.5 `filecmp`: File and directory comparisons

### 11.6 `tempfile`: Generate temporary files and directories

### 11.7 `glob`: Unix style pathname pattern expansion

### 11.8 `fnmatch`: Unix filename pattern matching

### 11.9 `linecache`: Random access to text lines

### 11.10 `shutil`: High-level file operations

### 11.11 `macpath`: Mac OS 9 path manipulation functions

- - - - -

##  12 Data persistence | 数据持久化

### 12.1 `pickle`: Python object serialization

### 12.2 `copyreg`: Register `pickle` support functions

### 12.3 `shelve`: Python object persistence

### 12.4 `marshal`: Internal Python object serialization

### 12.5 `dbm`: Interfaces to Unix "databases"

### 12.6 `sqlite3`: DB-API 2.0 interface for SQLite databases

- - - - -

##  13 Data compression and archiving | 数据压缩与存档

### 13.1 `zlib`: Compression comptable with gzip

### 13.2 `gzip`: Support for gzip files

### 13.3 `bz2`: Support for bzip2 comppression

### 13.4 `lzma`: Compression using the LZMA algorithm

### 13.5 `zipfile`: Work with ZIP archives

### 13.6 `tarfile`: Read and write tar archive files

- - - - -

##  14 File formats | 文件格式

### 14.1 `csv`: CSV file reading and writing

### 14.2 `configparser`: Configuration file parser

### 14.3 `netrc`: netrc file processing

### 14.4 `xdrlib`: Encode and decode XDR data

### 14.5 `plistlib`: Generate and parse Mac OS X `.plist` files

- - - - -

##  15 Cryptographic services | 加密服务

### 15.1 `hashlib`: Secure hashes and message digests

### 15.2 `hmac`: Keyed-hashing for message authentication

### 15.3 `secrets`: Generate secure random numbers for managing secrets

- - - - -

##  16 Generic services | 通用服务

### 16.1 `os`: Miscellaneous operating system interfaces

### 16.2 `io`: Core tools for working with streams

### 16.3 `time`: Time access and conversions

### 16.4 `argparse`: Parser for command-line options, arguments and sub-commands

### 16.5 `getopt`: C-style parser for command-line options

### 16.6 `logging`: Logging facility for Python

### 16.7 `logging.config`: Logging configuration

### 16.8 `logging.handlers`: Logging handlers

### 16.9 `getpass`: Portable password input

### 16.10 `curses`: Terminal handling for character-cell displays

### 16.11 `curses.textpad`: Text input widget for curses programs

### 16.12 `curses.ascii`: Utilities for ASCII characters

### 16.13 `curses.panel`: A panel stack extension for curses

### 16.14 `platform`: Access to underlying platform's identifying data

### 16.15 `errno`: Standard errno system symbols

### 16.16 `ctypes`: A foreign function library for Python

- - - - -

##  17 Concurrent execution | 并发执行

### 17.1 `threading`: Thread-based parallelism

### 17.2 `multiprocessing`: Process-based parallelism

### 17.3 The `concurrent` package

### 17.4 `concurrent.futures`: Launching parallel tasks

### 17.5 `subprocess`: Subprocess management

### 17.6 `sched`: Event scheduler

### 17.7 `queue`: A synchronized queue class

### 17.8 `dummy_threading`: Drop-in replacement for the `threading` module

### 17.9 `_thread`: Low-level threading API

### 17.10 `_dummy_thread`: Drop-in replacement for the `_thread` module

- - - - -

##  18 Interprocess communication and networking | 进程间通信与联网

### 18.1 `socket`: Low-level networking interface

### 18.2 `ssl`: TLS/SSL wrapper for socket objects

### 18.3 `select`: Waiting for I/O completion

### 18.4 `selectors`: High-level I/O multiplexing

### 18.5 `asyncio`: Asynchronous I/O, event loop, coroutines and tasks

### 18.6 `asyncore`: Asynchronous socket handler

### 18.7 `asynchat`: Asynchronous socket command/response handler

### 18.8 `signal`: Set handlers for asynchronous events

### 18.9 `mmap`: Memory-mapped file support

- - - - -

##  19 Internet data handling | 互联网数据处理

### 19.1 `email`: An email and MIME handling package

### 19.2 `json`: JSON encoder and decoder

### 19.3 `mailcap`: Mailcap file handling

### 19.4 `mailbox`: Manipulate mailboxes in various formats

### 19.5 `mimetypes`: Map filenames to MIME types

### 19.6 `base64`: Base16, Base32, Base64, Base85 data encodings

### 19.7 `binhex`: Encode and decode binhex4 files

### 19.8 `binascii`: Convert between binary and ASCII

### 19.9 `quopri`: Encode and decode MIME quoted-printable data

### 19.10 `uu`: Encode and decode uuencode files

- - - - -

##  20 Structured markup processing tools | 结构化标记处理工具

### 20.1 `html`: HyperText Markup Language support

## 20.2 `html.parser`: Simple HTML and XHTML parser

## 20.3 `html.entities`: Definitions of HTML general entities

## 20.4 XML processing modules

## 20.5 `xml.etree.ElementTree`: The ElementTree XML API

## 20.6 `xml.dom`: The Document Object Model API

## 20.7 `xml.dom.minidom`: Minimal DOM implementation

## 20.8 `xml.dom.pulldom`: Support for building partial DOM trees

## 20.9 `xml.sax`: Support for SAX2 parsers

## 20.10 `xml.sax.handler`: Case classes for SAX handlers

## 20.11 `xml.sax.saxutils`: SAX utilities

## 20.12 `xml.sax.xmlparser`: Interface for XML parsers

## 20.13 `xml.parsers.expat`: Fase XML parsing using Expat

- - - - -

##  21 Internet protocols and support | 互联网协议与支持

### 21.1 `webbrowser`: Convenient web-browser controller

### 21.2 `cgi`: Common Gateway Interface support 

### 21.3 `cgitb`: Traceback manager for CGI script

### 21.4 `wsgiref`: WSGI utilities and reference implementation

### 21.5 `urllib`: URL handling modules

### 21.6 `urllib.request`: Extensible library for opening URLs

### 21.7 `urllib.response`: Response classes used by urllib

### 21.8 `urllib.parse`: Parse URLs into components

### 21.9 `urllin.error`: Exception classes raised by urllib.request

### 21.10 `urllib.robotparser`: Parser for robots.txt

### 21.11 `http`: HTTP modules

### 21.12 `http.client`: HTTP protocol client

### 21.13 `ftplib`: FTP protocol client

### 21.14 `poplib`: POP3 protocol client

### 21.15 `imaplib`: IMAP4 protocol client

### 21.16 `nntplib`: NNTP protocol client

### 21.17 `smtplib`: SMTP protocol client

### 21.18 `smtpd`: SMTP Server

### 21.19 `telnetlib`: Telnet client

### 21.20 `uuid`: UUID objects according to RFC 4122

### 21.21 `socketserver`: A framework for network servers

### 21.22 `http.server`: HTTP servers

### 21.23 `http.cookies`: HTTP state management

### 21.24 `http.cookiejar`: Cookie handling for HTTP clients

### 21.25 `xmlrpc`: XML-RPC server and client modules

### 21.26 `xmlrpc.client`: XML-RPC client access

### 21.27 `xmlrc.server`: Basic XML-RPC servers

### 21.28 `ipaddress`: IPv4/IPv6 manipulation library

- - - - -

##  22 Multimedia services | 多媒体服务

### 22.1 `audioop`: Manipulate raw audio data

### 22.2 `aifc`: Read and write AIFF and AIFC files

### 22.3 `sunau`: Read and write Sun AU files

### 22.4 `wave`: Read and write WAV files

### 22.5 `chunk`: Read IFF chunked data

### 22.6 `colorsys`: Conversions between color systems

### 22.7 `imghdr`: Determine the type pf an image

### 22.8 `sndhdr`: Determine type of sound file

### 22.9 `ossaudiodev`: Access to SOO-compatible audio devices

- - - - -

##  23 Internationalization | 国际化

### 23.1 `gettext`: Multilingual internationalization services

### 23.2 `locale`: Internationalization services

- - - - -

##  24 Program frameworks | 程序框架

### 24.1 `turtle`: Turtle graphics

### 24.2 `cmd`: Support for line-oriented command interpreters

### 24.3 `shlex`: Simple lexical analysis

- - - - -

##  25 Graphical user interfaces with Tk | Tk 图形用户界面

### 25.1 `tkinter`: Python interface to Tcl/Tk

### 25.2 `tkinter.ttk`: Tk themed widgets

### 25.3 `tkinter.tix`: Extension widgets for Tk

### 25.4 `tkinter.scrolledtext`: Scrooled text widget

### 25.5 IDLE

### 25.6 Other graphical user interface packages

- - - - -

##  26 Development tools | 开发工具

### 26.1 `typing`: Support for type hints

### 26.2 `pydoc`: Documentation generator and online help system

### 26.3 `doctest`: Test interface Python examples

### 26.4 `unittest`: Unit testing framework

### 26.5 `unittest.mock`: mock object library

### 26.6 `unittest.mock`: getting started

### 26.7 2to3: Automated Python 2 to 3 code traslation

### 26.8 `test`: Regression tests package for Python

### 26.9 `test.support`: Utilities for the Python test suite

- - - - -

##  27 Debugging and profiling | 调试与分析

### 27.1 `bdb`Debugger framework

### 27.2 `faulthandler`: Dump the Python traceback

### 27.3 `pdb`: The Python Debugger

### 27.4 The Python profilers

### 27.5 `timeit`: Measure execution time of small code snippets

### 27.6 `trace`: Trace or track Python statement execution

### 27.7 `tracemalloc`: Trace memory allcations

- - - - -

##  28 Software packaging and distribution | 软件打包与分发

### 28.1 `distutils`: Building and installing Python modules

### 28.2 `ensurepip`: Bootstrapping the `pip` installer

### 28.3 `venv`: Creation of virtual environments

### 28.4 `zipapp`: Manage executable Python ZIP archives

- - - - -

##  29 Python runtime services | Python 运行时服务

### 29.1 `sys`: System-specific parameters and functions

### 29.2 `sysconfig`: Provide access to Python's configuration information

### 29.3 `builtins`: Built-in objects

### 29.4 `__main__`: Top-level script environment

### 29.5 `warnings`: Warning control

### 29.6 `contextlib`: Utilities for `with`-statement contexts

### 29.7 `abc`: Abstract Base Classes

### 29.8 `atexit`: Exit hadlers

### 29.9 `traceback`: Print of retrieve a stack traceback

### 29.10 `__future__`: Future statement definitions

### 29.11 `gc`: Garbage Collector interface

### 29.12 `inspect`: Inspect live objects

### 29.13 `site`: Site-specific configuration hook

### 29.14 `fpectl`: Floating-point exception control

- - - - -

##  30 Custom Python interpreters | 自定义 Python 解释器

### 30.1 `code`: Interpreter base classes

### 30.2 `codeop`: Compile Python code

- - - - -

##  31 Importing modules | 导入模块

### 31.1 `zipimport`: Import modules from ZIP archives

### 31.2 `pkgutils`: Package extension utility

### 31.3 `modulefinder`: Find modules used by a script

### 31.4 `runpy`: Locating and executing Python modules

### 31.5 `importlib`: The implementation of `import`

- - - - -

##  32 Python language services | Python 语言服务

### 32.1 `parser`: Access Python parse trees

### 32.2 `ast`: Abstract Syntax Trees

### 32.3 `symtable`: Access to the compiler's symbol tables

### 32.4 `symbol`: Constants used with Python parse trees

### 32.5 `token`: Constants used with Python parse trees

### 32.6 `keyword`: Testing for Python keywords

### 32.7 `tokenize`: Tokenizer for Python source

### 32.8 `tabnanny`: Detenction of ambiguous indentation

### 32.9 `pyclbr`: Python class broswer support

### 32.10 `py_compile`: Compile Python source files

### 32.11 `compileall`: Byte-compile Python libraries

### 32.12 `dis`: Disassembler for Python bytecode

### 32.13 `pickletools`: Tools for pickle developers

- - - - -

##  33 Miscellaneous services | 杂项服务

### 33.1 `formatter`: Generic output formatting

- - - - -

##  34 MS Windows specific services | 微软 Windows 专属服务

### 34.1 `msilib`: Read and write Microsoft Installer files

### 34.2 `msvcrt`: Useful routines from the MS VC++ runtime

### 34.3 `winreg`: Windows registry access

### 34.4 `winsound`: Sound-playing interface for Windows

- - - - -

##  35 Unix specific services | Unix 专属服务

### 35.1 `posix`: The most common POSIX system calls

### 35.2 `pwd`: The password database

### 35.3 `spwd`: The shadow password database

### 35.4 `grp`: The group database

### 35.5 `crypt`: Function to check Unix passwords

### 35.6 `termios`: POSIX style tty control

### 35.7 `tty`: Terminal control functions

### 35.8 `pty`: Pseudo-terminal utilities

### 35.9 `fcntl`: The `fcntl` and `ioctl` system calls

### 35.10 `pipes`: Interface to shell piplines

### 35.11 `resource`: Resource usage information

### 35.12 `nis`: Interface to Sun's NIS (Yellow Pages)

### 35.13 `syslog`: Unix syslog library routines

- - - - -

##  36 Superseded modules | 被取代的模块

### 36.1 `optparse`: Parser for command-line options

### 36.2 `imp`: Access the import internals

- - - - -

##  37 Undocumented modules

### 37.1 Platform specific modules