#   Pandas Outline

- - - - -

### cz

input/output
    pickling
    flat file
    clipboard
    Excel
    JSON
    HTML
    HDFStore: PyTable (HDF5)
    feather
    parquet
    ORC
    SAS
    SPSS
    SQL
    Google BigQuery
    STATA
general functions
    data manipulation
    top-level missing data
    top-level conversions
    top-level dealing with datatimelike
    top-level dealing with intervals
    top-level evaluation
    hashing
    testing
series
    construtor
    attributes
    conversion
    indexing, iteration
    binary operator functions
    function application, groupby & window
    computations / descriptive stats
    reindexing / selection / label manipulation
    missing data handling
    reshaping, sorting
    combining / joining / merging
    time series-related
    accessors
    plotting
    serialization / io / conversion
DataFrame
    constructor
    attributes and underlying data
    conversion
    indexing, iteration
    binary operator functions
    function application, GroupBy & window
    computations / descriptive stats
    reindexing / selection / label manipulation
    missing data handling
    reshaping, sorting, trasposing
    conbining / joining / merging
    time series-related
    metadata
    plotting
    spars accessor
    serialization / io / conversion
pandas arrays
    `pandas.array`
    datetime data
    timedelta data
    timespan data
    period
    interval
    nullable integer
    categorical data
    sparse data
    text
    boolean data with missing values
panel
index objects
    index
    numeric index
    CategoricalIndex
    MultiIndex
    DatetimeIndex
    TimedeltaIndex
    PeriodIndex 
date offsets
    DateOffset
    BusinessDay
    BusinessHour
    CustomBusinessDay
    CustomBusinessHour
    MonthOffset
    MonthEnd
    MonthBegin
    BusinessMonthEnd
    BusinessMonthBegin
    CustomBusinessMonthEnd
    CustomBusinessMonthBegin
    SemiMonthOffset
    SemiMonthEnd
    SemiMonthBegin
    Week
    WeekOfMonth
    LastWeekOfMonth
    QuarterOffset
    BQuarterEnd
    BquarterBegin
    YearOffset
    BYearEnd
    BYearBegin
    YearEnd
    YearBegin
    FY5253
    FY5253Quarter
    Easter
    Tick
    Day
    Hour
    Minute
    Second
    Milli
    Micro
    Nano
    BDay
    BMonthEnd
    BMonthBegin
    CBMonthEnd
    CBMonthBegin
    CDay
frequencies
    `pandas.tseries.frequencies.to_offset`
window
    standard moving window functions
    standard expanding window functions
    exponentially-weighted moving window functions
    window indexer
GroupBy
    Indexing, iteration
    fucntion application
    computations / descriptive stats
resampling
    indexing, iteration
    function applcation
    computations / descriptive stats
style
    styler constructor
    styler properties
    style applecation
    builtin styles
    style export and import
plotting
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
general utility functions
    working with options
    teting functions
    exceptions and warnings
    data types related functionality
extensions