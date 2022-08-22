# AWS Solutions Architect Associate - Laboratorio 20

<br>

### Objetivo: 
* Creación de un IAM User Programmatic
* Uso del SDK de Python (boto3)
* Uso de IAM roles

### Tópico:
* Security,Identity & Compliance

### Dependencias:
* Ninguna

<br>

---

### A - Creación de un IAM User Programmatic

<br>

1. Hacer uso de nuestra Key Pair. De no ser así, acceder al servicio EC2 y luego a la opción "Key Pair" de cada región indicada. Generar llave RSA y .pem.

2. Acceder al servicio AWS Cloud9 y generar un nuevo ambiente de trabajo (Ubuntu 18.04 LTS)

3. Ejecutar los siguientes comandos en nuestro Cloud9

```bash
#Ubuntu 18.04
sudo apt-get update
git clone https://github.com/jbarreto7991/aws-solutionsarchitectassociate.git
```

4. **1_lab20-vpc-ec2-iam.yaml**. En la sección "ParameterValue", reemplazar el nombre del KeyPair creado en el paso 1. Esta plantilla creará una VPC, 02 subnets públicas y demás componentes de red; además de una instancia EC2. Esta instancia instalará python3, pip3 y awscliv2; además descargará código python del repositorio en /home/ubuntu. Validar la creación del Stack desde la consola AWS a través del servicio AWS CloudFormation. El siguiente comando considerar reemplazar el valor del Key Pair con el valor respectivo.

```bash
aws cloudformation create-stack --stack-name lab20-vpc-ec2-iam --template-body file://~/environment/aws-solutionsarchitectassociate/Lab-20/code/1_lab20-vpc-ec2-iam.yaml --parameters ParameterKey=KeyPair,ParameterValue="aws-solutionsarchitectassociate" --capabilities CAPABILITY_IAM --region us-east-1

```

5. Accedemos al servicio IAM y generamos un IAM User Programmatic a través de la siguiente configuración. En el paso final damos clic en "Create User". Luego, copiar los valores "Access key ID" y "Secret access key."

    * Username: User01
    * Select AWS credential type: Access key - Programmatic access
    * Set Permissions: Attach existing policies directly
    * Search: AmazonS3FullAccess


<br>

<img src="images/Lab20_01.jpg">

<br>

<img src="images/Lab20_02.jpg">

<br>

<img src="images/Lab20_03.jpg">

<br>

<img src="images/Lab20_04.jpg">

<br>

<img src="images/Lab20_05.jpg">

<br>

<img src="images/Lab20_06.jpg">

<br>

6. Desde Cloud9, generamos un bucket S3 usando AWSCLI. Reemplazamos las variables $nombre y $apellido con nuestros datos personales.

```bash
aws s3api create-bucket --bucket $nombre-$apellido-aws-solutionsarchitectassociate --region us-east-1
```
<br>

### B - Uso del SDK de Python (boto3)

<br>

7. Accedemos por SSH a la instancia EC2 y editamos las variables "$aws_access_key_id" y "$aws_Secret_access_key" del archivo 2_sdk_python_s3_with_accesskey.py ubicado en /home/ubuntu. Guardamos los cambios y ejecutamos el archivo en mención usando python3. Validamos que el script lista todos los buckets S3 de nuestra cuenta AWS.

```bash
#Conexión a la instancia EC2
ssh -i keypair_name.pem ubuntu@public_ip

#Ejecucción de archivo python
python3 2_sdk_python_s3_with_accesskey.py
```
<br>

<img src="images/Lab20_07.jpg">

<br>

8. Usando python3 ejecutaremos el archivo "3_sdk_python_s3_without_accesskey.py". Tendremos error al ejecutar el archivo.

```bash
#Ejecucción de archivo python
python3 2_sdk_python_s3_with_accesskey.py
```

<br>

### C - Uso de IAM roles

<br>

9. Accedemos al servicio IAM, ingresamos a la opción "Roles" y damos clic en el botón "Create Role". Seleccionamos/ingresamos los siguientes valores, luego damos clic en el botón "Create role"

    * Trusted entity type: AWS Service
    * Use case: EC2
    * Permissions policies: AmazonS3FullAccess
    * Role name: ec2_role_lab20

<br>

<img src="images/Lab20_08.jpg">

<br>

<img src="images/Lab20_09.jpg">

<br>

<img src="images/Lab20_10.jpg">

<br>

<img src="images/Lab20_11.jpg">

<br>

10. Accedemos al servicio EC2, seleccionamos la instancia EC2 "IAM Challenge" y agregamos el role "ec2_role_lab20" previamente creado.

<br>

<img src="images/Lab20_12.jpg">

<br>

<img src="images/Lab20_13.jpg">

<br>

11. Usando python3 ejecutaremos el archivo "3_sdk_python_s3_without_accesskey.py" nuevamente. En esta ocasión validamos que nos devuelve como resultado la lista de buckets S3.

```bash
#Ejecucción de archivo python
python3 2_sdk_python_s3_with_accesskey.py
```


---

### Eliminación de recursos

<br>

```bash
aws cloudformation delete-stack --stack-name lab20-vpc-ec2-iam --region us-east-1
```