from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users')
router.register(r'skills', SkillViewSet, basename='skills')
router.register(r'socials', SocialLinksViewSet, basename='socials')
router.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('', include(router.urls)),

    path('users/me/', UserMeView.as_view(), name='user-me'),

    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('projects/my/', MyProjectsView.as_view(), name='my-projects'),
    path('projects/create/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),

    path('offers/', OfferCreateView.as_view(), name='offer-create'),
    path('offers/my/', MyOffersView.as_view(), name='my-offers'),
    path('offers/<int:pk>/update/', OfferUpdateView.as_view(), name='offer-update'),
    path('offers/<int:pk>/delete/', OfferDeleteView.as_view(), name='offer-delete'),

    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('reviews/create/', ReviewCreateView.as_view(), name='review-create'),
]
