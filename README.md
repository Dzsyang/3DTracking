# A 3D real-time tracking microscopy based on machine learning algorithm (T370PRP45001)

## Introduction

- Goal: Individual identification and tracking with high density.
- Milestones: 2D with low density ---> 2D with high density ---> 3D with high density.
- Languages: `Python` for machine learning; `C++` for controlling.

## Group Members

<a href="https://github.com/Dzsyang/3DTracking/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Dzsyang/3DTracking" />
</a>

## Progress Log

## References (Literature Review)

### all-in-one

- **BTrack**
  - Paper:
    - [Automated deep lineage tree analysis using a Bayesian single cell tracking approach](https://www.frontiersin.org/article/10.3389/fcomp.2021.734559) [![doi:10.3389/fcomp.2021.734559](https://img.shields.io/badge/doi-10.3389%2Ffcomp.2021.734559-blue)](https://doi.org/10.3389/fcomp.2021.734559)
    - [Local cellular neighbourhood controls proliferation in cell competition](http://www.molbiolcell.org/content/28/23/3215.abstract) [![doi:10.1091/mbc.E17-06-0368](https://img.shields.io/badge/doi-10.1091%2Fmbc.E17--06--0368-blue)](https://doi.org/10.1091/mbc.E17-06-0368)
  - Code:
    - [Github repo](https://github.com/quantumjot/btrack)
    - Form: Python package
  - Using:
  - Methods:
  - Test:
- **Deeptrack**
  - Paper:
    - [Quantitative Digital Microscopy with Deep Learning](https://pubs.aip.org/aip/apr/article/8/1/011310/238663/Quantitative-digital-microscopy-with-deep-learning)
  - Code:
    - [Github repo](https://github.com/DeepTrackAI/DeepTrack2)
    - Form: Python package
  - Using:
    - U-Net
    - lodeSTAR
    - MAGIK
  - Methods:
  - Test:
    - [ ] in ``
- **ULTRACK**
  - Paper:
    - [Large-Scale Multi-Hypotheses Cell Tracking Using Ultrametric Contours Maps](https://www.researchgate.net/publication/373016698_Large-Scale_Multi-Hypotheses_Cell_Tracking_Using_Ultrametric_Contours_Maps)
  - Code:
    - [Github repo](https://github.com/royerlab/ultrack)
    - Form: Python package
  - Using:
    - Watershed
    - Cellpose
    - Stardist
    - U-Net
    - ILP(integer linear programming)
  - Methods:
  - Test:
    - [ ] in ``
- **EmbedTrack**
  - Paper:
    - [EmbedTrack—Simultaneous Cell Segmentation and Tracking Through Learning Offsets and Clustering Bandwidths](https://ieeexplore.ieee.org/document/9834915)
  - Code:
    - [Github repo](https://github.com/kaloeffler/EmbedTrack)
    - Form: Python project (no package)
  - Using:
  - Methods:
  - Test:
- **LIM tracker**
  - Paper
    - [LIM Tracker: a software package for cell tracking and analysis with advanced interactivity](https://www.nature.com/articles/s41598-022-06269-6)
  - Code:
    - [Github repo](https://github.com/LIMT34/LIM-Tracker)
    - Form: Fiji plugin
  - Using:
    - Cellpose
    - Stardist
  - Methods:
  - Test:

### cell segmentation

- **Cellpose**
  - Paper
    - [Cellpose3: one-click image restoration for improved cellular segmentation](https://www.biorxiv.org/content/10.1101/2024.02.10.579780v1)
  - Code:
    - [Github repo](https://github.com/MouseLand/cellpose)
    - Form: Python package
  - Using:
    - Pytorch
  - Methods:
  - Test:
    - [ ] in `tests/cell_segment/cellpose/`
- **Stardist**
  - Paper:
    - [Cell Detection with Star-Convex Polygons](https://link.springer.com/chapter/10.1007/978-3-030-00934-2_30)
    - [Star-convex Polyhedra for 3D Object Detection and Segmentation in Microscopy](https://openaccess.thecvf.com/content_WACV_2020/papers/Weigert_Star-convex_Polyhedra_for_3D_Object_Detection_and_Segmentation_in_Microscopy_WACV_2020_paper.pdf)
  - Code:
    - [Github repo](https://github.com/stardist/stardist)
    - Form: Python package / Desktop app / Fiji/ImageJ/... plugin
  - Using:
    - Tensorflow
  - Methods:
  - Test:
    - [ ] in `tests/cell_segment/stardist/`
