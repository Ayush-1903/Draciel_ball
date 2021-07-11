from django.shortcuts import render,redirect

def home(request):
	return render(request,'ball/home.html')

def main(request):
	return render(request,'ball/main.html')

def game(request):
	return render(request,'ball/game.html')