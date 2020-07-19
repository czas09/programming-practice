#   Python Standard Library: Built-in Modules

- - - - -

##  6 Text precessing services | 文本处理服务

### 6.1 `string`: Common string operations

6.1.1 String constants
6.1.2 Custom String Formatting
6.1.3 Format String Syntax
    6.1.3.1 Format Specification Mini-Language
    6.1.3.2 Format examples
6.1.4 Template string
6.1.5 Helper functions

### 6.2 `re`: Regular expression operations

6.2.1 Regular Expression Syntax
6.2.2 Module Contents
    `re.compile(pattern, flags=0)`
    `re.match(pattern, string, flags=0)`
6.2.3 Regular Expression Objects
6.2.4 Match Objects
6.2.5 Regular Expression Examples
    6.2.5.1 Checking for a Pair
    6.2.5.2 Simulating scanf()
    6.2.5.3 search() vs. match()
    6.2.5.4 Making a Phonebook
    6.2.5.5 Text Munging
    6.2.5.6 Finding all Adverbs
    6.2.5.7 Finding all Adverbs and their Positions
    6.2.5.8 Raw String Notation
    6.2.5.9 Writing a Tokenizer

### 6.3 `difflib`: Helpers for computing deltas

6.3.1 SquenceMatch Objects
6.3.2 SequenceMatcher Examples
6.3.3 Differ Objects
6.3.4 Differ Example
6.3.5 A command-line interface to difflib

### 6.4 `textwrap`: Text wrapping and filling

### 6.5 `unicodedata`: Unicode database

### 6.6 `stringprep`: Internet string preparation

### 6.7 `readline`: GNU readline interface

6.7.1 Init file
6.7.2 Line buffer
6.7.3 History file
6.7.4 History list
6.7.5 Startup hooks
6.7.6 Completion
6.7.7 Example

### 6.8 `rlcompleter`: Completion function for GNU readline

- - - - -

##  7 Binary data services | 二进制数据服务

### 7.1 `struct`: Interpret bytes as packed binary data

7.1.1 Functions and Exceptions
7.1.2 Format Strings
    7.1.2.1 Byte Order, Size, and Alignment
    7.1.2.2 Format Characters
    7.1.2.3 Examples
7.1.3 Classes

### 7.2 `codecs`: Codec registry and base classes

7.2.1 Codec Base Classes
    7.2.1.1 Error Handlers
    7.2.1.2 Stateless Encoding and Decoding
    7.2.1.3 Incremental Encoding and Decoding
        7.2.1.3.1 IncrementalEncoder Objects
        7.2.1.3.2 IncrementalDncoder Objects
    7.2.1.4 Stream Encoding and Decoding
        7.2.1.4.1 StreamWriter Objects
        7.2.1.4.2 StreamReader Objects
        7.2.1.4.3 StreamReaderWriter Objects
        7.2.1.4.4 StreamRecoder Objects
7.2.2 Encodings and Unicode
7.2.3 Standard Encodings
7.2.4 Python Specific Encodings
    7.2.4.1 Text Encodings
    7.2.4.2 Binary Transforms
    7.2.4.3 Text Transforms
7.2.5 `encodings.idna`: Internationalized Domain Names in Applications
7.2.6 `encodings.mbcs`: Windows ANSI codepage
7.2.7 `encodings.utf_8_sig`: UTF-8 codec with BOM signature

- - - - -

### 8 Data types | 数据类型

### 8.1 `datetime`: Basic date and time types

8.1.1 Available Types
8.1.2 `timedelta` Objects
8.1.3 `date` Objects
8.1.4 `datetime` Objects
8.1.5 `time` Objects
8.1.6 `tzinfo` Objects
8.1.7 `timezone` Objects
8.1.8 `strftime()` and `strptime` Behaviour

### 8.2 `calendar`: General calendar-related functions

### 8.3 `collections`: Container datatypes

8.3.1 `ChainMap` Objects
8.3.2 `Counter` Objects
8.3.3 `deque` Objects
8.3.4 `defaultdict` Objects
8.3.5 `namedtuple()` Functory Function for Tuples with Named Fields
8.3.6 `OrderedDict` Objects
8.3.7 `UserDict` Objects
8.3.8 `UserList` Objects
8.3.9 `UserString` Objects

### 8.4 `collections.abc`: Abstract base classes for containers

8.4.1 Collections Abstract Base Classes

### 8.5 `heapq`: Heap queue algorithm

8.5.1 Basic Examples
8.5.2 Priority Queue Implementation Notes
8.5.3 Theory

### 8.6 `bisect`: Array bisection algorithm

8.6.1 Searching Sorted Lists
8.6.2 Other Examples

### 8.7 `array`: Efficient arrays of numeric values

### 8.8 `weakref`: Weak references

8.8.1 Weak Reference Objects
8.8.2 Example
8.8.3 Finalizer Objects
8.8.4 Comparing finalizers with `__del__()` methods

### 8.9 `types`: Dynamic type creation and names for built-in types

8.9.1 Dynamic Type Creation
8.9.2 Standard Interpreter Types
8.9.3 Additional Utility Classes and Functions
8.9.4 Coroutine Utility Functions

### 8.10 `copy`: Shallow and deep copy operations

### 8.11 `pprint`: Data pretty printer

8.11.1 PrettyPrinter Objects
8.11.2 Example

### 8.12 `reprlib`: Alternate `repr()` implementation

8.12.1 Repr Objects
8.12.2 Subclassing Repr Objects

### 8.13 `enum`: Supprt for enumerations

