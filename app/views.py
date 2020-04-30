"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from app.forms import Dostawcy
from app.forms import Odbiorcy
from app.forms import Koszty
from pulp import *


#from app.forms import Odbiorca1
#from app.forms import Odbiorca2
#from app.forms import Odbiorca3



def home(request):
    if request.method == 'POST':
        dostawcy = Dostawcy(request.POST)
        odbiorcy = Odbiorcy(request.POST)
        koszty = Koszty(request.POST)
        if dostawcy.is_valid() and odbiorcy.is_valid() and koszty.is_valid() :
            deliver1 = int(dostawcy.cleaned_data['deliver1'])
            deliver2 = int(dostawcy.cleaned_data['deliver2'])
            deliver3 = int(dostawcy.cleaned_data['deliver3'])

            receiver1 = int(odbiorcy.cleaned_data['receiver1'])
            receiver2 = int(odbiorcy.cleaned_data['receiver2'])
            receiver3 = int(odbiorcy.cleaned_data['receiver3'])

            d1o1 = int(koszty.cleaned_data['d1o1'])
            d1o2 = int(koszty.cleaned_data['d1o2'])
            d1o3 = int(koszty.cleaned_data['d1o3'])
            
            d2o1 = int(koszty.cleaned_data['d2o1'])
            d2o2 = int(koszty.cleaned_data['d2o2'])
            d2o3 = int(koszty.cleaned_data['d2o3'])
            
            d3o1 = int(koszty.cleaned_data['d3o1'])
            d3o2 = int(koszty.cleaned_data['d3o2'])
            d3o3 = int(koszty.cleaned_data['d3o3'])



            Warehouses = [0,1,2]
            supply = { 0: deliver1,
                      1: deliver2,
                      2: deliver3
                      }
            Distributors = [0, 1, 2]
            demand = { 0: receiver1,
                       1: receiver2,
                       2: receiver3
                      }
            #static variables for debugging purposes
            costs = [   #dsitributors
                #D  E  F
                #[3, 5, 7],#A  Warehouse
                #[12, 10, 9],#B  Warehouse
                #[13, 3, 9],#C  Warehouse

                  #D      E     F
                [d1o1, d1o2, d1o3],#A  Warehouse
                [d2o1, d2o2, d2o3],#B  Warehouse
                [d3o1, d3o2, d3o3],#C  Warehouse
        
            ]

            prob = LpProblem("Transportation Problem",LpMinimize)
            


            Routes = [(x,y) for x in Warehouses for y in Distributors]
            route_vars = LpVariable.dicts("Droga ",(Warehouses,Distributors),0,None,LpInteger)

            prob += lpSum([route_vars[x][y]*costs[x][y] for (x,y) in Routes]), "Sum of Transporting Costs"
            for x in Warehouses:
                prob += lpSum([route_vars[x][y] for y in Distributors]) <= supply[x], "Sum of Products out of Warehouse %s"%x
            for y in Distributors:
                prob += lpSum([route_vars[x][y] for x in Warehouses]) >= demand[y], "Sum of Products into Distributors %s"%y


            prob.writeLP("TransportationProblem.lp")
            prob.solve()
            print("Status:", LpStatus[prob.status])
            for v in prob.variables():
                v.name = v.name.replace("__0"," A  ")
                v.name = v.name.replace("___0","-D")
                print(v.name, "=", v.varValue)
            print("Total Cost of transportation = ", value(prob.objective))
            finalCost = value(prob.objective)

            listVariables = prob.variables()
            d1o1_result = (listVariables[0].varValue)
            d1o2_result = (listVariables[1].varValue)
            d1o3_result = (listVariables[2].varValue)
            
            d2o1_result = (listVariables[3].varValue)
            d2o2_result = (listVariables[4].varValue)
            d2o3_result = (listVariables[5].varValue)
            
            d3o1_result = (listVariables[6].varValue)
            d3o2_result = (listVariables[7].varValue)
            d3o3_result = (listVariables[8].varValue)
            
            return render(
                request,
                'app/solution.html',
                {
                    'dostawcy':Dostawcy,
                    'odbiorcy':Odbiorcy,
                    'koszty':Koszty,
                    'finalCost':finalCost,
                    'd1o1_result':d1o1_result,
                    'd1o2_result':d1o2_result,
                    'd1o3_result':d1o3_result,

                    'd2o1_result':d2o1_result,
                    'd2o2_result':d2o2_result,
                    'd2o3_result':d2o3_result,
                    
                    'd3o1_result':d3o1_result,
                    'd3o2_result':d3o2_result,
                    'd3o3_result':d3o3_result,


                    'title':'Strona główna',
                    'year':datetime.now().year,
                }   
            )

    else:
        dostawcy = Dostawcy()
        odbiorcy = Odbiorcy()
        koszty = Koszty()

        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/index.html',
            {
                'dostawcy':Dostawcy,
                'odbiorcy':Odbiorcy,
                'koszty':Koszty,

                'title':'Strona główna',
                'year':datetime.now().year,
            }   
        )



def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Kontakt',
            'message':'Kontakt ze mną',
            'year':datetime.now().year,
        }
    )

def teoria(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/teoria.html',
        {
            'title':'Teoria',
            'message':'',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )



