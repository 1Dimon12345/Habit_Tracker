from django.shortcuts import render
def index(request):
    my_text= "ghbdtn"
    if request.method=='POST':
        password=request.POST.get('password')
        username=request.POST.get('username')
        my_text=f'Успех вы зарегестрированы как {username}!'
    return render(request, 'main/index.html',{'my_text':my_text})
