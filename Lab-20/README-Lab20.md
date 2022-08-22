# AWS Solutions Architect Associate - Laboratorio 20

<br>

### Objetivo: 
* Creación de un IAM User Programmatic
* Uso del SDK de Python (boto3)
* Uso de IAM roles

### Tópico:
* Security,Identity & Compliance

### Dependencias:
* Ninguna

<br>

---

### A - Creación de un IAM User Programmatic

<br>

1. Hacer uso de nuestra Key Pair. De no ser así, acceder al servicio EC2 y luego a la opción "Key Pair" de cada región indicada. Generar llave RSA y .pem.

2. Acceder al servicio AWS Cloud9 y generar un nuevo ambiente de trabajo (Ubuntu 18.04 LTS)

3. Ejecutar los siguientes comandos en nuestro Cloud9

```bash
#Ubuntu 18.04
sudo apt-get update
git clone https://github.com/jbarreto7991/aws-solutionsarchitectassociate.git
```

4. **1_lab20-vpc-ec2-iam.yaml**. En la sección "ParameterValue", reemplazar el nombre del KeyPair creado en el paso 1. Esta plantilla creará una VPC, 02 subnets públicas y demás componentes de red; además de una instancia EC2. Validar la creación del Stack desde la consola AWS a través del servicio AWS CloudFormation. El siguiente comando considerar reemplazar el valor del Key Pair con el valor respectivo.

```bash
aws cloudformation create-stack --stack-name lab20-vpc-ec2-iam --template-body file://~/environment/aws-solutionsarchitectassociate/Lab-20/code/1_lab20-vpc-ec2-iam.yaml --parameters ParameterKey=KeyPair,ParameterValue="aws" --capabilities CAPABILITY_IAM --region us-east-1

```


```bash
aws cloudformation delete-stack --stack-name lab19-vpc-ec2-alb-nvirginia --region us-east-1
aws cloudformation delete-stack --stack-name lab19-vpc-ec2-alb-paris --region eu-west-3

```