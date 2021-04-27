from django.shortcuts import render
from rest_framework.views import APIView
from list_task_.settings_local import SERVER_VERSION
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from list_task_.settings import BASE_DIR


class About(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated]
    template_name = 'about.html'

    def get(self, request):
        context = {
            'server_version': SERVER_VERSION,
            'username': request.user
        }
        return Response(context)
