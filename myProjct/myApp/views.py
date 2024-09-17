from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer, ProjectCreateSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=False, methods=['get'], url_path='my-projects', permission_classes=[IsAuthenticated])
    def list_user_projects(self, request):
        projects = request.user.projects.all()
        serializer = self.get_serializer(projects, many=True)
        return Response(serializer.data)
