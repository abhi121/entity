from rest_framework import serializers
from entity.models import Entity
from entity.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class EntitySerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = Entity
        fields = ['id', 'name', 'tags', 'image_url', 'height', 'width', 'created_at', 'updated_at']

    def create(self, validated_data):
        tag_list = validated_data.pop('tags')
        entity = Entity.objects.create(**validated_data)
        for tag in tag_list:
            already_present_tag = Tag.objects.filter(name=tag.get('name')).first()
            if already_present_tag == None:
                already_present_tag = Tag.objects.create()
                already_present_tag.name = tag.get('name')
                already_present_tag.save()
            entity.tags.add(already_present_tag)
        entity.save()
        return entity
