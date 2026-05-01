# Data Science Learning Repository

A comprehensive, well-organized collection of Python scripts and Jupyter notebooks covering fundamental programming concepts, data manipulation, analysis, and visualization using industry-standard libraries.

## 📁 Repository Structure

This repository is organized into topic-based folders for easy navigation and progressive learning:

```
Data_Science/
├── 01_Python_Basics/     # Python fundamentals and core concepts
├── 02_NumPy/             # NumPy arrays and numerical computing
├── 03_Pandas/            # Data manipulation and analysis
├── 04_Matplotlib/        # Data visualization
└── Resources/            # Sample datasets and data files
```

---

## 📚 Contents

### 01_Python_Basics
**Fundamental Python programming concepts**

#### Core Concepts
- `01_problem.py` - Problem-solving exercises
- `01_takingInput.py` - Input handling and user interaction
- `02_matchCase.py` - Pattern matching and conditional logic
- `03_formattingString.py` - String formatting techniques
- `04_loops.py` - Loop structures and iteration

#### Data Structures
- `05_listMethod.py` - List methods and operations
- `06_tupleMethod.py` - Tuple methods and immutable sequences
- `07_setMethod.py` - Set methods and unique element handling
- `08_dictionaryMethod.py` - Dictionary methods and key-value operations

#### Advanced Concepts
- `09_fileHandling.py` + `09_file_handling.ipynb` - File I/O operations
- `10_class.py` + `10_oops.ipynb` - Object-Oriented Programming
- `11_listComprehension.py` + `11_list_comprehensions.ipynb` - List comprehensions
- `12_lamdaFunction.py` - Lambda functions

**Total Files:** 16 (`.py` scripts + `.ipynb` notebooks)

---

### 02_NumPy
**Numerical computing and array operations**

#### Array Basics
- `13_numpy.py` - NumPy introduction and basics
- `14_npArray.py` - Array creation and manipulation
- `15_numpySquaring.py` - Array operations and squaring
- `16_numpyArray.py` - Advanced array techniques
- `17_reshaping.py` - Array reshaping and transformation

#### Indexing & Operations
- `18_indexing_&_Sclicing.py` - Array indexing and slicing
- `19_multidimensional_Indexing.py` - Multidimensional indexing
- `20_data_typeInNumpy.py` - NumPy data types
- `21_broadcastingArray.py` - Broadcasting operations
- `22_MathematicalFunction.py` - Mathematical functions

#### Interactive Notebooks
- `13-14-15_Speedtest.ipynb` - Performance comparisons
- `16-17_Creating_numpy_arrays.ipynb` - Array creation techniques
- `19_Multidimensional-Indexing-and-Axis.ipynb` - Multidimensional operations
- `20_Numpy-Data-Types.ipynb` - Data type handling
- `21_Broadcasting.ipynb` - Broadcasting concepts
- `22_MathematicalFunctions.ipynb` - Mathematical operations

#### Practice
- `numpy_exercises/` - NumPy practice exercises

**Total Files:** 21 (`.py` scripts + `.ipynb` notebooks + exercises folder)

---

### 03_Pandas
**Data manipulation and analysis with DataFrames**

#### Core Concepts
- `23_coreDataStructure.py` + `23_Core Data Structures.ipynb` - Series and DataFrame basics
- `24_creatingDataFrame.py` + `24_Creating DataFrames.ipynb` - DataFrame creation methods
- `25_dataSectionFiltering.py` + `25_Data-Selection-Filtering.ipynb` - Data selection and filtering

#### Data Processing
- `26_dataCleaning&Preprocessing.py` + `26_Data-Cleaning-and-preprocessing.ipynb` - Data cleaning
- `27_data_Transformation.py` + `27-Data-Transformation.ipynb` - Data transformation
- `28_melt&Pivot.py` + `28-Melt-and-Pivot.ipynb` - Reshaping data
- `29_Aggregration&Grouping.py` + `29-Aggregation-and-Grouping.ipynb` - Grouping and aggregation

#### Data Integration
- `30_Merging&Joining.py` + `30-MergingandJoining.ipynb` - Merging and joining datasets
- `31_WorkingWithCSVs.py` + `31-Working-with-CSVs.ipynb` - CSV file operations

**Total Files:** 18 (`.py` scripts + `.ipynb` notebooks)

---

### 04_Matplotlib
**Data visualization and plotting**

#### Plotting Basics
- `32_IntroductionToMatplotlib.py` + `32&33-IntroductiontoMatplotlib.ipynb` - Matplotlib introduction
- `33.matplotlibStyle.py` - Styling and customization

#### Chart Types
- `34_barChartInMatplotlib.py` + `34&35-BarPlot.ipynb` - Bar charts
- `35_barhChart.py` - Bar chart variations
- `36_pieChart.py` + `36-PieCharts.ipynb` - Pie charts
- `37_stackPlots.py` + `37-Stack_Plots.ipynb` - Stack plots
- `38_Histogram.py` - Histograms

**Total Files:** 11 (`.py` scripts + `.ipynb` notebooks)

---

### Resources
**Sample datasets and data files**

- `data.json` - JSON data samples
- `data_cleaning_sample.csv` - Data cleaning practice dataset
- `sample_dataset.csv` - General sample dataset
- `sample_dataset.xlsx` - Excel format dataset
- `student_dataset.csv` - Student information dataset
- `text.txt` - Text file for file handling practice
- `updated.csv` - Output file from data operations

