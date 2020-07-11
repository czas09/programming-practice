#   Scikit-learn Outline

- - - - -

### cz

supervised learning
    linear models
        ordinary learst squares
        ridge regression and classification
        Lasso
        multi-task Lasso
        Elastic-Net
        multi-task Elastic-Net
        least angle regression
        LARS Lasso
        orthogonal matching pursuit (OMP)
        Bayesian regression
        Logistic regression
        generalized linear regression
        stochastic gradient descent (SGD)
        perceptron
        passive aggressive algorithms
        robustness regression: outliers and modeling errors
        polynomial regression: extending linear models with basis functions
    linear and quadratic discriminant analysis
        dimensionality reduction using linear descriminant analysis
        mathematical formulation of the LDA and QDA classifiers
        mathematical formulation of LDA dimensionality reduction
        shrinkage
        estimation algorithms
    kernel ridge regression
    support vector machines
        classification
        regression
        density estimation, novelty detection
        complexity
        tips on practial use
        kernel functions
        mathematical formulation
        implmentation details
    stochastic gradient descent
        classification
        regression
        stochastic gradient descent for sparse data
        complexity
        stopping criterion
        tips on practial use
        kernel functions
        mathematical formulation
        implmentation details
    nearest neighbors
        unsupervised nearest neighbors
        nearest neighbors classfication
        nearest neighbors regression
        nearest neighbors algorithms
        nearest centroid classifier
        nearest neighbors transformer
        neighborhood components analysis
    Gaussian processes
        Gaussian process regression (GPR)
        GPR examples
        Gaussian process classification (GPC)
        GPC examples
        kernels for Gaussian Processes
    cross decomposition
    naive Bayes
        Gaussian naive Bayes
        multinomial naive Bayes
        complement naive Bayes
        Bernoulli naive Bayes
        categorical naive Bayes
        out-of-core naive Bayes model fitting
    decision trees
        classification
        regression
        multi-output problems
        complexity
        tips on practical use
        tree algorithms: ID3, C4.5, C5.0 and CART
        mathematical formulation
        minimal cost-complexity pruning
    ensemble mathods
        bagging meta-estimator
        forests of randomized trees
        AdaBoost
        gradient tree boosting
        histogram-based gradient boosting
        voting classifier
        coting regressor
        stacked generalization
    multiclass and multilabel algorithms
        multilabel classification format
        one-vs-the-rest
        one-vs-one
        error-correcting output-codes
        multioutput regression
        multioutput classification
        classifier chain
        regressor chain
    feature selection
        removing features with low variance
        uniariate feature selection
        recursive feature elimination
        feature selection using SelectFromModel
        feature selection as part of a pipeline
    semi-supervised
        label propagation
    isotonic regression
    probability calibration
        calibrating curves
        calibrating a classifier
        usage
    neural network models (supervised)
        multi-layer perceptron
        classification
        regression
        regularization
        algorithms
        complexity
        mathematical formulation
        tips on practical use
        more control woth warm_start
unsupervised
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
model selection and evaluation
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
inspection
    partial dependence plots
        mathematical definition
        computation methods
    permutation feature importance
        outlinge of the permutation importance algorithm
        relation to impurity-based importance in trees
        misleading values on strongly correlated features
visualizations
    available plotting utilities
        functions
        display objects
dataset transformations
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
dataset loading utilities
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
computing with scikit-learning
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