8.13.1 Module Contents
8.13.2 Creating an Enum
8.13.3 Programmatic access to enumeration members and their attributes
8.13.4 Duplicating enum members and values
8.13.5 Ensuring unique enumeration values
8.13.6 Using automatic values
8.13.7 Iteration
8.13.8 Comparisons
8.13.9 Allowed members and attributes of enumrations
8.13.10 Restricted subclassing of enumerations
8.13.11 Pickling
8.13.12 Functional API
8.13.13 Derived Enumerations
    8.13.13.1 IntEnum
    8.13.13.2 IntFlag
    8.13.13.3 Flag
    8.13.13.4 Others
8.13.14 Interesting examples
    8.13.14.1 Omitting values
        8.13.14.1.1 Using `auto`
        8.13.14.1.2 Using `objects`
        8.13.14.1.3 Using a descriptive string
        8.13.14.1.4 Using a custom `__new__()`
    8.13.14.2 OrderedEnum
    8.13.14.3 DuplicateFreeEnum
    8.13.14.4 Planet
8.13.15 How are Enums different?
    8.13.15.1 Enum Classes
    8.13.15.2 Enum Members (aka instances)
    8.13.15.3 Finer Points
        8.13.15.3.1 Supported `__dunder__()` names
        8.13.15.3.2 Supported `_sunder_()` names 
        8.13.15.3.3 `Enum` member type
        8.13.15.3.4 Boolean value of `Enum` classes and members
        8.13.15.3.5 `Enum` classes with methods
        8.13.15.3.6 Combining members of `Flag`

- - - - -

##  9 Numeric and mathmatical modules | 数字与数学模块

### 9.1 `numbers`: Numeric abstract base classes

9.1.1 The numeric tower
9.1.2 Notes for type implemetators
    9.1.2.1 Adding more numeirc ABCs
    9.1.2.2 Implementing the arithmetic operations

### 9.2 `math`: Mathematical functions

9.2.1 Number-theoretic and representation functions
9.2.2 Power and logarithmic functions
9.2.3 Trigonometric functions
9.2.4 Angular conversion
9.2.5 Hyperbolic functions
9.2.6 Special functions
9.2.7 Constants

### 9.3 `cmath`: Mathematical functions for complex numbers

9.3.1 Conversions to and from polar coordinates
9.3.2 Power and logarithmic functions
9.3.3 Trigonometric functions
9.3.4 Hyperbolic functions
9.3.5 Classification functions
9.3.6 Constants

### 9.4 `decimal`: Decimal fixed point and floating point arithmetic

9.4.1 Quick-start tutorial
9.4.2 Decimal objects
    9.4.2.1 Logical operands
9.4.3 Context objects
9.4.4 Constants
9.4.5 Rounding modes
9.4.6 Signals
9.4.7 Floating Point Notes
    9.4.7.1 Mitigating round-off error with increased precision
    9.4.7.2 Special values
9.4.8 Working with threads
9.4.9 Recipes
9.4.10 Decimal FAQ

### 9.5 `fractions`: Rational numbers

### 9.6 `random`: Generate pseudo-random numbers

9.6.1 Bookkeeping functions
9.6.2 Functions for integers
9.6.3 Functions for sequences
9.6.4 Real-valued distributions
9.6.5 Alternative Generator
9.6.6 Notes on Reproducibility
9.6.7 Examples and Recipes

### 9.7 `statistics`: Mathematical statistics functions

9.7.1 Averages and measures of central location
9.7.2 Measures of spread
9.7.3 Function details
9.7.4 Excetions

- - - - -

##  10 Functional programming modules | 函数式编程模块
    
### 10.1 `itertools`: Functions creating iterators for efficient looping

10.1.1 Itertool functions
10.1.2 Itertools Recipes

### 10.2 `functools`: Higher-order functions and operations on callable objects

10.2.1 `partial` Objects

### 10.3 `operator`: Standard operators as functions

10.3.1 Mapping Operators to Functions
10.3.2 Inplace Operators

- - - - -

##  11 File and directory access | 文件与目录访问

### 11.1 `pathlib`: Object-oriented filesystem paths

11.1.1 Basic use
11.1.2 Pure paths
    11.1.2.1 General preperties
    11.1.2.2 Operators
    11.1.2.3 Accessing individual parts
    11.1.2.4 Methods and properties
11.1.3 Concrete paths
    11.1.3.1 Methods

### 11.2 `os.path`: Common pathname manipulations

### 11.3 `fileinput`: Iterate over lines from multiple input streams

### 11.4 `stat`: Interpreting `stat()` results

### 11.5 `filecmp`: File and directory comparisons

11.5.1 The `dircmp` class

### 11.6 `tempfile`: Generate temporary files and directories

11.6.1 Examples
11.6.2 Deprecated functions and variables

### 11.7 `glob`: Unix style pathname pattern expansion

### 11.8 `fnmatch`: Unix filename pattern matching

### 11.9 `linecache`: Random access to text lines

### 11.10 `shutil`: High-level file operations

11.10.1 Directory and files operations
    11.10.1.1 copytree example
    11.10.1.2 rmtree example
11.10.2 Archiving operations
    11.10.2.1 Archiving example
11.10.3 Querying the size of the output terminal

### 11.11 `macpath`: Mac OS 9 path manipulation functions

- - - - -

##  12 Data persistence | 数据持久化

### 12.1 `pickle`: Python object serialization

12.1.1 Relationship to other Python modules
    12.1.1.1 Comparison with `marshal`
    12.1.1.2 Comparison with `json`
