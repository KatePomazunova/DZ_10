from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .forms import QuoteForm, AuthorForm, TagForm

from .models import Author, Quote, Tag
from .utils import get_mongodb


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


def author_about(request, _id):
    author = Author.objects.get(_id)
    return render(request, 'quotes/author.html', context={'author': author})


def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/add_quote.html', context={'form': QuoteForm(), 'message':'form not valid'})
    
    return render(request, 'quotes/add_quote.html', context={'form': QuoteForm()})


def add_author(request):
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')

    return render(request, 'quotes/add_author.html', context={"title": f"title", "form": form})