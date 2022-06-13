from InnerEye.ML.configs.segmentation.ProstateBase import ProstateBase


class HeadAndNeckAB442a(ProstateBase):
    def __init__(self) -> None:
        super().__init__(
            ground_truth_ids=[
                "spinal_cord", "spc_muscle", "smg_r", "smg_l",
                "optic_nerve_r", "lens_r", "globe_r", "cochlea_r",
                "pituitary_gland", "parotid_r", "parotid_l",
                "optic_chiasm", "mpc_muscle", "mandible",
                "lacrimal_gland_r", "lacrimal_gland_l", "optic_nerve_l",
                "lens_l", "globe_l", "cochlea_l", "external", "brainstem"],
            azure_dataset_id="HeadAndNeckInnerEyeAddenbrookes_02092020",
            crop_size=(8, 256, 256),
            test_crop_size=(8, 256, 256),
            inference_stride_size=(4, 128, 128),
            feature_channels=[8],
            num_dataload_workers=4,
            dataset_csv="dataset.csv",
            num_downsampling_paths=3,
        )
