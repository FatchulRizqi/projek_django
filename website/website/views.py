from django.shortcuts import render

def welcome(request):
    context= {
        "title":"My website",
        "links":[
            ["#about","About me"],
            ["#skills", "My Skills"],
            ["#contact", "My Contact"],
        ]
    }
    return render(request,'index.html', context)

def wa(request):
    return render(request, 'wa.html')


# def about(request):
#     return render(request,include('about.urls'))

# def contact(request):
#     return render(request, 'kontak.html')








