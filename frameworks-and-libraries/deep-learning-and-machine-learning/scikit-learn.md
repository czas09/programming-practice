#   Scikit-learn

- - - - -

##  1 Supervised learning

### 1.1 Linear Models

1.1.1 Ordinary Least Squares
1.1.2 Ridge regression and classification
1.1.3 Lasso
1.1.4 Multi-task Lasso
1.1.5 Elastic-Net
1.1.6 Multi-task Elastic-Net
1.1.7 Least Angle Regression
1.1.8 LARS Lasso
1.1.9 Orthogonal Matching Pursuit (OMP)
1.1.10 Bayesian Regression
1.1.11 Logistic Regression
1.1.12 Generalized Linear Regression
1.1.13 Stochastic Gradient Descent (SGD)
1.1.14 Perceptron
1.1.15 Passive Aggressive Algorithms
1.1.16 Robustness regression: outliers and modeling errors
1.1.17 Polynomial regression: extending linear models with basis functions

### 1.2 linear and Quadratic Discriminant Analysis

1.2.1 Dimensionality reduction using linear descriminant analysis
1.2.2 Mathematical formulation of the LDA and QDA classifiers
1.2.3 Mathematical formulation of LDA dimensionality reduction
1.2.4 Shrinkage
1.2.5 Estimation algorithms

### 1.3 Kernel ridge regression

### 1.4 Support Vector Machines

1.4.1 Classification
1.4.2 Regression
1.4.3 Density estimation, novelty detection
1.4.4 Complexity
1.4.5 Tips on Practial Use
1.4.6 Kernel functions
1.4.7 Mathematical formulation
1.4.8 Implmentation details

### 1.5 Stochastic Gradient Descent

1.5.1 Classification
1.5.2 Regression
1.5.3 Stochastic Gradient Descent for sparse data
1.5.4 Complexity
1.5.5 Stopping criterion
1.5.6 Tips on Practial Use
1.5.7 Mathematical formulation
1.5.8 Implmentation details

### 1.6 Nearest Neighbors

1.6.1 Unsupervised Nearest Neighbors
1.6.2 Nearest Neighbors Classfication
1.6.3 Nearest Neighbors Regression
1.6.4 Nearest Neighbors Algorithms
1.6.5 Nearest Centroid Classifier
1.6.6 Nearest Neighbors Transformer
1.6.7 Neighborhood Components Analysis

### 1.7 Gaussian Processes

1.7.1 Gaussian Process Regression (GPR)
1.7.2 GPR examples
1.7.3 Gaussian Process Classification (GPC)
1.7.4 GPC examples
1.7.5 Kernels for Gaussian Processes

### 1.8 Cross decomposition

### 1.9 Naive Bayes

1.9.1 Gaussian Naive Bayes
1.9.2 Multinomial Naive Bayes
1.9.3 Complement Naive Bayes
1.9.4 Bernoulli Naive Bayes
1.9.5 Categorical Naive Bayes
1.9.6 Out-of-core naive Bayes model fitting

### 1.10 Decision trees

1.10.1 Classification
1.10.2 Regression
1.10.3 Multi-output problems
1.10.4 Complexity
1.10.5 Tips on Practical Use
1.10.6 Tree algorithms: ID3, C4.5, C5.0 and CART
1.10.7 Mathematical formulation
1.10.8 Minimal Cost-Complexity Pruning

### 1.11 Ensemble methods

1.11.1 Bagging meta-estimator
1.11.2 Forests of randomized trees
1.11.3 AdaBoost
1.11.4 Gradient Tree Boosting
1.11.5 Histogram-Based Gradient Boosting
1.11.6 Voting Classifier
1.11.7 Coting Regressor
1.11.8 Stacked Generalization

### 1.12 Multiclass and multilabel algorithms

1.12.1 Multilabel classification format
1.12.2 One-Vs-The-Rest
1.12.3 One-Vs-One
1.12.4 Error-Correcting Output-Codes
1.12.5 Multioutput regression
1.12.6 Multioutput classification
1.12.7 Classifier Chain
1.12.8 Regressor Chain

