## Topic: DRF JWT Authenticantion and Authorization 

Youtube Link : https://www.youtube.com/watch?v=AfYfvjP1hK8&list=PLOLrQ9Pn6caw0PjVwymNc64NkUNbZlhFw&index=3

Objectives 

## Why JWT
## JWT Process
## Configure DRF
## Develop our react app to handle JWT

## HTTP request are stateless

Client (React)                     Server (DRF Api)

1- HTTP Request ------>
                    <------ Retrieve Data

2- HTTP Request ------>
                    <------ Return Data

HTTP is a stateless protocol, which means that the server treats each request it receives as an isolated transaction. It does not maintain any memory or knowledge of previous requests made by the same client. Each request is processed independently, and the server does not automatically associate it with any previous or subsequent requests.
                

## Why JWT  

-Http request are stateless which means if we send two request these two requests will not know each other and others same.

-Now this raises a problem which is if user logins to our server in first request then tries to get access with another request , the server will again want to login because the server does not remember the first request or the first login.

-Now JWT has solution for this problem , how ?

## JWT Process


Client (React)                     Server (DRF Api)

1- HTTP Request Login ------>       *validates the credentials and give back 
                                <------ access and refresh token

*client stores the token and sends it with each request , 
2- Token + Request ------>
                          <------ Server validates the tokens and returns required data

## Access Token :
    * An Access Token is a type of token used for authentication and authorization in token-based authentication systems like JWT.
    * The Access Token is typically short-lived and has an expiration time.
    * It is used by the client to access protected resources on the server.

## Refresh Token :
    * A Refresh Token is a type of token used in token-based authentication systems to obtain new Access Tokens without re-authenticating the user.
    * It is a long-lived token with a longer expiration time compared to the Access Token.
    * The Refresh Token is issued to the client during the initial authentication process or when the Access Token expires or becomes invalid, the client can use the Refresh Token to request a new set of tokens.
    * It helps reduce the frequency of user logins and improves the user experience by maintaining longer sessions.


## Development requirements

## Django Rest Framework

* Login service --> provide users JWT
    -Apply authentication
    -Install djangorestframeworksimpleJWT -> just follow getting started steps.
    -Use Default User module in django
    -add JWT settings you dont need to change anything
    -Test if the login is working use postman.



# Signup  
```python
class SignUpView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user_created = serializer.save()
            if user_created:
                return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

```
# Login 

# Logout
* Process Refresh Tokens

## React
* Login  --> store JWT
* Handle Refresh Tokens -> Get new access token
