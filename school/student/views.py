from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from . models import Sign
from . models import Course_datas
from . models import Add_students
from django.http.response import HttpResponse

def student(request):
    return render(request,'dashboard.html')
def coureses(request):
        cr=Course_datas.objects.all()
        return render(request,'courses.html',{'cr':cr})
    # return render(request,'courses.html')

def view_student(request):
    cor=Course_datas.objects.all()
    st=Add_students.objects.all()
    return render(request,'viewstudents.html',{'cor':cor,'st':st})

def index(request):
    return render(request,'index.html')
def sign_up(request):
    return render(request,'sign-up.html')

def registration(request):
     if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        password= make_password(request.POST['password'])
        if Sign.objects.filter(email=email).exists():
            messages.error(request,"Email exist in database")
            return redirect('/')
        else:
            Sign.objects.create(name=name,email=email,password=password)
            return redirect('/index/')
        
def course_add(request):
     if request.method == 'POST':
        course=request.POST['course']
        fees=request.POST['fees']
        comment= request.POST['comment']
        Course_datas.objects.create(course=course,fees=fees,comment=comment)
        return redirect('/courses/')
    

def user_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        if Sign.objects.filter(email=email).exists():
            obj = Sign.objects.get(email=email)
            password = obj.password
            if check_password(password,password):
                return redirect("/dashboard/")
            else:
                return HttpResponse("password incorrect")
    else:
        return HttpResponse("Email is not rajister")


# def addstudent(request):
#     if request.method == "POST":
#         sname = request.POST["sname"]
#         semail = request.POST["semail"]
#         smobile = request.POST["smobile"]
#         sdegree = request.POST["sdegree"]
#         scollege = request.POST["scollege"]
#         saddress = request.POST["saddress"]
#         sid = request.POST["course"]
#         t = request.POST["total_amount"]
#         total_amount = int(t)
#         p = request.POST["paid_amount"]
#         paid_amount = int(p)
#         d = request.POST["due_amount"]
#         due_amount = int(d)
#         scourse = Course_datas.objects.get(id=sid)
#         if Add_students.objects.filter(semail=semail).exists():
#             messages.error(request,"Email is  already exists")
#         elif Add_students.objects.filter(smobile=smobile).exists:
#             messages.error(request,"mobile is  already exists")
#         else:
#             Add_students.objects.create(sname=sname,
#                                         semail=semail,
#                                         smobile=smobile,
#                                         sdegree=sdegree,
#                                         scollege=scollege,
#                                         saddress=saddress,
#                                         total_amount=total_amount,
#                                         paid_amount=paid_amount,
#                                         due_amount=due_amount,
#                                         scourse=scourse,
#                                         )
#             return redirect("/view_student/")
#     # return redirect("/view_student/")


def addstudent(request):
    t=Add_students()
    t.sname=request.POST['sname']
    t.semail = request.POST["semail"]
    t.smobile = request.POST["smobile"]
    t.sdegree = request.POST["sdegree"]
    t.semail = request.POST["semail"]
    t.scollege = request.POST["scollege"]
    t.saddress = request.POST["saddress"]
    t.saddress = request.POST["saddress"]
    k = request.POST["total_amount"]
    t.total_amount = int(k)
    p = request.POST["paid_amount"]
    t.paid_amount = int(p)
    d = request.POST["due_amount"]
    t.due_amount = int(d)
    tid=request.POST['course']
    t.scourse=Course_datas.objects.get(id=tid)
    t.save()
    return redirect('/view_student/')

def deletecourse(request):
     id=request.GET['id']
     Course_datas.objects.get(id=id).delete()
     return redirect('/courses/')

def updatecourse(request):
    if request.method == "POST":
        uid = request.POST["id"]
        course=request.POST['course']
        fees=request.POST['fees']
        comment= request.POST['comment']
        Course_datas.objects.filter(id=uid).update(course=course,fees=fees,comment=comment)
        return redirect('/courses/')

def update(request, uid):
    user = Course_datas.objects.get(id=uid)
    return render(request, "update.html", {"user": user})

  
        
        
        
        
        
        

    
            
    
        
    
        
