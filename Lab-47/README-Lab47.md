# AWS Solutions Architect Associate - Laboratorio 47

<br>

### Objetivo: 
* Obtención de credenciales temporales STS consumiendo el servicio de Cognito Identity Pool usando AWSCLI

### Tópico:
* Security, Identity & Compliance

### Dependencias:
* Ninguna

<br>

---

### A - Obtención de credenciales temporales STS consumiendo el servicio de Cognito Identity Pool usando AWSCLI

<br>

1. Debemos tener una llave Key Pair disponible. De no ser así, acceder al servicio EC2 y luego a la opción "Key Pair". Generar llave RSA y .pem 

2. Acceder al servicio AWS Cloud9 y generar un nuevo ambiente de trabajo (Ubuntu 18.04 LTS)

3. Ejecutar los siguinentes comandos en nuestro Cloud9

```bash
#Ubuntu 18.04
sudo apt-get update
git clone https://github.com/jbarreto7991/aws-solutionsarchitectassociate.git
```

4. Acceder al laboratorio 47 (Lab-47), carpeta "code". Validar que se cuenta con el archivo "1_lab47-cognito-identitypool.yaml". Analizar el contenido de este archivo

5. Desplegar la plantilla CloudFormation ejecutando AWSCLI. Considerar los parámetros a ser ingresados.

6. **1_lab47-cognito-identitypool.yaml**. Esta plantilla tiene por objetivo el despliegue de un recurso "Cognito User Pool" y de un recurso "Cognito Identity Pool". Esta y la siguiente plantilla podrán ser lanzadas en paralelo.

```bash
aws cloudformation create-stack --stack-name lab47-cognito-identitypool --template-body file://~/environment/aws-solutionsarchitectassociate/Lab-47/code/1_lab47-cognito-identitypool.yaml --capabilities CAPABILITY_IAM
```

7. **2_lab47-ec2-cognito.yaml**. Esta plantilla tiene por objetivo el despliegue de un recurso "Cognito User Pool" y de un recurso "Cognito Identity Pool". Esta y la siguiente plantilla podrán ser lanzadas en paralelo.

```bash
aws cloudformation create-stack --stack-name lab47-ec2-cognito --template-body file://~/environment/aws-solutionsarchitectassociate/Lab-47/code/2_lab47-ec2-cognito.yaml --capabilities CAPABILITY_IAM
```

8. Terminado el aprovisionamiento de los recursos, validar en el servicio Cognito la creación de un recurso "Cognito User Pool" y de un recurso "Cognito Identity Pool". Revisar las configuraciones desplegadas. 

<br>

9. Desde Cloud9, ejecutamos los siguientes comandos. 

<br>

<img src="images/Lab47_01.jpg">

<br>



1. Lanzar una instancia EC2:
   - Asignar el siguiente permiso: "AmazonCognitoPowerUser"
   - Instalación AWSCLI: "sudo apt-get install awscli -y"
   - Instalación unzip: "sudo apt-get install unzip"
   - Instalación de JSON: "sudo apt-get install jq -y"


2. Instalar awscli v2:
cd /home/ubuntu/environment
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
cd /home/ubuntu/environment/aws/
./install


3. Validar la instalación de awscli v2.
aws --version
aws-cli/2.2.32 Python/3.8.8 Linux/5.4.0-1045-aws exe/x86_64.ubuntu.18 prompt/off
[Si no se visualiza el upgrade en la versión del awscli, reiniciar la instancia EC2]


4. Identificación de Cognito User Pool ID
USERPOOL_ID=$(aws cognito-idp list-user-pools --max-results 20 | jq -r '.UserPools[] | .Id')
echo $USERPOOL_ID

{
    "UserPools": [
        {
            "Id": "us-east-1_g9DbK7YTL",
            "Name": "Pool-04sal81eq9qG",
            "LambdaConfig": {},
            "LastModifiedDate": "2021-08-25T01:29:13.853000+00:00",
            "CreationDate": "2021-08-25T01:29:13.853000+00:00"
        }
    ]
}


