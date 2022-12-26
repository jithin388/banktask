from .models import Category
from.models import place
def menu_links(request):
    links=Category.objects.all()
    link=place.objects.all()
    return dict(links=links,link=link)