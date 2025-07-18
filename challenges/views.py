from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse



challenges_dict = {
    "january": "Eat no meat for entire month.",
    "february": "Train for entire month.",
    "march": "Go swimming for entire month.",
    "april": "Go running for entire month.",
    "may": "Play sports for entire month.",
    "jun": "Focus on work for entire month.",
    "july": "Spend time with family for entire month.",
    "august": None,
    "september": None,
    "october": None,
    "november": None,
    "december": None
}
# Create your views here.


def monthly_challenge_bu_number(request, selected_month):
        month_list = list(challenges_dict.keys())
        if selected_month > len(month_list):
            return HttpResponseNotFound("Invalid url.")
        
        forward_month = month_list[selected_month-1]
        redirect_path = reverse("month-challenge", args=[forward_month])
        return HttpResponseRedirect(redirect_path)
    


def index(request):
    month_links = ""
    months = list(challenges_dict.keys())
    
    return render(request, "challenges/index.html", {
        "months": months
    })

def  monthly_challenge(request, selected_month):
    try:
        challenge_text = challenges_dict[selected_month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_title": selected_month
            
        })
        
    except:
        raise Http404()
    
    
