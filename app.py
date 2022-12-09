import lightning as L
from lai_jupyter import JupyterLab


class JupyterLabManager(L.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.jupyter_work = JupyterLab(cloud_compute=L.CloudCompute("cpu-small"))

    def run(self):
        self.jupyter_work.run()

    def configure_layout(self):
        return [{"name": "JupyterLab", "content": self.jupyter_work}]


app = L.LightningApp(JupyterLabManager())