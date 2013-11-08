from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

from rest_framework.renderers import JSONRenderer, JSONPRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics

from goudimel.models import Book
from goudimel.models import Piece
from goudimel.models import Phrase

from goudimel.serializers.book import BookSerializer
from goudimel.serializers.piece import PieceSerializer
from goudimel.serializers.phrase import PhraseSerializer

from goudimel.renderers.custom_html_renderer import CustomHTMLRenderer


@api_view(('GET',))
def api_root(request, format=None):
    return Response({'books': reverse('books-list', request=request, format=format),
                     'pieces': reverse('pieces-list', request=request, format=format),
                     'phrases': reverse('phrases-list', request=request, format=format)})


@ensure_csrf_cookie
def home(request):
    data = {}
    return render(request, "index.html", data)


class BookListHTMLRenderer(CustomHTMLRenderer):
    template_name = "book/book_list.html"


class BookDetailHTMLRenderer(CustomHTMLRenderer):
    template_name = "book/book_detail.html"


class BookList(generics.ListCreateAPIView):
    model = Book
    serializer_class = BookSerializer
    renderer_classes = (JSONRenderer, JSONPRenderer, BookListHTMLRenderer)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Book
    serializer_class = BookSerializer
    renderer_classes = (JSONRenderer, JSONPRenderer, BookDetailHTMLRenderer)


class PieceListHTMLRenderer(CustomHTMLRenderer):
    template_name = "piece/piece_list.html"


class PieceDetailHTMLRenderer(CustomHTMLRenderer):
    template_name = "piece/piece_detail.html"


class PieceList(generics.ListCreateAPIView):
    model = Piece
    serializer_class = PieceSerializer
    renderer_classes = (JSONRenderer, JSONPRenderer, PieceListHTMLRenderer)


class PieceDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Piece
    serializer_class = PieceSerializer
    renderer_classes = (JSONRenderer, JSONPRenderer, PieceDetailHTMLRenderer)


class PhraseListHTMLRenderer(CustomHTMLRenderer):
    template_name = "phrase/phrase_list.html"


class PhraseDetailHTMLRenderer(CustomHTMLRenderer):
    template_name = "phrase/phrase_detail.html"


class PhraseList(generics.ListCreateAPIView):
    model = Phrase
    serializer_class = PhraseSerializer
    renderer_classes = (JSONRenderer, JSONPRenderer, PhraseListHTMLRenderer)


class PhraseDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Phrase
    serializer_class = PhraseSerializer
    renderer_classes = (JSONRenderer, JSONPRenderer, PhraseDetailHTMLRenderer)
