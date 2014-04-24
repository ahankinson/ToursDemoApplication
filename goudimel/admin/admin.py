from django.contrib import admin

from goudimel.models import Book
from goudimel.models import Piece
from goudimel.models import Phrase


def reindex_in_solr(modeladmin, request, queryset):
    # calls the save method on every item, ensuring the
    # post_save handler is called
    for item in queryset:
        item.save()
reindex_in_solr.short_description = "Re-Index Selected Items"


class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'publisher', 'remarks')
    list_display = ('title', 'publisher', 'rism_id', 'cesr_id', 'num_pages')
    list_filter = ('publisher',)
    actions = [reindex_in_solr]


class PieceAdmin(admin.ModelAdmin):
    search_fields = ('title', 'book_id__title')
    list_filter = ('book_id', 'composer_src', 'forces')
    list_display = ('title', 'composer_src', 'forces', 'book_id')
    actions = [reindex_in_solr]


class PhraseAdmin(admin.ModelAdmin):
    search_fields = ('phrase_text',)
    list_filter = ('piece_id',)
    list_display = ('phrase_text', 'piece_id', 'phrase_num', 'phrase_start', 'phrase_stop', 'rhyme')
    list_editable = ('phrase_num', 'phrase_start', 'phrase_stop', 'rhyme')
    actions = [reindex_in_solr]


admin.site.register(Book, BookAdmin)
admin.site.register(Piece, PieceAdmin)
admin.site.register(Phrase, PhraseAdmin)