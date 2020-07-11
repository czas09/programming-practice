#   The Python Language Reference

- - - - -

##  1 Introduction

- - - - -

##  2 Lecical analysis | 词法分析

### 2.cz Keywords | 关键字

`False`
`None`
`True`
`and`
`as`
`assert`
`break`
`class`
`continue`
`def`
`del`
`elif`
`else`
`except`
`finally`
`for`
`from`
`global`
`if`
`import`
`in`
`is`
`lambda`
`nonlocal`
`not`
`or`
`pass`
`raise`
`return`
`try`
`while`
`with`
`yield`

- - - - -

##  3 Data model | 数据模型

### 3.1 Objects, values and types

### 3.2 The standard type hierarchy | 标准的类型层级

None
NotImplemented
Ellipsis
`numbers.Number`
    `numbers.Integral`
        Integers (`int`)
        Booleans (`bool`)
    `numbers.Real`(`float`)
    `numbers.Complex`(`complex`)
Sequences (序列)
    Immutable sequences
        Strings (字符串)
        Tuples (元组)
        Bytes (字节串)
    Mutable sequences
        Lists (列表)
        Byte arrays (字节数组)
Set types
    Sets
    Frazen sets
Mappings
    Dictionaries

    ```
    `array` module
    `collections` module
        `namedtuple()`
        `deque`
        `ChainMap`
        `Counter`
        `OrderedDict`
        `defaultdict`
        `UserDict`
        `UserList`
        `UserString`
    ```

Callable types
    User-defined functions
        Special attrbutes
    Instance mathods
    Generator functions
    Coroutine functions
    Asynchronous generator functions
    Built-in functions
    Built-in methods
    Classes
    Class instances
Modules
Custom classes
Class instances
I/O objects (file objects)

    ```
    `os` module
    `io` module
    ```

Internal types
    Code objects
    Frame objects
    Traceback objects
    Slice objects
    Static method objects
    Class method objects

### 3.3 Special method names

3.3.1 Basic customization
    `object.__new__(cls[, ...])`
    `object.__init__(slef[, ...])`
    `object.__del__(self)`
    `object.__repr__(self)`
    `object.__str__(self)`
    `object.__bytes__(self)`
    `object.__format__(self, format_spec)`
    `object.__lt__(self, other)`
    `object.__le__(self, other)`
    `object.__eq__(self, other)`
    `object.__ne__(self, other)`
    `object.__gt__(self, other)`
    `object.__ge__(self, other)`
    `object.__hash__(self)`
    `object.__bool__(self)`

3.3.2 Customizing attribute access
    `object.__getattr__(self, name)`
    `object.__getattribute__(self, name)`
    `object.__setattribute__(self, name, value)`
    `object.__delattr__(self, name)`
    `object.__dir__(self)`

    3.3.2.1 Customizing module attribute access
    3.3.2.2 Implementing Descriptors
        `object.__get__(self, instance, owner)`
        `object.__set__(self, instance, value)`
        `object.__delete__(self, instance)`
        `object.__set_name__(self, owner, name)`
    3.3.2.3 Invoking Descriptors
        Direct Call
        Instance Binding
        Class Binding
        Super Binding
    3.3.2.4 __slots__
        `object.__slots__`

3.3.3 Customizing class creation
    `classmethod object.__init_subclass__(cls)`

    3.3.3.1 Metaclasses
    3.3.3.2 Determing the appropriate metaclass
    3.3.3.3 Prepareing the class namespace
    3.3.3.4 Executing the class body
    3.3.3.5 Creating the class object
    3.3.3.6 Uses for metaclasses

3.3.4 Customizing instance and subclass checks
    `class.__instancecheck__(self, instance)`
    `class.__subclasscheck__(self, subclass)`

3.3.5 Emulating callable objects
    `object.__call__(self[, args...])`

3.3.6 Emulating container types
    `object.__len__(self)`
    `object.__length_hint__(self)`
    `object.__getitem__(self, key)`
    `object.__setitem__(self, key, value)`
    `object.__delitem__(self, key)`
    `object.__missing__(self, key)`
    `object.__iter__(self)`
    `object.__reversed__(self)`
    `object.__contains__(self, item)`

3.3.7 Emulating numeric types
    `object.__add__(self, other)`
    `object.__sub__(self, other)`
    `object.__mul__(self, other)`
    `object.__matmul__(self, other)`
    `object.__truediv__(self, other)`
    `object.__floordiv__(self, other)`
    `object.__mod__(self, other)`
    `object.__divmod__(self, other)`
    `object.__pow__(self, other[, modulo])`
    `object.__lshift__(self, other)`
    `object.__rshift__(self, other)`
    `object.__and__(self, other)`
    `object.__xor__(self, other)`
    `object.__or__(self, other)`

    `object.__radd__(self, other)`
    `object.__rsub__(self, other)`
    `object.__rmul__(self, other)`
    `object.__rmatmul__(self, other)`
    `object.__rtruediv__(self, other)`
    `object.__rfloordiv__(self, other)`
    `object.__rmod__(self, other)`
    `object.__rdivmod__(self, other)`
    `object.__rpow__(self, other)`
    `object.__rlshift__(self, other)`
    `object.__rrshift__(self, other)`
    `object.__rand__(self, other)`
    `object.__rxor__(self, other)`
    `object.__ror__(self, other)`

    `object.__iadd__(self, other)`
    `object.__isub__(self, other)`
    `object.__imul__(self, other)`
    `object.__imatmul__(self, other)`
    `object.__itruediv__(self, other)`
    `object.__ifloordiv__(self, other)`
    `object.__imod__(self, other)`
    `object.__ipow__(self, other[, modulo])`
    `object.__ilshift__(self, other)`
    `object.__irshift__(self, other)`
    `object.__iand__(self, other)`
    `object.__ixor__(self, other)`
    `object.__ir__(self, other)`

    `object.__neg__(self)`
    `object.__pos__(self)`
    `object.__abs__(self)`
    `object.__invert__(self)`

    `object.__complex__(self)`
    `object.__int__(self)`
    `object.__float__(self)`

    `object.__index__(self)`

    `object.__round__(self)`
    `object.__trunc__(self)`
    `object.__floor__(self)`
    `object.__ceil__(self)`