### 1.13 Feature selection

1.13.1 Removing features with low variance
1.13.2 Uniariate feature selection
1.13.3 Recursive feature elimination
1.13.4 Feature selection using SelectFromModel
1.13.5 Feature selection as part of a pipeline

### 1.14 Semi-Supervised

1.14.1 Label Propagation

### 1.15 Isotonic regression

### 1.16 Probability calibration

1.16.1 Calibrating curves
1.16.2 Calibrating a classifier
1.16.3 Usage

### 1.17 Neural network models (supervised)

1.17.1 Multi-layer Perceptron
1.17.2 Classification
1.17.3 Regression
1.17.4 Regularization
1.17.5 Algorithms
1.17.6 Complexity
1.17.7 Mathematical formulation
1.17.8 Tips on Practical Use
1.17.9 More control woth warm_start

- - - - -

##  2 Unsupervised learning

Gaussian mixture models
    Gaussian mixture
    variational Bayesian Gaussian mixture
manifold learning
    introduction
    isomap
    locally linear embedding
    modified locally linear embedding
    Hessian eigenmapping
    spactral embedding
    local tangent space alignment
    multi-dimensional scaling (MDS)
    t-distributed stochastic neighbor embedding (t-SNE)
    tips on pratical use
clustering
    overview of clustering methods
    K-means
    affinity propagation
    mean shift
    spectral clustering
    hierarchical clustering
    DBSCAN
    OPTICS
    Brich
    clustering performance evaluation
biclustering
    spectral co-clustering
    spectral biclustering
    biclustering evaluation
deconposing signals in components (matric factorization problems)
    principal component analysis (PCA)
    truncated singular value decomposition and latent semantic analysis
    dictionary learing
    factor analysis
    independent component analysis (ICA)
    non-negative matrix factorization (NMF or NNMF)
    latent dirichlet allocation (LDA)
convariance estimation
    empirical covariance
    shrunk covariance
    sparse inverse covariance
    robust covariance estimation
navelty and outlier detection
    overview of outlier detection methods
    novelty detection
    outlier detection
    novolty detection with local outlier factor
density estimation
    density estimation: histograms
    kernel density estimation
neural network models (unsupervised)
    restricated Boltzmann machines

##  3 Model selection and evaluation

cross-validation: evaluating estimator performance
    computing cross-validated metrics
    cross validation iterators
    a note on shuffling
    cross validation and model selection
tuning the hyper-parameters of an estimator
    exhaustive grid search
    randomized parameter optimization
    tips for parameter search
    alternatives to brute force parameter search
metrics and scoring: quantifying the quality of predictions
    the `scoring` parameter: defining model evaluation rules
    classification metrics
    multilabel ranking metrics
    regression metrics
    clustering metrics
    dummy estimators
model persistence
    persistence examples
    security & maintainability limitations
validation curves: plotting scores to evaluate models
    validation curve
    learning curve

##  4 Inspection

partial dependence plots
    mathematical definition
    computation methods
permutation feature importance
    outlinge of the permutation importance algorithm
    relation to impurity-based importance in trees
    misleading values on strongly correlated features

##  5 Visualizations

available plotting utilities
    functions
    display objects

##  6 Dataset transformations

pipelines and composite estimators
    pipeline: chaining estimators
    transforming target in regression
    FeatureUnion: composite feature spaces
    ColumnTransformer for heterogeneous data
    visualizing composite estimators
feature extraction
    loading features from dicts
    feature hashing
    text feature extraction
    image feature extraction
preprocessing data
    standardization, or mean removal and variance scaling
    non-linear transformation
    marmalization
    encoding categorical features
    discretization
    imputation of missing values
    generating polynomial features
    cunstom tranformers
imputation of missing values
    univariate vs. multivariate imputation
    univariate feature imputation
    multivariate feature imputation
    references
    nearest neighbors imputation
    marking imputed values
