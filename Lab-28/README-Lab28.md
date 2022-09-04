# AWS Solutions Architect Associate - Laboratorio 28

<br>

### Objetivo: 
* Entendimiento de AWS S3 Presign

### Tópico:
* Storage

### Dependencias:
* Ninguna

<br>


---

### A - Entendimiento de AWS S3 Presign

<br>

1. Creamos un bucket S3 con valores por defecto y agregamos un objeto al bucket. El objeto tendrá por nombre "s3-presign-file.txt" el cual tendrá como contenido la palabra "test"

<br>

<img src="images/lab28_01.jpg">

<br>

2. Accedemos al objeto (dando clic sobre este) y luego damos clic en "Object URL" (sección "Properties"). Al tratar de acceder a la URL nos veremos imposibilitados debido a que tanto el bucket como el objeto son privados y no es posible acceder a estos de forma pública. La pantalla mostrará el mensaje "AccessDenied".

<br>

<img src="images/lab28_02.jpg">

<br>

<img src="images/lab28_03.jpg">

<br>

3. A nivel de Bucket, seleccionamos el objeto, damos clic en la opción "Actions" y luego damos clic en la opción "Share with a presigned URL". Ingresamos el intervalo de tiempo adecuado para que nuestro objeto sea público (por ejemplo 2 minutos, según la imagen) y creamos una URL prefirmarda ("Presigned URL"). 

<br>

<img src="images/lab28_04.jpg">

<br>

<img src="images/lab28_05.jpg">

<br>

4. Copiamos la URL prefirmada y pegamos esta sobre el navegador. Validaremos que a pesar que el bucket y el objeto son privado, podemos acceder de forma pública al contenido del objeto. La URL obtenida será similar a:


https://s3-jorge-barreto-aws-solutionsarchitectassociate.s3.us-east-1.amazonaws.com/s3-presign-file.txt?response-content-disposition=inline&X-Amz-Security-Token=AAAAAAAAAAluX2VjEAUaCXNhLWVhc3QtMSJIMEYCIQDoNkSf2AArxJ9ag5Xap3TsmhlWAr%2FWZT89gC9F3MMIHQIhAPcUrsZpBLnAXCwiV033NV9LmWl3bMKYXb%2BdePXowQzmKvECCI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQARoMMDY4MjQyMzc4NTQyIgz%2Fxdkej0khic%2F%2BaCoqxQI0QkPz8UQtDxm9GZ6TxZoWVj5d8B5F%2FJrLamua%2BiHfZgxNbd0yEc%2Bp9XW%2BukOht%2BBtiE4QX7vGlk5lNKc4CkncIl1uEvoi%2B%2FV7OG7sB%2Bj9gbCag%2F60utOpc7gUhVHFsqPVxiS2Ha%2BupMBssRar46SR0rVWHZCV0GEstc0dUdVmb4OZ0SpuKUrUGcXkZ5Gy7GQyVRuU0tSkKIpCNqGAOhJHmCGqU0m68wxMsSQO4Au6PdQMeobldx13ctHPTSz7FhAt40mRxzeKMOxqZlZ4XX0P%2BQyHu7G8JCCCCCCCCCCz2lJuwh7h27vaXH7Kn%2BN8AgIKxaFMLsCzru%2BFI33rn6ob0jDQQa%2BZWwutlaL3jEPxARiwn1%2FMfCMoL6j8yN1i%2BQIGM3dDwdEeT%2F3V%2B2BGzu3%2FhzTlS%2B8seR3FghCcNMrAqeQAzSqmMK74x5gGOrIC4JqeuE0Uno%2FuMXMdUAvdQHq2lGue%2BroO2nBGic%2BGdrkdejLQhs%2B09aj%2BNgAfoOtRleCJtd6niK4bNBWWCLV6OeKPkp0lrY%2BROa0whBtNsLn7KXs2MQ8%2FVLGQKiwK2kK20hj7QV5MqXvWMgzcI9IgpKBQD4yQncWA%2BISC2EDc%2BuAiZzsmdqf5ULk2o38g0yOv7kdUxDDDDDDDDDDaBDikl7SNBPSHc1fQkmYrU0gQnSO22DXfuxYq%2BNdk4CdsC9xXvdoBuiHCtXO5phGvFsXGjRWg1TTevRu0I%2BJ21B9K%2F5hUsCGr3LeVEcBrxI7waKV8PgeEjloSw0%2B1RBM8peIYf8RmpNzlxHIg8xC5Zu7YPXtTelX5ieu50UvcR085uubr3A%2F3CJZB1P5FbQ44BBBBBBBBBB&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220902T162128Z&X-Amz-SignedHeaders=host&X-Amz-Expires=119&X-Amz-Credential=AAAAAAAAAA4XHF3VAMXZ%BBBBBBBBBB%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=aaaaaaaaaa4df181a2cb179dec960d831335528629170f340e9570bbbbbbbbbb


