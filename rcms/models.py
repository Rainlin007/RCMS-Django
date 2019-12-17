from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Group(BaseModel):
    name = models.CharField(max_length=64, blank=True, null=True)


class Project(BaseModel):
    name = models.CharField(max_length=64, blank=True, null=True)
    group = models.ForeignKey(
        "Group", on_delete=models.CASCADE, blank=True, null=True)


class Item(BaseModel):
    path = models.CharField(max_length=64, blank=True, null=True)
    comment = models.CharField(max_length=64, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    project = models.ForeignKey(
        "Project", on_delete=models.CASCADE, blank=True, null=True)


class User(BaseModel):
    token = models.CharField(max_length=64, blank=True, null=True)
    account = models.CharField(max_length=64, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
