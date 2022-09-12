# AWS Solutions Architect Associate - Laboratorio 37

<br>

### Objetivo: 
*  Configuración e integración de "Cognito (User Pool)" y una distribución "CloudFront"

### Tópico:
* Database

### Dependencias:
* Ninguno

### Laboratorio base:
* Basado en el siguiente laboratorio: https://identity-round-robin.awssecworkshops.com/serverless/task2/

<br>


---

### A - Configuración e integración de "Cognito (User Pool)" y una distribución "CloudFront"

<br>

1. Acceder al servicio AWS Cloud9 y generar un nuevo (o encender nuestro) ambiente de trabajo (Ubuntu 18.04 LTS)

2. Ejecutar los siguinentes comandos en nuestro Cloud9

```bash
#Ubuntu 18.04
sudo apt-get update
git clone https://github.com/jbarreto7991/aws-solutionsarchitectassociate.git
```

3. Acceder al laboratorio 37 (Lab-37), carpeta "code". Validar que se cuenta con la plantilla de cloudformation "1_lab37_cognito-userpool-cloudfront".

4. Desplegar la respectiva plantilla CloudFormation ejecutando AWSCLI.

<br>

5. **1_lab37_cognito-userpool-cloudfront** Esta plantilla no contiene parámetros de despliegue. Después del despliegue, analizar los recursos aprovisionados: dos buckets S3 (uno para ser usado por el Crawler de Glue y el otro para ser usado por Athena) y el AWS Glue Database "lab31-glue-database".

```bash
aws cloudformation create-stack --stack-name lab37-cognito-userpool-cloudfront --template-body file://~/environment/aws-solutionsarchitectassociate/Lab-37/code/1_lab37-cognito-userpool-cloudfront.yaml --capabilities CAPABILITY_IAM
```

<br>
