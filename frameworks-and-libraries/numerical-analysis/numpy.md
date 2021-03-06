#   NumPy Reference

- - - - -

##  1 Array objects

### 1.1 The N-dimensional array (`ndarray`)

1.1.1 Constructing arrays
1.1.2 Indexing arrays
1.1.3 Internal memory layout of an ndarray
1.1.4 Array attributes
    1.1.4.1 Memory layout
    1.1.4.2 Data type
    1.1.4.3 Other attributes
    1.1.4.4 Array Interface
    1.1.4.5 `ctypes`foreign function interface
1.1.5 Array methods
    1.1.5.1 Array conversion
    1.1.5.2 Shape manipulation
    1.1.5.3 Item selection and manipulation
    1.1.5.4 Calculation
1.1.6 Arithmetic, matrix multiplication, and comparison operations
1.1.7 Special methods

### 1.2 Scalars

1.2.1 Built-in scalar types
1.2.2 Attributes
1.2.3 Indexing
1.2.4 Methods
1.2.5 Defining new types

### 1.3 Data type objects (`dtype`)

1.3.1 Specifying and constructing data types
1.3.2 `dtype`
    1.3.2.1 Attributes
    1.3.2.2 Methods

### 1.4 Indexing

1.4.1 Basic Slicing and Indexing
1.4.2 Advanced Indexing
    1.4.2.1 Integer array indexing
        1.4.2.1.1 Purely integer array indexing
        1.4.2.1.2 Combining advanced and basic indexing
    1.4.2.2 Boolean array indexing
1.4.3 Detailed notes
1.4.4 Field Access
1.4.5 Flat Iterator indexing

### 1.5 Iterating Over Arrays

1.5.1 Single Array Iteration
    1.5.1.1 Controlling Iteration Order
    1.5.1.2 Modifying Array Values
    1.5.1.3 Using an External Loop
    1.5.1.4 Tracking an Index or Multi-Index
    1.5.1.5 Alternative Looping and Element Access
    1.5.1.6 Buffering the Array Elements
    1.5.1.7 Iterating as a Specific Data Type
1.5.2 Broadcasting Array Iteration
    1.5.2.1 Iterator-Allocated Output Arrays
    1.5.2.2 Outer Product Iteration
    1.5.2.3 Reduction Iteration
1.5.3 Putting the Inner Loop in Cython

### 1.6 Standard array subclasses

1.6.1 Special attributes and methods
1.6.2 Matrix objects
1.6.3 Memory-mapped file arrays
1.6.4 Character arrays (`numpy.char`)
1.6.5 Record arrays (`numpy.rec`)
1.6.6 Masked arrays (`numpy.ma`)
1.6.7 Standard container class
1.6.8 Array Iterators
    1.6.8.1 Default iteration
    1.6.8.2 Flat iteration
    1.6.8.3 N-dimensional enumeration
    1.6.8.4 Iterator for brodcasting

### 1.7 Masked arrays

1.7.1 The `numpy.ma` module
    1.7.1.1 Rationale
    1.7.1.2 What is a masked array?
    1.7.1.3 The `numpy.ma` module
1.7.2 Using numpy.ma
    1.7.1.1 Constructing masked arrays
    1.7.1.2 Accessing the data
    1.7.1.3 Accessing the mask
    1.7.1.4 Accessing only the valid entries
    1.7.1.5 Modifying the mask
        1.7.1.5.1 Masking an entry
        1.7.1.5.2 Unmasking an entry
    1.7.1.6 Indexing and slicing
    1.7.1.7 Operations on masked arrays
1.7.3 Examples
    1.7.3.1 Data with a given value representing missing data
    1.7.3.2 Filling in the missing data
    1.7.3.3 Numerical operations
    1.7.3.4 Ignoring extreme values
1.7.4 Constants of the `numpy.ma` module
1.7.5 The `MaskedArray` class
    1.7.5.1 Attributes and preperties of masked arrays
1.7.6 `MaskedArray` methods
    1.7.6.1 Conversion
    1.7.6.2 Shape manipulation
    1.7.6.3 Item selection and manipulation
    1.7.6.4 Pickling and copy
    1.7.6.5 Calculations
    1.7.6.6 Arithmetic and comparison operations
        1.7.6.6.1 Conmparison operators
        1.7.6.6.2 Truth value of an array (`bool`)
        1.7.6.6.3 Arithmetic
        1.7.6.6.4 Arithmetic, in-place
    1.7.6.7 Representation
    1.7.6.8 Special methods
    1.7.6.9 Specific methods
        1.7.6.9.1 Handling the mask 
        1.7.6.9.2 Handling the `fill_value`
        1.7.6.9.3 Counting the missing elements
