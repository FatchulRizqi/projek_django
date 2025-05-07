from django.shortcuts import render

def welcome(request):
    context= {
        "links":[
            ["about/","About"],
            ["contact/", "Contact"]
        ]
    }
    return render(request,'index.html', context)

# def about(request):
#     return render(request,include('about.urls'))

# def contact(request):
#     return render(request, 'kontak.html')








