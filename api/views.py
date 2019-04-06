from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse

import json

# Create your views here.
def search(request):
	if request.method == 'GET':
		query = request.GET.get('query', '')

		users = User.objects.filter(username__contains=query)

		user_data = []
		for user in users:
			user_data.append({
				'username': user.username,
			})
		return HttpResponse(json.dumps(user_data), content_type="application/json")
