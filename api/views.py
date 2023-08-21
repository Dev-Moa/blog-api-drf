from .models import Post
from .serializer import PostSerializer, UserSerializer
from rest_framework.permissions import BasePermission,SAFE_METHODS,IsAuthenticated,AllowAny
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class PostWritePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
    
# signup
class SignUpView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user_created = serializer.save()
            if user_created:
                return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# logout
class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView,PostWritePermission):
    permission_classes =[PostWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