<br>

<img src="images/lab28_06.jpg">

<br>

<img src="images/lab28_07.jpg">

<br>

5. La URL tendrá la siguiente estructura:

https://s3-jorge-barreto-aws-solutionsarchitectassociate.s3.us-east-1.amazonaws.com/s3-presign-file.txt?
<br>
response-content-disposition=inline
<br>& **X-Amz-Security-Token=** AAAAAAAAAAluX2VjEAUaCXNhLWVhc3QtMSJIMEYCIQDoNkSf2AArxJ9ag5Xap3TsmhlWAr%2FWZT89gC9F3MMIHQIhAPcUrsZpBLnAXCwiV033NV9LmWl3bMKYXb%2BdePXowQzmKvECCI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQARoMMDY4MjQyMzc4NTQyIgz%2Fxdkej0khic%2F%2BaCoqxQI0QkPz8UQtDxm9GZ6TxZoWVj5d8B5F%2FJrLamua%2BiHfZgxNbd0yEc%2Bp9XW%2BukOht%2BBtiE4QX7vGlk5lNKc4CkncIl1uEvoi%2B%2FV7OG7sB%2Bj9gbCag%2F60utOpc7gUhVHFsqPVxiS2Ha%2BupMBssRar46SR0rVWHZCV0GEstc0dUdVmb4OZ0SpuKUrUGcXkZ5Gy7GQyVRuU0tSkKIpCNqGAOhJHmCGqU0m68wxMsSQO4Au6PdQMeobldx13ctHPTSz7FhAt40mRxzeKMOxqZlZ4XX0P%2BQyHu7G8JCCCCCCCCCCz2lJuwh7h27vaXH7Kn%2BN8AgIKxaFMLsCzru%2BFI33rn6ob0jDQQa%2BZWwutlaL3jEPxARiwn1%2FMfCMoL6j8yN1i%2BQIGM3dDwdEeT%2F3V%2B2BGzu3%2FhzTlS%2B8seR3FghCcNMrAqeQAzSqmMK74x5gGOrIC4JqeuE0Uno%2FuMXMdUAvdQHq2lGue%2BroO2nBGic%2BGdrkdejLQhs%2B09aj%2BNgAfoOtRleCJtd6niK4bNBWWCLV6OeKPkp0lrY%2BROa0whBtNsLn7KXs2MQ8%2FVLGQKiwK2kK20hj7QV5MqXvWMgzcI9IgpKBQD4yQncWA%2BISC2EDc%2BuAiZzsmdqf5ULk2o38g0yOv7kdUxDDDDDDDDDDaBDikl7SNBPSHc1fQkmYrU0gQnSO22DXfuxYq%2BNdk4CdsC9xXvdoBuiHCtXO5phGvFsXGjRWg1TTevRu0I%2BJ21B9K%2F5hUsCGr3LeVEcBrxI7waKV8PgeEjloSw0%2B1RBM8peIYf8RmpNzlxHIg8xC5Zu7YPXtTelX5ieu50UvcR085uubr3A%2F3CJZB1P5FbQ44BBBBBBBBBB
<br> & **X-Amz-Algorithm=**
AWS4-HMAC-SHA256
<br> & **X-Amz-Date=**
20220902T162128Z
<br> & **X-Amz-SignedHeaders=**
host
<br> & **X-Amz-Expires=**
119
<br> &  **X-Amz-Credential=** 
AAAAAAAAAA4XHF3VAMXZ%BBBBBBBBBB%2Fus-east-1%2Fs3%2Faws4_request
<br> & **X-Amz-Signature=**
aaaaaaaaaa4df181a2cb179dec960d831335528629170f340e9570bbbbbbbbbb

<br>

6. Luego que haya pasado el tiempo configurado (2 minutos) accedemos nuevamente al objeto a través de la URL. Validaremos que no contamos con acceso.

<br>

7. Será posible realizar estos pasos a través de AWSCLI. Aprovisionamos una instancia de Cloud9 y ejecutamos los siguientes comandos:

```bash
#Guardar el nombre del último bucket creado en una variable
BUCKET_NAME=$(aws s3 ls | sort -r | awk 'NR ==1 { print $3 }')
#Identificar el objeto donde se generará la URL Presigned. Para este laboratorio el objeto será "s3-presign-file.txt"
aws s3 ls s3://$BUCKET_NAME --recursive
#Generar URL Presigned. El valor 120 hace referencia a los 2 minutos (en segundos)
aws s3 presign s3://$BUCKET_NAME/s3-presign-file.tx --expires 120
```

<br>

<img src="images/lab28_08.jpg">

<br>

8. El comando "S3 presign" sólo genera URL GET prefirmadas (descarga de objetos), si se desea cargar archivos en un bucket de S3 usando POST URL prefirmadas o PUT URL prefirmadas, se deberá usar el SDK de AWS.

