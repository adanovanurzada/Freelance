from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator


class Skill(models.Model):
    skill_name = models.CharField(max_length=50)

    def __str__(self):
        return self.skill_name


class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('client', 'Client'),
        ('freelancer', 'Freelancer'),
    )

    phone_number = PhoneNumberField(null=True, blank=True)
    full_name = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    bio = models.TextField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(65)], null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    skills = models.ManyToManyField(Skill, related_name='users', blank=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class SocialLinks(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='social_links')
    platform_name = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return f'{self.platform_name} - {self.url}'


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Project(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects')
    skills_required = models.ManyToManyField(Skill, related_name='projects')
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Offer(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='offers')
    freelancer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='offers')
    message = models.TextField(null=True, blank=True)
    proposed_budget = models.DecimalField(max_digits=10, decimal_places=2)
    proposed_deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)



class Review(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='reviews')
    rating_choices = [(i, str(i)) for i in range(1, 6)]
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='given_reviews')
    target = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='received_reviews')
    rating = models.IntegerField(choices=rating_choices)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)



