# AWS Solutions Architect Associate - Laboratorio 17

<br>

### Objetivo: 
* Despliegue de contenido dinámico en ClodFront

### Tópico:
* Content Delivery
* Compute

### Dependencias:
* Ninguna

<br>

---

### A - Despliegue de contenido dinámico en ClodFront

<br>

1. Debemos tener una llave Key Pair disponible. De no ser así, acceder al servicio EC2 y luego a la opción "Key Pair". Generar llave RSA y .pem 

2. Acceder al servicio AWS Cloud9 y generar un nuevo ambiente de trabajo (Ubuntu 18.04 LTS)

3. Ejecutar los siguinentes comandos en nuestro Cloud9

```bash
#Ubuntu 18.04
sudo apt-get update
git clone https://github.com/jbarreto7991/aws-solutionsarchitectassociate.git
```

4. Acceder al laboratorio 17 (Lab-17), carpeta "code". Validar que se cuenta con dos archivos CloudFormation: "1_lab17-vpc.yaml" y "2_lab17-ec2.yaml". Analizar el contenido de estos archivos.

5. Desplegar cada plantilla CloudFormation ejecutando AWSCLI. Considerar los parámetros a ser ingresados.

    <br>
6. **1_lab17-vpc.yaml** (Esperar el despliegue total de esta plantilla cloudformation para continuar con la siguiente plantillas). En la sección "ParameterValue", ingresar el nombre del KeyPair creado en el paso 1. Esta plantilla creará la VPC "192.168.0.0/16", 06 Subnets dentro de este CIDR, un NAT Instances y demás componentes de red. No deberán existir redes existentes en este rango de IPs. Validar la creación del Stack desde la consola AWS a través del servicio AWS CloudFormation. El siguiente comando considera el valor "aws-solutionsarchitectassociate" para el KeyPair, reemplazar el nombre según la llave respectiva.

```bash
aws cloudformation create-stack --stack-name lab17-vpc --template-body file://~/environment/aws-solutionsarchitectassociate/Lab-17/code/1_lab17-vpc.yaml --parameters ParameterKey=KeyPair,ParameterValue="aws-solutionsarchitectassociate" --capabilities CAPABILITY_IAM
```

7. **2_lab17-ec2.yaml**. En la sección "Parameters", ingresar el nombre del KeyPair creado en el paso 1. Esta plantilla creará dos instancias EC2 (PROD BACKEND y PROD DB), un balanceador de aplicaciones y un Bucket S3 (con el nombre 'aws-solutionsarchitectassociate-${AWS::AccountId}').

```bash
aws cloudformation create-stack --stack-name lab17-ec2 --template-body file://~/environment/aws-solutionsarchitectassociate/Lab-17/code/2_lab17-ec2.yaml --parameters ParameterKey=KeyPair,ParameterValue="aws-solutionsarchitectassociate" --capabilities CAPABILITY_IAM
```


### Eliminación de recursos

```bash
aws cloudformation delete-stack --stack-name lab16-cloudfront-s3
```

---

### Enlaces

 - https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/UpdatingExistingObjects.html