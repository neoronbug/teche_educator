from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages 
from . import forms
from school_app.forms import UserProfileInfoForm, UserForm,Login_form_page
import os
import sqlite3

# Create your views here.
regisration_status = [False,True]
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_index(request):
	
	# registered = False

	# if request.method == 'POST':
	# 	print("form valid")
	# 	form_ = forms.test_form(request.POST, request.FILES)
	# 	# print(form_)
	# 	if form_.is_valid():
	# 		# handle_uploaded_file(request.FILES['fac1_prlf'])
	# 		print(form_.cleaned_data)
	# 		# user  = form_.save()
	# 		# user.save()

	# 		profile = form_.save(commit=False)
	# 		if 'pic' in request.FILES:
	# 			print('yes')
	# 		else:
	# 			print("file not here")
	# 		profile.save()

	# 		# profile = profile_form.save(commit = True)
	# 		# profile.user = user

	# 		# if 'profile_pic' in request.FILES:
	# 		# 	profile.profile_pic = request.FILES['media']

	# 		# profile.save()

	# 		registered = True
	# 	else:
	# 		print('form not valid')
	# else:
	# 	print('form not valid')
	# 	form_ = forms.test_form()
	dict_ = {'link':"/media/profile_pics/pic_.jpg"}
	return render(request, 'schools_website/index.html', {'dict_':dict_})






#  -------------- 







def display_page_view(request, value):
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	con = sqlite3.connect("{}/db.sqlite3".format(BASE_DIR))
	cur = con.cursor()
	cur.execute("SELECT * FROM school_app_user_profile_info WHERE name=?",(value,))
	row = cur.fetchone()
	con.close()
	dict_ = {
				"website_title":"{}".format(value.title()),
				"address":row[2],
				"name":row[3].title(),
				"phone_no":row[4],
				"website_link":row[5],
				"description":row[6],
				"fac1_dsg":row[7],
				"fac1_name":row[8].title(),
				"fac1_prlf":"/media/{}".format(row[9]),
				"fac1_qlf":row[10],
				"edu_awards":row[11],
				"edu_services":row[12],
				"fac2_dsg":row[13],
				"fac2_name":row[14].title(),
				"fac2_prlf":"/media/{}".format(row[15]),
				"fac2_qlf":row[16],
				"fac3_dsg":row[17],
				"fac3_name":row[18].title(),
				"fac3_prlf":"/media/{}".format(row[19]),
				"fac3_qlf":row[20],
				"fac4_dsg":row[21],
				"fac4_name":row[22].title(),
				"fac4_prlf":"/media/{}".format(row[23]),
				"fac4_qlf":row[24],
				"fac5_dsg":row[25],
				"fac5_name":row[26].title(),
				"fac5_prlf":"/media/{}".format(row[27]),
				"fac5_qlf":row[28],
				"fac6_dsg":row[29],
				"fac6_name":row[30].title(),
				"fac6_prlf":"/media/{}".format(row[31]),
				"fac6_qlf":row[32],
				"portfolio_site":row[33],
				"principal_image":"/media/{}".format(row[34]),
				"principal_message_details":row[40],
				"profile_pic":"/media/{}".format(row[35]),
				"sch_featured_img1":"/media/{}".format(row[36]),
				"sch_featured_img2":"/media/{}".format(row[37]),
				"sch_featured_img3":"/media/{}".format(row[38]),
				"school_logo":"/media/{}".format(row[39]),


				}
	return render(request, 'schools_website/display_page.html', context=dict_)


def front_page_view(request):
	dict_ = {"website_title":"{}".format("Website".title())}
	return render(request, 'schools_website/front_page.html', context=dict_)


def login(request):
	if regisration_status[0] is False:
		if request.method == 'POST':
			data = Login_form_page(data=request.POST)
			if data.is_valid():
				print(data.cleaned_data)
			regisration_status[0] = True
			response = HttpResponse("You are Logged in Now.......   Congrats")
			response.set_cookie(data.cleaned_data['user_name'], '1')
			return response
		else:
			login_form = Login_form_page()
			return render(request, 'schools_website/login.html', {'login_form':login_form,})
	else:
		dict_ = {"website_title":"{}".format("You are Logged In".title())}		
		return render(request, 'schools_website/display_page.html', context = dict_)



def register(request):

	registered = False#regisration_status[0]
	if 'zeeshan_login' in request.COOKIES:
		value = request.COOKIES['zeeshan_login']
		response = HttpResponse("You are Registered in.... No need to regster".title())
		response.delete_cookie('zeeshan_login')
		return response

	else:
		if request.method == 'POST':
			user_form = UserForm(data=request.POST)
			profile_form = UserProfileInfoForm(request.POST, request.FILES)

			if user_form.is_valid() and profile_form.is_valid():

				user  = user_form.save()
				user.set_password(user.password)
				user.save()

				profile = profile_form.save(commit = False)
				profile.user = user
				profile.save()
				regisration_status[0] = True
				registered = True
			else:
				print(user_form.errors, profile_form.errors)

		else:
			user_form = UserForm()
			profile_form = UserProfileInfoForm()

		return render(request, 'schools_website/register.html', {
																'user_form':user_form,
																'profile_form': profile_form,
																'registered':registered})

