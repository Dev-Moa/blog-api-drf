## Permission in  django and drf

Review,apply and build custom user permissions

## Objectives
-Project level permission
-Django users/group permissions
-View level permissions
-Object level permissions
-developing custom permissions


Permission levels are :
    -Project level permission
    -View level permissions        
    -Object level permissions


-There are different types of permission :

1-AllowAny : This permission class will allow unrestricted access .

2-IsAuthenticated :This permission will allow access to registered users

3-IsAdminUser : This permission class will deny permission to any user, unless user.is_staff is True.

4- IsAuthenticatedOrReadOnly : This permission class will allow authenticated users to perform any request,but unregistered users will have read access only.

5-DjangoModelPermissionsOrAnonReadOnly : This permission will follow the permission you applied user in the admin but if the user is anonymous it will allow to read only.

NOTE : Cannot apply DjangoModelPermissionsOrAnonReadOnly on a view that does not set `.queryset` or have a `.get_queryset()` method.

NOTE : you can also create your own custom permission.

## Project level permission : is used wide permission where by any one trying access our app is applied to this type of permissioon

To create project level permission go to setting and choose any type of permission to apply to the project.

```python

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':[
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    ]
}

```


## View level permission : is used in view and by using the same project level you can now use it in specific view 

To create view level permission go to specific views and apply any type of default django permission to the view

```python

from rest_framework.permissions import IsAuthenticated


```

## Object level permission :
To create object level permission follow these steps

-create group and give object permission like view specific model aka object like view post or add post or change post etc.
-create user and add that user to created group.
-then for this permission to work use one of two classes to apply : 
    1-DjangoModelPermissions : This class applies the view the permission you have registered in the admin.
    2-DjangoModelPermissionsOrAnonReadOnly : This class is similiar to the old one but allows anonymous users read only access. 

```python
from rest_framework.permissions import BasePermission,SAFE_METHODS,DjangoModelPermissionsOrAnonReadOnly

class PostList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
```


### Login facility for djangorestframework

same way as the django login just add the following the project level urls

```python

    path("api-auth/", include("rest_framework.urls")),

```


## Permission and HTTP Requests 

View -> GET 
Add ->  POST 
Change -> PUT 
Delete ->  DELETE

## Custom Permission

To create custom permission use BASEPERMISSION class from rest_framework.permissions

```python 

from rest_framework.permissions import BasePermission,SAFE_METHODS

class PostWritePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

```

in this case we are creating a permission that allows only authors to edit their post not other posts.
we are extending the BasePermission class and using has_object_permission function to check if the request is in SAFE_METHODS [GET,HEADER,OPTION] and the return true which allow read permission for get requests but if the request is other than get request or SAFE_METHODS like update or delete then we are checking if the user sending the request is equal to the author of the post if true these requests will be allowed otherwise not .

