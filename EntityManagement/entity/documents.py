from django_elasticsearch_dsl import  Document, fields
from elasticsearch_dsl import Index
from django_elasticsearch_dsl.registries import registry
from .models import Tag

tag = Index('tags')
tag.settings(
number_of_shards=1,
    number_of_replicas=0
)


@registry.register_document
@tag.document
class TagDocument(Document):
    name = fields.TextField(
        attr='name',
        fields={
            'suggest': fields.Completion(),
        }
    )

    class Django:
        model = Tag
        fields = ['id']
