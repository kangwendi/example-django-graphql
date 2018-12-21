from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from cookbook.ingredients.models import Category, Ingredient

from django.contrib.auth import get_user_model
import graphene
from graphql import GraphQLError

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(selfself, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )

        user.set_password(password)
        user.save()

        return CreateUser(user=user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

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

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class Query(object):
    category = relay.Node.Field(CategoryNode)
    Ingredient = relay.Node.Field(IngredientNode)
    Users = graphene.List(
        UserType,
        offset=graphene.Int(),
        limit=graphene.Int()
    )
    me = graphene.Field(UserType)
    wenkatagori = graphene.Field(CategoryNode)

    def resolve_Users(self, info, offset=None, limit=None):
        qs = get_user_model().objects.all()[offset:limit]

        return qs

    def resolve_me(self,info):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Not Logged!")

        return user

    def resolve_wenkatagori(self, info):
        return Category.objects.all()

    all_categories = DjangoFilterConnectionField(CategoryNode)
    all_ingredient = DjangoFilterConnectionField(IngredientNode)