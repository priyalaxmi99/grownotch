from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.

def index(request):
	if request.method == "POST":
		try:ch1 = request.POST['check1']
		except:ch1 = ""
		try:ch2 = request.POST['check2']
		except:ch2 = ""
		try:ch3 = request.POST['check3']
		except:ch3 = ""
		try:ch4 = request.POST['check4']
		except:ch4 = ""
		sub = "New response has been submitted!"
		msg = """Name : {}\nMobile : {}\nEmail : {}\nWebsite URL : {}\nMessgae : {}\nWhat they need : {},{},{},{}""".format(request.POST['name'],request.POST['phone'],request.POST['email'],request.POST['website'],request.POST['messagedetails'],ch1,ch2,ch3,ch4)
		# send_mail(sub, msg, settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		try:send_mail(sub, msg, settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		except:send_mail("Reg - SMTP not working", "Someone tried to submit response!\nSMTP Not working fine\nKindly contact Admin", settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		messages.success(request,"Your response has been submitted successfully!")
		return redirect('index1')
	return render(request, "index.html",locals())
def about(request):
	return render(request, "aboutus.html",locals())
def localseo(request):
	if request.method == "POST":
		sub = "New response has been submitted!"
		msg = """Name : {}\nMobile : {}\nEmail : {}\nWebsite URL : {}""".format(request.POST['name'],request.POST['phone'],request.POST['email'],request.POST['website'])
		# send_mail(sub, msg, settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		try:send_mail(sub, msg, settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		except:send_mail("Reg - SMTP not working", "Someone tried to submit response!\nSMTP Not working fine\nKindly contact Admin", settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		messages.success(request,"Your response has been submitted successfully!")
		return redirect('localseo')
	return render(request, "local-seo.html",locals())
def globalseo(request):
	if request.method == "POST":
		sub = "New response has been submitted!"
		msg = """Name : {}\nMobile : {}\nEmail : {}\nWebsite URL : {}""".format(request.POST['name'],request.POST['phone'],request.POST['email'],request.POST['website'])
		# send_mail(sub, msg, settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		try:send_mail(sub, msg, settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		except:send_mail("Reg - SMTP not working", "Someone tried to submit response!\nSMTP Not working fine\nKindly contact Admin", settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		messages.success(request,"Your response has been submitted successfully!")
		return redirect('globalseo')
	return render(request, "search-engine-optimization.html",locals())
def content(request):
	if request.method == "POST":
		sub = "New response has been submitted!"
		msg = """Name : {}\nMobile : {}\nEmail : {}\nWebsite URL : {}""".format(request.POST['name'],request.POST['phone'],request.POST['email'],request.POST['website'])
		# send_mail(sub, msg, settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		try:send_mail(sub, msg, settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		except:send_mail("Reg - SMTP not working", "Someone tried to submit response!\nSMTP Not working fine\nKindly contact Admin", settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		messages.success(request,"Your response has been submitted successfully!")
		return redirect('content')
	return render(request, "content-writing.html",locals())
def orm(request):
	if request.method == "POST":
		sub = "New response has been submitted!"
		msg = """Name : {}\nMobile : {}\nEmail : {}\nWebsite URL : {}""".format(request.POST['name'],request.POST['phone'],request.POST['email'],request.POST['website'])
		# send_mail(sub, msg, settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		try:send_mail(sub, msg, settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		except:send_mail("Reg - SMTP not working", "Someone tried to submit response!\nSMTP Not working fine\nKindly contact Admin", settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		messages.success(request,"Your response has been submitted successfully!")
		return redirect('orm')
	return render(request, "online-reputation-management.html",locals())
def dm(request):
	if request.method == "POST":
		sub = "New response has been submitted!"
		msg = """Name : {}\nMobile : {}\nEmail : {}\nWebsite URL : {}""".format(request.POST['name'],request.POST['phone'],request.POST['email'],request.POST['website'])
		# send_mail(sub, msg, settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		try:send_mail(sub, msg, settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		except:send_mail("Reg - SMTP not working", "Someone tried to submit response!\nSMTP Not working fine\nKindly contact Admin", settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		messages.success(request,"Your response has been submitted successfully!")
		return redirect('dm')
	return render(request, "digital-marketing.html",locals())
