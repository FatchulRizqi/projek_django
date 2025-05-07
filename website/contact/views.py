from django.shortcuts import render

# Create your views here.
def contact(request):
    context= {
        "links":[
            ["/", "Home"],
            ["/about/","About"]
        ]
    }
    return render(request, 'contact/kontak.html',context)