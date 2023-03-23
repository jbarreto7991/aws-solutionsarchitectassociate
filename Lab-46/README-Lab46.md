# AWS Solutions Architect Associate - Laboratorio 46

<br>

### Objetivo: 
* Implementación de Cognito User Pool

### Tópico:
* Security, Identity & Compliance

### Dependencias:
* Ninguna

<br>

---

### A - Implementación de Cognito User Pool

<br>

1. Desde la nueva consola de Cognito (v2), accedemos al servicio "Cognito - User Pools" y damos clic en el botón "Create user pool". Ingresamos/seleccionamos los siguientes valores. Finalmente dar clic en el botón "Create user pool"

  - Authentication providers
    - Provider types: Cognito user pool
    - Cognito user pool sign-in options: Email
  - Password policy
    - Password policy mode: Cognito defaults
  - Multi-factor authentication
    - MFA enforcement: Require MFA - Recommended
    - MFA methods: Authenticator apps
  - User account recovery:
    - Self-service account recovery: Enable self-service account recovery - Recommended
    - Delivery method for user account recovery messages: Email only
  - Self-service sign-up:
    - Self-registration: Enable self-registration
  - Cognito-assisted verification and confirmation:
    - Allow Cognito to automatically send messages to verify and confirm - Recommended
    - Attributes to verify: Send email message, verify email address
  - Verifying attribute changes
    - Keep original attribute value active when an update is pending - Recommended
    - Active attribute values when an update is pending: Email address
  - Required attributes
    - Additional required attributes
      - family_name
      - name
  - Email: Send email with Cognito
  - User pool name:
    - User pool name: Lab46-UserPool
  - Hosted authentication pages: Use the Cognito Hosted UI
  - Domain
    - Domain type: Use a Cognito domain
    - Cognito domain: *Ingrese nombre personalizado* (P.ej.: lab46-userpool)
  - Initial app client
    - App type: Public client
    - App client name: app-client-name
    - Client secret: Generate a client secret
  - Allowed callback URLs: https://google.com/authenticate
 
<br>

<img src="images/Lab46_02.jpg">

<br>

<img src="images/Lab46_03.jpg">

<br>

<img src="images/Lab46_04.jpg">

<br>

<img src="images/Lab46_05.jpg">

<br>

<img src="images/Lab46_06.jpg">

<br>

<img src="images/Lab46_07.jpg">

<br>

<img src="images/Lab46_09.jpg">

<br>

<img src="images/Lab46_10.jpg">

<br>

<img src="images/Lab46_11.jpg">

<br>

<img src="images/Lab46_12.jpg">

<br>

<img src="images/Lab46_13.jpg">

<br>

<img src="images/Lab46_14.jpg">

<br>

<img src="images/Lab46_15.jpg">

<br>

<img src="images/Lab46_16.jpg">

<br>

2. Una vez aprovisionado el recurso, accedemos al detalle del mismo y revisamos las secciones:

  - User pool overview
    * *User pool ID*
  - Users
  - Groups
  - Sign-in experience
    - Password policy
    - Multi-factor authentication
    - User account recovery
  - Sign-up experience
    - Required attributes
    - Self-service sign-up
  - Messaging
  - App integration
    - Configuration for all app clients
      * Cognito domain
    - App client list
      * App clients and analytics
        * *Client ID*
        * *Cliente Secret*
        * *Hosted UI*
  - User pool properties

<br>

<img src="images/Lab46_17.jpg">

<br>

<img src="images/Lab46_18.jpg">

<br>

<img src="images/Lab46_19.jpg">

<br>

<img src="images/Lab46_20.jpg">

<br>


3. Desde la sección, "App Integration" > "App client list" > "App client" > "Hosted UI". Dar clic en el botón "View Hosted UI"

<br>

<img src="images/Lab46_21.jpg">

<br>

4. Aparecerá un login en el cual visualizamos los campos "Email" y "Password". El campo "Email" corresponde a la sección "Sign-in experience > Cognito user pool sign-in > Cognito user pool sign-in options". Damos clic en el enlace "Sign Up".

<br>

<img src="images/Lab46_22.jpg">

<br>

<img src="images/Lab46_23.jpg">

<br>

5. En esta nueva ventana visualizaremos los campos "Email", "Name", "Family Name" y "Password". Los campos "Email", "Name" y "Family Name" corresponden a la sección "Sign-up experience > Required attributes". Ingresamos los valores solicitados y damos clic en el botón "Sign Up"

<br>

<img src="images/Lab46_25.jpg">

<br>

<img src="images/Lab46_24.jpg">

<br>

6. En las dos ventanas descritas anteriormente y en la siguiente, podremos validar que la URL desde donde estamos haciendo estas acciones corresponde al dominio creado en la sección "App Integration > Domain"

<br>

<img src="images/Lab46_26.jpg">

<br>

7. Desde nuestro correo registrado como usuario revisaremos el "Verification code" recibido e ingresamos este valor. Este nuevo paso se activa debido a que durante el proceso de creación se indicó a "Cognito-assisted verification and confirmation" el valor "Send email message, verify email address (Allow Cognito to automatically send messages to verify and confirm - Recommended)"

<br>

<img src="images/Lab46_34.jpg">

<br>

<img src="images/Lab46_27.jpg">

<br>

<img src="images/Lab46_28.jpg">

<br>

