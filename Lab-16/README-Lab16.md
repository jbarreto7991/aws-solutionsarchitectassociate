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

3. Acceder al laboratorio 16 (Lab-16), carpeta "code". Validar que se cuenta con un archivo CloudFormation: "1_lab16-cloudfront-s3.yaml" y un folder de nombre "2_lab16-s3-htmlresources". Analizar el contenido de estos elementos.

5. Desplegar la plantilla CloudFormation ejecutando AWSCLI.

    <br>
6. **1_lab16-cloudfront-s3.yaml** Esta plantilla no contiene parámetros de despliegue. 

```bash
aws cloudformation create-stack --stack-name lab16-cloudfront-s3 --template-body file://~/environment/aws-solutionsarchitectassociate/Lab-16/code/1_lab16-cloudfront-s3.yaml 
```


### Eliminación de recursos

```bash
aws cloudformation delete-stack --stack-name lab15-alb-targetgroup
aws cloudformation delete-stack --stack-name lab15-ec2
aws cloudformation delete-stack --stack-name lab15-vpc
```