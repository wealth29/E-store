from django.db import models

# Create your models here.

class Tag(models.Model):
    label = models.CharField(max_length=225)

class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(
        'contenttypes.ContentType', on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = models.GenericForeignKey('content_type', 'object_id')