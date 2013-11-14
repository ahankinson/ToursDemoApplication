from django.views.generic import View
from django.shortcuts import render

from goudimel.helpers.solrsearch import SolrSearch

class JsonResponse(object):
	pass


class SearchView(View):
	def get(self, request):
		return render(request, "search/search_page.html", {})