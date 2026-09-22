from django.shortcuts import render

from django.views.generic import View

from crm.models import Employee

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator

from json import loads
# Create your views here.
@method_decorator(csrf_exempt,name="dispatch")
class EmployeeListCreateView(View):

    def get(self,request):

        qs = Employee.objects.all().values()

        employee_list = list(qs)

        return JsonResponse(employee_list,safe=False)

    def post(self,request):

        form_data =loads(request.body)

        Employee.objects.create(
            name=form_data.get("name"),
            department=form_data.get("department"),
            salary=form_data.get("salary"),
            location = form_data.get("location"),
            email=form_data.get("email")
        )

        resonse_data={"message":"Employee created.."}

        return JsonResponse(resonse_data)

@method_decorator(csrf_exempt,name="dispatch")
class EmployeeRetrieveUpdateDeleteView(View):

    def get(self,request,pk=None):

        qs = Employee.objects.filter(id=pk).values()

        employee_detail = list(qs)

        return JsonResponse(employee_detail,safe=False)

    def delete(self,request,pk=None):

        Employee.objects.get(id=pk).delete()

        return JsonResponse({"message":"deleted.."})


    




