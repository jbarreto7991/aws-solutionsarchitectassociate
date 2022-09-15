# AWS Solutions Architect Associate - Laboratorio 39

<br>

### Objetivo: 
*  Configuración de "Event Bridge (Rule with an event pattern)", "GuardDuty" y notificaciones "SNS" para identificación de amenazas en nuestra cuenta de AWS.

### Tópico:
* Management & Governance
* Application Integration
* Security, Identity & Compliance

### Dependencias:
* Ninguno

<br>


---

### A - Configuración de "Event Bridge (Rule with an event pattern)", "GuardDuty" y notificaciones "SNS" para identificación de amenazas en nuestra cuenta de AWS.

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

3. Acceder al laboratorio 39 (Lab-39), carpeta "code". Validar que se cuenta con la plantilla de cloudformation "1_lab39-eventbridge-guardduty-sns".

<br>

4. Desplegar la respectiva plantilla CloudFormation ejecutando AWSCLI.

<br>

5. **1_lab39-eventbridge-guardduty-sns** Esta plantilla contiene los siguientes parámetros de despliegue: KeyPair, SubnetID y VPCID. Reemplazar estos valores en la siguiente línea de comando. Será válido usar la consola de AWS para el despliegue de esta plantilla. Esta plantilla aprovisionará dos instancias EC2: Atacante y victima". La instancia atacante tendrá instalado "nmap". La instancia victima tendrá instalado "apache2".

<br>

```bash
aws cloudformation create-stack --stack-name lab39-eventbridge-guardduty-sns --template-body file://~/environment/aws-solutionsarchitectassociate/Lab-39/code/1_lab39-eventbridge-guardduty-sns.yaml --parameters ParameterKey=KeyPair,ParameterValue="aws-solutionsarchitectassociate" ParameterKey=Subnet,ParameterValue="subnet-43d4a125" ParameterKey=VPC,ParameterValue="vpc-dd59d8a0" --capabilities CAPABILITY_NAMED_IAM
```

<br>

6. 