1.7.7 Masked array operations
    1.7.7.1 Constants
    1.7.7.2 Creation
        1.7.7.2.1 From existing data
        1.7.7.2.2 Ones and zeros
    1.7.7.3 Inspecting the array
    1.7.7.4 Manipulating a MaskedArray
        1.7.7.4.1 Changing the shape
        1.7.7.4.2 Modifying axes
        1.7.7.4.3 Changing the number of dimensions
        1.7.7.4.4 Joining arrays
    1.7.7.5 Operations on masks
        1.7.7.5.1 Creating a mask
        1.7.7.5.2 Accessing a mask
        1.7.7.5.3 Finding masked data
        1.7.7.5.4 Modifying a mask
    1.7.7.6 Conversion operations
        1.7.7.6.1 > to a masked array
        1.7.7.6.2 > to a ndarray
        1.7.7.6.3 > to another object
        1.7.7.6.4 Filling a masked array
    1.7.7.7 Masked arrays arithmetics
        1.7.7.7.1 Arithmetics
        1.7.7.7.2 Minimum/maximum
        1.7.7.7.3 Sorting
        1.7.7.7.4 Algebra
        1.7.7.7.5 Polynomial fit
        1.7.7.7.6 Clipping and rounding
        1.7.7.7.7 Miscellanea

### 1.8 The Array interface

1.8.1 Python side
1.8.2 C-struct access
1.8.3 Type description examples
1.8.4 Differences with Array Interface

### 1.9 Datetimes and Timedeltas

1.9.1 Basic Datetimes
1.9.2 Datetime and Timedelta Arithmetic
1.9.3 Datetime Units
1.9.4 Business Day Functionality
    1.9.4.1 `np.is_busday()`
    1.9.4.2 `np.busday_count()`
        1.9.4.2.1 Custom Weekmasks


- - - - -

##  2 Constants

- - - - -

##  3 Universal functions (`ufunc`)

### 3.1 Broadcasting

### 3.2 Output type determination

### 3.3 Use of internal buffers

### 3.4 Error handling

### 3.5 Casting Rules

### 3.6 Overriding Ufunc behaviour

### 3.7 `ufunc`

3.7.1 Optional keyword arguments
3.7.2 Attributes
3.7.3 Methods

### 3.8 Available ufuncs

3.8.1 Math operations
3.8.2 Trigonometric functions
3.8.3 Bit-twiddling functions
3.8.4 Comparison functions
3.8.5 Floating functions

- - - - -

##  4 Routines

### 4.1 Array creation routines

4.1.1 Ones and zeros
4.1.2 From existing data
4.1.3 Creating record arrays (`numpy.rec`)
4.1.4 Creating character arrays (`numpy.char`)
4.1.5 Numerical ranges
4.1.6 Building matrices
4.1.7 The Matrix class

### 4.2 Array manipulation routines

4.2.1 
4.2.2 
4.2.3 
4.2.4 
4.2.5 
4.2.6 
4.2.7 
4.2.8 
4.2.9 
4.2.10 

### 4.3 Binary operations

4.3.1 
4.3.2 
4.3.3 

### 4.4 String operations

4.4.1 
4.4.2 
4.4.3 
4.4.4 

### 4.5 C-Types Foreign Function Interface (`numpy.ctypeslib`)

### 4.6 Datetime Support Functions

4.6.1 
4.6.2 
4.6.3 

### 4.7 Data type routines

4.7.1 
4.7.2 
4.7.3 
4.7.4 
4.7.5 
4.7.6 
4.7.7 
4.7.8 
4.7.9 
4.7.10 

### 4.8 Optionally Scipy-accelerated routines (`numpy.dual`)

4.8.1 
4.8.2 
4.8.3 

### 4.9 Mathematical functions with automatic domain (`numpy.math`)

### 4.10 Floating point error handling

4.10.1 
4.10.2 

### 4.11 Discrete Fourier Transform (`numpy.fft`)

4.11.1 
4.11.2 
4.11.3 
4.11.4 
4.11.5 
4.11.6 
4.11.7 
4.11.8 
4.11.9 
4.11.10 
4.11.11 
4.11.12 

### 4.12 Financial functions

4.12.1 

### 4.13 Functional programming

4.13.1 
4.13.2 
4.13.3 
4.13.4 
4.13.5 

### 4.14 NumPy-specific help functions

4.14.1 
4.14.2 

### 4.15 Indexing routines

4.15.1 
4.15.2 
4.15.3 
4.15.4 

### 4.16 Input and output

4.16.1 
4.16.2 
4.16.3 
4.16.4 
4.16.5 
4.16.6 
4.16.7 
4.16.8 
4.16.9 

### 4.17 Linear algebra (`numpy.linalg`)

4.17.1 
4.17.2 
4.17.3 
4.17.4 
4.17.5 
4.17.6 
4.17.7 

