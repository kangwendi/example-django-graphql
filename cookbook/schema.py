import graphene
import graphql_jwt
from graphene_django.debug import DjangoDebug

import cookbook.ingredients.schema


class Query(cookbook.ingredients.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    debug = graphene.Field(DjangoDebug, name='__debug')

class Mutation(cookbook.ingredients.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
