from django.shortcuts import render

# Create your views here.
def main(request):
    events = []

    return render(
        request,
        "main.html",
        {
            "events": events,
        }
    )