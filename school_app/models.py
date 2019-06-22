from django.db import models
from django.contrib.auth.models import User



class test_model_form(models.Model):
	name = models.CharField(max_length=30)
	pic = models.FileField(upload_to='profile_pics/', blank=True)

class user_profile_info(models.Model):
	user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

	name = models.CharField(max_length=40)
	address = models.CharField(max_length=30,default='name')
	website = models.CharField(max_length=30,default='name')
	phone_no = models.IntegerField(blank=True,default='345353')
	description = models.CharField(blank=True, default='Your School Details',max_length=400)

	fac1_name = models.CharField(max_length=40,default='name')
	fac1_qlf = models.CharField(max_length=40,default='name')
	fac1_dsg = models.CharField(max_length=40,default='name')
	fac1_prlf = models.ImageField(upload_to= 'profile_pics/',blank=True)

	fac2_name = models.CharField(max_length=40,default='name')
	fac2_qlf = models.CharField(max_length=40,default='name')
	fac2_dsg = models.CharField(max_length=40,default='name')
	fac2_prlf = models.ImageField(upload_to= 'profile_pics/',blank=True)

	fac3_name = models.CharField(max_length=40,default='name')
	fac3_qlf = models.CharField(max_length=40,default='name')
	fac3_dsg = models.CharField(max_length=40,default='name')
	fac3_prlf = models.ImageField(upload_to= 'profile_pics/',blank=True)

	fac4_name = models.CharField(max_length=40,default='name')
	fac4_qlf = models.CharField(max_length=40,default='name')
	fac4_dsg = models.CharField(max_length=40,default='name')
	fac4_prlf = models.ImageField(upload_to= 'profile_pics/',blank=True)


	fac5_name = models.CharField(max_length=40,default='name')
	fac5_qlf = models.CharField(max_length=40,default='name')
	fac5_dsg = models.CharField(max_length=40,default='name')
	fac5_prlf = models.ImageField(upload_to= 'profile_pics/',blank=True)


	fac6_name = models.CharField(max_length=40,default='name')
	fac6_qlf = models.CharField(max_length=40,default='name')
	fac6_dsg = models.CharField(max_length=40,default='name')
	fac6_prlf = models.ImageField(upload_to= 'profile_pics/',blank=True)


	sch_featured_img1 = models.ImageField(upload_to= 'profile_pics/',blank=True)
	sch_featured_img2 = models.ImageField(upload_to= 'profile_pics/',blank=True)
	sch_featured_img3 = models.ImageField(upload_to= 'profile_pics/',blank=True)

	school_logo = models.ImageField(upload_to= 'profile_pics/',blank=True)
	principal_image = models.ImageField(upload_to= 'profile_pics/',blank=True)

	portfolio_site = models.URLField(blank=True)
	profile_pic = models.ImageField(upload_to= 'profile_pics/',blank=True)

	edu_services = models.CharField(max_length=40,default='name')
	edu_awards = models.CharField(max_length=40,default='name')
	principal_message = models.CharField(max_length=400,default='name')


	def __str__(self):
		return self.user.username


