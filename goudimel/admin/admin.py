from django.contrib import admin

from goudimel.models import Book
from goudimel.models import Piece
from goudimel.models import Phrase


class BookAdmin(admin.ModelAdmin):
    pass


class PieceAdmin(admin.ModelAdmin):
    pass


class PhraseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)
admin.site.register(Piece, PieceAdmin)
admin.site.register(Phrase, PhraseAdmin)