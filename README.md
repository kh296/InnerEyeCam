# InnerEyeCam

Package to simplify installation and use under MacOS of [InnerEye-DeepLearning](https://github.com/microsoft/InnerEye-DeepLearning) applications.

This package contains the following:

- `install.sh`: script for installing [InnerEye-DeepLearning](https://github.com/microsoft/InnerEye-DeepLearning);
- `ML`: directory containing modules modified with respect to the
  [InnerEye-DeepLearning](https://github.com/microsoft/InnerEye-DeepLearning)
  originals, and containing a `configs` sub-directory for storing
  model configurations;
- environment.yml : file defining creation of 'conda' environment for running
  [InnerEye-DeepLearning](https://github.com/microsoft/InnerEye-DeepLearning)
  applications;
- runner.py : script for running
  [InnerEye-DeepLearning](https://github.com/microsoft/InnerEye-DeepLearning)
  applications;
- settings.py : settings for configuration variables used when running
  [InnerEye-DeepLearning](https://github.com/microsoft/InnerEye-DeepLearning)
  applications;
- conda-setup.sh : script for activating the `conda` environment for running
  [InnerEye-DeepLearning](https://github.com/microsoft/InnerEye-DeepLearning)
  applications;
- train.sh : script for executing a
  [InnerEye-DeepLearning](https://github.com/microsoft/InnerEye-DeepLearning)
  training run.
- test: directory for scripts to test installation.
- README.md : file containing this help information.

## Installation

1. Clone the [InnerEyeCam]() repository:

   ```
   git clone
   ```

2. Ensure that a working installation of [conda](https://docs.conda.io/projects/conda/en/latest/) is available.  By default `conda` tools for MacOS are
assumed to be in the directory: `/opt/miniconda3/`.  If this isn't the case,
then the file `InnerEyeCam/conda-setup.sh` needs to be changed to reflect the
actual location.

3. Change to the directory `InnerEyeCam`:
   
   ```
   cd InnerEyeCam
   ```

4. Run the install script:

   ```
   ./install.sh
   ```

   This performs the following operations:
   
    - It clones [InnerEye-DeepLearning](https://github.com/microsoft/InnerEye-DeepLearning) into the same directory as `InnerEyeCam`, deleting any pre-existing clone, then check out the version tagged v0.3.

    - It recursviely copies the `InnerEyeCam` directory to
      `InnerEye-DeepLearning'.

    - Within `InnerEye-DeepLearning`, It copies from `InnerEyeCam/ML`
      to `InnerEye/ML` the files:

      ```
      model_testing.py
      dataset/full_image_dataset.py
      visualizers/plot_cross_validation.py
      ```

      The first two have changes with respect to the [InnerEye-DeepLearning](https://github.com/microsoft/InnerEye-DeepLearning) originals,
      to enable multi-threading under MacOS.  The third has changes
      to avoid crashes in cases of datasets with CSV_SERIES_HEADER and/or
      CSV_INSTITUTION_HEADER undefined.

    - It copies `InnerEyeCam/environment.yml` to `InnerEye-DeepLearning`.
      
    - It creates a `conda` environment for running
      [InnerEye-DeepLearning](https://github.com/microsoft/InnerEye-DeepLearning)
      applications.

5. After installation, the directory structure should be as follows:
   ```
                   |
        ----------------------
        |                    |       
   InnerEyeCam     InnerEye-DeepLearning
                             |
                      ----------------
                      |              |
                   InnerEye     InnerEyeCam
   ```
   When running on Azure, it's expected that all code should be in
   a single directory tree: `InnerEye-DeepLearning`.  All subsequent
   user modifications should then be in `InnerEye-DeepLearning/InnerEyeCam`.

## Preparing to run [InnerEye-DeepLearning](https://github.com/microsoft/InnerEye-DeepLearning)

1. Add any model configurations to be used to the directory
   `InnerEye-DeepLearning/InnerEyeCam/ML/configs/segmentation`.

2. Edit as needed `InnerEye-DeepLearning/InnerEyeCam/settings.yml`.  For
   explanation of settings, see:
   - [How to setup Azure Machine Learning for InnerEye - Step 6](https://github.com/microsoft/InnerEye-DeepLearning/blob/main/docs/setting_up_aml.md#step-6-update-the-variables-in-settingsyml)

3. Edit as needed `InnerEye-DeepLearning/InnerEyeCam/train.sh`.  This includes
   examples of commands for running `InnerEye-DeepLearning` applications
   locally and on Azure, with explanations of the parameters used.

# Performing a training run

1. Execute the script `InnerEye-DeepLearning/InnerEyeCam/train.sh`.

2. If submitting to Azure, progress can be monitored at:
   - [https://ml.azure.com/](https://ml.azure.com/)
