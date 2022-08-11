# AWS Solutions Architect Associate - Laboratorio 11

<br>

### Objetivo: 
* Despliegue de una balanceador de aplicaciones (Application Load Balancer)

### Tópico:
* Compute

### Dependencias:
* Ninguna

<br>

---

### A - Despliegue de una balanceador de aplicaciones (Application Load Balancer)


<br>

1. Debemos tener una llave Key Pair disponible. De no ser así, acceder al servicio EC2 y luego a la opción "Key Pair". Generar llave RSA y .pem 

2. Acceder al servicio AWS Cloud9 y generar un nuevo ambiente de trabajo (Ubuntu 18.04 LTS)

3. Ejecutar los siguinentes comandos en nuestro Cloud9

```bash
#Ubuntu 18.04
sudo apt-get update
git clone https://github.com/jbarreto7991/aws-solutionsarchitectassociate.git
```

4. Acceder al laboratorio 11 (Lab-11), carpeta "code". Validar que se cuenta con dos archivos CloudFormation: "1_lab11-vpc.yaml" y "2_lab11-ec2.yaml"  Analizar el contenido de estos archivos.

5. Desplegar cada plantilla CloudFormation ejecutando AWSCLI. Considerar los parámetros a ser ingresados.

    <br>
10. **1_lab11-vpc.yaml** (Esperar el despliegue total de esta plantilla cloudformation para continuar con la siguiente plantilla). En la sección "ParameterValue", ingresar el nombre del KeyPair creado en el paso 1. Esta plantilla creará la VPC "192.168.0.0/16" y 06 Subnets dentro de este CIDR. No deberán existir redes existentes en este rango de IPs. Validar la creación del Stack desde la consola AWS a través del servicio AWS CloudFormation. El siguiente comando considera el valor "
aws-solutionsarchitectassociate" para el KeyPair, reemplazar el nombre según la llave respectiva.

```bash
aws cloudformation create-stack --stack-name lab11-vpc --template-body file://~/environment/aws-solutionsarchitectassociate/Lab-11/code/1_lab11-vpc.yaml --parameters ParameterKey=KeyPair,ParameterValue="
aws-solutionsarchitectassociate" --capabilities CAPABILITY_IAM
```
    
<img src="images/lab06_08.jpg">
<br>

<img src="images/lab06_09.jpg">
<br>
