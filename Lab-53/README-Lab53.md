# AWS Solutions Architect Associate - Laboratorio 53

<br>

### Objetivo: 
* Interactuar con la API de Amazon Polly


### Tópico:
* Machine Learning

### Dependencias:
* Ninguna

<br>

---

### A - Interactuar con la API de Amazon Polly

<br>

1. Acceder al servicio AWS Cloud9 y generar un nuevo ambiente de trabajo (Ubuntu 18.04 LTS). Todo el siguiente laboratorio deberá realizar en la región N. Virginia (us-east-1)

<br>

2. Ejecutar los siguientes comandos:

```bash
#Commands
sudo apt-get update
sudo apt-get install pwgen
sudo apt-get install software-properties-common
sudo apt-add-repository universe
sudo apt-get update
sudo apt-get install python3-pip
pip3 install boto3

git clone https://github.com/jbarreto7991/aws-solutionsarchitectassociate.git

cp ~/environment/aws-solutionsarchitectassociate/Lab-53/code/* .

python3 polly.py

var=$(pwgen 13 1)
BUCKET=aws-architect-solutions-training-$var
aws s3 mb s3:/$BUCKET
BUCKET=$(aws s3 ls | sort -r | awk 'NR ==1 { print $3 }')

#aws s3api create-bucket --bucket $BUCKET --region us-east-1
aws s3 website s3://$BUCKET/ --index-document index.html --error-document error.html

aws s3 cp /tmp/speech.mp3 s3://$BUCKET
aws s3 cp ~/environment/aws-solutionsarchitectassociate/Lab-53/code/index.html s3://$BUCKET
aws s3api put-object-acl --bucket $BUCKET --key speech.mp3 --acl public-read
aws s3api put-object-acl --bucket $BUCKET --key index.html --acl public-read

#ACCESS URL S3
http://aws-architect-solutions-training-$var.s3-website-us-east-1.amazonaws.com/


```