5. Creación del usuario "thomas" con contraseña "12345678-Aa". Se visualiza el siguiente resultado. 

aws cognito-idp admin-create-user --user-pool-id  $USERPOOL_ID --username thomas --temporary-password "12345678-Aa" --region us-east-1

{
    "User": {
        "Username": "thomas",
        "Attributes": [
            {
                "Name": "sub",
                "Value": "5fe4b732-bca0-41ae-a154-fceb9bae2488"
            }
        ],
        "UserCreateDate": "2021-08-25T02:27:53.665000+00:00",
        "UserLastModifiedDate": "2021-08-25T02:27:53.665000+00:00",
        "Enabled": true,
        "UserStatus": "FORCE_CHANGE_PASSWORD"
    }
}


6. Desde la consola de Cognito User Pool, ir a la sección "General settings - Users and groups". Se visualiza que el usuario tiene  por estado "FORCE_CHANGE_PASSWORD"

USERPOOL_CLIENTID=$(aws cognito-idp list-user-pool-clients --user-pool-id $USERPOOL_ID | jq -r '.UserPoolClients[] | .ClientId')
echo $USERPOOL_CLIENTID

{
    "UserPoolClients": [
        {
            "ClientId": "2csej03oulmbk60is6fcmv968l",
            "UserPoolId": "us-east-1_g9DbK7YTL",
            "ClientName": "PoolClient-VxrCDGs5oA0a"
        }
    ]
}


7. Loguear el usuario "thomas" de contraseña "12345678-Aa"

aws cognito-idp initiate-auth --auth-flow USER_PASSWORD_AUTH --client-id $USERPOOL_CLIENTID --auth-parameters USERNAME=thomas,PASSWORD="12345678-Aa" --region us-east-1

{
    "ChallengeName": "NEW_PASSWORD_REQUIRED",
    "Session": "AYABeFU7S7vncUSuglW2UEjOppAAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHiAcAt7Ei832QLLvv5tnR-fAKEzaf-OMDg-j1aLh6qMVAHBykCelPwX2BlZNuk6xNlqAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQM8v22XML6RPMToQiAAgEQgDvuc1iYlLsxFYSxXiBQVGpNAq2ppvK-xwrKuCUhCwS8bOzOwxNeFOpG0_IMQ0J2zFdyvay0Ypz-fytFXwIAAAAADAAAEAAAAAAAAAAAAAAAAABqF9VDIzOmqPrvHLndK0nW_____wAAAAEAAAAAAAAAAAAAAAEAAAC2zNQlVdeWFsn3SYWNpmrchQmqNN6eTNDPL3ryJKgyYyGfRmO2qcMZacuA4tOORuczNf5rvQo0R_f4P25RaJbEH-t_c4lXnD_TFzVX3-zMMIQLQWTUhIUpkOK_kOrg24agEbZ5RaNnEn9Fs1JF6GRaDFN_MLQxfeNmm7ytEf4hZMLa9jU8SZbCtefdTp_bN-MBTYEJTPbpD5Ch_TpZXxsHHFq0c0BI7WSzEvt2sSyfFu0VU6DXRwWRkFnZjbGA9csc57Kytr1C",
    "ChallengeParameters": {
        "USER_ID_FOR_SRP": "thomas",
        "requiredAttributes": "[]",
        "userAttributes": "{}"
    }
}


8. Cambiar la contraseña del usuario "thomas" por "12345678-Bb"

SESSION=$(aws cognito-idp initiate-auth --auth-flow USER_PASSWORD_AUTH --client-id $USERPOOL_CLIENTID --auth-parameters USERNAME=thomas,PASSWORD="12345678-Aa" --region us-east-1 | jq -r '.Session')
echo $SESSION

aws cognito-idp respond-to-auth-challenge --client-id $USERPOOL_CLIENTID --challenge-name NEW_PASSWORD_REQUIRED --session $SESSION --challenge-responses USERNAME=thomas,NEW_PASSWORD="12345678-Bb" --region us-east-1

