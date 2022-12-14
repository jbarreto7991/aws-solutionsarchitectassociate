# AWS Solutions Architect Associate - Laboratorio 54

<br>

### Objetivo: 
* Uso del servicio ECR (Elastic Container Registry) y upload de una imagen Docker
* Creación de un cluster ECS-EC2 (Elastic Container Services) y uso de un task definition y services

### Tópico:
* Container

### Dependencias:
* Ninguna

<br>

---

### A - Uso del servicio ECR (Elastic Container Registry) y upload de una imagen Docker

<br>

<br>

1. Acceder al servicio AWS Cloud9 y generar un nuevo (o encender nuestro) ambiente de trabajo (Ubuntu 18.04 LTS)

2. Ejecutar los siguientes comandos en nuestro Cloud9

```bash
#Ubuntu 18.04
sudo apt-get update
git clone https://github.com/jbarreto7991/aws-solutionsarchitectassociate.git
```

3. Acceder al laboratorio 54 (Lab-54), carpeta "code" y desplegar la plantilla "1_lab54-vpc-alb-rds.yaml" vía CloudFormation usando AWSCLI. Esta plantilla contiene un parámetro de despliegue "Key Pair" el cual se deberá personalizar.

```bash
aws cloudformation create-stack --stack-name lab54-vpc-alb-rds --template-body file://~/environment/aws-solutionsarchitectassociate/Lab-54/code/1_lab54-vpc-alb-rds.yaml --parameters ParameterKey=KeyPair,ParameterValue="aws-solutionsarchitectassociate" --capabilities CAPABILITY_IAM
```

4. Desde Cloud9