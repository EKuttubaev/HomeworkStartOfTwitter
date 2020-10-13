from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from twitter.forms import TweetForm
from twitter.models import Tweet


class HomeView(TemplateView):
    template_name = "home.html"


class AboutView(TemplateView):
    template_name = "about.html"


class NewPageView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        tweets = Tweet.objects.all()
        return render(request, "new_page.html", context={
            "tweets": tweets
        })

    class Meta:
        verbose_name_plural = "Твиты"
        verbose_name = "Твит"


class TweetDoView(TemplateView):
    template_name = "tweet_page.html"

    def dispatch(self, request, *args, **kwargs):
        form = TweetForm()

        if request.method == "POST":
            form = TweetForm(request.POST)

            if form.is_valid():
                form.instance.author = request.user
                form.instance.created_date = datetime.now()
                form.save()
                return redirect("new_page")

        return render(request, self.template_name, {"form": form})
