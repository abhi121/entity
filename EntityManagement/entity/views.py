from rest_framework import serializers, viewsets
from django.http import HttpResponse, JsonResponse
from entity.models import Entity, Tag
from entity.serializers import EntitySerializer, TagSerializer
from rest_framework.decorators import action
from entity.documents import TagDocument


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'name'

    @action(detail=True)
    def entities(self, request, name):
        tag = self.get_object()
        entities = tag.entities.all()
        serializer = EntitySerializer(entities, many=True)
        return JsonResponse(serializer.data, safe=False)


def discover(request):
    if request.method == 'GET':
        results = []
        search = request.GET.get('name', '')
        """
        query to be used here
        result = TagDocument.search().suggest('name',search,completion={"fields": "name.suggest"})
        but it is giving zero results and also confusing. as it was taking time so for now i have used wildcard
        """
        result = TagDocument.search().query('wildcard', name='*'+search+'*')
        for res in result:
            results.append(res.name)
        return JsonResponse({'results': results})
