from pathlib import Path
import subprocess
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from InnerEye.ML import runner


def main() -> None:
    runner.run(project_root=project_root,
               yaml_config_file=Path(project_root)/"InnerEyeCam/settings.yml",
               post_cross_validation_hook=runner
               .default_post_cross_validation_hook)


if __name__ == '__main__':
    cmd = 'pip install azureml-sdk[notebooks]'
    subprocess.run(cmd.split(), capture_output=True)
    main()
    pass
