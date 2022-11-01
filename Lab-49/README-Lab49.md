# AWS Solutions Architect Associate - Laboratorio 49

<br>

### Objetivo: 
* Integración entre WAF y API Gateway y configuración de ACLs “manual ip block rule” y “sqli rule”

### Tópico:
* Compute
* Security, Identity & Compliance
* Database
* Application Integration

### Dependencias:
* Ninguna

<br>

---

### A - Integración entre WAF y API Gateway y configuración de ACLs “manual ip block rule” y “sqli rule”


<br>

1. Debemos tener una llave Key Pair disponible. De no ser así, acceder al servicio EC2 y luego a la opción "Key Pair". Generar llave RSA y .pem 

2. Acceder al servicio AWS Cloud9 y generar un nuevo ambiente de trabajo (Ubuntu 18.04 LTS)

3. Ejecutar los siguinentes comandos en nuestro Cloud9

```bash
#Ubuntu 18.04
sudo apt-get update
git clone https://github.com/jbarreto7991/aws-solutionsarchitectassociate.git
```

4. Acceder al laboratorio 49 (Lab-49), carpeta "code". Validar que se cuenta con el archivo "1_lab49-waf.json" y la carpeta "SAM". Analizar el contenido de estos archivos.

5. Desplegar la plantilla CloudFormation **1_lab49-waf.json** ejecutando AWSCLI 

```bash
aws cloudformation create-stack --stack-name lab48-vpc --template-body file://~/environment/aws-solutionsarchitectassociate/Lab-48/code/1_lab48-vpc.yaml --parameters ParameterKey=KeyPair,ParameterValue="aws-solutionsarchitectassociate" --capabilities CAPABILITY_IAM
```





---

### Eliminación de recursos

```bash
Cognito - Delete Domain Name
aws cloudformation delete-stack --stack-name lab48-cognito
aws cloudformation delete-stack --stack-name lab48-alb-targetgroup
Eliminar Target Group
aws cloudformation delete-stack --stack-name lab48-ec2
aws cloudformation delete-stack --stack-name lab48-vpc
```