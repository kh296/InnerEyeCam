#!/bin/bash

# Set InnerEye version
INNEREYE_VERSION="v0.3"

# Clone the InnerEye-DeepLearning repository, deleting any pre-existing clone,
# then checkout required version.
cd ..
rm -rf InnerEye-DeepLearning
git clone https://github.com/microsoft/InnerEye-DeepLearning
cd InnerEye-DeepLearning
git checkout ${INNEREYE_VERSION}

# Copy InnerEyeCam codebase to InnerEye-DeepLearning
cd ..
cp -rp InnerEyeCam InnerEye-DeepLearning

# Copy modified files from InnerEyeCam/ML to InnerEye/ML.
FILES="model_testing.py\
       dataset/full_image_dataset.py\
       visualizers/plot_cross_validation.py"
cd InnerEye-DeepLearning
for FILE in ${FILES}
do
       	cp InnerEyeCam/ML/${INNEREYE_VERSION}/${FILE} InnerEye/ML/${FILE}
done

# Copy model configuration files from InnerEyeCam/${INNEREYE_VERSION}
# to InnerEye-DeepLearning/InnerEyeCam
cp -rp InnerEyeCam/ML/${INNEREYE_VERSION}/configs InnerEyeCam/ML

# Copy modified environment file from InnerEyeCam to InnerEye-DeepLearning.
cp InnerEyeCam/${INNEREYE_VERSION}/environment.yml ./environment.yml

# Create conda environment for running InnerEye-DeepLearning applications.
source InnerEyeCam/conda-setup.sh
conda env remove --name InnerEyeCam
conda env create
conda activate InnerEyeCam
