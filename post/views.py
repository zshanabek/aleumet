from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from django.db.models import Count
from rest_framework import viewsets, mixins, generics, permissions, status, filters
from rest_framework.views import APIView
from datetime import datetime
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

    @action(detail=False, methods=['GET'])
    def numbers(self, request, *args, **kwargs):
        res = Post.objects.values_list('id', flat=True)
        return Response(res, status=status.HTTP_200_OK)

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
        Like.objects.get(post=self.get_object(), user=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Analitics(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def group_by_date(self, data):
        posts = {}
        for item in data:
            day = item['created_at'].split('T')[0]
            if day not in posts.keys():
                posts[day] = []
            posts[day].append(item)
        return posts

    def get(self, request, format=None):
        queryset = Post.objects.all()
        date_from = self.request.query_params.get('date_from', None)
        date_to = self.request.query_params.get('date_to', None)
        if date_from and date_to:
            date_from = datetime.strptime(date_from, '%Y-%m-%d')
            date_to = datetime.strptime(date_to, '%Y-%m-%d')
            queryset = queryset.filter(
                created_at__gte=date_from, created_at__lte=date_to)
        serializer = PostSerializer(queryset, many=True)
        return Response(self.group_by_date(serializer.data), status=status.HTTP_200_OK)