{
    "ChallengeParameters": {},
    "AuthenticationResult": {
        "AccessToken": "eyJraWQiOiJcL2RSK2FBdStBTE82UTZtMlFwMmVQejJlR3BtUHlUTmpYNUNIT0p4a1pqMD0iLCJhbGciOiJSUzI1NiJ9.eyJvcmlnaW5fanRpIjoiMjdhMTdiZmUtZDUwNi00ZmU2LWFlYTYtNTk5MjVkNjIwZTM0Iiwic3ViIjoiNWZlNGI3MzItYmNhMC00MWFlLWExNTQtZmNlYjliYWUyNDg4IiwiZXZlbnRfaWQiOiI5YzBhZWI0NS1jZDNlLTRjOTYtOTY1OS05ODRkNGUwZGNjYWEiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwiYXV0aF90aW1lIjoxNjI5ODU5MTYyLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9nOURiSzdZVEwiLCJleHAiOjE2Mjk4NjI3NjIsImlhdCI6MTYyOTg1OTE2MiwianRpIjoiNTc0YjA4MWMtMDgyYS00N2U4LWE2ZTEtNGI1YTFlODdmYTFmIiwiY2xpZW50X2lkIjoiMmNzZWowM291bG1iazYwaXM2ZmNtdjk2OGwiLCJ1c2VybmFtZSI6InRob21hcyJ9.HjJoastEEE5IkALFt9v0qBh5KT1kfPBCmyX6wGTDDHZ8FopdP4mlRSJA6X_1crxh64sajTBttaLb1c1vLjLY5ZbaIVGVkA1yKb5iAH1y1JBXNRPWdmxDn7Lg24rvZe7J5QQxd-MZwAyFYtp93cdiNE8UWuGywg4VKwp9ceavyTvOen6FqBXLFMG8bkl8BqDCNyet1PDPPIkirZ6wicBe9UMkEfHH2YwN6EWDgEjH-e_q0Q-VeRuGlj0l1Wh8nb-rZX8-6ArT1fk6-gFoF73-Hg3k-5rQKzht-tw42pwc8-PgoiIGER2_HUfwylpnIb_qGZZXumT-qfWCUMLUiCIAbQ",
        "ExpiresIn": 3600,
        "TokenType": "Bearer",
        "RefreshToken": "eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.sK49bAP0YPyyLwep7vEiVWR_WvIR0so41B4tRTYLuP0VvBQnIIXC1qcHdOZZ9fbttipDqhNNw_bkfTkw9rriAHiIL744Uvzk7gUcRS1lG52_yJpUlK9Lo2_JnErTc2NERn8r5mFA6_1zKu_dySDyn81VhpmgM3nwQ4MEgLwNAolUsVxw2FJ99QXg9i9pLREGR5VCSWorlYyncg7kWbVNDVtxKp4h672jD07E4z_ekVg-0doVo_2v6hl9RIyJF6lG4KPfMNEBm9Yk0YTheUad5oxI3chZQyjhQ4xMXNcrN0lscZQzcDV0ODIctlGvbSoKa07iSOJBuML7JgUc50rtog.GeyNcoW4A_Qx3hKh.A8jGOwhFwsIGczQYYvRUwCURNjhZC4uSAt-FabrvZ7CrUiZMh8eB1Ez58bCagxfiqleK_JKhCLgrQmuDzp4vz2rHruYP6bv8Ki8njC6i4bpSJMjj9ylGpHz60jiFYbqFzeK2usBDdkEslwun3TOUvmov2pa7AiM_i_MdBAUkNtXk5uFkC10wuYrWVOghILLN-ia7hItwdPBuC-ppmj9_aIV6Z-cvY3qWjW-7_SvlUMf61Zk1Tmag9XYQLa15DhyfXUshqd7Dk54OZnrZefjxq2FbdtIDw8fcuUJQM8M03dFSjwyMBikc_fTuoYuDBjHnHgAXKGDlGdyFv7QMAn-QvDyEvL2LR2HlOZWn_Vjt6jwnN75_z1okk53Fdzi20SDE34xjBsadk0yEkOvJv1Gtv7j1Q3Loixwb8-TaMBXmG2OWUnmGl5WujgPeiyfG-7xWqEkjKSTqD4HdWj2HcOaBkY0uCb_fwvKML4ZDRqHREbR9cRQbr083xWMk67QiyasdwpzLNL1rUZZUjGN16WGSmjkZwCLv3-hHbGMVcLpyNakYYR8DEAI82E3CuFt72ZQsX1fjZ_pXKroCZnp5uIM1BBKZpPBWdrL4al5MzSBP6iYQHCSeSRd066s3f2qtIa4LqPiM7tbe8K33nolVrf107j8AqkQye-dFsForriSXV-Uk7Kd8aB7rMJjYQ-Pp4PN6WuOprwI5nbf5N7hmFfFG7xGDCG0DheL-MBhz1DBtaPUewLCFUHHQKhdqFsPGlEvrBZOcaxUFkUxUVKWGYJnj7rr-u_nJuL_rIAIz4JHtWIgxHbr831jEi2Frqibdduiw1q6pn4WiEe4h4HYE7Mm_SvOZsTDx8fI-Yvg3NGolyX0-Ad7aC2B3mPXJ5ppeJTz8nNmgGiE2EAkjFayLTdCUm4sXTClOXi_4L5VB55lhbcQlqVG-oTPAVE1yHZX_tipYNKcDaDgsOSIkW2MUfingP-gMXTV5s2Op7fKZja7ASdmjVJfXgETOAiQsAL9bTpn7R2xb9AWQYdgez-MRsULue6gK1S8pfzTcCGgCXhfm1vO2VzVDO3P5tE_14avJB3j3zlA1AXv7IJAojgyeiKajA0k0RAJGAYzJ-xn6Jr_G4TngS8vuR4a5f2dsDnTpXjqQ3c10nqIL4Ny2cq_AidwMONkcynvXi1OL-sOfbYZmXwuSvXJDp8RSt01y4G8qT-cvHOcB3zxzBICRk3LtbDMenq-u0YGnDq5l7pPRJbYMI7Z0fwRnSynicFVNZrIPOTSpoF-AeA.9fIS0cx9JBW-hSQZxTv0zg",
        "IdToken": "eyJraWQiOiJGU3dCK1wvSFFiUXZHQTVoWkZuMjBVMHI5b0s5Vmx4cENuckpXaTdxZ1RtMD0iLCJhbGciOiJSUzI1NiJ9.eyJvcmlnaW5fanRpIjoiMjdhMTdiZmUtZDUwNi00ZmU2LWFlYTYtNTk5MjVkNjIwZTM0Iiwic3ViIjoiNWZlNGI3MzItYmNhMC00MWFlLWExNTQtZmNlYjliYWUyNDg4IiwiYXVkIjoiMmNzZWowM291bG1iazYwaXM2ZmNtdjk2OGwiLCJldmVudF9pZCI6IjljMGFlYjQ1LWNkM2UtNGM5Ni05NjU5LTk4NGQ0ZTBkY2NhYSIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjI5ODU5MTYyLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9nOURiSzdZVEwiLCJjb2duaXRvOnVzZXJuYW1lIjoidGhvbWFzIiwiZXhwIjoxNjI5ODYyNzYyLCJpYXQiOjE2Mjk4NTkxNjIsImp0aSI6IjA5MzI0ZTUzLThjMTAtNDQzNC1hZDkwLTBjMTY3YTVlODE4MyJ9.4Ks_bglmvidUzQzuiGNv7t0hsOxFKOliec8iDyTIDtjIY4caq2Kkj9KxCA6J0g6oTq_43JvKpaTlc_AmviMseDav_BxdJ1ZHCyse9BmMwbe17d5sy9w6FQx2yWssBUDkdBoaVYG43BS0-0mpr9IO5vVj_g1Ld6-Rl_8KNTFqmuN_7rv6IicZf-y6S2N9EW18j9uB7CL0mBvFMHH0liBa1dv-n0QsEbn21Z1PxtdJ6gsbgLTI6vkDgBMPPQNbZPFi1r227KYQklkR_H7_quRrJ3WB_8VNsL5ANKY4K-a2RF-h1iwgfShR9V-GDZibr4GQXd-SEUxaD-JbQELQl8CIeA"
    }
}


