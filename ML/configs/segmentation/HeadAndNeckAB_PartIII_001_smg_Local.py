from pathlib import Path
from platform import platform

import pandas as pd

from InnerEye.ML.configs.segmentation.ProstateBase import ProstateBase
from InnerEye.ML.utils.split_dataset import DatasetSplits

class HeadAndNeckAB_PartIII_001_smg_Local(ProstateBase):
    def __init__(self) -> None:
        if "Linux" == platform():
            local_dataset=Path("/r02/voxtox/project_data_2022_nifti")
            output_to="/r02/voxtox/inner_eye_training"
        else:
            local_dataset=Path("/Users/karl/data/HeadAndNeck_PartIII_20220312")
            output_to="/Users/karl/data/inner_eye_training"
        super().__init__(
            ground_truth_ids=[
                "smg_left", "smg_right"],
            local_dataset=local_dataset,
            crop_size=(16, 128, 128),
            test_crop_size=(128, 512, 512),
            inference_stride_size=(48, 512, 512),
            #crop_size=(16, 128, 128),
            #test_crop_size=(32, 256, 256),
            #inference_stride_size=(16, 128, 128),
            feature_channels=[16],
            num_dataload_workers=4,
            dataset_csv="dataset_smg.csv",
            num_downsampling_paths=4,
            check_exclusive=False,
            output_to=output_to,
        )

    def get_model_train_test_dataset_splits(
            self, dataset_df: pd.DataFrame) -> DatasetSplits:
        """
        Return an adjusted split
        """
        return DatasetSplits.from_proportions(
                dataset_df,
                proportion_train=0.80,
                proportion_val=0.15,
                proportion_test=0.05,
                random_seed=0)
