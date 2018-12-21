from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from cookbook.ingredients.models import Category, Ingredient

class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name']
        # only_fields = ('name',)
        # exclude_fields = ('ingredients',)
        interfaces = (relay.Node, )

class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        filter_fields = {
            'name': ['exact','icontains','istartswith'],
            'notes': ['exact','icontains'],
            'category': ['exact'],
            'category__name': ['exact']
        }
        interfaces = (relay.Node, )

class Query(object):
    category = relay.Node.Field(CategoryNode)
    Ingredient = relay.Node.Field(IngredientNode)

    all_categories = DjangoFilterConnectionField(CategoryNode)
    all_ingredient = DjangoFilterConnectionField(IngredientNode)