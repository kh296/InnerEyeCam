import pandas as pd

from InnerEye.ML.configs.segmentation.ProstateBase import ProstateBase
from InnerEye.ML.utils.split_dataset import DatasetSplits


class HeadAndNeckAB_OSAI_001_smg(ProstateBase):
    def __init__(self) -> None:
        super().__init__(
            ground_truth_ids=[
                "smg_l", "smg_r"],
            azure_dataset_id="HeadAndNeckInnerEyeAddenbrookes_02092020",
            crop_size=(16, 128, 128),
            test_crop_size=(32, 256, 256),
            inference_stride_size=(16, 128, 128),
            feature_channels=[32],
            num_dataload_workers=8,
            dataset_csv="dataset.csv",
            num_downsampling_paths=4,
            check_exclusive=False,
        )

    def get_model_train_test_dataset_splits(
            self, dataset_df: pd.DataFrame) -> DatasetSplits:
        """
        Return an adjusted split
        """
        return DatasetSplits.from_proportions(
                dataset_df,
                proportion_train=0.8,
                proportion_val=0.05,
                proportion_test=0.15,
                random_seed=0)
