# AWS Solutions Architect Associate - Laboratorio 23

<br>

### Objetivo: 
* Entendimiento de STS (Secure Token Service)

### Tópico:
* Security,Identity & Compliance

### Dependencias:
* Implementación del Laboratorio 22

<br>

---

### A - Entendimiento de STS (Secure Token Service)

<br>

1. Desplegamos la plantilla AWS CloudFormation ubicada en /code/1_lab23-sts-crossaccount.yaml en nuestra cuenta de AWS. Debido a que hemos desplegado varias plantilla en laboratorios anteriores, no se detallará el pasa a paso de este procedimiento.

    * Despliegue manual a través de la consola AWS
    * Despliegue usando AWSCLI en Cloud9
        * En la sección "ParameterValue", seleccionar el valor de "KeyPair"
        * Seleccionar el valor de "Subnet"
        * Seleccionar el valor de "VPC"

```bash

#Ubuntu 18.04
sudo apt-get update
git clone https://github.com/jbarreto7991/aws-solutionsarchitectassociate.git

aws cloudformation create-stack --stack-name lab23-sts-crossaccount --template-body file://~/environment/aws-cloudpractitioner/Lab-23/code/1_lab23-sts-crossaccount.yaml --parameters ParameterKey=KeyPair,ParameterValue="cloud-solutionsarchitect" ParameterKey=Subnet,ParameterValue="subnet-29b70f18"  ParameterKey=VPC,ParameterValue="vpc-dd59d8a0" --capabilities CAPABILITY_IAM
```




2. 





<br>

2. Accedemos al servicio AWS Organizations y damos clic en el botón "Create an organization". 

<br>

<img src="images/Lab22_01.jpg">

<br>


================================
   STS (Secure Token Service)
================================


5. En el origen, crear una instancia EC2:
   - Asociar la política creada en los pasos anteriores. 
   - La instancia deberá contar con la política "AmazonS3FullAccess".
   - La instancia deberá tener instalado awscli: 
     - "sudo apt-get update"
	 - "sudo apt-get install awscli -y"


6. Desde la instancia EC2, ubicada en la cuenta origen, ejecutar el siguiente comando:
aws sts assume-role --role-arn "arn:aws:iam::AWSID-DestinationAccount:role/CrossAccount" --role-session-name CrossAccount


7. Validar el resultado obtenido:
{
    "Credentials": {
        "AccessKeyId": "ASIASFZMA3DECLOXCPAR",
        "SecretAccessKey": "nJ6msnN/TxisM0y/ycIA0moBnPnyIGKxjKw9iWYn",
        "SessionToken": "FwoGZXIvYXdzEAoaDDAg3NCx66w2Oz4n7SKyAag/VaCcbsHoAQxiMX5LgNeY5X0jaWgubAgWz+vG2REq0JYJfBqMC36El/WZ+Qv6fxX6sH6gs/Wf5IHNT8wFzXQV8jHU6X+j7sQ12U6wtAld+GHIJX7w7Js6teMwCmJVWz+l3yGza5hKW99GQLf7sLLpTkgvLjF4LXUoc+DAK2kEsGCeeGWGg3y6pLyVT+GVh55fJuDVRf6rcL34NJ53sewwVORqNQUM4XDLbwPrbxRtWj4o77eUiQYyLQhJq63C1J8/tP/2B3tCGZePYURdfwg20RDVaqm8j2LpWgEotqksK8Xv8s5V4w==",
        "Expiration": "2021-08-24T17:18:55Z"
    },
    "AssumedRoleUser": {
        "AssumedRoleId": "AROASFZMA3DEIBANOGYQ3:CrossAccount10",
        "Arn": "arn:aws:sts::149879314632:assumed-role/CrossAccount10/CrossAccount10"
    }
}


8. Desde la instancia, ejecutar los siguientes comandos:
aws s3 ls


9. Validar que se muestran los buckets resultantes de la cuenta origen.


10. Configurar el archivo "credentials" en la instancia EC2 origen. Se utilizarán los valores obtenidos en la ejecución del comando STS

nano ~/.aws/credentials

[account1]
AWS_ACCESS_KEY_ID=ASIASFZXXXXXCLOXCPAR
AWS_SECRET_ACCESS_KEY=nJ6msnN/TXXXXXXXXXXXXXXXnPnyIGKxjKw9iWYn
AWS_SESSION_TOKEN=FwoGZXIvYXdzEAoaDDAg3NCx66w2Oz4n7SKyAag/VaCcbsHoAQxiMX5LgNeY5X0jaWgubAgWz+vG2REq0JYJfBqMC36El/WZ+Qv6fxX6sH6gs/Wf5IHNT8wFzXQV8jHU6X+j7sXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXyGza5hKW99GQLf7sLLpTkgvLjF4LXUoc+DAK2kEsGCeeGWGg3y6pLyVT+GVh55fJuDVRf6rcL34NJ53sewwVORqNQUM4XDLbwPrbxRtWj4o77eUiQYyLQhJq63C1J8/tP/2B3tCGZePYURdfwg20RDVaqm8j2LpWgEotqksK8Xv8s5V4w==


11. Configurar el archivo "config" en la instancia EC2 origen. Se utilizarán los valores obtenidos en la ejecución del comando STS

nano ~/.aws/config
[account1]


12. Ejecutar los siguientes comandos:

aws s3 ls
aws s3 ls --profile XXXXXXXXXX
