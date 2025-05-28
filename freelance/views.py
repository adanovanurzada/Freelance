from django.shortcuts import render
from rest_framework import generics, viewsets, permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from .models import *
from .serializers import *
from .permissions import IsClientOrReadOnly, IsOwnerOrReadOnly, IsFreelancerOrReadOnly, IsOfferOwner
from .filters import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer


    def create(self, request, *args, **kwargs):
        serializers = self.get_serializer(date=request.data)
        serializers.is_valid(raise_exception=True)
        user = serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)



class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request: Request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        try:
            serializers.is_valid(raise_exception=True)
        except Exception:
            return Response({'detail': 'Неверные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializers.validated_data
        return Response(serializers.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, reguest, *args, **kwargs):
        try:
            refresh_token =reguest.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_402_PAYMENT_REQUIRED)



class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class UserMeView(generics.RetrieveUpdateAPIView):
    serializer_class = UserMeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class SocialLinksViewSet(viewsets.ModelViewSet):
    queryset = SocialLinks.objects.all()
    serializer_class = SocialLinksSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProjectFilter
    search_fields = ['client']
    ordering_fields = ['created_at', 'budget']
    permission_classes = [permissions.AllowAny]




class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer


class MyProjectsView(generics.ListAPIView):
    serializer_class = ProjectDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(client=self.request.user)


class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsClientOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)


class ProjectUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class ProjectDeleteView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class OfferListView(generics.ListAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = OfferFilter
    search_fields = ['created_at']
    permission_classes = [permissions.AllowAny]



class OfferDetailView(generics.RetrieveAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferDetailSerializer


class OfferCreateView(generics.CreateAPIView):
    serializer_class = OfferDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsFreelancerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(freelancer=self.request.user)


class MyOffersView(generics.ListAPIView):
    serializer_class = OfferListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Offer.objects.filter(freelancer=self.request.user)


class OfferUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsOfferOwner]


class OfferDeleteView(generics.DestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsOfferOwner]


class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ReviewFilter
    search_fields = ['rating']
    ordering_fields = ['created_at']
    permission_classes = [permissions.AllowAny]


class ReviewDetailView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer


class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(freelancer=self.request.user)

