# AWS Solutions Architect Associate - Laboratorio 22

<br>

### Objetivo: 
* Crear una cuenta AWS a través del servicio AWS Organizations
* Hacer "Switch Role" entre cuentas de AWS

### Tópico:
* Management & Governance
* Security,Identity & Compliance

### Dependencias:
* Contar con una cuenta de correo electrónico. Se hará uso de esta cuenta de correo electrónico con el objetivo de crear una nueva cuenta AWS desde el servicio AWS Organizations.

<br>

---

### A - Crear una cuenta AWS a través del servicio AWS Organizations

<br>

1. Durante el desarrollo de este laboratorio haremos uso de dos cuentas de AWS, llamaremos cuenta "A" a la cuenta "Padre" (o cuenta administradora de "AWS Organizations") y cuenta "B" a la cuenta hija (o cuenta que forma parte de una organización).

<br>

2. Accedemos al servicio AWS Organizations y damos clic en el botón "Create an organization". 

<br>

<img src="images/Lab22_01.jpg">

<br>

3. Seguidamente, dar clic en el botón "Add an AWS Account" y seleccionar/ingresar los siguientes valores. Luego, dar clic en "Create AWS Account"

    * Select "Create an AWS Account"
    * AWS account name: "Ingresar alias de la cuenta, por ejemplo Sandbox o awstraining-01"
    * Email address of the account's owner: "Ingresar email indicado en el inicio del laboratorio"
    * IAM role name: OrganizationAccountAccessRole (valor por defecto)

<br>

<img src="images/Lab22_02.jpg">

<br>

<img src="images/Lab22_03.jpg">

<br>


4. Después de unos segundos, AWS habrá generado nuestra cuenta de AWS.

<br>

<img src="images/Lab22_04.jpg">

<br>

5. En otro navegador o algún navegador oculto abrimos la página de AWS con el objetivo de loguearnos a nuestra nueva cuenta de AWS. Accedemos como Root User, damos clic en el botón "Next", luego damos clic en la opción "Forgot Password". Seguimos los pasos enviados a través del correo electrónico asociada a la nueva cuenta AWS.

<br>

<img src="images/Lab22_05.jpg">

<br>

<img src="images/Lab22_06.jpg">

<br>

6. Reseteamos la contraseña y volvemos a loguear a nuestra nueva cuenta de AWS. Si tenemos problemas con la activación de la nueva cuenta considerar los siguientes escenerarios:

    * Es probable que al acceder a algún servicio AWS de nuestra nueva cuenta, sea necesario realizar algunos pasos más. Seguir las indicaciones brindadas.
    * Es problema que al acceder a algún servicio AWS de nuestra nueva cuenta tengamos que esperar hasta 24 horas para que los servicios sean activados.
    * De no tener nuestra cuenta activa en 24 horas generar un caso vía CHAT con AWS.
        * Service: Account Management
        * Category: General Account Question
        * Severity: General question
        * Subject: Agregar información
        * Description: Agregar información

<br>

<img src="images/Lab22_07.jpg">

<br>

<img src="images/Lab22_08.jpg">

<br>

<img src="images/Lab22_09.jpg">

<br>

<img src="images/Lab22_10.jpg">

<br>

7. Una vez dentro de nuestra nueva cuenta AWS, accedemos al servicio de AWS Organizations. Validamos que esta nueva cuenta pertenece a nuestra organización (Organization ID)

<br>

<img src="images/Lab22_11.jpg">

<br>

8. Accedemos al servicio S3 (en nuestra nueva cuenta AWS) y generamos un bucket S3 de prueba en la región de N.Virginia.

    * Bucket Name: nombre-apellido-aws-account02

<br>

9. Regresamos a nuestra primera cuenta AWS y generamos un bucket S3 de prueba en la región de N.Virginia.

    * Bucket Name: nombre-apellido-aws-account01

<br>

