from django.shortcuts import render , HttpResponse
import requests
import json

def index(request):

    if request.method=='POST':

        clientKey = request.POST['g-recaptcha-response']
        secretKey= '6LfE8OYUAAAAAOx_bQ055xSlgz2uU-Ayu1bzJx5d'
        captchaData = {
            'secret' : secretKey,
            'response': clientKey
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=captchaData)
        response = json.loads(r.text)
        verify = response['success']
        print('autorizado ? : ',verify)
        if verify:
            return HttpResponse('<script> alert("autenticado com sucesso");</script>')
        else:
            return HttpResponse('<script> alert("Você e um robo");</script>')
    return render(request, 'recaptha/index.html')