unsupervised dimensionality reduction
    PCA: principal component analysis
    random projections
    feature agglomeration
random projection
    the Johnson-Lindenstrauss lemma
    Gaussian random projection
    sparse random projection
kernel approximation
    Nystroem method for kernel approximation
    radial basis function kernel
    additive Chi squared kernel
    skewed Chi squared kernel
    mathematical details
pairwise metrics, affinities and kernels
    cosine similarity
    linear kernel
    polynomial kernel
    Sigmoid kernel
    RBF kernel
    Laplacian kernel
    Chi-squared kernel
transforming the prediction target (`y`)
    label binarization
    label excoding

##  7 Dataset loading utilities

general dataset API
toy datasets
    Boston house prices dataset
    Iris plants dataset
    Diabetes dataset
    optical recognition of handwritten digits dataset
    Linnerrud dataset
    wine recognition dataset
    breast cancer wisconsin (diagnostic) dataset
real world datasets
    the Olivetti faces dataset
    the 20 newsgourp text dataset
    the labeled faces in the wild face recognition dataset
    forest covertypes
    RCV1 dataset
    Kddcup 99 dataset
    California housing dataset
generated datasets
    generators for classification and clustering
    generators for regression
    generators for manifoid learning
    generators for decomposition
loading other datasets
    sample images
    datasets in svmlight / libsvm format
    downloading datasets from the openml.org repository
    loading from external datasets

##  8 Computing with scikit-learning

strategies to scale computationally: bigger data
    scaling with scale computationally: bigger data
computational performance
    prediction latency
    prediction throughout
    tips and tricks
parallelism, resource mangement, and configuration
    parallelism
    configuration switches



`sklearn.base`: base classes and utility functions
    base classes
    functions
`sklearn.cluster`: clustering
    classes
    functions
`sklearn.compose`: composite estimators
`sklearn.covariance`: covariance estimators
`sklearn.cross_decomposition`: cross decomposition
`sklearn.datasets`: datasets
    loaders
    samples generators
`sklearn.decomposition`: matrix decomposition
`sklearn.discriminant_analysis`: discriminant analysis
`sklearn.dummy`: dummy estimators
`sklearn.ensemble`: ensemble methods
`sklearn.exceptions`: exceptions and warnings
`sklearn.experimental`: experimental
`sklearn.feature_extraction`: feature extraction
    from images
    from text
`sklearn.feature_selection`: feature selection
`sklearn.gaussian_process`: Gaussian processes
`sklearn.impute`: impute
`sklearn.inspection`: inspection
    plotting
`sklearn.isotonic`: isotonic regression
`sklearn.kernel_approximation`: kernel approximation
`sklearn.kernal_ridge`: kernel ridge regression
`sklearn.linear_model`: linear models
    linear classifiers
    classical linear regressors
    regressors with variable selection
    Bayesian regressors
    multi-task linear regressor with variable selection
    outlier-robust regressors
    geenralized linear models (GLM) for regression
    miscellaneous
`sklearn.manifold`: manifold learning
`sklearn.metrics`: metrics
    model selection interface
    classification metrics
    regression metrics
    multilabel ranking metrics
    clustering metrics
    biclustering metrics
    pairwaise metrics
    plotting
`sklearn.mixture`: Gaussian mixture models
`sklearn.model_selection`: model selection
    splitter classes
    splitter functions
    hyper-parameter optimizers
    model validation
`sklearn.multiclass`: multiclass and multilabel classification
`sklearn.multioutput`: multioutput regression and classification
`sklearn.naive_bayes`: naive Bayes
`sklearn.neighbors`: nearest neighbors
`sklearn.neural_network`: neural network nodels
`sklearn.pipeline`: pipeline
`sklearn.preprosessing`: preprocessing and normalization
`sklearn.random_projection`: random projection
`sklearn.semi_supervised`: semi-supervised learning
`sklearn.svm`: support vector machine 
`sklearn.tree`: decision tree
`sklearn.utils`: utilities