from django.contrib.auth.models import User
from django.db import models
import uuid
from django.utils import timezone
from udt.choices import REQUEST_TYPE_CHOICES, REQUEST_VIA_CHOICES, GEO_CHOICES, FILTER_BY_TOOL_CHOICES, SEVERITY_CHOICES, TASKS_CHOICES


class WorkOrder(models.Model):
    uid = models.URLField(primary_key=True, default=uuid.uuid4, editable=False)
    request_type = models.CharField(max_length=10, choices=REQUEST_TYPE_CHOICES)
    requested_via = models.CharField(max_length=20, choices=REQUEST_VIA_CHOICES)
    geo = models.CharField(max_length=15, choices=GEO_CHOICES)
    filter_by_tool = models.CharField(max_length=20, choices=FILTER_BY_TOOL_CHOICES)
    task = models.CharField(max_length=250, choices=TASKS_CHOICES)
    owner = models.ForeignKey(User)
    # assign_to = models.ForeignKey(User, related_name='assigned_to', blank=True, null=True)
    task_received = models.DateTimeField(default=timezone.now)
    link = models.CharField(max_length=500)
    severity = models.CharField(max_length=5, choices=SEVERITY_CHOICES)
    request_contained = models.PositiveIntegerField(default=1)
    affected_items = models.PositiveIntegerField(default=1)
    subject = models.CharField(max_length=250)
    description = models.TextField()
    status = models.CharField(max_length=6, default='Opened')

    class Meta:
        ordering = ('-task_received',)

    def __str__(self):
        return self.subject
