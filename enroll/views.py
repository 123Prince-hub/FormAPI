from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def home(request):
    # fm.order_fields(field_order=['email', 'name'])    # change order of form fields
    # fm = StudentRegistration(auto_id='some_%s')     #customize Id attribute in form
    # fm = StudentRegistration(auto_id=True)     #ID name as field name in form
    # fm = StudentRegistration(label_suffix="")     # remove or customize colun form field lable
    # fm = StudentRegistration(label_suffix="-")     # customize colun form field lable
    # fm = StudentRegistration(initial={'name':'Prince', 'email':'princekirad11@gmail.com'})     # default value in form field
    fm = StudentRegistration()
    return render(request, "index.html", {"form":fm})
