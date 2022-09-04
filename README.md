# AWS Solutions Architect Associate

### **Autor:** Jorge Barreto | AWSx9 & AWS Community Builder | [LinkedIn](https://www.linkedin.com/in/jorgebarretoolivos/)
<br>

**Objetivo:**
Este repositorio tiene por objetivo desarrollar laboratorios complementarios al curso de preparación para la certificación de AWS Solutions Architect Associate.

---

#### **Laboratorio 01: VPC & NAT**  [README-Lab01.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-01/README-Lab01.md)
* Construcción de una VPC usando subnet públicas (ruteando a través de un Internet Gateway) y subnets privadas (ruteando a través de un NAT Instances)
* Configuración de un NAT Instances

#### **Laboratorio 02: EBS & KMS** [README-Lab02.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-02/README-Lab02.md)
* Asociar volumen EBS
* Aumentar tamaño del volumen EBS
* Reconocimiento del servicio KMS (Key Mananagement Service)

#### **Laboratorio 03: EC2, AWSCLI, metadata & S3** [README-Lab03.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-03/README-Lab03.md)
* Instalación y configuración del Backend en la instancia EC2. Uso de AWSCLI y la metadata en la instancia EC2
* Configuración de "Static website hosting" en S3 (Front)
* Instalación y configuración de la base de datos en la instancia EC2.

#### **Laboratorio 04: Security Groups** [README-Lab04.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-04/README-Lab04.md)
* Análisis y configuración de Security Groups

#### **Laboratorio 05: Elastic IP** [README-Lab05.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-05/README-Lab05.md)
* Análisis y configuración de una Elastic IP

#### **Laboratorio 06: System Manager - Session Manager** [README-Lab06.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-06/README-Lab06.md)
* Configuración de System Manager - Session Manager en instancias Linux/Ubuntu
* Eliminación del security group sg_ssh de las instancias EC2
* Eliminación de la instancia PROD BASTION

#### **Laboratorio 07: VPC Flow Logs & Athena** [README-Lab07.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-07/README-Lab07.md)
* Habilitación de los VPC Flow Logs
* Uso de Amazon Athena para la lectura de los VPC Flow Logs

#### **Laboratorio 08: Network ACL** [README-Lab08.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-08/README-Lab08.md)
* Configuración de NACL (Network Access Control List)

#### **Laboratorio 09: VPC Endpoint Gateway & Interface** [README-Lab09.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-09/README-Lab09.md)
* Configuración de VPC Endpoint Gateway
* Configuración de VPC Endpoint Interface

#### **Laboratorio 10: VPC Peering Connection** [README-Lab10.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-10/README-Lab10.md)
* Configuración de Peering Connection

#### **Laboratorio 11: ALB (Application Load Balancer)** [README-Lab11.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-11/README-Lab11.md)
* Despliegue de una balanceador de aplicaciones (Application Load Balancer)

#### **Laboratorio 12: ALB (Application Load Balancer) & Sticky Session** [README-Lab12.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-12/README-Lab12.md)
* Configuración de Sticky Session en el Application Load Balancer (ALB)

#### **Laboratorio 13: ALB (Application Load Balancer) & Listener Rules** [README-Lab13.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-13/README-Lab13.md)
* Configuración del Listener Rules en el Application Load Balancer (ALB)

#### **Laboratorio 14: ALB (Application Load Balancer), Certificate Manager & Route53** [README-Lab14.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-14/README-Lab14.md)
* Creación de un certificado SSL/TLS y su asociación al Application Load Balancer

#### **Laboratorio 15: EC2 AutoScaling Group, Launch Configuration, SNS & CloudWatch Alarm** [README-Lab15.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-15/README-Lab15.md)
* Configuración de "EC2 AutoScaling Group" usando "Launch Configuration", "SNS" y "CloudWatch Alarm"

#### **Laboratorio 16: CloudFront & S3** [README-Lab16.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-16/README-Lab16.md)
* Despliegue de contenido estático en ClodFront
* Configuración de Cache con TTL 0 en CloudFront
* Identificar la configuración OAI (Origin Access Identities) en la distribución CloudFront y el bucket S3

#### **Laboratorio 17: CloudFront, S3 & OAI** [README-Lab17.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-17/README-Lab17.md)
* Despliegue de una distribución CloudFront usando como origen un bucket de S3
* Configurar OAI (Origin Access Identities) en la distribución CloudFront y el bucket S3

#### **Laboratorio 18: CloudFront, Certificate Manager & Route53** [README-Lab18.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-18/README-Lab18.md)
* Despliegue de una distribución CloudFront con dominio personalizado usando Route53 y certificado SSL/TLS con Certificate Manager

#### **Laboratorio 19: Route53 & Routing Policies** [README-Lab19.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-19/README-Lab19.md)
* Configuración del "Routing Policies Latency" en Route 53
* Configuración del "Routing Policies Weighted" en Route 53

#### **Laboratorio 20: IAM User Programmatic, SDK & IAM Roles** [README-Lab20.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-20/README-Lab20.md)
* Creación de un IAM User Programmatic
* Uso del SDK de Python (boto3)
* Uso de IAM roles

#### **Laboratorio 21: IAM & Evaluating permission levels** [README-Lab21.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-21/README-Lab21.md)
* Evaluando niveles de permisos en IAM

#### **Laboratorio 22: AWS Organizations & Switch Role Account** [README-Lab22.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-22/README-Lab22.md)
* Crear una cuenta AWS a través del servicio AWS Organizations
* Hacer "Switch Role" entre cuentas de AWS

#### **Laboratorio 23: IAM Roles & STS** [README-Lab23.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-23/README-Lab23.md)
* Entendimiento de STS (Secure Token Service)

#### **Laboratorio 24: AWS Organizations, OU & SCPs** [README-Lab24.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-24/README-Lab24.md)
* Entendimiento de OU (Organizational Unit) en AWS Organizations
* Entendimiento de SCPs (Service Control Policies) en AWS Organizations

#### **Laboratorio 25: EBS Performance** [README-Lab25.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-25/README-Lab25.md)
* Analizar métricas de performance en volúmenes EBS

#### **Laboratorio 26: EC2 Instances Store** [README-Lab26.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-26/README-Lab26.md)
* Configuración de volúmenes EC2 Instances Store (Volúmenes Efímeros)

#### **Laboratorio 27: CloudFormation - Mappings, Conditions & Parameters** [README-Lab27.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-27/README-Lab27.md)
* Desplegar un stack de CloudFormation multi-región usando "Mappings", "Conditions" y "Parameters"

#### **Laboratorio 28: S3 Presign - GetObject** [README-Lab28.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-28/README-Lab28.md)
* Entendimiento de AWS S3 Presign (GetObject)

#### **Laboratorio 29: S3 CORS** [README-Lab29.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-29/README-Lab29.md)
* Configuración de Cross-origin resource sharing (CORS) en S3 (Permissions)

#### **Laboratorio 30: S3 Glacier & AWSCLI** [README-Lab30.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-30/README-Lab30.md)
* Subir archivos directamente a S3 Glacier usando AWSCLI

#### **Laboratorio 31: S3, Glue, Crawler & Athena** [README-Lab31.md](https://github.com/jbarreto7991/aws-solutionsarchitectassociate/blob/main/Lab-31/README-Lab31.md)
* Integración de S3, Glue, Crawler y Athena










