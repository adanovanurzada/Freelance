from django_filters import FilterSet
from .models import *


class ProjectFilter(FilterSet):
    class Meta:
        model = Project
        fields = {
            'client': ['exact'],
            'budget': ['gte', 'lte'],
        }


class OfferFilter(FilterSet):
    class Meta:
        model = Offer
        fields = {
            'freelancer': ['exact'],
            'proposed_budget': ['gte', 'lte'],
        }


class ReviewFilter(FilterSet):
    class Meta:
        model = Review
        fields = {
            'target': ['exact'],
            'rating': ['exact', 'gte'],
        }


class UserProfileFilter(FilterSet):
    class Meta:
        model = UserProfile
        fields = {
            'full_name': ['exact'],
            'age': ['gte', 'lte'],
        }
