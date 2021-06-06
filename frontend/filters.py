import django_filters
from frontend.models import PostPage




class PostFilter(django_filters.FilterSet):


    class Meta:
        model = PostPage
        fields = [
            'pst_title',
            'category',
            'price',
        ]