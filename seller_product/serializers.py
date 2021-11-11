from rest_framework.serializers import ModelSerializer
from seller_product.models import Comment, Product, Tag

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['seller_email', 'name', 'price', 'picture','brand', 'description']

class ProductsViewSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'picture', 'brand', 'description']

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'product', 'rating', 'content']

class TagSerializer(ModelSerializer):

    class Meta:
        model = Tag
        fields = ['tag']

class ProductsViewSeller(ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'