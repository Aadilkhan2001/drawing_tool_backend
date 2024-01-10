from django.conf import settings
from django.db.models import F
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from api.models import Drawing, Shape, Annotation
from datetime import datetime, timedelta
from api.serializers import DrawingSerializer, ShapeSerializer, LoginRequestSerializer, LoginResponseSerializer, AnnotationSerializer
from services.jwt_service import JwtService
from api.authentication import JWTAuthentication

class LoginApiView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = User.objects.filter(username=username).first()
        jwt_service = JwtService()
        if not user:
            created_user = User.objects.create_user(username=username)
            created_user.set_password(password)
            created_user.save()
            token = jwt_service.generate_token(created_user.id)
            expires = datetime.utcnow() + timedelta(seconds=settings.JWT_EXPIRATION_DELTA)
            response = LoginResponseSerializer(data={'token': token, 'expires': str(expires)})
            if response.is_valid():
                return Response(response.data, status=status.HTTP_200_OK)
            else:
                return Response(response.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            if user.password == password:
                return Response({"password": ["Incorrect Password"]}, status=status.HTTP_400_BAD_REQUEST)
            token = jwt_service.generate_token(user.id)
            expires = datetime.utcnow() + timedelta(seconds=settings.JWT_EXPIRATION_DELTA)
            response = LoginResponseSerializer(data={'token': token, 'expires': str(expires)})
            if response.is_valid():
                return Response(response.data, status=status.HTTP_200_OK)
            else:
                return Response(response.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DrawingModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    serializer_class = DrawingSerializer
    queryset = Drawing.objects.all()

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        return super().create(request, *args, **kwargs)

class ShapeModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    serializer_class = ShapeSerializer
    queryset = Shape.objects.all()

    def get_queryset(self):
        user_drawings = Drawing.objects.filter(user=self.request.user)
        queryset = self.queryset.filter(drawing__in=user_drawings)
        return queryset

class AnnotationModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    serializer_class = AnnotationSerializer
    queryset = Annotation.objects.all()

    def get_queryset(self):
        queryset = (self.queryset.filter(shape__drawing__user=self.request.user).
            annotate(
            user_shapes=F('shape__drawing__user'),
            user_drawings=F('shape__drawing'),
            ).distinct()
        )
        return queryset