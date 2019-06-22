from django import forms
from django.contrib.auth.models import User
from school_app.models import user_profile_info, test_model_form


class test_form(forms.ModelForm):
	class Meta():
		model = test_model_form
		fields = ('name','pic')



class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model = User
		fields = ('username','email','password')



class Login_form_page(forms.Form):
	user_name = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		fields = ('username','password')




class UserProfileInfoForm(forms.ModelForm):

	# name = forms.CharField(widget= forms.TextInput
 #                           (attrs={'placeholder':'Name'}))
	# # user_name = forms.CharField(widget= forms.TextInput
 # #                           (attrs={'placeholder':'User Name'}))
	# # email = forms.EmailField(widget= forms.TextInput
	# # 							 (attrs = {'placeholder':'yourschool@mail.com'}))
	# address = forms.CharField(widget= forms.TextInput
	# 							 (attrs = {'placeholder':'Your Address'}))
	# website = forms.CharField(widget= forms.TextInput
	# 							 (attrs = {'placeholder':'www.website.com'}))
	# phone_no = forms.IntegerField(widget= forms.TextInput
	# 							 (attrs = {'placeholder':'03XX XXXXXXXX'}))





	description = forms.CharField(widget = forms.Textarea 
							(attrs={'rows': 15,
							'cols' : 55,
							'placeholder':'Please Enter Some Details of your School / University.... '}))

	# fac1_name = forms.CharField(widget= forms.TextInput
 #                           (attrs={'placeholder':'Name'}))
	# fac1_qlf = forms.CharField(widget= forms.TextInput
 #                           (attrs={'placeholder':'Qualification '}))
	# fac1_dsg = forms.CharField(widget= forms.TextInput
 #                           (attrs={'placeholder':'Designation '}))
	# fac1_prlf = forms.ImageField()

	# fac2_name = forms.CharField(widget= forms.TextInput
 #                           (attrs={'placeholder':'Name'}))
	# fac2_qlf = forms.CharField(widget= forms.TextInput
 #                           (attrs={'placeholder':'Qualification '}))
	# fac2_dsg = forms.CharField(widget= forms.TextInput
 #                           (attrs={'placeholder':'Designation '}),blank=True)
	# fac2_prlf = forms.ImageField(upload_to= 'user_media_files',blank=True)

	# fac3_name = forms.CharField(widget= forms.TextInput
 #                           (attrs={'placeholder':'Name'}),blank=True)
	# fac3_qlf = forms.CharField(widget= forms.TextInput
 #                           (attrs={'placeholder':'Qualification '}),blank=True)
	# fac3_dsg = forms.CharField(widget= forms.TextInput
 #                           (attrs={'placeholder':'Designation '}),blank=True)
	# fac3_prlf = forms.ImageField(upload_to= 'user_media_files',blank=True)


	# fac4_name = forms.CharField(widget= forms.TextInput
 #                           (attrs={'placeholder':'Name'}),blank=True)
	# fac4_qlf = forms.CharField(widget= forms.TextInput
 #                           (attrs={'placeholder':'Qualification '}),blank=True)
	# fac4_dsg = forms.CharField(widget= forms.TextInput
 #                           (attrs={'placeholder':'Designation '}),blank=True)
	# fac4_prlf = forms.ImageField(upload_to= 'user_media_files',blank=True)


	# fac5_name = forms.CharField(widget= forms.TextInput
 #                           (attrs={'placeholder':'Name'}),blank=True)
	# fac5_qlf = forms.CharField(widget= forms.TextInput
 #                           (attrs={'placeholder':'Qualification '}),blank=True)
	# fac5_dsg = forms.CharField(widget= forms.TextInput
 #                           (attrs={'placeholder':'Designation '}),blank=True)
	# fac5_prlf = forms.ImageField(upload_to= 'user_media_files',blank=True)


	# fac6_name = forms.CharField(widget= forms.TextInput
 #                           (attrs={'placeholder':'Name'}),blank=True)
	# fac6_qlf = forms.CharField(widget= forms.TextInput
 #                           (attrs={'placeholder':'Qualification '}),blank=True)
	# fac6_dsg = forms.CharField(widget= forms.TextInput
 #                           (attrs={'placeholder':'Designation '}),blank=True)
	# fac6_prlf = forms.ImageField(upload_to= 'user_media_files',blank=True)

	# sch_featured_img1 = forms.ImageField(upload_to= 'user_media_files',blank=True)
	# sch_featured_img2 = forms.ImageField(upload_to= 'user_media_files',blank=True)
	# sch_featured_img3 = forms.ImageField(upload_to= 'user_media_files',blank=True)






	services_selction = (
    (1, ("Primary")),
    (2, ("Middle")),
    (3,	("High")),
    (4,	("FA/FSC")),
    (5,	("BS/BSC/MSC"))
	)
	edu_services = forms.ChoiceField(choices = services_selction, widget=forms.Select())

	awards = (
    (1, ("Top 10 position in Board")),
    (2, ("Top 20 position in Board")),
    (3,	("Top 30 position in Board")),
    (4,	("Ranked in top 10 Schools of Dist")),
    (5,	("Other"))
	)
	edu_awards = forms.ChoiceField(choices = awards, widget=forms.Select())

	# school_logo = forms.ImageField(upload_to= 'user_media_files',blank=True)
	# principal_image = forms.ImageField(upload_to= 'user_media_files',blank=True)

	principal_message = forms.CharField(widget = forms.Textarea 
							(attrs={'rows': 15,
							'cols' : 55,
							'placeholder':'Please Typle Principal Message Here ..... '}))	

	class Meta():
		model = user_profile_info
		fields = ('name','address','website','phone_no','description','fac1_name','fac1_qlf','fac1_dsg','phone_no','fac1_prlf','fac2_name','fac2_qlf','fac2_dsg','fac2_prlf','fac3_name','fac3_qlf','fac3_dsg','fac3_prlf','fac4_name','fac4_qlf','fac4_dsg','fac4_prlf','fac5_name','fac5_qlf','fac5_dsg','fac5_prlf','fac6_name','fac6_qlf','fac6_dsg','fac6_prlf','sch_featured_img1','sch_featured_img2','sch_featured_img3','school_logo','principal_image','principal_message','edu_services','edu_awards')