9. Loguear al usuario "thomas" con la nueva contraseña. Almacenar en variable el campo "IdToken"

aws cognito-idp initiate-auth --auth-flow USER_PASSWORD_AUTH --client-id $USERPOOL_CLIENTID --auth-parameters USERNAME=thomas,PASSWORD="12345678-Bb" --region us-east-1

:::::::::::::::::::::::::::::::::::::
Obtener el campo IdToken manualmente
:::::::::::::::::::::::::::::::::::::

USERPOOL_IDTOKEN="eyJraWQiOiJGU3dCK1wvSFFiUXZHQTVoWkZuMjBVMHI5b0s5Vmx4cENuckpXaTdxZ1RtMD0iLCJhbGciOiJSUzI1NiJ9.eyJvcmlnaW5fanRpIjoiYTdkMzMwOGYtNzJlZS00NmZlLWEyMDItNmFlZDQ3MzIxMmMzIiwic3ViIjoiNWZlNGI3MzItYmNhMC00MWFlLWExNTQtZmNlYjliYWUyNDg4IiwiYXVkIjoiMmNzZWowM291bG1iazYwaXM2ZmNtdjk2OGwiLCJldmVudF9pZCI6ImEwODA0ZGIxLWEzNmQtNGIxNy04Zjg4LWFjOWFmYTQyZTZmZiIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjI5ODYwMTIxLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9nOURiSzdZVEwiLCJjb2duaXRvOnVzZXJuYW1lIjoidGhvbWFzIiwiZXhwIjoxNjI5ODYzNzIxLCJpYXQiOjE2Mjk4NjAxMjEsImp0aSI6ImUxMmY3ZWZlLTk3MzEtNGE4NS1hNzIzLWVjYmE3NzkxMDljOCJ9.12wZj7hn5sGzwfHiq2bBbQqntFnHLkwrmDNxqCVg0-ON4_Wk0UE-f3IHbRmAi0VvL-nvchxq2sR5NWKOq3njt0M45jKxEvW6Rj4lrRBMn5Fl9Q5GgK-N0X5Dd1IU8yJcrXcGeSj5oNfmW0uvvd_ZuBm2XkfcXfd81EnLyP1aReMO2KP6vBsD-hxgMWm4khywIvZYBSDMvdr0tFX-Pz-ayLSNIRzI8Vp5I7h2WODupx1USrKCn-OY-Cd6UNYVESKZnumeMYq-HY03AR8xywW8xryu4uZkSontTc6xg5ulfKqBfOF-APl_QxtfEptJOxVY8cJIIOqTriiQ20W-hr2JYQ"