**Total Files:** 7 data files

---

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.x
NumPy
Pandas
Matplotlib
Jupyter Notebook (for .ipynb files)
```

### Installation
```bash
pip install numpy pandas matplotlib jupyter openpyxl
```

### Running the Files

**Python Scripts:**
```bash
# Navigate to the topic folder
cd 01_Python_Basics
python 01_takingInput.py
```

**Jupyter Notebooks:**
```bash
# Navigate to the topic folder
cd 03_Pandas
jupyter notebook 24_Creating\ DataFrames.ipynb
```

## Topics Covered

### Programming Fundamentals
✓ Basic Input/Output  
✓ String Formatting  
✓ Control Flow (Loops & Conditionals)  
✓ Data Structures (Lists, Tuples, Sets, Dictionaries)  
✓ List Comprehensions  
✓ Lambda Functions  
✓ Object-Oriented Programming  
✓ File I/O Operations  

### Data Science & Analysis
✓ NumPy Arrays & Operations  
✓ Array Reshaping & Manipulation  
✓ **Pandas** - Data manipulation and analysis
✓ **Matplotlib & Seaborn** - Data visualization  
✓ **Statistical Analysis** - Descriptive and inferential statistics
✓ **Exploratory Data Analysis (EDA)** - Data exploration techniques
✓ **Data Cleaning & Preprocessing** - Handling missing values, outliers, normalization
✓ **Feature Engineering** - Creating and selecting features
✓ **Correlation & Relationships** - Finding patterns in data

### Machine Learning
✓ **Supervised Learning**
  - Regression (Linear, Polynomial, Ridge, Lasso)
  - Classification (Logistic Regression, Decision Trees, Random Forest, SVM, KNN)
✓ **Unsupervised Learning**
  - Clustering (K-Means, Hierarchical, DBSCAN)
  - Dimensionality Reduction (PCA, t-SNE)
✓ **Model Evaluation & Validation**
  - Train-Test Split
  - Cross-Validation
  - Performance Metrics (Accuracy, Precision, Recall, F1-Score, AUC-ROC)
✓ **Hyperparameter Tuning** - Grid Search, Random Search
✓ **Model Interpretation** - Feature importance, SHAP values

### Advanced Topics
✓ **Time Series Analysis** - Trend, seasonality, forecasting
✓ **Natural Language Processing (NLP)** - Text processing, sentiment analysis
✓ **Deep Learning** - Neural Networks, TensorFlow, PyTorch
✓ **Big Data & Spark** - Distributed computing basics
✓ **SQL & Databases** - Data retrieval and manipulation  

## 📖 Learning Path

This repository is designed for progressive learning. Follow the numbered folders in sequence:

### 🟢 Beginner Level
**Start here if you're new to Python**

1. **01_Python_Basics/** - Master Python fundamentals
   - Input/Output operations
   - Control flow (loops, conditionals)
   - Data structures (lists, tuples, sets, dictionaries)
   - File handling basics
   - Object-Oriented Programming
   - Functional programming (lambda, comprehensions)

### 🟡 Intermediate Level
**Build your data science toolkit**

2. **02_NumPy/** - Learn numerical computing
   - Array creation and manipulation
   - Indexing and slicing
   - Broadcasting and vectorization
   - Mathematical operations
   - Performance optimization

3. **03_Pandas/** - Master data manipulation
   - DataFrames and Series
   - Data selection and filtering
   - Data cleaning and preprocessing
   - Data transformation and reshaping
   - Grouping and aggregation
   - Merging and joining datasets

### 🔴 Advanced Level
**Visualize and communicate insights**

4. **04_Matplotlib/** - Create compelling visualizations
   - Basic plotting techniques
   - Customization and styling
   - Multiple chart types (bar, pie, histogram, stack plots)
   - Data storytelling

### 🎯 Next Steps
After completing this repository, you'll be ready for:
- **Statistical Analysis** - Hypothesis testing, distributions
- **Machine Learning** - Scikit-learn, model building
- **Deep Learning** - Neural networks with TensorFlow/PyTorch
- **Advanced Visualization** - Seaborn, Plotly, interactive dashboards

## Recommended Tools & Libraries

| Topic | Library |
|-------|---------|
| Data Manipulation | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Machine Learning | Scikit-learn, XGBoost, LightGBM |
| Deep Learning | TensorFlow, PyTorch, Keras |
| Statistical Analysis | SciPy, Statsmodels |
| Data Processing | Jupyter Notebook |
| Databases | SQLAlchemy, MongoDB |

## 💡 Key Features

✅ **Well-Organized Structure** - Topic-based folders for easy navigation  
✅ **Progressive Learning** - Numbered folders guide your learning journey  
✅ **Dual Format** - Both `.py` scripts and `.ipynb` notebooks for each topic  
✅ **Hands-On Practice** - Real datasets in Resources folder  
✅ **Comprehensive Coverage** - From Python basics to data visualization  
✅ **Industry-Standard Tools** - NumPy, Pandas, Matplotlib  
✅ **Ready to Run** - All file paths updated and working  

## 🎓 Ideal For

- **Beginners** learning Python from scratch
- **Students** building data science fundamentals
- **Professionals** transitioning to data science careers
- **Self-learners** following a structured curriculum
- **Educators** looking for organized teaching materials

## License

This is an educational repository for learning purposes.
