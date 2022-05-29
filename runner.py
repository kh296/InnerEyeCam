from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent / "InnerEye-DeepLearning"
sys.path.insert(0, str(project_root))
from InnerEye.ML import runner


def main() -> None:
    runner.run(project_root=project_root,
               yaml_config_file=Path("settings.yml"),
               post_cross_validation_hook=runner
               .default_post_cross_validation_hook)


if __name__ == '__main__':
    main()
    pass