3.3.8 With statement context managers
    `object.__enter__(self)`
    `object.__exit__(self, exc_type, exc_value, traceback)`

3.3.9 Special method lookup

### 3.4 Coroutines | 协程

3.4.1 Awaitable objects | 可等待对象
    `object.__await__(self)`

3.4.2 Coroutine objects | 协程对象
    `coroutine.send(value)`
    `coroutine.throw(type[, value[, trackback]])`
    `coroutine.close()`

3.4.3 Asynchronous iterators | 异步迭代器
    `object.__aiter__(self)`
    `object.__anext__(self)`

3.4.4 Asynchronous context managers | 异步上下文管理器
    `object.__aenter__(self)`
    `object.__aexit__(self, exc_type, exc_value, traceback)`

- - - - -

##  4 Execution model | 执行模型

### 4.1 Structure of a program

### 4.2 Naming and binding

4.2.1 Binding of names
4.2.2 Resolution of names
4.2.3 Builtins and restricted execution
4.2.4 Interaction with dynamic features

### 4.3 Exceptions

- - - - -

##  5 The import system | 导入系统

### 5.1 `importlib`

### 5.2 Packages

5.2.1 Regular packages
5.2.2 Namespace packages

### 5.3 Searching

5.3.1 The module cache
5.3.2 Finders and loaders
5.3.3 Import hooks
5.3.4 The meta path

### 5.4 Loading

5.4.1 Loaders
5.4.2 Submodules
5.4.3 Module spec
5.4.4 Import-related module attributes
5.4.5 module.__path__
5.4.6 Module reprs

### 5.5 The path based finder

5.5.1 Path entry finders
5.5.2 Path entry finder protocol

### 5.6 Replacing the standard import system

### 5.7 Special considerations for `__main__`

5.7.1 `__main__.__spec__`

### 5.8 Open issues

- - - - -

##  6 Expressions | 表达式

### 6.1 Arithmetic conversions | 算术转换

### 6.2 Atoms | 原子

6.2.1 Identifiers (names)
6.2.2 Literals
6.2.3 Parenthesized forms
6.2.4 Displays for lists, sets and dictionaries
6.2.5 List displays
6.2.6 Set displays
6.2.7 Dictionary displays
6.2.8 Generator expressions
6.2.9 Yield expressions
    6.2.9.1 Generator-iterator methods
        `generator.__next__()`
        `generator.send(value)`
        `generator.throw(type[, value[, traceback]])`
        `generator.close()`
    6.2.9.2 Examples
    6.2.9.3 Asynchronous generator functions
    6.2.9.4 Asynchronous generator-iterator methods
        `coroutine agen.__anext__()`
        `coroutine agen.asend(value)`
        `coroutine agen.athrow(type[, value[, traceback]])`
        `coroutine agen.aclose()`

### 6.3 Primaries | 原型

6.3.1 Attribute references | 属性引用
6.3.2 Subcriptions | 抽取
6.3.3 Slicings | 切片
6.3.4 Calls | 调用

### 6.4 Await expression | await 表达式

### 6.5 The power operator | 幂运算符

### 6.6 Unary arithmetic and bitwise operations | 一元算术与位运算

### 6.7 Binary arithmetic operations | 二元算术运算

### 6.8 Shifting operations | 位移运算

### 6.9 Binary bitwise operations | 二元位运算

### 6.10 Comparisons | 比较

6.10.1 Value comparisons
6.10.2 Membership test operations
6.10.3 Identity comparisons

### 6.11 Conditional expressions | 条件表达式

### 6.12 Lambdas | lambda 式

### 6.13 Expression lists | 表达式列表

### 6.14 Evaluation order | 求值顺序

### 6.15 Oprator precedence | 运算符优先级

- - - - -

##  7 Simple statement | 简单语句

### 7.1 Expression statements

### 7.2 Assignment statements

7.2.1 Augmented assignment statements
7.2.2 Annotated assignment statements

### 7.3 The `assert` statement

### 7.4 The `pass` statement

### 7.5 The `del` statement

### 7.6 The `return` statement

### 7.7 The `yield` statement

### 7.8 The `raise` statement

### 7.9 The `break` statement

### 7.10 The `continue` statement

### 7.11 The `import` statement

### 7.12 Future statemtns

### 7.13 The `global` statement

### 7.14 The `nonlocal` statement

- - - - -

##  8 Compound statement | 复合语句

### 8.1 The `if` statement

### 8.2 The `while` statement

### 8.3 The `for` statement

### 8.4 The `try` statement

### 8.5 The `with` statement

### 8.6 Function definitions

### 8.7 Class definitions

### 8.8 Coroutines

8.8.1 Coroutine function definition
8.8.2 The `async for` statement
8.8.3 The `async with` statement

- - - - -

##  9 Top-level componets

### 9.1 Complete Python programs

### 9.2 File imput interactive input

### 9.3 Expression input