### 4.18 Logic functions

4.18.1 
4.18.2 
4.18.3 
4.18.4 
4.18.5 

### 4.19 Masked array operations

4.19.1 
4.19.2 
4.19.3 
4.19.4 
4.19.5 
4.19.6 
4.19.7 

### 4.20 Mathematical functions

4.20.1 
4.20.2 
4.20.3 
4.20.4 
4.20.5 
4.20.6 
4.20.7 
4.20.8 
4.20.9 
4.20.10 
4.20.11 

### 4.21 Matrix library (`numpy.matlib`)

4.21.1 
4.21.2 
4.21.3 
4.21.4 
4.21.5 
4.21.6 
4.21.7 
4.21.8 

### 4.22 Miscellaneous routines

4.22.1 
4.22.2 
4.22.3 
4.22.4 
4.22.5 
4.22.6 

### 4.23 Padding Arrays

4.23.1 

### 4.24 Ploynomials

4.24.1 

### 4.25 Random sampling (`numpy.random`)

4.25.1 
4.25.2 
4.25.3 
4.25.4 

### 4.26 Set routines

4.26.1
4.26.2

### 4.27 Sorting, searching, and counting

4.27.1 
4.27.2 
4.27.3 

### 4.28 Statistics

4.28.1 
4.28.2 
4.28.3 
4.28.4 

### 4.29 Test support (`numpy.testing`)

4.29.1 
4.29.2 
4.29.3 
4.29.4 

### 4.30 Windows functions

4.30.1 

- - - - -

##  5 Global State

### 5.1 Performance-Related Options

5.1.1 
5.1.2 

### 5.2 Interoperability-Related Options

### 5.3 Debugging-Related Options

5.3.1 

- - - - -

##  6 Packaging (`numpy.distutils`)

### 6.1 Modules in `numpy.distutils`

### 6.2 Configuration class

### 6.3 Building Installable C libraries

6.3.1 
6.3.2 

### 6.4 Conversion of `.src` files

- - - - -

##  7 NumPy Distutils: User Guide

### 7.1 SciPy structure

### 7.2 Requirements for SciPy packages

### 7.3 The `setup.py` file

7.3.1 
7.3.2 
7.3.3 
7.3.4 
7.3.5 
    7.3.5.1 
    7.3.5.2 
7.3.6 
7.3.7 
7.3.8 
7.3.9 
7.3.10 
7.3.11 

### 7.4 The `__init__.py` file

### 7.5 Extra features in NumPy Distutils

7.5.1 
7.5.2 

- - - - -

##  8 NumPy C-API

### 8.1 Python Types and C-Structures

8.1.1 
8.1.2 

### 8.2 System configuration

8.2.1 
8.2.2 
8.2.3 
8.2.4 

### 8.3 Data Type API

8.3.1 
8.3.2 
8.3.3 
8.3.4 

### 8.4 Array API

8.4.1 
8.4.2 
8.4.3 
8.4.4 
8.4.5 
8.4.6 
8.4.7 
8.4.8 
8.4.9 
8.4.10 
8.4.11 
8.4.12 
8.4.13 
8.4.14 

### 8.5 Array Iterator API

8.5.1 
8.5.2 
8.5.3 
8.5.4 
8.5.5 
8.5.6 
8.5.7 

### 8.6 Ufunc API

8.6.1 
8.6.2 
8.6.3 
8.6.4 
8.6.5 

### 8.7 Generalized Universal Function API

8.7.1 
8.7.2 
8.7.3 

### 8.8 NumPy core libraries

8.8.1 

### 8.9 C API Deprecations

8.9.1 
8.9.2 

- - - - -

##  9 NumPy internals

### 9.1 NumPy C Code Explanations

9.1.1 
9.1.2 
9.1.3 
9.1.4 
9.1.5 
9.1.6 
    9.1.6.1 
9.1.7 
    9.1.7.1 
    9.1.7.2 
        9.1.7.2.1 
        9.1.7.2.2 
        9.1.7.2.3 
    9.1.7.3 
    9.1.7.4 
        9.1.7.4.1 
        9.1.7.4.2 
        9.1.7.4.3 
        9.1.7.4.4 

### 9.2 Memory Alignment

9.2.1 
9.2.2 
9.2.3 

### 9.3 internal organization of NumPy arrays

### 9.4 Multidimentional Array Indexing Order Issues

- - - - -

##  10 NumPy and SWIG

### 10.1 numpy.i: a SWIG Inteface File for NumPy

10.1.1 
10.1.2 
10.1.3 
10.1.4 
10.1.5 
10.1.6 
10.1.7 

### 10.2 Testing the numpy.i Typemaps

10.2.1 
10.2.2 
10.2.3 
10.2.4 
10.2.5 
10.2.6 