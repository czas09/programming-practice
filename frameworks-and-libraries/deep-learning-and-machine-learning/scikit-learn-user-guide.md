#   Scikit-learn User Guide

- - - - -

##  1 Supervised learning

### 1.1 Linear Models

1.1.1 Ordinary Least Squares
    1.1.1.1 Ordinary Least Squares Complexity
1.1.2 Ridge regression and classification
    1.1.2.1 Regression
    1.1.2.2 Classification
    1.1.2.3 Ridge Complexity
    1.1.2.4 Setting the regularization parameter: genralized Cross-Validation
1.1.3 Lasso
    1.1.3.1 Setting regularization parameter
        1.1.3.1.1 Using cross-validation
        1.1.3.1.2 Information-criteria based model selection
        1.1.3.1.3 Comparison with the regularization parameter of SVM
1.1.4 Multi-task Lasso
1.1.5 Elastic-Net
1.1.6 Multi-task Elastic-Net
1.1.7 Least Angle Regression
1.1.8 LARS Lasso
1.1.9 Orthogonal Matching Pursuit (OMP)
1.1.10 Bayesian Regression
    1.1.10.1 Bayesian Ridge Regression
    1.1.10.2 Automatic Relevance Determination (ARD)
1.1.11 Logistic Regression
1.1.12 Generalized Linear Regression
1.1.13 Stochastic Gradient Descent (SGD)
1.1.14 Perceptron
1.1.15 Passive Aggressive Algorithms
1.1.16 Robustness regression: outliers and modeling errors
    1.1.16.1 Different scenario and useful concepts
    1.1.16.2 RANSAC: RANdom SAmple Consensus
    1.1.16.3 Theil-Sen estimator: generalized-median-based estimator
    1.1.16.4 Huber Regression
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
    1.4.1.1 Multi-class classification
    1.4.1.2 Scores and probabilities
    1.4.1.3 Unbalanced problems
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
    1.6.1.1 Finding the Nearest Neighbors
    1.6.1.2 KDTree and BallTree Classes
1.6.2 Nearest Neighbors Classfication
1.6.3 Nearest Neighbors Regression
1.6.4 Nearest Neighbors Algorithms
    1.6.4.1 Brute Force
    1.6.4.2 K-D Tree
    1.6.4.3 Ball Tree
    1.6.4.4 Choice of Nearest Neighbors Algorithm
    1.6.4.5 Effect of `leaf_size`
1.6.5 Nearest Centroid Classifier
    1.6.5.1 Nearest Shrunken Centroid
1.6.6 Nearest Neighbors Transformer
1.6.7 Neighborhood Components Analysis
    1.6.7.1 Classification
    1.6.7.2 Dimensionality reduction
    1.6.7.3 Mathematical formulation
        1.6.7.3.1 Mahalanobis distance
    1.6.7.4 Implementation
    1.6.7.5 Complexity
        1.6.7.5.1 Training
        1.6.7.5.2 Transform

### 1.7 Gaussian Processes

1.7.1 Gaussian Process Regression (GPR)
1.7.2 GPR examples
    1.7.2.1 GPR with noise-level estimation
    1.7.2.2 Comparison of GPR and Kernel Ridge Regression
    1.7.2.3 GPR on Mauna Loa C)2 data
1.7.3 Gaussian Process Classification (GPC)
1.7.4 GPC examples
    1.7.4.1 Probabilistic predictions with GPC
    1.7.4.2 Illustration of GPC on the XOR dataset
    1.7.4.3 Gaussian process classification (GPC) on iris dataset
1.7.5 Kernels for Gaussian Processes
    1.7.5.1 Gaussian Process Kernel API
    1.7.5.2 Basic kernels
    1.7.5.3 Kernel operatiors
    1.7.5.4 Radial-basis funtion (RBF) kernel
    1.7.5.5 Matérn kernel
    1.7.5.6 Rational quadratic kernel
    1.7.5.7 Exp-Sine-Squared kernel
    1.7.5.8 Dot-Product kernel

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
    1.11.2.1 Random Forests
    1.11.2.2 Extremely Randomized Trees
    1.11.2.3 Parameters
    1.11.2.4 Parallelization
    1.11.2.5 Feature importance evaluation
    1.11.2.6 Totally Random Trees Embedding
