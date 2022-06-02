from datetime import datetime
from pathlib import Path
import subprocess
import sys

# Allow for this file to be in a directory
# inside or alongside InnerEye-DeepLearning.
runner_path = Path(__file__).resolve()
if (runner_path.parent.parent / "InnerEye-DeepLearning").exists():
    project_root = runner_path.parent.parent / "InnerEye-DeepLearning"
else:
    project_root = runner_path.parent.parent

sys.path.insert(0, str(project_root))


def main() -> None:
    from InnerEye.ML import runner
    runner.run(project_root=project_root,
               yaml_config_file=Path(project_root)/"InnerEyeCam/settings.yml",
               post_cross_validation_hook=runner
               .default_post_cross_validation_hook)


if __name__ == '__main__':
    # Workaround to obtain older versions of some packages.
    # These are downgrades to some of the packages installed
    # in the conda environment setup.
    if not Path("runner.log").exists():
        cmd = 'pip install azureml-sdk[notebooks]'
        print(f"Completing installation: '{cmd}'")
        cmd_output = subprocess.run(cmd.split(), capture_output=True, text=True)
        with open("runner.log", "w") as runner_log:
            now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            header = f"{now} - '{runner_path}'"
            bannerline = min(80, len(header)) * "="
            runner_log.write(bannerline)
            runner_log.write(f"\n{header}\n")
            runner_log.write(bannerline)
            runner_log.write(f"\n\n{cmd}\n\n{cmd_output.stdout}")

    main()
    pass