echo $USERPOOL_IDTOKEN


10. Obtener el valor del campo "IdentityId"

IDENTITYPOOL_ID=$(aws cognito-identity list-identity-pools --max-results 10 | jq -r '.IdentityPools[] | .IdentityPoolId')
echo $IDENTITYPOOL_ID
{
    "IdentityPools": [
        {
            "IdentityPoolId": "us-east-1:b3a32e36-af28-4799-a74d-f92787c84f0f",
            "IdentityPoolName": "IdPool_UrTb6Kosst6l"
        }
    ]
}


aws cognito-identity get-id --identity-pool-id $IDENTITYPOOL_ID --logins cognito-idp.us-east-1.amazonaws.com/$USERPOOL_ID=$USERPOOL_IDTOKEN --region us-east-1

{
    "IdentityId": "us-east-1:41a5a5dc-8899-410b-ac28-75d3680434cf"
}


11. Obtener credenciales desde STS

IDENTITYPOOL_IDENTITYID=$(aws cognito-identity get-id --identity-pool-id $IDENTITYPOOL_ID --logins cognito-idp.us-east-1.amazonaws.com/$USERPOOL_ID=$USERPOOL_IDTOKEN --region us-east-1 | jq -r '.IdentityId')
echo $IDENTITYPOOL_IDENTITYID

