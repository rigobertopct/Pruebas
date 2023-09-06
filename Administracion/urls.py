from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_file_upload.django import FileUploadGraphQLView
from .schema import schema

app_name = 'Administracion'

urlpatterns = [
    path('', csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True, schema=schema)))
]