1.11.3 AdaBoost
1.11.4 Gradient Tree Boosting
    1.11.4.1 Classification
    1.11.4.2 Regression
    1.11.4.3 Fitting additional weak-learners
    1.11.4.4 Controlling the tree size
    1.11.4.5 Mathematical formulation
    1.11.4.6 Loss Functions
    1.11.4.7 Shrinkage via learning rate
    1.11.4.8 Subsampling
    1.11.4.9 Interpretation with feature importance
1.11.5 Histogram-Based Gradient Boosting
    1.11.5.1 Usage
    1.11.5.2 Missing values support
    1.11.5.3 Sample weight support
    1.11.5.4 Monotonic Constaints
    1.11.5.5 Low-level parallelism
    1.11.5.6 Why it's faster
1.11.6 Voting Classifier
    1.11.6.1 Majority Class Labels (Majority/Hard Voting)
    1.11.6.2 Usage
    1.11.6.3 Weight Average Probabilities (Soft Voting)
    1.11.6.4 Using the `VotingClassifier` with `GridSearchCV`
    1.11.6.5 Usage
1.11.7 Voting Regressor
1.11.8 Stacked Generalization

### 1.12 Multiclass and multilabel algorithms

1.12.1 Multilabel classification format
1.12.2 One-Vs-The-Rest
    1.12.2.1 Multiclass learning
    1.12.2.2 Multilabel learning
1.12.3 One-Vs-One
    1.12.3.1 Multiclass learning
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
    1.13.4.1 L1-based feature selection
    1.13.4.2 Tree-based feature selection
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
1.17.9 More control with warm_start

- - - - -

##  2 Unsupervised learning

### 2.1 Gaussian mixture models

2.1.1 Gaussian Mixture
    2.1.1.1 Pros and con of class `GaussianMixture`
    2.1.1.2 Selecting the number of components in a classical Gaussian Mixture Model
    2.1.1.3 Estimation algorithm Expectation-maximization
2.1.2 Variational Bayesian Gaussian Mixture
    2.1.2.1 Estimation algorithm: variational inference
    2.1.2.2 Pros and cons of variational inference with `BayesianGaussianMixture`
    2.1.2.3 The Dirichlet Process

### 2.2 Manifold learning

2.2.1 Introduction
2.2.2 Isomap
    2.2.2.1 Complexity
2.2.3 Locally Linear Embedding
    2.2.3.1 Complexity
2.2.4 Modified Locally Linear Embedding
2.2.5 Hessian Eigenmapping
    2.2.5.1 Complexity
2.2.6 Spactral Embedding
    2.2.6.1 Complexity
2.2.7 Local Tangent Space Alignment
    2.2.7.1 Complexity
2.2.8 Multi-dimensional Scaling (MDS)
    2.2.8.1 Metric MDS
    2.2.8.2 Nonmetric MDS
2.2.9 t-distributed Stochastic Neighbor Embedding (t-SNE)
    2.2.9.1 Optimizing t-SNE
    2.2.9.2 Barnes-Hut t-SNE
2.2.10 Tips on Pratical Use

### 2.3 Clustering

2.3.1 Overview of clustering methods
2.3.2 K-means
    2.3.2.1 Low-level perallelism
    2.3.2.2 Mini Batch K-Means
2.3.3 Affinity Propagation
2.3.4 Mean Shift
2.3.5 Spectral clustering
    2.3.5.1 Diffent label assignment strategies
    2.3.5.2 Spectral Clustering Graphs
2.3.6 Hierarchical clustering
    2.3.6.1 Different linkage type: Ward, complete, average, and single linkage
    2.3.6.2 Visualization of cluster hierarchy
    2.3.6.3 Adding connectivity constraints
    2.3.6.4 Varying the metric
2.3.7 DBSCAN
2.3.8 OPTICS
2.3.9 Birch
2.3.10 Clustering performance evaluation
    2.3.10.1 Adjusted rand index
    2.3.10.2 Mutual Information based scores
    2.3.10.3 Homogeneity, completeness and V-measure
    2.3.10.4 Fowlkes-Mallows scores
    2.3.10.5 Silhouette Coeffivient
    2.3.10.6 Calinski-Harabasz Index
    2.3.10.7 Davies-Bouldin Index
    2.3.10.8 Contingency Matrix

### 2.4 Biclustering

2.4.1 Spectral Co-Clustering
2.4.2 Spectral Biclustering
2.4.3 Biclustering evaluation

### 2.5 Decomposing signals in components (matrix factorization problems)

