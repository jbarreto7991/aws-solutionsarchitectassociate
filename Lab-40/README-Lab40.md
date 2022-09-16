# AWS Solutions Architect Associate - Laboratorio 40

<br>

### Objetivo: 
*  Configuración y gestión a través de los métodos create, send, receive, y delete de una cola SQS usando el SDK de NodeJS 

### Tópico:
* Application Integration

### Dependencias:
* Ninguno

<br>


---

### A - Configuración y gestión a través de los métodos create, send, receive, y delete de una cola SQS usando el SDK de NodeJS 

<br>


1. Acceder al servicio AWS Cloud9 y generar un nuevo (o encender nuestro) ambiente de trabajo (Ubuntu 18.04 LTS)

<br>

2. Ejecutar los siguinentes comandos en nuestro Cloud9

```bash
#Ubuntu 18.04
sudo apt-get update
git clone https://github.com/jbarreto7991/aws-solutionsarchitectassociate.git
```

<br>

3. Acceder al laboratorio 40 (Lab-40), carpeta "code". Validar que se cuenta con la plantilla de cloudformation "1_lab40-sqs".

<br>

4. Desplegar la respectiva plantilla CloudFormation ejecutando AWSCLI.

<br>

5. **1_lab40-sqs** Esta plantilla contiene los siguientes parámetros de despliegue: KeyPair, SubnetID y VPCID. Reemplazar estos valores en la siguiente línea de comando. Será válido usar la consola de AWS para el despliegue de esta plantilla. Esta plantilla aprovisionará una instancia EC2 que contará con un proyecto de SQS.

<br>

```bash
aws cloudformation create-stack --stack-name lab40-sqs --template-body file://~/environment/aws-solutionsarchitectassociate/Lab-40/code/1_lab40-sqs.yaml --parameters ParameterKey=KeyPair,ParameterValue="aws-solutionsarchitectassociate" ParameterKey=Subnet,ParameterValue="subnet-43d4a125" ParameterKey=VPC,ParameterValue="vpc-dd59d8a0" --capabilities CAPABILITY_NAMED_IAM
```

<br>

6. Generar un usuario programático con la política asociada "AmazonSQSFullAccess"
Access key ID: AKIAQ7Y4QB4XMYFMMXSP
Secret access key: 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


3. Configurar el usuario programático en la aplicación. Acceder al archivo config.json y reemplazar las secciones correspondientes.

cd /home/ubuntu/aws-sqs-node-js-example/
nano config.json

{
    "accessKeyId": "AKIAQ7Y4QB4XMYFMMXSP",
    "secretAccessKey": "wL50B8mHrdoZhRKH70QjeJPYHCNu+a5Yfdfd6RSo",
    "region": "us-east-1"
}


4. Ejecutar los siguientes comandos:

cd /home/ubuntu/aws-sqs-node-js-example/
node app.js

#Respuesta
AWS SQS example app listening at http://:::80


5. Desde la IP Pública de la instancia validar el servicio. Se mostrará la siguiente respuesta:
#Respuesta
Cannot GET /


6. Creando mi primera cola SQS
 - Analizar el siguiente archivo "app.js". Validar los diferentes métodos existentes
 - Analizar la sección "/create" del archivo app.js
 - Desde el navegador acceder a PUBLIC_IP/create

#Resultado
{"ResponseMetadata":{"RequestId":"6232757b-f740-5ee4-b827-2cd45a2a98b8"},"QueueUrl":"https://sqs.us-east-1.amazonaws.com/068242378542/MyFirstQueue"}

 
7. Desde el servicio de SQS de AWS, validar la creación del recurso. Desde la sección "Details" guardar el valor del campo "URL".
URL = https://sqs.us-east-1.amazonaws.com/068242378542/MyFirstQueue

#Obteniendo la URL usando AWSCLI
REGION=$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone | sed 's/\(.*\)[a-z]/\1/')
aws sqs list-queues --region $REGION | jq -r '.QueueUrls[]'


8. Desde la instancia EC2, modificar el archivo "app.js". Agregar valor en el campo "queueUrl" (valor obtenido en el paso anterior).

// Require objects.
var express  = require('express');
var app      = express();
var aws      = require('aws-sdk');
var queueUrl = "https://sqs.us-east-1.amazonaws.com/068242378542/MyFirstQueue";
var receipt  = "";


9. Analizar la sección "/send" del archivo app.js


10. Desde el navegador acceder a PUBLIC_IP/send. Analizar el servicio SQS.

#Resultado
{"ResponseMetadata":{"RequestId":"3a7de4d5-361d-52e4-8bf2-bd6521b97d7b"},"MD5OfMessageBody":"86fb269d190d2c85f6e0468ceca42a20","MessageId":"e3dc20ec-7178-4e88-b059-4b00bec25b28"}


11. Analizar la sección "/receive" del archivo app.js


12. Desde el navegador acceder a PUBLIC_IP/receive. Analizar el servicio SQS.

#Resultado
{"ResponseMetadata":{"RequestId":"9f71f403-cdcd-535a-871b-adb3d5b45083"},"Messages":[{"MessageId":"5fa43bc0-ef8e-4848-8ec3-373f544efbc0","ReceiptHandle":"AQEBjtMl+SJ8UgOrAETZPne8ZxPfaKzr1S5CF/iHcY5kgQolk7uV2VGOlMEOsA49PQBgFmvv/A6oYcKPLrTpLsd00K3VTXFjlpJn/fEMCdbCL21tK3yOaXF8sspCQOqZ7cabcYlXGg8x3rqSc/22I2Hc7qSHfcmyAl4QJeZo1kZOwCG5TU0fgQHpi52Iz/fWqS6LPHSVDfZaYYKhIGg0fMgJNSrXxv+T9Zou0o3Hfy4S/VvvRy//7AG3dL2uOYAMDIBDGFLLjwGgYMMcdHt25iJHYgdxilUfWLPH8omJhXOrCq6bO+UZATS9tgBWUQzrX9toNIXb8MSjnsYxd73ko6o8q4L6uxrZ2fZ5XaJm/sUGj0oHGtaAvYfGsoYVS+J0zI/EIlPQpJA8URMZkjlckbqwsg==","MD5OfBody":"86fb269d190d2c85f6e0468ceca42a20","Body":"Hello world!"}]}


13. Analizar la sección "/delete" del archivo app.js. Agregar valor en el campo "receipt" (valor obtenido en el paso anterior).

// Require objects.
var express  = require('express');
var app      = express();
var aws      = require('aws-sdk');
var queueUrl = "https://sqs.us-east-1.amazonaws.com/068242378542/MyFirstQueue";
var receipt  = "";



14. Desde el navegador acceder a PUBLIC_IP/delete. Analizar el servicio SQS. 

#Resultado
{"ResponseMetadata":{"RequestId":"5ccfd7da-79e9-54be-9c33-8e6a60cfa978"}}


15. Desde el navegador acceder a PUBLIC_IP/purge. Analizar el servicio SQS. 