12.1.2 Data stream format
12.1.3 Module interface
12.1.4 What can bo pickled and unpickled?
12.1.5 Pickling Class Instance
    12.1.5.1 Persistence of External Objects
    12.1.5.2 Dispatch Tables
    12.1.5.3 Handling Stateful Objects
12.1.6 Restricting Glabals
12.1.7 Performance
12.1.8 Examples

### 12.2 `copyreg`: Register `pickle` support functions

12.2.1 Example

### 12.3 `shelve`: Python object persistence

12.3.1 Restrictions
12.3.2 Example

### 12.4 `marshal`: Internal Python object serialization

### 12.5 `dbm`: Interfaces to Unix "databases"

12.5.1 `dbm.gnu`: GNU's reinterpretation of dbm
12.5.2 `dbm.ndbm`: Interface based on ndbm
12.5.3 `dbm.dumb`: Portable DBM implementation

### 12.6 `sqlite3`: DB-API 2.0 interface for SQLite databases

12.6.1 Module function and constants
12.6.2 Connection Objects
12.6.3 Cursor Objects
12.6.4 Row Objects
12.6.5 Exceptions
12.6.6 SQLite and Python types
    12.6.6.1 Introduction
    12.6.6.2 Using adaptaters to store additional Python types in SQLite databases
        12.6.6.2.1 Letting your object adapt itself
        12.6.6.2.2 Registering an adapter callable
    12.6.6.3 Converting SQLite values to custom Python types
    12.6.6.4 Default adapters and converters
12.6.7 Controlling Transactions
12.6.8 Using `sqlite3` efficiently
    12.6.8.1 Using shortcus methods
    12.6.8.2 Accessing columns by name instead of by index
    12.6.8.3 Using the connection as a context manager
12.6.9 Common issues
    12.6.9.1 Multithreading

- - - - -

##  13 Data compression and archiving | 数据压缩与存档

### 13.1 `zlib`: Compression comptable with gzip

### 13.2 `gzip`: Support for gzip files

13.2.1 Examples of usage

### 13.3 `bz2`: Support for bzip2 comppression

13.3.1 (De)compression of files
13.3.2 Incremental (de)compression
13.3.3 One-shot (de)compression

### 13.4 `lzma`: Compression using the LZMA algorithm

13.4.1 Reading and wirting compressed files
13.4.2 Compressing and decompressing data in memory
13.4.3 Miscellaneous
13.4.4 Specifying custom filter chains
13.4.5 Examples

### 13.5 `zipfile`: Work with ZIP archives

13.5.1 ZipFile Objects
13.5.2 PyZipFile Objects
13.5.3 ZipInfo Objects
13.5.4 Command-Line Interface
    13.5.4.1 Command-line options

### 13.6 `tarfile`: Read and write tar archive files

13.6.1 TarFile Objects
13.6.2 Tarinfo Objects
13.6.3 Command-Line Interface
    13.6.3.1 Command-line options
13.6.4 Examples
13.6.5 Supported tar formats
13.6.6 Unicode issues

- - - - -

##  14 File formats | 文件格式

### 14.1 `csv`: CSV file reading and writing

14.1.1 Module Contents
14.1.2 Dialects and Formatting Parameters
14.1.3 Reader Objects
14.1.4 Writer Objects
14.1.5 Examples

### 14.2 `configparser`: Configuration file parser

14.2.1 Quick Start
14.2.2 Supported Datatypes
14.2.3 Fallback Values
14.2.4 Supported INI File Structure
14.2.5 Interpolation of values
14.2.6 Mapping Protocol Access
14.2.7 Customizing Parser Behaviour
14.2.8 Legacy API Examples
14.2.9 ConfigParser Objects
14.2.10 RawConfigParser Objects
14.2.11 Exceptions

### 14.3 `netrc`: netrc file processing

14.3.1 netrc Objects

### 14.4 `xdrlib`: Encode and decode XDR data

14.4.1 Packer Objects
14.4.2 Unpacker Objects
14.4.3 Exceptions

### 14.5 `plistlib`: Generate and parse Mac OS X `.plist` files

114.5.1 Examples

- - - - -

##  15 Cryptographic services | 加密服务

### 15.1 `hashlib`: Secure hashes and message digests

15.1.1 Hash algorihtms
15.1.2 SHAKE variable length digests
15.1.3 Key derivation
15.1.4 BLAKE2
    15.1.4.1 Creating hash objects
    15.1.4.2 Constants
    15.1.4.3 Examples
        15.1.4.1 Simple hashing
        15.1.4.2 Using different digest sizes
        15.1.4.3 Keyed hashing
        15.1.4.4 Randomized hashing
        15.1.4.5 Personalization
        15.1.4.6 Tree mode
    15.1.4.4 Credits

### 15.2 `hmac`: Keyed-hashing for message authentication

### 15.3 `secrets`: Generate secure random numbers for managing secrets

15.3.1 Random numbers
15.3.2 Generating tokens
    15.3.2.1 How many bytes should tokens use?
15.3.3 Other functions
15.3.4 Recipes and best practices

- - - - -

##  16 Generic services | 通用服务

### 16.1 `os`: Miscellaneous operating system interfaces

16.1.1 File Names, Command-Line Arguments, and Environment Variables
16.1.2 Process Parameters
16.1.3 File Object Creation
16.1.4 File Descriptor Operations
    16.1.4.1 Querying the size of a terminal
    16.1.4.2 Inheritance of File Descriptors
16.1.5 Files and Directories
    16.1.5.1 Linux extended attributes
16.1.6 Process Management
16.1.7 Interface to the scheduler
16.1.8 Miscellaneous System Information
16.1.9 Random numbers