2.5.1 Principal component analysis (PCA)
    2.5.1.1 Exact PCA and probabilistic interpretation
    2.5.1.2 Incremental PCA
    2.5.1.3 PCA using randomized SVD
    2.5.1.4 Kernel PCA
    2.5.1.5 Sparse principal components analysis (SparsePCA and MiniBatchSparsePCA)
2.5.2 Truncated singular value decomposition and latent semantic analysis
2.5.3 Dictionary learing
    2.5.3.1 Sparse coding with a precomputed dictionary
    2.5.3.2 Generic dictionary learning
    2.5.3.3 Mini-batch dictionary learning
2.5.4 Factor Analysis
2.5.5 Independent component analysis (ICA)
2.5.6 Non-negative matrix factorization (NMF or NNMF)
    2.5.6.1 NMF with the Frobenius norm
    2.5.6.2 NMF with a beta-divergence
2.5.7 Latent Dirichlet Allocation (LDA)

### 2.6 Convariance estimation

2.6.1 Empirical Covariance
2.6.2 Shrunk Covariance
    2.6.2.1 Basic shrinkage
    2.6.2.2 Ledoit-Wolf shrinkage
    2.6.2.3 Oracle Approximating Shrinkage
2.6.3 Sparse Inverse Covariance
2.6.4 Robust Covariance Estimation
    2.6.4.1 Minimum Covariance Determinant

### 2.7 Novelty and Outlier Detection

2.7.1 Overview of outlier detection methods
2.7.2 Novelty Detection
2.7.3 Outlier Detection
    2.7.3.1 Fitting an elliptic envelope
    2.7.3.2 Isolation Forest
    2.7.3.3 Local Outlier Factor
2.7.4 Novolty Detection with Local Outlier Factor

### 2.8 Density Estimation

2.8.1 Density Estimation: Histograms
2.8.2 Kernel Density Estimation

### 2.9 Neural network models (unsupervised)

2.9.1 Restricted Boltzmann machines
    2.9.1.1 Graphical model and parametrization
    2.9.1.2 Bernoulli Restricted Boltzmann machines
    2.9.1.3 Stochastic Maximum Likelihood learning

- - - - -

##  3 Model selection and evaluation

### 3.1 Cross-validation: evaluating estimator performance

3.1.1 Computing cross-validated metrics
    3.1.1.1 The cross_validate function and multiple metric evaluation
    3.1.1.2 Obtaining predictions by cross-validation
3.1.2 Cross validation iterators
    3.1.2.1 Cross-validation iterators for i.i.d. data
        3.1.2.1.1 K-fold
        3.1.2.1.2 Repeated K-fold
        3.1.2.1.3 Leave One Out (LOO)
        3.1.2.1.4 Leave P Out (LPO)
        3.1.2.1.5 Random permutations cross-validation a.k.a. Shuffle & Split
    3.1.2.2 Cross-validation iteratiors with stratification based on class labels
        3.1.2.2.1 Stratified k-fold
        3.1.2.2.2 Stratified Shuffle Split
    3.1.2.3 Cross-validation iterators for grouped data
        3.1.2.3.1 Group k-fold
        3.1.2.3.2 Leave One Group Out
        3.1.2.3.3 Leave P Group Out
        3.1.2.3.4 Group Shuffle Split
    3.1.2.4 Predefined Fold-Splits / Validation-Sets
    3.1.2.5 Cross validation of time series data
        3.1.2.5.1 Time Series Split
3.1.3 A note on shuffling
3.1.4 Cross validation and model selection

### 3.2 Tuning the hyper-parameters of an estimator

3.2.1 Exhaustive Grid Search
3.2.2 Randomized Parameter Optimization
3.2.3 Tips for parameter search
    3.2.3.1 Specifying an objective metric
    3.2.3.2 Specifying multiple metrics for evaluation
    3.2.3.3 Composite estimators and parameter spaces
    3.2.3.4 Model selection: developemt and evaluation
    3.2.3.5 Parallelism
    3.2.3.6 Robustness to failure
3.2.4 Alternatives to brute force parameter search
    3.2.4.1 Model specific cross-validation
    3.2.4.2 Information Criterion
    3.2.4.3 Out of Bag Estimates

### 3.3 Metrics and scoring: quantifying the quality of predictions

3.3.1 The `scoring` parameter: defining model evaluation rules
3.3.2 Classification metrics
3.3.3 Multilabel ranking metrics
3.3.4 Regression metrics
3.3.5 Clustering metrics
3.3.6 Dummy estimators

### 3.4 Model persistence

