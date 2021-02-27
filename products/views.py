from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
from .models import Product
from .form import ProductForms
#
# def bad_view(request,*args,**kwargs):
#     print(request.GET)
#     my_request_data=dict(request.GET)
#     new_product=my_request_data.get('new_product')
#     print(my_request_data,new_product)
#     if new_product[0].lower() == "true":
#         print("New product")
#         Product.objects.create(title=my_request_data.get("title")[0],content=my_request_data.get('content')[0])
#     return HttpResponse("Dont do this")



def home_view(request):
    context={'name': 'Farrukh Khan'}
    return render(request,'home.html',context)

def search_view(request,*args,**kwargs):
    query=request.GET.get('q')
    qs=Product.objects.filter(title__icontains=query[0])
    context={'name': 'Farrukh Khan',"query":qs}
    print(query,qs)
    return render(request,'home.html',context)

# def product_create_view(request,*args,**kwargs):
#     print(request.POST)
#     print(dict(request.GET))
#     if request.method =="POST":
#         post_data=request.POST or None
#         if post_data != None:
#             my_form=ProductForms(request.POST)
#             if my_form.is_valid():
#                 print(my_form.changed_data.get("title"))
#                 title_form_input=my_form.changed_data.get("title")
#                 Product.objects.create(title=title_form_input)
#
#             print(post_data)
#
#     context = {}
#     return render(request,'form.html',{})

#@login_required
@staff_member_required
def product_create_view(request,*args,**kwargs):
    form = ProductForms(request.POST or None)
    print(form)
    if form.is_valid():

        obj=form.save(commit=False)
        #do some stuff
        obj.user=request.user
        obj.save()
        # print(request.POST)
        # print(form.cleaned_data)
        # data = form.cleaned_data
        # A=Product.objects.create(**data)
        form=ProductForms()
        # return HttpResponseRedirect('/')
        # return redirect('/')
        # print(A)
    return render(request,'form.html',{"form":form})

def product_details_view(request, id, *args, **kwargs, ):
    try:
        Obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404('Page Not Found')

    #return HttpResponse(f"Product Id {Obj.id}")

    return render(request,'products/details.html', {'objects': Obj})


def product_details_view_api(request,id):
    try:
        Obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return JsonResponse({'message': 'Page Not Found'})
    return JsonResponse({'id': Obj.id})


def product_list_view(request,*args,**kwargs):
    qs=Product.objects.all();
    context={
        'object_list': qs
    }
    return render(request, 'list.html', context)

