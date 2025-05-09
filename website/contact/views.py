from django.shortcuts import render

# Create your views here.
def contact(request):
    context= {
        "title":"Apa yang bisa aku bantu?",
        "links":[
            ["/", "Home"],
            ["/about/","About"]
        ]
    }
    return render(request, 'contact/kontak.html',context)