import requests
from django.shortcuts import render, redirect

from .models import Address, Company, User, Geo, Post


def upload_data(request):
    user_url = 'http://jsonplaceholder.typicode.com/users'
    user_response = requests.get(user_url)
    post_url = 'http://jsonplaceholder.typicode.com/posts'
    post_response = requests.get(post_url)

    for user_data in user_response.json():
        cmp = Company(
            company_name=user_data['company']['name'], catchPhrase=user_data['company']['catchPhrase'],
            bs=user_data['company']['bs']
        )
        usr = User(
            name=user_data['name'], username=user_data['username'], email=user_data['email'], phone=user_data['phone'],
            website=user_data['website'], company=cmp
        )
        adr = Address(
            user=usr, street=user_data['address']['street'], suite=user_data['address']['suite'],
            city=user_data['address']['city'], zipcode=user_data['address']['zipcode']
        )
        geo = Geo(
            address=adr, latitude=user_data['address']['geo']['lat'], longitude=user_data['address']['geo']['lng']
        )

        cmp.save()
        usr.save()
        adr.save()
        geo.save()

    for post_data in post_response.json():
        pst = Post(
            user_id=post_data['userId'], title=post_data['title'], body=post_data['body']
        )
        pst.save()
    return redirect('index')


def index(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'test_task/index.html', context=context)
