from rest_framework import generics
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets

# Create your views here.
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    此视图自动提供`list`和`detail`操作
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SnippetViewSet(viewsets.ModelViewSet):
    '''
    此视图自动提供`list`,`create`,`retrieve`,`update`和`destroy`操作。
    另外我们还提供一个额外的`highlight`操作
    '''
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