8. Se nos redireccionará a la página, por ejemplo: "https://google.com/authenticate?code=df82558b-cc10-46b6-be3a-35a8915e7a7b". Este página corresponde al valor ingresado en la sección "App Integration" > "App client list" > "App client" > "Hosted UI" > "Allowed callback URLs". En esa misma sección se resalta que el campo "OAuth grant types" tiene por contenido "Authorization code grant". La URL generada por "Hosted UI" es, por ejemplo: "https://lab46-userpool.auth.us-east-1.amazoncognito.com/oauth2/authorize?client_id=qgj8h7bej84iksdjtoi2a5vlt&response_type=token&scope=email+openid+phone&redirect_uri=https%3A%2F%2Fgoogle.com%2Fauthenticate" 

<br>

<img src="images/Lab46_29.jpg">

<br>

<img src="images/Lab46_30.jpg">

<br>

9. Editamos la sección "Hosted UI" y modificamos el valor del campo "OAuth 2.0 grant types" por "Implicit gran". Guardamos los cambios y damos clic nuevamente sobre el botón "View Hosted UI". Validaremos que se nos redirecciona a la página, por ejemplo: "https://google.com/authenticate#access_token=eyJraWQiOiJQSkljd2N0ZjNJM2JCUlJoXC81NDIreW0wZkk2TXJQMDVaeG5FSG5pNTFSWT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1YmEyMTNlXXXXXXXXXXQxZDMtOWJiMS05MjUwZTRhOGMyZjAiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6InBob25lIG9wZW5pZCBlbWFpbCIsImF1dGhfdGltZSI6MTY3OTUzODY3OCwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tXC91cy1lYXN0LTFfdDFtMnRxb2ZYIiwiZXhwIjoxNjc5NTQyMjc4LCJpYXQiOjE2Nzk1Mzg2NzgsInZlcnNpb24iOjIsImp0aSI6IjVmYzQ1MTNlLWQzOTktNDc4Zi1iZGFmLTE2YTRhMjUyZTQ2MCIsImNsaWVudF9pZCI6InFnajhoN2Jlajg0aWtzZGp0b2kyYTV2bHQiLCJ1c2VybmFtZSI6IjViYTIxM2VkLWJlODUtNDFkMy05YmIxLTkyNTBlNGE4YzJmMCJ9.hr9iT63hXbMtDIIEbFrvhW6Ydx5GSOKWSVMxa1J4DB7reQmFN0PgLFMQui9lPgjrCohyEtXMHcvj3pni91vvdSt9vPBoQ0brOMX-Sjby-weTODxzpcmr3dTAnTKRxOb9u_D6URlIAHEn1a5wEQTIyN0XplYMwB2XXXXXXXXXXUqqqkjPIqaJ4REnItkkpaws-bvV50cvFhWrStlo0f9jcX2PlyKvRSMwcD-Gf-Z5_cvWjxZcKXPQG1l4B1rzMtIoF5GFU0BT7LCHDNUeCvEICzW3tvbVhuGlORkjkLDpbknI-YoPnrRe3g2jgRqxQqXLc4mZ6WlbeiJI-9qKxjOQGg&id_token=eyJraWQiOiJOUG5ZcFZHVUFlTDVEWGhUcnViWENYakkxNExheXVlNURFdHFzb1ZwKytBPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoibjJRX1J4cUpHTnJrSkFDN01oZjdoQSIsInN1YiI6IjViYTIxM2VkLWJlODUtNDFkMy05YmIxLTkyNTBlNGE4YzJmMCIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV90MW0ydHFvZlgiLCJjb2duaXRvOnVzZXJuYW1lIjoiNWJhMjEzXXXXXXXXXX00MWQzLTliYjEtOTI1MGU0YThjMmYwIiwiYXVkIjoicWdqOGg3YmVqODRpa3NkanRvaTJhNXZsdCIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjc5NTM4Njc4LCJleHAiOjE2Nzk1NDIyNzgsImlhdCI6MTY3OTUzODY3OCwianRpIjoiYjQwZjAzMzAtYTVmOS00YTMzLTk4OGMtMGJiODRlMTc2N2E1IiwiZW1haWwiOiJqYm8uNzk5MUBnbWFpbC5jb20ifQ.FS9BDCIBcaOBTUS87Og08mG10_oYwVWBy3c5JwWqkECNP7xkQLy-AKU0QiQrUcBz66SLP9yi8QkWP9wHj-UuC9uwj4ra9nj45ncWkLE3EQ9tGp25_NWyPyOCj5pStZzpfrvAEPDXqXs6a4iQw09EORP2iW0qthTgyRTCnta8s7eRB4THcgNlWrI-82-315zEq5Fq-laXGmM06MsPjjxew9k_pFL5mdb13zhdUUFI4lbEVFghN1k100UKqYL2YUzfbXXXXXXXXXXeynSOb00EuBgdOGEN0HDvfjbTXSXjvK5wMnnpL4zuuX1m9En_XmzKPwOw7WHAHNCEvsaTvTFqBA&token_type=Bearer&expires_in=3600"

<br>

<img src="images/Lab46_31.jpg">

<br>

<img src="images/Lab46_32.jpg">

<br>

10. Cuando "OAuth grant types" tiene por contenido "Authorization code grant", Cognito nos entrega un "code". Cuando "OAuth grant types" tiene por contenido "Implicit gran", Cognito nos entrega tokens.

<br>

11. Desde Cognito, accedemos a la sección "Users" y validamos que tenemos un usuario registrado. Desde esta sección podremos generar un usuario. Asimismo desde la "Hosted UI" (Login) podremos modificar la contraseña.

<br>

<img src="images/Lab46_33.jpg">

<br>

---

### Eliminación de recursos

```bash
Eliminar "Cognito - User Pool Name"
```