### 16.2 `io`: Core tools for working with streams

16.2.1 Overview
    16.2.1.1 Text I/O
    16.2.1.2 Binary I/O
    16.2.1.3 Raw I/O
16.2.2 High-level Module Interface
    16.2.2.1 In-memory streams
16.2.3 Class hierarchy
    16.2.3.1 I/O Base Classes
    16.2.3.2 Raw File I/O
    16.2.3.3 Buffered Streams
    16.2.3.4 Text I/O
16.2.4 Performance
    16.2.4.1 Binary I/O
    16.2.4.2 Text I/O
    16.2.4.3 Multi-threading
    16.2.4.4 Reentrancy

### 16.3 `time`: Time access and conversions

16.3.1 Functions
16.3.2 Clock ID Constants 
16.3.3 Timezone

### 16.4 `argparse`: Parser for command-line options, arguments and sub-commands

16.4.1 Example
    16.4.1.1 Creating a parser
    16.4.1.2 Adding arguments
    16.4.1.3 Parsing arguments
16.4.2 ArgumentParser objects
    16.4.2.1 prog
    16.4.2.2 usage
    16.4.2.3 description
    16.4.2.4 epilog
    16.4.2.5 parents
    16.4.2.6 formatter_class
    16.4.2.7 prefix_chars
    16.4.2.8 fromfile_prefix_chars
    16.4.2.9 argument_default
    16.4.2.10 allow_abbrev
    16.4.2.11 conflict_handler
    16.4.2.12 add_help
16.4.3 The add_argument() method
    16.4.3.1 name or flags
    16.4.3.2 action
    16.4.3.3 nargs
    16.4.3.4 cons
    16.4.3.5 default
    16.4.3.6 type
    16.4.3.7 choices
    16.4.3.8 required
    16.4.3.9 help
    16.4.3.10 metavar
    16.4.3.11 dest
    16.4.3.12 Action classes
16.4.4 The parse_args() method
    16.4.4.1 Option value syntax
    16.4.4.2 Invalid arguments
    16.4.4.3 Arguments constaining
    16.4.4.4 Argument abbreviations (prefix matching)
    16.4.4.5 Beyond `sys.argv`
    16.4.4.6 The Namespace object
16.4.5 Other utilities
    16.4.5.1 Sub-commands
    16.4.5.2 FileType objects
    16.4.5.3 Atgument groups
    16.4.5.4 Mutual exclusion
    16.4.5.5 Parser defaults
    16.4.5.6 Printing help
    16.4.5.7 Partial parsing
    16.4.5.8 Customizing file parsing
    16.4.5.9 Exiting methods
16.4.6 Upgrading optparse code

### 16.5 `getopt`: C-style parser for command-line options

### 16.6 `logging`: Logging facility for Python

16.6.1 Logger Objects
16.6.2 Logging Levels
16.6.3 Handler Objects
16.6.4 Formatter Objects
16.6.5 Filter Objects
16.6.6 LogRecord Objects
16.6.7 LogRecord attributes
16.6.8 LoggerAdapter Objects
16.6.9 Thread Safety
16.6.10 Module-Level Functions
16.6.11 Module-Level Attributes
16.6.12 Integration with the warnings module

### 16.7 `logging.config`: Logging configuration

16.7.1 Configuration functions
16.7.2 Configuration dictionary Details
    16.7.2.1 Dictionary Schema Details
    16.7.2.2 Incremental Configuration
    16.7.2.3 Object connections
    16.7.2.4 User-defined objects
    16.7.2.5 Access to external objects
    16.7.2.6 Access to internal objects
    16.7.2.7 Import resolution and custom importers
16.7.3 Configuration file format

### 16.8 `logging.handlers`: Logging handlers

16.8.1 StreamHandler
16.8.2 FileHandler
16.8.3 NullHandler
16.8.4 WatchedFileHandler
16.8.5 BaseRotatingHandler
16.8.6 RotatingFileHandler
16.8.7 TimedRotatingFileHandler
16.8.8 SocketHandler
16.8.9 DatagramHandler
16.8.10 SysLogHandler
16.8.11 NTEventLogHandler
16.8.12 SMTPHandler
16.8.13 MemoryHandler
16.8.14 HTTPHandler
16.8.15 QueueHandler
16.8.16 QueueListener

### 16.9 `getpass`: Portable password input

### 16.10 `curses`: Terminal handling for character-cell displays

16.10.1 Functions
16.10.2 Window Objects
16.10.3 Constants

### 16.11 `curses.textpad`: Text input widget for curses programs

16.11.1 Textbox objects

### 16.12 `curses.ascii`: Utilities for ASCII characters

### 16.13 `curses.panel`: A panel stack extension for curses

16.13.1 Functions
16.13.2 Panle Objects

### 16.14 `platform`: Access to underlying platform's identifying data

16.14.1 Cross Platform
16.14.2 Java
16.14.3 Windows Platform
    16.14.3.1 Win95/98 specific
16.14.4 Mac OS Platform
16.14.5 Unix Platform

### 16.15 `errno`: Standard errno system symbols

### 16.16 `ctypes`: A foreign function library for Python

