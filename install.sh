#!/bin/bash

# Clone the InnerEye-DeepLearning repository, deleting any pre-existing clone,
# then checkout version v0.3.
INNEREYECAM=`pwd`
cd ..
rm -rf InnerEye-DeepLearning
git clone https://github.com/microsoft/InnerEye-DeepLearning
cd InnerEye-DeepLearning
git checkout v0.3
cd ${INNEREYECAM}

# Copy files from InnerEyeCam to InnerEye-DeepLearning.
FILES="model_testing.py\
       dataset/full_image_dataset.py\
       visualizers/plot_cross_validation.py"
for FILE in ${FILES}
do
       	cp ML/${FILE} ../InnerEye-DeepLearning/InnerEye/ML/${FILE}
done

# Create conda environment for running InnerEye-DeepLearning applications.
source conda-setup.sh
conda env remove --name InnerEyeCam
conda env create
conda activate InnerEyeCam
pip install azureml-sdk[notebooks]
