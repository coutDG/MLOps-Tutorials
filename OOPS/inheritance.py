class ModelDeployment:
    def __init__(self , model_name , version):
        self.model_name = model_name
        self.version = version
    def deploy(self):
        print(f"Preparing {self.model_name} version {self.version}")
        

class DockerDeployment(ModelDeployment):
    def __init__(self, model_name, version , image_name):
        super().__init__(model_name , version)
        self.image_name = image_name
        
    def deploy(self):
        super().deploy()
        print(f"Starting container from image {self.image_name}")


deployment = DockerDeployment(
    model_name="churn-predictor",
    version = 'v1',
    image_name='churn-api:latest'
)

deployment.deploy()