16.16.1 ctypes tutorial
    16.16.1.1 Loading dynamic link libraries
    16.16.1.2 Access functions from loaded dlls
    16.16.1.3 Calling functions
    16.16.1.4 Fundamental data types
    16.16.1.5 Calling functions, continued
    16.16.1.6 Calling functions with your own cunstom data types
    16.16.1.7 Specifying the required argument types (function protopypes)
    16.16.1.8 Return types
    16.16.1.9 Passing pointers (or: passing parameters by reference)
    16.16.1.10 Structures and unions
    16.16.1.11 Structures/union alignment adn byte order
    16.16.1.12 Bit fields in structures and unions
    16.16.1.13 Arrays
    16.16.1.14 Pointers
    16.16.1.15 Type converisons
    16.16.1.16 Incomplete
    16.16.1.17 Callback
    16.16.1.18 Accessing values exported from dlls
    16.16.1.19 Surprises
    16.16.1.20 Variable-sized data types
16.16.2 ctypes reference
    16.16.2.1 Finding shared libraries
    16.16.2.2 Loading shared libraries
    16.16.2.3 Foreign functions
    16.16.2.4 Function prototypes
    16.16.2.5 Utility functions
    16.16.2.6 Data types
    16.16.2.7 Fundamental data types
    16.16.2.8 Structured data types
    16.16.2.9 Arrays and pointers

- - - - -

##  17 Concurrent execution | 并发执行

### 17.1 `threading`: Thread-based parallelism

17.1.1 Thread-Local Data
17.1.2 Thread Objects
17.1.3 Lock Objects
17.1.4 RLock Objects
17.1.5 Condition Objects
17.1.6 Semaphore Objects
    17.1.6.1 `Semaphore` Example
17.1.7 Event Objects
17.1.8 Timer Objects
17.1.9 Barrier Objects
17.1.10 Using locks, conditions, and semaphores in the `with` statement

### 17.2 `multiprocessing`: Process-based parallelism

17.2.1 Introduction
    17.2.1.1 The `Process` class
    17.2.1.2 Contexts and start methods
    17.2.1.3 Exchanging objects between precesses
    17.2.1.4 Synchronization between processes
    17.2.1.5 Sharing state between processes
    17.2.1.6 Using a pool of workers
17.2.2 Reference
    17.2.2.1 `Precess` and exceptions
    17.2.2.2 Pipes and Queues
    17.2.2.3 Miscellaneous
    17.2.2.4 Connection Objects
    17.2.2.5 Synchronization primitives
    17.2.2.6 Shared `ctypes` Objects
        17.2.2.6.1 The `multiprocessing.sharedctypes` module
    17.2.2.7 Managers
        17.2.2.7.1 Customized managers
        17.2.2.7.2 Using a remote manager
    17.2.2.8 Proxy Objects
        17.2.2.8.1 Cleanup
    17.2.2.9 Process Pools
    17.2.2.10 Listeners and Clients
        17.2.2.10.1 Address Formats
    17.2.2.11 Authentication keys
    17.2.2.12 Logging
    17.2.2.13 The `multiprocessing.dummy` module
17.2.3 Programming guidelines
    17.2.3.1 All start methods
    17.2.3.2 The _spawn_ and _forkserver_ start methods
17.2.4 Examples

### 17.3 The `concurrent` package

### 17.4 `concurrent.futures`: Launching parallel tasks

17.4.1 Executor Objects
17.4.2 ThreadPoolExecutor
    17.4.2.1 ThreadPoolExecutor Example
17.4.3 ProcessPoolExecutor
    17.4.3.1 ProcessPoolExecutor Example
17.4.4 Future Objects
17.4.5 Module Functions
17.4.6 Exception classes

### 17.5 `subprocess`: Subprocess management

17.5.1 Using the `subprocess` Module
    17.5.1.1 Frequently Used Arguments
    17.5.1.2 Popen Constructor
    17.5.1.3 Exceptions
17.5.2 Security Considerations
17.5.3 Popen Objects
17.5.4 Windows Popen Helpers
    17.5.4.1 Constants
17.5.5 Older high-level API
17.5.6 Replacing Plder Functions with the `subprocess` Module
    17.5.6.1 Replacing /bin/sh shell backquote
    17.5.6.2 Replacing shell pipeline
    17.5.6.3 Replacing `os.system()`
    17.5.6.4 Replacing the `os.spawn` family
    17.5.6.5 Replacing `os.popen()`, `os.popen2()`, `os.popen3()`
    17.5.6.6 Replacing functions from the `popen2` module
17.5.7 Legacy Shell Invocation Functions
17.5.8 Notes
    17.5.8.1 Converting an argument sequence to a string on Windows

### 17.6 `sched`: Event scheduler

17.6.1 Scheduler Objects

### 17.7 `queue`: A synchronized queue class

17.7.1 Queue Objects

### 17.8 `dummy_threading`: Drop-in replacement for the `threading` module

### 17.9 `_thread`: Low-level threading API

### 17.10 `_dummy_thread`: Drop-in replacement for the `_thread` module

- - - - -

##  18 Interprocess communication and networking | 进程间通信与联网

### 18.1 `socket`: Low-level networking interface

18.1.1 Socket families
18.1.2 Module contents
    18.1.2.1 Exceptions
    18.1.2.2 Constants
    18.1.2.3 Functions
        18.1.2.3.1 Creating sockets
        18.1.2.3.2 Other functions
18.1.3 Socket Objects
18.1.4 Notes on socket timeouts
    18.1.4.1 Timeouts and the `connect` method
    18.1.4.2 Timeouts and the `accept` method
18.1.5 Example

### 18.2 `ssl`: TLS/SSL wrapper for socket objects

18.2.1 
    18.2.1.1 
    18.2.1.2 
    18.2.1.3 
    18.2.1.4 
    18.2.1.5 
18.2.2 
18.2.3 
18.2.4 
    18.2.4.1 
    18.2.4.2 
    18.2.4.3 
    18.2.4.4 
