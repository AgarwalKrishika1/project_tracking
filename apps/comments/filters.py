from django_filters import rest_framework as django_filters, DateFromToRangeFilter
from apps.comments.models import Comment


class CommentFilterSet(django_filters.FilterSet):
    created_at = DateFromToRangeFilter(field_name="created_at")

    class Meta:
        model = Comment
        fields = []
