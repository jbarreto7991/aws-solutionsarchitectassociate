# AWS Solutions Architect Associate - Laboratorio 32

<br>

### Objetivo: 
* Configuración de un File System usando EFS en instancias Linux aprovisionadas en distintas VPCs.

### Tópico:
* Storage
* Networking
* Compute

### Dependencias:
* Ninguna

<br>


---

### A - Configuración de un File System usando EFS en instancias Linux aprovisionadas en distintas VPCs.

<br>

1. Acceder al servicio AWS Cloud9 y generar un nuevo (o encender nuestro) ambiente de trabajo (Ubuntu 18.04 LTS)

2. Ejecutar los siguinentes comandos en nuestro Cloud9

```bash
#Ubuntu 18.04
sudo apt-get update
git clone https://github.com/jbarreto7991/aws-solutionsarchitectassociate.git
```

3. Acceder al laboratorio 32 (Lab-32), carpeta "code". Validar que se cuenta con la plantilla de cloudformation "1_lab32-efs-vpc-peeringconnection.yaml".

4. Desplegar la respectiva plantilla CloudFormation ejecutando AWSCLI.

<br>

5. **1_lab32-efs-vpc-peeringconnection.yaml** Esta plantilla contiene los siguientes parámetros de despliegue: . Después del despliegue, se aprovisionarán los siguientes recursos: 02 VPCs, 01 Peering Connection y 03 EC2 Instances. Cada VPC tendrás 04 subnets (entre públicas y privadas), 01 NAT Instances y demás componentes de red.

```bash
aws cloudformation create-stack --stack-name lab31-s3-glue --template-body file://~/environment/aws-solutionsarchitectassociate/Lab-31/code/1_lab31-s3-glue.yaml 
```

<br>
