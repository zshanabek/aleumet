from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework import viewsets, mixins, generics, permissions, status, filters
from .models import *
from .serializers import *
from user.models import User


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = (filters.SearchFilter,)
    permission_classes = (permissions.IsAuthenticated,)
    search_fields = ('title',)

    def get_permissions(self):
        if self.action in ('retrieve', 'list'):
            return [permissions.AllowAny()]
        return super(PostViewSet, self).get_permissions()

    @action(detail=True, methods=['POST'])
    def like(self, request, *args, **kwargs):
        result = Like.objects.filter(
            post=self.get_object(), user=request.user).first()

        if result is None:
            result = Like.objects.create(
                user=request.user, post=self.get_object())
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['POST'])
    def unlike(self, request, *args, **kwargs):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
