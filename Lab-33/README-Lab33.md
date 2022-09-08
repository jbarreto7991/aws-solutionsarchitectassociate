# AWS Solutions Architect Associate - Laboratorio 33

<br>

### Objetivo: 
* Aprovisionamiento de una instancia RDS desde CloudFormation usando Secrets Manager como generador de credenciales

### Tópico:
* Database
* Security, Identity & Compliance

### Dependencias:
* Ninguna

<br>


---

### A - Aprovisionamiento de una instancia RDS desde CloudFormation usando Secret Manager como generador de credenciales

<br>

1. Debemos tener una llave Key Pair disponible. De no ser así, acceder al servicio EC2 y luego a la opción "Key Pair". Generar llave RSA y .pem 

2. Acceder al servicio AWS Cloud9 y generar un nuevo ambiente de trabajo (Ubuntu 18.04 LTS)

3. Ejecutar los siguinentes comandos en nuestro Cloud9

```bash
#Ubuntu 18.04
sudo apt-get update
git clone https://github.com/jbarreto7991/aws-solutionsarchitectassociate.git
```

4. Acceder al laboratorio 33 (Lab-33), carpeta "code". Validar que se cuenta con tres archivos CloudFormation: "1_lab33-vpc.yaml", "2_lab33-secret-manager-rds.yaml" y "3_lab33-ec2-s3.yaml". Analizar el contenido de estos archivos.

5. Desplegar cada plantilla CloudFormation ejecutando AWSCLI. Considerar los parámetros a ser ingresados.

    <br>
6. **1_lab33-vpc.yaml** (Esperar el despliegue total de esta plantilla cloudformation para continuar con las siguientes plantillas). En la sección "ParameterValue", ingresar el nombre del KeyPair creado en el paso 1. Esta plantilla creará la VPC "192.168.0.0/16", 06 Subnets dentro de este CIDR, un NAT Instances y demás componentes de red. No deberán existir redes existentes en este rango de IPs. Validar la creación del Stack desde la consola AWS a través del servicio AWS CloudFormation. El siguiente comando considera el valor "aws-solutionsarchitectassociate" para el KeyPair, reemplazar el nombre según la llave respectiva.

```bash
aws cloudformation create-stack --stack-name lab15-vpc --template-body file://~/environment/aws-solutionsarchitectassociate/Lab-33/code/1_lab33-vpc.yaml --parameters ParameterKey=KeyPair,ParameterValue="aws-solutionsarchitectassociate" --capabilities CAPABILITY_IAM
```

7. **2_lab33-secret-manager.yaml** (Esperar el despliegue total de esta plantilla cloudformation para continuar con la siguiente plantilla). En la sección "Parameters", ingresar el nombre del KeyPair creado en el paso 1. Esta plantilla creará una instancia EC2. Se estará generando una AMI al final del proceso de creación de la instancia.

```bash
aws cloudformation create-stack --stack-name lab15-ec2 --template-body file://~/environment/aws-solutionsarchitectassociate/Lab-33/code/2_lab33-secret-manager-rds.yaml --parameters ParameterKey=KeyPair,ParameterValue="aws-solutionsarchitectassociate" --capabilities CAPABILITY_IAM
```

8. En el despliegue de recursos a través de CloudFormation se han generado 6 subnets: 2 subnets públicas (a ser usadas por el BALANCEADOR), 2 subnets privadas (donde han sido desplegada un EC2 INSTANCE BACKEND) y otras 2 subnets privadas que actualmente no tiene uso, pero serán destinadas en los siguientes laboratorios para la base de datos.


9. **3_lab15-alb-targetgroup.yaml**. Esta plantilla no tiene parámetros por ingresar. Generará un target group y un balanceador de aplicaciones. Además, la instancia EC2 se asociará al target group en el puerto 80.

```bash
aws cloudformation create-stack --stack-name lab15-alb-targetgroup --template-body file://~/environment/aws-solutionsarchitectassociate/Lab-15/code/3_lab15-alb-targetgroup.yaml
```

10. Con la ejecución de estas tres plantillas, tenemos nuestro laboratorio base construido.

11. Validar que se esté generando la ami AMI_PHP. Esperar a que el status cambie de "Pending" a "Available"

<br>

<img src="images/Lab15_01.jpg">

<br>