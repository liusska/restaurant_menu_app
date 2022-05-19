import graphene
from graphene_django import DjangoObjectType

from .models import Menu
from users.schema import UserType


class MenuType(DjangoObjectType):
    class Meta:
        model = Menu


class Query(graphene.ObjectType):
    menu = graphene.List(MenuType)

    def resolve_menu(self, info, **kwargs):
        return Menu.objects.all()


class CreateMenuItem(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    image_url = graphene.String()
    ingredients = graphene.String()
    cooking_time = graphene.Int()
    description = graphene.String()
    posted_by = graphene.Field(UserType)

    class Arguments:
        name = graphene.String()
        image_url = graphene.String()
        ingredients = graphene.String()
        cooking_time = graphene.Int()
        description = graphene.String()

    def mutate(self, info, name, image_url, ingredients, cooking_time, description):
        user = info.context.user or None

        menu_item = Menu(
            name=name,
            image_url=image_url,
            ingredients=ingredients,
            cooking_time=cooking_time,
            description=description,
            posted_by=user,
        )
        menu_item.save()

        return CreateMenuItem(
            id=menu_item.id,
            name=menu_item.name,
            image_url=menu_item.image_url,
            ingredients=menu_item.ingredients,
            cooking_time=menu_item.cooking_time,
            description=menu_item.description,
            posted_by=menu_item.posted_by,
        )


class Mutation(graphene.ObjectType):
    create_menu_item = CreateMenuItem.Field()