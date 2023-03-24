from django.shortcuts import render


def home(request):
    data = {
        "movies": [
            (
                "Citizen Kane",  # Movie
                1941,  # Year
            ),
            (
                "Casablanca",
                1942,
            ),
            (
                "Psycho",
                1960,
            ),
        ]
    }
    return render(request, "listing.html", data)