def web(request):
	if request.method == "POST":
		sub = "New response has been submitted!"
		msg = """Name : {}\nMobile : {}\nEmail : {}\nWebsite URL : {}""".format(request.POST['name'],request.POST['phone'],request.POST['email'],request.POST['website'])
		# send_mail(sub, msg, settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		try:send_mail(sub, msg, settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		except:send_mail("Reg - SMTP not working", "Someone tried to submit response!\nSMTP Not working fine\nKindly contact Admin", settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		messages.success(request,"Your response has been submitted successfully!")
		return redirect('web')
	return render(request, "web-design.html",locals())
def smm(request):
	if request.method == "POST":
		sub = "New response has been submitted!"
		msg = """Name : {}\nMobile : {}\nEmail : {}\nWebsite URL : {}""".format(request.POST['name'],request.POST['phone'],request.POST['email'],request.POST['website'])
		# send_mail(sub, msg, settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		try:send_mail(sub, msg, settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		except:send_mail("Reg - SMTP not working", "Someone tried to submit response!\nSMTP Not working fine\nKindly contact Admin", settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		messages.success(request,"Your response has been submitted successfully!")
		return redirect('smm')
	return render(request, "social-media-marketing.html",locals())
def ppc(request):
	if request.method == "POST":
		sub = "New response has been submitted!"
		msg = """Name : {}\nMobile : {}\nEmail : {}\nWebsite URL : {}""".format(request.POST['name'],request.POST['phone'],request.POST['email'],request.POST['website'])
		# send_mail(sub, msg, settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		try:send_mail(sub, msg, settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		except:send_mail("Reg - SMTP not working", "Someone tried to submit response!\nSMTP Not working fine\nKindly contact Admin", settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		messages.success(request,"Your response has been submitted successfully!")
		return redirect('ppc')
	return render(request, "pay-per-click-marketing.html",locals())
def testi(request):
	if request.method == "POST":
		try:ch1 = request.POST['check1']
		except:ch1 = ""
		try:ch2 = request.POST['check2']
		except:ch2 = ""
		try:ch3 = request.POST['check3']
		except:ch3 = ""
		try:ch4 = request.POST['check4']
		except:ch4 = ""
		sub = "New response has been submitted!"
		msg = """Name : {}\nMobile : {}\nEmail : {}\nWebsite URL : {}\nMessgae : {}\nWhat they need : {},{},{},{}""".format(request.POST['name'],request.POST['phone'],request.POST['email'],request.POST['website'],request.POST['messagedetails'],ch1,ch2,ch3,ch4)
		# send_mail(sub, msg, settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		try:send_mail(sub, msg, settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		except:send_mail("Reg - SMTP not working", "Someone tried to submit response!\nSMTP Not working fine\nKindly contact Admin", settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		messages.success(request,"Your response has been submitted successfully!")
		return redirect('testi')
	return render(request, "testmonials.html",locals())
def contact(request):
	if request.method == "POST":
		try:ch1 = request.POST['check1']
		except:ch1 = ""
		try:ch2 = request.POST['check2']
		except:ch2 = ""
		try:ch3 = request.POST['check3']
		except:ch3 = ""
		try:ch4 = request.POST['check4']
		except:ch4 = ""
		sub = "New response has been submitted!"
		msg = """Name : {}\nMobile : {}\nEmail : {}\nWebsite URL : {}\nMessgae : {}\nWhat they need : {},{},{},{}""".format(request.POST['name'],request.POST['phone'],request.POST['email'],request.POST['website'],request.POST['messagedetails'],ch1,ch2,ch3,ch4)
		# send_mail(sub, msg, settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		try:send_mail(sub, msg, settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		except:send_mail("Reg - SMTP not working", "Someone tried to submit response!\nSMTP Not working fine\nKindly contact Admin", settings.EMAIL_HOST_USER, ["info@grownotch.com"])
		messages.success(request,"Your response has been submitted successfully!")
		return redirect('contact')
	return render(request, "contactus.html",locals())