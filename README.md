# Human Action Recognition in the Dark using Two-Stream CNN

![Demo](demo.gif)

## Overview

This repository contains code and resources for the project "Human Action Recognition in the Dark using Two-Stream CNN." The project aims to recognize human actions in low-light or dark environments by leveraging a two-stream Convolutional Neural Network (CNN) architecture. The two-stream CNN incorporates spatial and temporal information to improve action recognition performance under challenging lighting conditions.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Dataset](#dataset)
- [Training](#training)
- [Inference](#inference)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Prerequisites

Before running the code, ensure you have the following dependencies installed:

- Python 3.x
- TensorFlow
- Keras
- OpenCV
- NumPy
- Matplotlib

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/human-action-recognition.git
cd human-action-recognition
pip install -r requirements.txt


#for dataset

dataset/
    train/
        class_1/
            video_1.avi
            video_2.avi
            ...
        class_2/
            video_3.avi
            video_4.avi
            ...
        ...
    test/
        class_1/
            video_5.avi
            video_6.avi
            ...
        class_2/
            video_7.avi
            video_8.avi
            ...
        ...


# For training

python train.py --config config.yaml


# For Inference

python infer.py --input path/to/input/video.avi --model path/to/model/checkpoint.h5 --config config.yaml


# License

This project is licensed under the MIT License.

# Acknowledgments

We want to thank the authors of the datasets used in this project for making their data available. Additionally, we extend our gratitude to the open-source community for providing invaluable resources that helped us in building this project.


In this consolidated version, all the content from "Installation" to "Acknowledgments" is included in one `README.md` file. Again, make sure to customize the sections as needed for your specific project details and include relevant information about your work.