18.2.5 
    18.2.5.1 
    18.2.5.2 
    18.2.5.3 
18.2.6 
18.2.7 
18.2.8 
18.2.9 
    18.2.9.1 
    18.2.9.2 
        18.2.9.2.1 
        18.2.9.2.2 
        18.2.9.2.3 
    18.2.9.3 
18.2.10 

### 18.3 `select`: Waiting for I/O completion

18.3.1 
18.3.2 
18.3.3 
18.3.4 
18.3.5 

### 18.4 `selectors`: High-level I/O multiplexing

18.4.1 
18.4.2 
18.4.3 

### 18.5 `asyncio`: Asynchronous I/O, event loop, coroutines and tasks

18.5.1 Base Event Loop
    18.5.1.1 Run an event loop
    18.5.1.2 Calls
    18.5.1.3 Delayed calls
    18.5.1.4 Futures
    18.5.1.5 Tasks
    18.5.1.6 Creating connections
    18.5.1.7 Creating listening connections
    18.5.1.8 Watch file descriptors
    18.5.1.9 Low-level socket operations
    18.5.1.10 Resolve host name
    18.5.1.11 Connect pipes
    18.5.1.12 UNIX signals
    18.5.1.13 Executors
    18.5.1.14 Error Handling API
    18.5.1.15 Debug mode
    18.5.1.16 Server
    18.5.1.17 Handle
    18.5.1.18 Event loop examples
        18.5.1.18.1 Hello World with call_soon()
        18.5.1.18.2 Display the current date with call_later()
        18.5.1.18.3 Watch a file descriptor for read events
        18.5.1.18.4 Set signal handlers for SIGIT and SIGTERM
18.5.2 Event loops
    18.5.2.1 Event loop functions
    18.5.2.2 Available event loops
    18.5.2.3 Platform support
        18.5.2.3.1 Windows
        18.5.2.3.2 Mac OS X
    18.5.2.4 Event loop policies and the default policy
    18.5.2.5 Event loop policy interface
    18.5.2.6 Access to the global loop policy
    18.5.2.7 Customizing the event loop policy
18.5.3 Tasks and coroutines
    18.5.3.1 Coroutines
        18.5.3.1.1 Example: Hello World coroutine
        18.5.3.1.2 Example: Coroutine displaying the current date
        18.5.3.1.3 Example: Chain coroutines
    18.5.3.2 InvalidStateError
    18.5.3.3 TimeoutError
    18.5.3.4 Future
        18.5.3.4.1 Example: Future with run_until_complete()
        18.5.3.4.2 Example: Future with run_forever()
    18.5.3.5 Task
        18.5.3.5.1 Example: Parallel execution of tasks
    18.5.3.6 Task functions
18.5.4 Transports and protocols (callback based API)
    18.5.4.1 Transports
        18.5.4.1.1 BaseTransport
        18.5.4.1.2 ReadTransport
        18.5.4.1.3 WriteTransport
        18.5.4.1.4 DatagramTransport
        18.5.4.1.5 BaseSubprocessTransport
    18.5.4.2 Protocols
        18.5.5.2.1 Protocol classes
        18.5.5.2.2 Connection callbacks
        18.5.5.2.3 Streaming protocols
        18.5.5.2.4 Datagram protocols
        18.5.5.2.1 Flow control callbacks
        18.5.5.2.6 Coroutines and protocols
    18.5.4.3 Protocol examples
        18.5.4.3.1 TCP echo client protocol
        18.5.4.3.2 TCP echo server protocol
        18.5.4.3.3 UDP echo client protocol
        18.5.4.3.4 UDP echo server protocol
        18.5.4.3.5 Register an open socket to wait for data using a protocol
18.5.5 Streams (coroutine based API)
    18.5.5.1 Stream functions
    18.5.5.2 StreamReader
    18.5.5.3 StreamWriter
    18.5.5.4 StreamReaderProtocol
    18.5.5.5 IncompleteReadError
    18.5.5.6 LimitOverrunError
    18.5.5.7 Stream examples
        18.5.5.7.1 TCP echo client using streams
        18.5.5.7.2 TCP echo server using streams
        18.5.5.7.3 Get HTTP headers
        18.5.5.7.4 Register an open socket to wait for data using streams
18.5.6 Subprocess
    18.5.6.1 Windows event loop
    18.5.6.2 Create a subprocess: high-level API using Process
    18.5.6.3 Create a subprocess: low-level API using subprocess.Popen
    18.5.6.4 Constants
    18.5.6.5 Process
    18.5.6.6 Subprocess and threads
    18.5.6.7 Subprocess examples
        18.5.6.7.1 Subprocess using tranport and protocol
        18.5.6.7.2 Subprocess using streams
18.5.7 Synchronization primitives
    18.5.7.1 Locks
        18.5.7.1.1 Lock
        18.5.7.1.2 Event
        18.5.7.1.3 Condition
    18.5.7.2 Semaphores
        18.5.7.2.1 Semaphore
        18.5.7.2.2 BoundedSemaphore
18.5.8 Queues
    18.5.8.1 Queue
    18.5.8.2 PriorityQueue
    18.5.8.3 LifoQueue
        18.5.8.3.1 Exceptions
18.5.9 Develop with asyncio
    18.5.9.1 Debug mode of asyncio
    18.5.9.2 Cancellation
    18.5.9.3 Concurrency and multithreading
    18.5.9.4 Handle blocking functions correctly
    18.5.9.5 Logging
    18.5.9.6 Detext corouting objects never scheduled
    18.5.9.7 Detect exceptions never consumed
    18.5.9.8 Chain coroutines correctly
    18.5.9.9 Pending task destroyed
    18.5.9.10 Close transports and event loops

