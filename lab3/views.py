from django.shortcuts import render

def fruit_student(request):
    fruitList = ["Apple", "Mango", "Orange"]
    StudentList = ["Ayush", "Pratap", "Singh"]
    return render(request, "list.html", {"fruitList": fruitList, "StudentList": StudentList})
