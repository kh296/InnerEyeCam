#!/bin/bash

# Script for executing an InnerEye-DeepLearning training run.

# Set up conda and activate InnerEyeCam environment.
source ./conda-setup.sh
conda activate InnerEyeCam

# Execute cache.py module of black
# (https://black.readthedocs.io/en/stable/index.html).
# This seems to prevent some crashes that otherwise
# occur - reason not understood.
black ${CONDA_PREFIX}/lib/python3.7/site-packages/black/cache.py

# Run InnerEye-DeepLearning application.

# Obtain help information.
# --help : print help information
# python runner.py --help

# Run training on Azure.
# --azureml=True: Submit to Azure.
# --model=HeadAndNeckAB442a: Perform training for model
#    HeadAndNeckAB442a (.py file in ML/configs/segmentation)
# --num_epoch=120: Perform 120 passes of the training data.
# --number_of_cross_validation_splits=5: Split datasets into 5 parts
#    for cross validation.
# --monitoring_interval_seconds=120: Check progress every 1200 seconds.
# --experiment_name: Define name for this training run (experiment).
#python runner.py --azureml=True --model=HeadAndNeckAB442a --num_epoch=30 --train=True --number_of_cross_validation_splits=2 --cluster=NC24 --monitoring_interval_seconds=120 --experiment_name=head_and_neck_ab_120_epochs_5_splits

# Run training locally.
# --azureml=False: Don't submit to Azure.
# --model=HeadAndNeckAB_PartIII_001_smg_Local: Perform training for model
#    HeadAndNeckAB_PartIII_001_smg_Local (.py file in ML/configs/segmentation)
# --num_epoch=50: Perform 50 passes of the training data.
# --number_of_cross_validation_splits=0: Don't perform cross validation.
# --monitoring_interval_seconds=50: Check progress every 50 seconds.
# --experiment_name: Define name for this training run (experiment).
python runner.py --azureml=False --model=HeadAndNeckAB_PartIII_001_smg_Local --num_epoch=50 --train=True --number_of_cross_validation_splits=0 --monitoring_interval_seconds=50 --experiment_name=head_and_neck_ab_partiii_001_local_30_epochs_0_splits
