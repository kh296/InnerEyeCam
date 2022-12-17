#!/bin/bash

# Set InnerEye version
INNEREYE_VERSION="v0.8"

# Clone the InnerEye-DeepLearning repository, deleting any pre-existing clone,
# then checkout required version.
cd ..
rm -rf InnerEye-DeepLearning
git clone --recursive https://github.com/microsoft/InnerEye-DeepLearning
cd InnerEye-DeepLearning
git checkout ${INNEREYE_VERSION}

# Copy InnerEyeCam codebase to InnerEye-DeepLearning
cd ..
cp -rp InnerEyeCam InnerEye-DeepLearning

# Copy modified files from InnerEyeCam/ML to InnerEye/ML.
case ${INNEREYE_VERSION} in
	v0.3)
		FILES="model_testing.py\
			dataset/full_image_dataset.py\
			visualizers/plot_cross_validation.py"
		;;
	*)
		FILES="model_testing.py\
			dataset/full_image_dataset.py"
		;;
esac
cd InnerEye-DeepLearning
for FILE in ${FILES}
do
       	cp InnerEyeCam/${INNEREYE_VERSION}/ML/${FILE} InnerEye/ML/${FILE}
done

# Copy model configuration files from InnerEyeCam/${INNEREYE_VERSION}
# to InnerEye-DeepLearning/InnerEyeCam
mkdir -p InnerEyeCam/ML
cp -rp InnerEyeCam/${INNEREYE_VERSION}/ML/configs InnerEyeCam/ML/configs

# Copy modified environment file(s) from InnerEyeCam to InnerEye-DeepLearning.
cp InnerEyeCam/${INNEREYE_VERSION}/environment.yml ./environment.yml
SRC=InnerEyeCam/${INNEREYE_VERSION}/primary_deps_mac.yml
if [[ -e ${SRC} ]]; then
    cp ${SRC} ./primary_deps_mac.yml
fi

# Create conda environment for running InnerEye-DeepLearning applications.
source InnerEyeCam/conda-setup.sh
conda env remove --name InnerEyeCam
if [[ "$(uname)" == "Darwin" && ${INNEREYE_VERSION} != "v0.3" ]]; then
    conda env create --file primary_deps_mac.yml
else
    conda env create --file environment.yml
fi
conda activate InnerEyeCam

if [[ "$(uname)" == "Darwin" ]]; then
    pip install azureml-sdk[notebooks]
fi
