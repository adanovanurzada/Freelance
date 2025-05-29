from .models import *
from modeltranslation.translator import TranslationOptions, register

@register(Skill)
class SkillTranslationOptions(TranslationOptions):
    fields = ('skill_name',)

@register(UserProfile)
class UserProfileTranslationOptions(TranslationOptions):
    fields = ('full_name', 'bio')

@register(SocialLinks)
class SocialLinksTranslationOptions(TranslationOptions):
    fields = ('platform_name',)

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Offer)
class OfferTranslationOptions(TranslationOptions):
    fields = ('message',)

@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('comment',)
