from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'age',
                  'phone_number', 'status']
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, date):
        user = authenticate(**date)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Наверные учетные данные')

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                 'username': instance.username,
                 'email': instance.email,
        },
        'access': str(refresh.access_token),
        'refresh': str(refresh),

        }




class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class UserMeSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'first_name', 'last_name',
                  'phone_number', 'bio', 'age', 'avatar', 'skills']


class UserProfileSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    class Meta:
        model = UserProfile
        fields = '__all__'


class SocialLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProjectListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    client = UserProfileSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'budget', 'deadline', 'status', 'category', 'client']


class ProjectDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    client = UserProfileSerializer(read_only=True)
    skills_required = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class OfferListSerializer(serializers.ModelSerializer):
    project = ProjectListSerializer(read_only=True)
    freelancer = UserProfileSerializer(read_only=True)

    class Meta:
        model = Offer
        fields = ['id', 'project', 'freelancer', 'message',  'created_at']


class OfferDetailSerializer(serializers.ModelSerializer):
    project = ProjectDetailSerializer(read_only=True)
    freelancer = UserProfileSerializer(read_only=True)

    class Meta:
        model = Offer
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):
    reviewer = UserProfileSerializer(read_only=True)
    project = ProjectListSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'reviewer', 'project', 'rating', 'comment', 'created_at']


class ReviewDetailSerializer(serializers.ModelSerializer):
    reviewer = UserProfileSerializer(read_only=True)
    project = ProjectDetailSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

