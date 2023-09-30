from django.db import models

"""
class Visibility(models.Model):
          OPTIONS = (
          ('private', 'private'),
          ('public', 'public'),
          )
          option = models.CharField(
          max_length=20, choices=OPTIONS, default=None, blank=True, null=True),
          # post = models.ForeignKey(
          #     Post, related_name='posts_visibility', on_delete=models.CASCADE
          # )
          # created_at = models.DateTimeField(auto_now_add=True)

          # class Meta:
          #    ordering = ['-created_at']
          # """
