from django.shortcuts import render
from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView, RetrieveAPIView,\
    UpdateAPIView

from accounts.models import User
from accounts.serializers import UserRegistrationSerializer


class UserRegistrationView(CreateAPIView):
    """
    This API will be used to allow the users to SignUp for the WebApp.
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    # def post(self, request, *args):
    #     new_user_serializer = UserRegistrationSerializer(data=request.data)
    #     if new_user_serializer.is_valid():
    #         new_user = new_user_serializer.create(request.data)
    #         # after getting the new user we need to create a user profile for him
    #         UserProfile.objects.create(
    #             user=User.objects.get(id=new_user.get('id')),
    #             device_id=request.data.get('device_id'),
    #             first_login=False
    #         )
    #         if new_user:
    #             return Response(
    #                 data={
    #                     "data": new_user,
    #                     "success": True
    #                 }, status=status.HTTP_201_CREATED
    #             )
    #     return Response(
    #         data={
    #             "message": list(new_user_serializer.errors.values())[0][0],
    #             "success": False
    #         }, status=status.HTTP_400_BAD_REQUEST
    #     )
