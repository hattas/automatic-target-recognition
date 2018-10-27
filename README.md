# Automatic Target Recognition (ATR) for CT-based Airport Screening System

Description: Project to classify CT images as target or non-target.

EECE 5890: Machine Learning for Image Processing

Professor: [Dong Hye Ye, Ph.D.](https://sites.google.com/site/yedonghye/)

## Authors

* **[John Hattas](https://github.com/johnhattas)**
* **[Nathan Lang](https://github.com/Nathanlang14)**

## ATR

### Targets
* Saline
  * 3.5%, 10%, 15% concentrations
* Modeling (polymer) clay
* Rubber sheets: ¼” thickness (minimum) + other rubber in bags

### Non-Targets
* Food
* Drinks
* Electronics
* Magazines
* Containers not filled with saline

### Dataset
Cropped CT image for each segmented object
#### Target labels
Non-target:0,
Saline:1,
Rubber:2,
Clay:3

### Image Quality
Many artifacts which lead to imprecise density, volume, mass, shape

### Possible features
* Mass
* Mean
* Standard deviation
* Histograms
* Higher-order moments
  * Skew, kurtosis, entropy
* Texture
  * Wavelets

### Possible classifiers
* PCA
* SVM
* Decision Tree
* Adaboost
* Deep neural network

### Performance metric
PD = # targets detected / # targets scanned<br>
PFA = # false alarm objects / # non-targets scanned

Goal: PD > 90%, PFA < 10%

### Data Files
Nifti file format: Standard Neuroimaging File Format<br>
.nii.gz: gzipped image

#### Python
[PyNifti](http://niftilib.sourceforge.net/pynifti/)<br>
[NiBabel](http://nipy.org/nibabel/) (newer version of PyNifti)

#### Visualization
[MIPAV](https://mipav.cit.nih.gov/)