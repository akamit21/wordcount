from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
	return render(request, "home.html", {'name':'Amit Kumar'})

def count(request):
	data = request.GET['word_area']
	word_list = data.split()
	length = len(word_list)

	word_dic = {}
	for word in word_list:
		if word in word_dic:
			word_dic[word] += 1
		else:
			word_dic[word] = 1

	return render(request, "count.html", {'string':data, 'length':length, 'pwc':word_dic.items()})
