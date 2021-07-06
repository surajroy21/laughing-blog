from rest_framework import serializers
from  .models import Blog,Author

class BlogListAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class AuthorListAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'