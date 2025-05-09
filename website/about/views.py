from django.shortcuts import render

# Create your views here.
def about(request):
    context= {
        'title': "Tentang aku",
        "links":[
            ["/", "Home"],
            ["/contact/","Contact"],
            ["nomor/", "Nomor"]
        ]
    }
    return render(request, 'about/about.html',context)

def nomor(request):
    return render(request, 'about/nomor.html')