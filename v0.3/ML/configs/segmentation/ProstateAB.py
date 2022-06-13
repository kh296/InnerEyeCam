from InnerEye.ML.configs.segmentation.ProstateBase import ProstateBase


class ProstateAB(ProstateBase):
    def __init__(self) -> None:
        super().__init__(
            azure_dataset_id="ProstateInnerEyeAddenbrookes_02092020",  # type: ignore
            crop_size=(32, 224, 224),
            test_crop_size=(128, 320, 320),  # type: ignore
            inference_stride_size=(64, 160, 160),  # type: ignore
        )