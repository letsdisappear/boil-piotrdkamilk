from django import forms

class Dostawcy(forms.Form):
    deliver1 = forms.IntegerField(label='Dostawca 1', initial="50")
    deliver2 = forms.IntegerField(label='Dostawca 2 ', initial="70")
    deliver3 = forms.IntegerField(label='Dostawca 3 ', initial="30")

class Odbiorcy(forms.Form):
    receiver1 = forms.IntegerField(label='Odbiorca 1 ', initial="20")
    receiver2 = forms.IntegerField(label='Odbiorca 2 ', initial="40")
    receiver3 = forms.IntegerField(label='Odbiorca 3', initial="90")

class Koszty(forms.Form):
    d1o1 = forms.CharField(label='D1 > O1', initial="3")
    d1o2 = forms.IntegerField(label='D1 > O2', initial="5")
    d1o3 = forms.IntegerField(label='D1 > O3', initial="7")
    d2o1 = forms.IntegerField(label='D2 > O1', initial="12")
    d2o2 = forms.IntegerField(label='D2 > O2', initial="10")
    d2o3 = forms.IntegerField(label='D2 > O3', initial="9")
    d3o1 = forms.IntegerField(label='D3 > O1', initial="13")
    d3o2 = forms.IntegerField(label='D3 > O2', initial="3")
    d3o3 = forms.IntegerField(label='D3 > O3', initial="9")
    


 