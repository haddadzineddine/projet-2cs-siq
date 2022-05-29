import typer
import yaml
import socket

user = {
    "name": "John",
    "token": "12345"
}

IP = socket.gethostbyname(socket.gethostname())


class Deployment:
    def __init__(self, name, label, image, ip):
        self.name = name
        self.label = label
        self.image = image
        self.ip = ip

    def __getDeploymentTemplate():
        with open("templates/deployment.yaml") as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    def __generateDeployment(self):
        template = Deployment.__getDeploymentTemplate()
        template["metadata"]["name"] = self.name
        template['metadata']['labels']['app'] = self.label
        template['spec']['selector']['matchLabels']['app'] = self.label
        template['spec']['template']['metadata']['labels']['app'] = self.label
        template["spec"]["template"]["spec"]["containers"][0]["image"] = self.image
        template['spec']['template']['spec']['containers'][0]['name'] = self.name + '-conatiner'
        template['spec']['template']['spec']['containers'][0]['env'].append({
            "name": "DISPLAY",
            "value": self.ip + ":0.0"
        })
        return template

    def export(self):
        with open("generators/deployment.yaml", "w") as f:
            yaml.dump(self.__generateDeployment(), f)


def main():
    deployment = Deployment(
        user['name'], user['name'], 'haddadzineddine/packet-tracer', IP)

    deployment.export()


if __name__ == "__main__":
    main()