3.4.1 Persistence examples
3.4.2 Security & maintainability limitations

### 3.5 validation curves: plotting scores to evaluate models

3.5.1 Validation curve
3.5.2 Learning curve

- - - - -

##  4 Inspection

### 4.1 Partial dependence plots

4.1.1 Mathematical Definition
4.1.2 Computation Methods

### 4.2 Permutation feature importance

4.2.1 Outlinge of the permutation importance algorithm
4.2.2 Relation to impurity-based importance in trees
4.2.3 Misleading values on strongly correlated features

- - - - -

##  5 Visualizations

### 5.1 Available Plotting Utilities
    
5.1.1 Functions
5.1.2 Display objects

- - - - -

##  6 Dataset transformations

### 6.1 Pipelines and composite estimators

6.1.1 Pipeline: chaining estimators
6.1.2 Transforming target in regression
6.1.3 FeatureUnion: composite feature spaces
6.1.4 ColumnTransformer for heterogeneous data
6.1.5 Visualizing Vomposite Estimators

### 6.2 Feature extraction

6.2.1 Loading features from dicts
6.2.2 Feature hashing
6.2.3 Text feature extraction
6.2.4 Image feature extraction

### 6.3 Preprocessing data

6.3.1 Standardization, or mean removal and variance scaling
6.3.2 Non-linear transformation
6.3.3 Normalization
6.3.4 Encoding categorical features
6.3.5 Discretization
6.3.6 Imputation of missing values
6.3.7 Generating polynomial features
6.3.8 Custom tranformers

### 6.4 Imputation of missing values

6.4.1 Univariate vs. Multivariate Imputation
6.4.2 Univariate feature imputation
6.4.3 Multivariate feature imputation
6.4.4 References
6.4.5 Nearest neighbors imputation
6.4.6 Marking imputed values

### 6.5 Unsupervised dimensionality reduction

6.5.1 PCA: principal component analysis
6.5.2 Random projections
6.5.3 Feature agglomeration

### 6.6 Random Projection

6.6.1 The Johnson-Lindenstrauss lemma
6.6.2 Gaussian random projection
6.6.3 Sparse random projection

### 6.7 Kernel Approximation

6.7.1 Nystroem Method for Kernel Approximation
6.7.2 Radial Basis Function Kernel
6.7.3 Additive Chi Squared Kernel
6.7.4 Skewed Chi Squared Kernel
6.7.5 Mathematical Details

### 6.8 Pairwise metrics, Affinities and Kernels

6.8.1 Cosine similarity
6.8.2 Linear kernel
6.8.3 Polynomial kernel
6.8.4 Sigmoid kernel
6.8.5 RBF kernel
6.8.6 Laplacian kernel
6.8.7 Chi-squared kernel

### 6.9 Transforming the prediction target (`y`)

6.9.1 Label binarization
6.9.2 Label excoding

- - - - -

##  7 Dataset loading utilities

### 7.1 General dataset API

### 7.2 Toy datasets

7.2.1 Boston house prices dataset
7.2.2 Iris plants dataset
7.2.3 Diabetes dataset
7.2.4 Optical recognition of handwritten digits dataset
7.2.5 Linnerrud dataset
7.2.6 Wine recognition dataset
7.2.7 Breast cancer wisconsin (diagnostic) dataset

### 7.3 Real world datasets

7.3.1 The Olivetti faces dataset
7.3.2 The 20 newsgourp text dataset
7.3.3 The Labeled Faces in the Wild face recognition dataset
7.3.4 Forest covertypes
7.3.5 RCV1 dataset
7.3.6 Kddcup 99 dataset
7.3.7 California housing dataset

### 7.4 Generated datasets

7.4.1 Generators for classification and clustering
7.4.2 Generators for regression
7.4.3 Generators for manifoid learning
7.4.4 Generators for decomposition

### 7.5 Loading other datasets

7.5.1 Sample images
7.5.2 Datasets in svmlight / libsvm format
7.5.3 Downloading datasets from the openml.org repository
7.5.4 Loading from external datasets

- - - - -

##  8 Computing with scikit-learning

### 8.1 Strategies to scale computationally: bigger data

8.1.1 Scaling with scale computationally: bigger data

### 8.2 Computational Performance

8.2.1 Prediction Latency
8.2.2 Prediction Throughout
8.2.3 Tips and Tricks

### 8.3 Parallelism, resource mangement, and configuration

8.3.1 Parallelism
8.3.2 Configuration switches