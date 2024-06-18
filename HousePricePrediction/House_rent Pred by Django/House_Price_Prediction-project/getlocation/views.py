
from django.shortcuts import render
from .models import Country, Divisions, District,Upazila

def dependantfield(request):
    countryid = request.GET.get('country', None)
    divisionid = request.GET.get('division', None)
    districtid=request.GET.get('district',None)
    upazilaid=request.GET.get('upazila',None)

    division = None
    district = None
    upazila=None
    if countryid:
        getcountry = Country.objects.get(id=countryid)
        division = Divisions.objects.filter(country=getcountry)
    if divisionid:
        getdivision = Divisions.objects.get(id=divisionid)
        district = District.objects.filter(division=getdivision)
        
    if districtid:
        getdistrict=District.objects.get(id=districtid)
        upazila=Upazila.objects.filter(district=getdistrict)
    country = Country.objects.all()
    return render(request, 'dependantfield.html', locals())