### 18.6 `asyncore`: Asynchronous socket handler

18.6.1 
18.6.2 

### 18.7 `asynchat`: Asynchronous socket command/response handler

18.7.1 

### 18.8 `signal`: Set handlers for asynchronous events

18.8.1 
    18.8.1.1 
    18.8.1.2 
18.8.2 
18.8.3 

### 18.9 `mmap`: Memory-mapped file support

- - - - -

##  19 Internet data handling | 互联网数据处理

### 19.1 `email`: An email and MIME handling package

19.1.1 
19.1.2 
    19.1.2.1 
    19.1.2.2 
    19.1.2.3 
19.1.3 
19.1.4 
19.1.5 
19.1.6 
19.1.7 
    19.1.7.1 
19.1.8 
19.1.9 
19.1.10 
19.1.11 
19.1.12 
19.1.13 
19.1.14 
19.1.15 

### 19.2 `json`: JSON encoder and decoder

19.2.1 Basic Usage
19.2.2 Encoders and Decoders
19.2.3 Exceptions
19.2.4 Standard Compliance and Interoperability
    19.2.4.1 Character Encodings
    19.2.4.2 Infinite and NaN Number Values
    19.2.4.3 Repeated Names Within an Object
    19.2.4.4 Top-level Non-Object, Non-Array Values
    19.2.4.5 Implementation Limitations
19.2.5 Command-Line Interface
    19.2.5.1 Command-Line Options

### 19.3 `mailcap`: Mailcap file handling

### 19.4 `mailbox`: Manipulate mailboxes in various formats

19.4.1 
    19.4.1.1 
    19.4.1.2 
    19.4.1.3 
    19.4.1.4 
    19.4.1.5 
19.4.2 
    19.4.2.1 
    19.4.2.2 
    19.4.2.3 
    19.4.2.4 
    19.4.2.5 
19.4.3 
19.4.4 

### 19.5 `mimetypes`: Map filenames to MIME types

19.5.1 

### 19.6 `base64`: Base16, Base32, Base64, Base85 data encodings

### 19.7 `binhex`: Encode and decode binhex4 files

19.7.1 

### 19.8 `binascii`: Convert between binary and ASCII

### 19.9 `quopri`: Encode and decode MIME quoted-printable data

### 19.10 `uu`: Encode and decode uuencode files

- - - - -

##  20 Structured markup processing tools | 结构化标记处理工具

### 20.1 `html`: HyperText Markup Language support

### 20.2 `html.parser`: Simple HTML and XHTML parser

20.2.1 Example HTML Parser Application
20.2.2 `HTMLParser` Methods
20.2.3 Examples

### 20.3 `html.entities`: Definitions of HTML general entities

### 20.4 XML processing modules

20.4.1 
20.4.2 

### 20.5 `xml.etree.ElementTree`: The ElementTree XML API

20.5.1 Tutorial
    20.5.1.1 XML tree and elemts
    20.5.1.2 Parsing XML
    20.5.1.3 Pull API for non-blocking parsing
    20.5.1.4 Finding interesting elements
    20.5.1.5 Modifying an XML File
    20.5.1.6 Building XML documents
    20.5.1.7 Parsing XML with Namespaces
    20.5.1.8 Additional resources
20.5.2 XPath support
    20.5.2.1 Example
    20.5.2.2 Supported XPath syntax
20.5.3 Reference
    20.5.3.1 Functions
    20.5.3.2 Element Objects
    20.5.3.3 ElementTree Objects
    20.5.3.4 QName Objects
    20.5.3.5 TreeBuilder Objects
    20.5.3.6 XMLParser Objects
    20.5.3.7 XMLPulParser Objects
    20.5.3.8 Exceptions

### 20.6 `xml.dom`: The Document Object Model API

20.6.1 
20.6.2 
    20.6.2.1 
    20.6.2.2 
    20.6.2.3 
    20.6.2.4 
    20.6.2.5 
    20.6.2.6 
    20.6.2.7 
    20.6.2.8 
    20.6.2.9 
    20.6.2.10 
    20.6.2.11 
    20.6.2.12 
20.6.3 
    20.6.3.1 
    20.6.3.2 

### 20.7 `xml.dom.minidom`: Minimal DOM implementation

20.7.1 
20.7.2 
20.7.3 

### 20.8 `xml.dom.pulldom`: Support for building partial DOM trees

20.8.1 

### 20.9 `xml.sax`: Support for SAX2 parsers

20.9.1 

### 20.10 `xml.sax.handler`: Case classes for SAX handlers

20.10.1 
20.10.2 
20.10.3 
20.10.4 

### 20.11 `xml.sax.saxutils`: SAX utilities

### 20.12 `xml.sax.xmlparser`: Interface for XML parsers

20.12.1 
20.12.2 
20.12.3 
20.12.4 
20.12.5 
20.12.6 

### 20.13 `xml.parsers.expat`: Fase XML parsing using Expat

20.13.1 
20.13.2 
20.13.3 
20.13.4 
20.13.5 

- - - - -

##  21 Internet protocols and support | 互联网协议与支持

### 21.1 `webbrowser`: Convenient web-browser controller

21.1.1 

### 21.2 `cgi`: Common Gateway Interface support 

21.2.1 
21.2.2 
21.2.3 
21.2.4 
21.2.5 
21.2.6 
21.2.7 
21.2.8 
21.2.9 

