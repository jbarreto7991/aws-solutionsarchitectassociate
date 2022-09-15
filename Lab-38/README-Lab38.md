# AWS Solutions Architect Associate - Laboratorio 38

<br>

### Objetivo: 
*  Configuración de "CloudWatch Event Rules (Schedule)" y el apagado/encendido automático de instancias EC2 usando Lambdas y Tags

### Tópico:
* Management & Governance
* Compute

### Dependencias:
* Ninguno

<br>


---

### A - Configuración de "CloudWatch Event Rules (Schedule)" y el apagado/encendido automático de instancias EC2 con Tags usando Lambdas

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

3. Acceder al laboratorio 38 (Lab-38), carpeta "code". Validar que se cuenta con la plantilla de cloudformation "1_lab38-ec2-tags".

<br>

4. Desplegar la respectiva plantilla CloudFormation ejecutando AWSCLI.

<br>

5. **1_lab38-ec2-tags** Esta plantilla contiene los siguientes parámetros de despliegue: KeyPair, SubnetID y VPCID. Reemplazar estos valores en la siguiente línea de comando. Será válido usar la consola de AWS para el despliegue de esta plantilla. Esta plantilla aprovisionará una instancia EC2 con las aplicaciones "apache2" y el "Agente Unificado Cloudwatch" (agente instalado desde "System Manager - Parameter Store")

```bash
aws cloudformation create-stack --stack-name lab38-ec2-tags --template-body file://~/environment/aws-solutionsarchitectassociate/Lab-38/code/1_lab38-ec2-tags.yaml --parameters ParameterKey=KeyPair,ParameterValue="aws-solutionsarchitectassociate" ParameterKey=Subnet,ParameterValue="subnet-43d4a125" ParameterKey=Vpc,ParameterValue="vpc-dd59d8a0" --capabilities CAPABILITY_NAMED_IAM
```

<br>

6. Ingresar al servicio "System Manager - Run Command", dar clic en el botón "Run Command". Buscar la opción "AWS-RunShellScript" y seleccionarla. 

<br>

<img src="images/Lab37_05.jpg">

<br>




===================================
               Lambda
===================================


1. Generar la siguiente política. Asociar la siguiente política al servicio Lambda a través de un rol.

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:Start*",
        "ec2:Stop*",
        "ec2:DescribeInstances"
      ],
      "Resource": "*"
    }
  ]
}


2. Crear una función Lambda
 - Function Name: ec2_stopstart
 - Runtime: Python 3.9
 - Permissions: Use an existing role (Seleccionar el rol generado anteriormente)


import boto3
import time
from datetime import timedelta
from datetime import datetime
from datetime import date, timedelta

#define boto3 the connection
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    
	# Get current time in format H:M

    current_time = datetime.now()
    utc = current_time - timedelta(hours=5)
    current_time_utc=utc.strftime("%H:%M")
    print (current_time_utc)

	# Find all the instances that are tagged with Scheduled:True
    filters = [{
            'Name': 'tag:Scheduled',
            'Values': ['True']
        }
    ]

	# Search all the instances which contains scheduled filter 
    instances = ec2.instances.filter(Filters=filters)

    stopInstances = []   
    startInstances = []   

	# Locate all instances that are tagged to start or stop.
    for instance in instances:
        
        for tag in instance.tags:
            if tag['Key'] == 'ScheduleStop':
                if tag['Value'] == current_time_utc:
                    stopInstances.append(instance.id)
                    pass
                pass
            if tag['Key'] == 'ScheduleStart':
                if tag['Value'] == current_time_utc:
                    startInstances.append(instance.id)
                    pass
                pass
            pass
        pass
    
    print (current_time_utc)
    
    # shut down all instances tagged to stop. 
    if len(stopInstances) > 0:
        # perform the shutdown
        stop = ec2.instances.filter(InstanceIds=stopInstances).stop()
        print (stop)
    else:
        print ("No instances to shutdown")

    # start instances tagged to stop. 
    if len(startInstances) > 0:
        # perform the start
        start = ec2.instances.filter(InstanceIds=startInstances).start()
        print (start)
    else:
        print ("No instances to start")



3. Agregar los siguientes tag a la instancia "EC2 CloudWatch". Considerar las horas en formato de 24 horas.

     Key       | Value
-------------------------
Scheduled      | True
ScheduleStart  | HH:MM
ScheduleStop   | HH:MM


4. Ejecutar manualmente la función Lambda. Validar el encendido y apagado de la instancia según hora de ejecución.


5. Acceder al servicio CloudWatch Events > Rules. Create Rules. Considerar las siguientes configuracions. Luego crear la regla en estado habilitado.

Event Sources 
 - Event Source: Schedule
 - Fixe rate of: 1 Minute
Targets
 - Lambda function


6. Validar el encendido y apagado de la instancia según hora de ejecución de CloudWatch Event Rules. Revisar los logs en CloudWatch Logs - Log groups.






