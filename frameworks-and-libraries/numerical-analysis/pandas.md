#   Pandas Outline

- - - - -

### cz

Input/Output
    Pickling
    Flat file
    Clipboard
    Excel
    JSON
    HTML
    HDFStore: PyTable (HDF5)
    Feather
    Parquet
    ORC
    SAS
    SPSS
    SQL
    Google BigQuery
    STATA
General functions
    Data manipulations
    Top-level missing data
    Top-level conversions
    Top-level dealing with datatimelike
    Top-level dealing with intervals
    Top-level evaluation
    Hashing
    Testing
Series
    Construtor
    Attributes
    Conversion
    Indexing, iteration
    Binary operator functions
    Function application, groupby & window
    Computations / descriptive stats
    Reindexing / selection / label manipulation
    Missing data handling
    Reshaping, sorting
    Combining / joining / merging
    Time series-related
    Accessors
        Datetimelike preperties
            Datetime preperties
            Datetime methods
            Period preperties
            Timedelta preperties
            Timedelta methods
        String handling
        Categorical accessor
        Sparse accessor
        Metadata
    Plotting
    Serialization / IO / conversion
DataFrame
    Constructor
    Attributes and underlying data
    Conversion
    Indexing, iteration
    Binary operator functions
    Function application, GroupBy & window
    Computations / descriptive stats
    Reindexing / selection / label manipulation
    Missing data handling
    Reshaping, sorting, trasposing
    Combining / joining / merging
    Time series-related
    Metadata
    Plotting
    Sparse accessor
    Serialization / IO / conversion
Pandas arrays
    `pandas.array`
    Datetime data
        Properties
        Methods
    Timedelta data
        Properties
        Methods
    Timespan data
    Period
        Properties
        Methods
    Interval data
        Properties
    Nullable integer
    Categorical data
    Sparse data
    Text data
    Boolean data with missing values
Panel
Index objects
    Index
        Properties
        Modifying and computations
        Compatibility with MultiIndex
        Missing values
        Conversion
        Sorting
        Time-specific operations
        Combining / joining / set operations
        Selecting
    Numeric index
    CategoricalIndex
        Categorical components
        Modifying and computations
    IntervalIndex
        IntervalIndex components
    MultiIndex
        MultiIndex constructors
        MultiIndex properties
        MultiIndex components
        MultiIndex selecting
    DatetimeIndex
        Time/Date components
        Selecting
        Time-specific operations
        Conversion
        Methods
    TimedeltaIndex
        Components
        Conversion
        Methods
    PeriodIndex
        Properties
        Methods 
Date offsets
    DateOffset
        Properties
        Methods
    BusinessDay
        Properties
        Methods
    BusinessHour
        Properties
        Methods
    CustomBusinessDay
        Properties
        Methods
    CustomBusinessHour
        Properties
        Methods
    MonthOffset
        Properties
        Methods
    MonthEnd
        Properties
        Methods
    MonthBegin
        Properties
        Methods
    BusinessMonthEnd
        Properties
        Methods
    BusinessMonthBegin
        Properties
        Methods
    CustomBusinessMonthEnd
        Properties
        Methods
    CustomBusinessMonthBegin
        Properties
        Methods    
    SemiMonthOffset
        Properties
        Methods    
    SemiMonthEnd
        Properties
        Methods    
    SemiMonthBegin
        Properties
        Methods    
    Week
        Properties
        Methods    
    WeekOfMonth
        Properties
        Methods    
    LastWeekOfMonth
        Properties
        Methods    
    QuarterOffset
        Properties
        Methods    
    BQuarterEnd
        Properties
        Methods    
    BquarterBegin
        Properties
        Methods    
    YearOffset
        Properties
        Methods    
    BYearEnd
        Properties
        Methods    
    BYearBegin
        Properties
        Methods    
    YearEnd
        Properties
        Methods    
    YearBegin
        Properties
        Methods    
    FY5253
        Properties
        Methods    
    FY5253Quarter
        Properties
        Methods    
    Easter
        Properties
        Methods    
    Tick
        Properties
        Methods    
    Day
        Properties
        Methods    
    Hour
        Properties
        Methods    
    Minute
        Properties
        Methods    
    Second
        Properties
        Methods    
    Milli
        Properties
        Methods    
    Micro
        Properties
        Methods    
    Nano
        Properties
        Methods    
    BDay
        Properties
        Methods    
    BMonthEnd
        Properties
        Methods    
    BMonthBegin
        Properties
        Methods    
    CBMonthEnd
        Properties
        Methods    
    CBMonthBegin
        Properties
        Methods    
    CDay
        Properties
        Methods
Frequencies
    `pandas.tseries.frequencies.to_offset`
Window
    Standard moving window functions
    Standard expanding window functions
    Exponentially-weighted moving Window functions
    Window indexer
GroupBy
    Indexing, iteration
    Fucntion application
    Computations / descriptive Stats
Resampling
    Indexing, iteration
    Function applcation
    Computations / descriptive stats
Style
    Styler constructor
    Styler properties
    Style applecation
    Builtin styles
    Style export and import
Plotting
    `pandas.plotting.andrews_curves`
    `pandas.plotting.autocorrelation_plot`
    `pandas.plotting.bootstrap_plot`
    `pandas.plotting.boxplot`
    `pandas.plotting.deregister_matplotlib_converters`
    `pandas.plotting.lag_plot`
    `pandas.plotting.parallel_coordinates`
    `pandas.plotting.plot_params`
    `pandas.plotting.radviz`
    `pandas.plotting.register_matplotlib_converters`
    `pandas.plotting.scater_matrix`
    `pandas.plotting.table`
General utility functions
    Working with options
    Testing functions
    Exceptions and warnings
    Data types related functionality
        Dtype introspection
        Iterable introspection
        Scalar introspection
Extensions
    `pandas.api.extension.register_extension_dtype`
    `pandas.api.extension.register_dataframe_accessor`
    `pandas.api.extension.register_series_accessor`
    `pandas.api.extension.register_index_accessor`
    `pandas.api.extension.ExtensionDtype`
    `pandas.api.extension.ExtensionArray`
    `pandas.arrays.PandasArray`
    `pandas.api.indexers.check_array_indexer`