10. Desde la cuenta AWS Origen, ingresamos al servicio IAM y generamos un usuario IAM tipo "Password - AWS Management Console access" con las siguientes características:

    * User name: user
    * Select AWS credential type: Password - AWS Management Console access
    * Console password: Custom password (Ingresar contraseña)
    * Require password reset: Deshabilitar opción
    * Attach existing policies directly
    * Policy name: Administrator Access

<br>

<img src="images/Lab22_12.jpg">

<br>

<img src="images/Lab22_13.jpg">

<br>

<img src="images/Lab22_14.jpg">

<br>

<img src="images/Lab22_15.jpg">

<br>


### B - Hacer "Switch Role" entre cuentas de AWS

<br>

11. Desde la cuenta AWS origen generamos la siguiente polìtica personaliza “PolicyCrossAccount”. Reemplazamos el valor de AWSID-DestinationAccount por el número de cuenta de la cuenta destino (12 dígitos).

```bash
{    
    "Version": "2012-10-17",    
    "Statement": 
    {        
        "Effect": "Allow",        
        "Action": "sts:AssumeRole",        
        "Resource": [            
            "arn:aws:iam::${AWSID-DestinationAccount}:role/RoleCrossAccount" 
        ]
    }
}
```

<br>

<img src="images/Lab22_16.jpg">

<br>

<img src="images/Lab22_17.jpg">

<br>

<img src="images/Lab22_18.jpg">

<br>

12. Asignamos la política "PolicyCrossAccount" a el usuario "User" previamente generado. Se validará que el usuario "User" contará con 02 políticas, siendo una de ellas de tipo "AWS managed policy" y la otra de tipo "Managed policy".

<br>

<img src="images/Lab22_19.jpg">

<br>

<img src="images/Lab22_20.jpg">

<br>

<img src="images/Lab22_21.jpg">

<br>

<img src="images/Lab22_22.jpg">

<br>

13. En la cuenta destino, creamos un rol de nombre "RoleCrossAccount" asociado al ID de la cuenta origen (El nombre "RoleCrossAccount" corresponde a lo detallado en la política del paso 11). Considerar los siguientes valores:

    * Trusted Entity Type: AWS Account
    * An AWS Account: Another AWS Account
        * Account ID: Cuenta AWS origen
    * Permissions policies: AdministratorAccess
    * Role name: RoleCrossAccount

<br>

<img src="images/Lab22_23.jpg">

<br>

<img src="images/Lab22_24.jpg">

<br>

<img src="images/Lab22_25.jpg">

<br>

<img src="images/Lab22_26.jpg">

<br>

14. Accedemos al rol "RoleCrossAccount" creado. Analizamos las secciones "Permissions" y "Trust relationships". 

<br>

<img src="images/Lab22_27.jpg">

<br>

15. Accedemos modo usuario (no modo root) usando el usuario "User" de nuestra cuenta origen. Al ingresar de este modo, AWS solicitará ingresar el número de cuenta AWS. Accederemos como "Usuario de IAM". Dentro de AWS, validaremos que nuestra usuario se carga en la consola. Damos clic en el botón ubicado al lado derecho superior, y luego damos clic en la opción "Switch role". 


<br>

<img src="images/Lab22_28.jpg">

<br>

<img src="images/Lab22_29.jpg">

<br>

16. Ingresamos los siguientes valores y damos clic en la opción "Cambiar función". Validaremo que nos encontramos en la cuenta destino a través del servicio S3. Asi mismo en la sección derecha superior podremos ver que se carga el rol "RoleCrossAccount"

    * Cuenta: Ingresamos el ID de la cuenta destino
    * Función: RoleCrossAccount
    * Nombre de Visualización: Ingreso no obligatorio
    * Color: Selección no obligatorio

<br>

<img src="images/Lab22_30.jpg">

<br>

<img src="images/Lab22_31.jpg">

<br>

<img src="images/Lab22_32.jpg">

<br>


