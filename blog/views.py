from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status


def home(request):
    return JsonResponse({'name': 'saikat'})


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
    return Response(api_urls)


class BlogViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    permission_classes_by_action = {'create': [
        AllowAny], 'update': [AllowAny], 'delete': [AllowAny]}
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

# Create your views here.
