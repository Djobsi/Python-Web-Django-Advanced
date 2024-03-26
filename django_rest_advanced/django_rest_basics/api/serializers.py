from django_rest_basics.api.models import Author, Book
from rest_framework import serializers


class AuthorForBookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("name", )


class AuthorForCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("name", )


class BookForListSerializer(serializers.ModelSerializer):
    author = AuthorForBookListSerializer(many=False)

    class Meta:
        model = Book
        # fields = ("pk", "title", "author", "genre")
        fields = "__all__"


class BookForCreateSerializer(serializers.ModelSerializer):
    author = AuthorForCreateSerializer(many=False)

    class Meta:
        model = Book
        fields = "__all__"

    def create(self, validated_data):
        author_data = self.validated_data.pop("author", None)

        author, _ = Author.objects.get_or_create(**author_data)

        book_data = {
            **self.validated_data,
            "author": author,
        }

        return Book.objects.create(**book_data)


class BookForAuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class AuthorForListSerializer(serializers.ModelSerializer):
    book_set = BookForAuthorListSerializer(many=True)

    class Meta:
        model = Author
        fields = ("name", "book_set")