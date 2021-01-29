from .models import Profile
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from .serializers import ProfileSerializer,RegisterSerializer
from rest_framework.response import Response
from rest_framework import status,generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated,AllowAny

@api_view(["GET"])
@permission_classes((IsAuthenticated, ))
def get_profiles(request):
    if request.method == "GET":
        users = Profile.objects.all()
        serializer = ProfileSerializer(users, many=True)
        return Response(serializer.data)

@api_view(["GET","PUT"])
@permission_classes((IsAuthenticated, ))
def get_update_profile(request,user_id):
    user = get_object_or_404(Profile,id=user_id)
    if request.method == "GET":
        serializer =  ProfileSerializer(user)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ProfileSerializer(user,data=request.data)
        if request.user.id != user_id:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if serializer.is_valid():
            serializer.save()
            data={
                "message":"Post updated successfully"
            }
            return Response(data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