aws cognito-identity get-credentials-for-identity --identity-id $IDENTITYPOOL_IDENTITYID --logins cognito-idp.us-east-1.amazonaws.com/$USERPOOL_ID=$USERPOOL_IDTOKEN

{
    "IdentityId": "us-east-1:41a5a5dc-8899-410b-ac28-75d3680434cf",
    "Credentials": {
        "AccessKeyId": "ASIAQ7Y4QB4XHQACLMOS",
        "SecretKey": "gE3PMdFOUwa0Kr13YDPqiB09XnOhiBU01gyElH36",
        "SessionToken": "IQoJb3JpZ2luX2VjEAQaCXVzLWVhc3QtMSJHMEUCIQCxSkr0ANrfbHoNyv6hrQiFjTjh/7d3IJMKYcXjh1V+aQIgaa+S5gi4jDQZEWrfClVydItxqrxyh0NW4wtvLFv+pxIqxAQIPBAAGgwwNjgyNDIzNzg1NDIiDC32igogwpTYgW6xsiqhBDDpir+quukJDQkPV4koSEQcmNaaepkz8qN1dr0G9N+M6slWV3BkU7yvJBqdZX1C5/H4dbp9cC8BEEwwtspQr4UZfvm9OmY+aRES5jBFbv5n5Lofdh2Cx8Zl9fqEI16E/b1PLlA8EjQlgWorFkgeRyrC4oh1J17d6G+7s92wOFsgdpJbu5b3nOpyV+8MnXs30bNM/KDBebi1mYxK4FQP7ODvjBcdvzPm7DbS7zoE3j0O4WQexs5Y8wZzu3eElpiAiTPyPrlc+lkYuf+tiQg2bVfMpY5S/Vwzthm0+F55LKUt+qIWErzWWClUzzsOHUy1UB9/HLe9XHmadBvDhoAoyCStWCDB+33tdVjw/2xqmrzwCfmhYl1ELPEqN41LLRKjXT8yBghZHX/p9NHLML2/CwJ2gTdeA2FC3gR4aZCxBD3jUhtrNU50TANq7wVEUOnuju6sKpiMl1oMH8M1y9wFzAyY9WSuyI02nEZedDDKYF0r5jPdixRvf4/65J39487RmUVOV9siM8yocebnEsIe2jXx+k9NGVoBcVTLpdaTq1CE8PIPybzgqgwkATgGB5wTVE2shTcE3AOqWaqX8YQsVEk342mdCgN33jL0KLq4YY5QPC8Wd8slaDAhJ1vdf9miBj31IB4j30oepFZ9dp26Qwp8DK2DDl+CHdLXTDt3bAkKA3LSpu+eJ+n3uyz3R+rwwnbxIhidKTu/JW6qaG7wuzEbMOPolokGOoUCW1j8NMFtCT9gjecTjVcfbiK2ONJdXdsSBVPU4Jas5mAze3/HOmbV9JWro+Q2qXsCuiixIGn87TeWqHa9TwIeX9Oy4DIWfdnQxi8UyL26t77EKtbN9EbOtOeK4/upyx5jfDoXclWo/pN0ghUmT/C3s0oYsFX28LOYYk+cJOm3OxDQ5bG9EuJU7twf3MYUruz7yk6PQDmDZiNKCpo0WaPwccHCAPHYbfhNWY3vTw9dByF0xZejPQua6HsaF4u6KnktrKUHxkoie5YX84I/1in8n5oqv7wTGrhpJf9ChhKv5ZAVPDgOSNMg0R8JIY6ta/GaA/qZnjVAd/sqqoyQPyjbB4qKilzB",
        "Expiration": "2021-08-25T04:09:23+00:00"
    }
}








### Eliminación de recursos

```bash
aws cloudformation delete-stack --stack-name lab47-cognito-identitypool
```
