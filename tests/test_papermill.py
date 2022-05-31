from papermill import execute_notebook
from pathlib import Path

# Define directories for input and output data.
data_dir = Path("data").resolve()
tmp_dir = Path("tmp").resolve()
tmp_dir.mkdir(parents=True, exist_ok=True)

# Define paths to template notebook and results notebook.
template_notebook = data_dir / "segmentation_report.ipynb"
result_notebook = tmp_dir / "report_Segmentation.ipynb"

# Use as metric values results from an InnerEye training run.
notebook_params = {
        "train_metrics_csv": "",
        "val_metrics_csv": str(data_dir / "val_metrics.csv"),
        "test_metrics_csv": str(data_dir / "test_metrics.csv"),
        }

def test_execute_notebook():
    # Test execution of Jupyter notebooks by papermill.
    # Use with incompatible versions of jupyter-console and jupyter-client
    # can result in traceback ending:
    # RuntimeWarning: coroutine 'ZMQSocketChannel.msg_ready' was never awaited.
    # See, for example:
    # https://github.com/jupyter/jupyter_console/issues/241
    # This test should then fail.
    if result_notebook.exists():
        result_notebook.unlink()
    execute_notebook(input_path=str(template_notebook),
                     output_path=str(result_notebook),
                     parameters=notebook_params,
                     progress_bar=False,
                     iopub_timeout=10)
    assert result_notebook.exists()
