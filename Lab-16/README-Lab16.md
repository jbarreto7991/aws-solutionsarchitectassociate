# AWS Solutions Architect Associate - Laboratorio 16

<br>

### Objetivo: 
* Restringir el acceso al contenido de S3 usando OAI (Origin Access Identities) en CloudFront 


### Tópico:
* Storage
* Content Delivery

### Dependencias:
* Ninguna

<br>

---

### A - Restringir el acceso al contenido de S3 usando OAI (Origin Access Identities) en CloudFront 


<br>

1. Acceder al servicio AWS Cloud9 y generar un nuevo (encender nuestro) ambiente de trabajo (Ubuntu 18.04 LTS)

2. Ejecutar los siguinentes comandos en nuestro Cloud9

```bash
#Ubuntu 18.04
sudo apt-get update
git clone https://github.com/jbarreto7991/aws-solutionsarchitectassociate.git
```

3. Acceder al laboratorio 13 (Lab-13), carpeta "code". Validar que se cuenta con tres archivos CloudFormation: "1_lab13-vpc.yaml", "2_lab13-ec2.yaml" y "3_lab13_alb_targetgroup". Analizar el contenido de estos archivos.

5. Desplegar cada plantilla CloudFormation ejecutando AWSCLI. Considerar los parámetros a ser ingresados.

    <br>
6. **1_lab13-vpc.yaml** (Esperar el despliegue total de esta plantilla cloudformation para continuar con las siguientes plantillas). En la sección "ParameterValue", ingresar el nombre del KeyPair creado en el paso 1. Esta plantilla creará la VPC "192.168.0.0/16", 06 Subnets dentro de este CIDR, un NAT Instances y demás componentes de red. No deberán existir redes existentes en este rango de IPs. Validar la creación del Stack desde la consola AWS a través del servicio AWS CloudFormation. El siguiente comando considera el valor "aws-solutionsarchitectassociate" para el KeyPair, reemplazar el nombre según la llave respectiva.

```bash
aws cloudformation create-stack --stack-name lab13-vpc --template-body file://~/environment/aws-solutionsarchitectassociate/Lab-13/code/1_lab13-vpc.yaml --parameters ParameterKey=KeyPair,ParameterValue="aws-solutionsarchitectassociate" --capabilities CAPABILITY_IAM
```


### Eliminación de recursos

```bash
aws cloudformation delete-stack --stack-name lab15-alb-targetgroup
aws cloudformation delete-stack --stack-name lab15-ec2
aws cloudformation delete-stack --stack-name lab15-vpc
```