### 21.3 `cgitb`: Traceback manager for CGI script

### 21.4 `wsgiref`: WSGI utilities and reference implementation

21.4.1 
21.4.2 
21.4.3 
21.4.4 
21.4.5 
21.4.6 

### 21.5 `urllib`: URL handling modules

### 21.6 `urllib.request`: Extensible library for opening URLs

21.6.1 Request Objects
21.6.2 OpenerDirector Objects
21.6.3 BaseHandler Objects
21.6.4 HTTPRedirectHandler Objects
21.6.5 HTTPCookieProcessor Objects
21.6.6 ProxyHandler Objects
21.6.7 HTTPPasswordMgr Objects
21.6.8 HTTPPasswordMgrWithPriorAuth Objects
21.6.9 AbstractBasicAuthHandler Objects
21.6.10 HTTPBasicAuthHandler Objects
21.6.11 ProxyBasicAuthHandler Objects
21.6.12 AbstractDigestAuthHandler Objects
21.6.13 HTTPDigestAuthHandler Objects
21.6.14 ProxyDigestAuthHandler Objects
21.6.15 HTTPHandler Objects
21.6.16 HTTPSHandler Objects
21.6.17 FileHandler Objects
21.6.18 DataHandler Objects
21.6.19 FTPHandler Objects
21.6.20 CacheFTPHandler Objects
21.6.21 UnknownHandler Objects
21.6.22 HTTPErrorProcessor Objects
21.6.23 Examples
21.6.24 Legacy interface
21.6.25 `urllib.request` Restrictions

### 21.7 `urllib.response`: Response classes used by urllib

### 21.8 `urllib.parse`: Parse URLs into components

21.8.1 URL Parsing
21.8.2 Parsing ASCII Encoded Bytes
21.8.3 Structured Parser Results
21.8.4 URL Quoting

### 21.9 `urllin.error`: Exception classes raised by urllib.request

### 21.10 `urllib.robotparser`: Parser for robots.txt

### 21.11 `http`: HTTP modules

21.11.1 HTTP status codes

### 21.12 `http.client`: HTTP protocol client

21.12.1 HTTPConnection Objects
21.12.2 HTTPResponse Objects
21.12.3 Examples
21.12.4 HTTPMessage Objects

### 21.13 `ftplib`: FTP protocol client

21.13.1 
21.13.2 

### 21.14 `poplib`: POP3 protocol client

21.14.1 
21.14.2 

### 21.15 `imaplib`: IMAP4 protocol client

21.15.1 
21.15.2 

### 21.16 `nntplib`: NNTP protocol client

21.16.1 
    21.16.1.1 
    21.16.1.2 
21.16.2 

### 21.17 `smtplib`: SMTP protocol client

21.17.1 
21.17.2 

### 21.18 `smtpd`: SMTP Server

21.18.1 
21.18.2 
21.18.3 
21.18.4 
21.18.5 

### 21.19 `telnetlib`: Telnet client

21.19.1 
21.19.2 

### 21.20 `uuid`: UUID objects according to RFC 4122

21.20.1

### 21.21 `socketserver`: A framework for network servers

21.21.1 
21.21.2 
21.21.3 
21.21.4 
    21.21.4.1 
    21.21.4.2 
    21.21.4.3 

### 21.22 `http.server`: HTTP servers

### 21.23 `http.cookies`: HTTP state management

21.23.1 
21.23.2 
21.23.3 

### 21.24 `http.cookiejar`: Cookie handling for HTTP clients

21.24.1 
21.24.2 
21.24.3 
21.24.4 
21.24.5 
21.24.6 

### 21.25 `xmlrpc`: XML-RPC server and client modules

### 21.26 `xmlrpc.client`: XML-RPC client access

21.26.1
21.26.2
21.26.3
21.26.4
21.26.5
21.26.6
21.26.7
21.26.8
21.26.9

### 21.27 `xmlrc.server`: Basic XML-RPC servers

21.27.1 
    21.27.1.1 
21.27.2 
21.27.3 
21.27.4 
21.27.5 

### 21.28 `ipaddress`: IPv4/IPv6 manipulation library

21.28.1 
21.28.2 
    21.28.2.1 
    21.28.2.2 
    21.28.2.3 
        21.28.2.3.1 
        21.28.2.3.2 
21.28.3 
    21.28.3.1 
    21.28.3.2 
    21.28.3.3 
21.28.4 
    21.28.4.1
        21.28.4.1.1 
21.28.5 
21.28.6 

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

26.1.1 
26.1.2 
26.1.3 
26.1.4 
26.1.5 
26.1.6 
26.1.7 

### 26.2 `pydoc`: Documentation generator and online help system

### 26.3 `doctest`: Test interface Python examples

26.3.1 
26.3.2 
26.3.3 
    26.3.3.1 
    26.3.3.2 
    26.3.3.3 
    26.3.3.4 
    26.3.3.5 
    26.3.3.6 
    26.3.3.7 
26.3.4 
26.3.5 
26.3.6 
    26.3.6.1 
    26.3.6.2 
    26.3.6.3 
    26.3.6.4 
    26.3.6.5 
    26.3.6.6 
26.3.7 
26.3.8 

### 26.4 `unittest`: Unit testing framework

26.4.1 
26.4.2 
    26.4.2.1 
26.4.3 
26.4.4 
26.4.5 
26.4.6 
26.4.7 
26.4.8 
    26.4.8.1 
        26.4.8.1.1
    26.4.8.2 
    26.4.8.3 
        26.4.8.3.1
26.4.9 
    26.9.1 
    26.9.2 
26.4.10 

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