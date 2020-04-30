\* Transportation_Problem *\
Minimize
Sum_of_Transporting_Costs: 6 Droga__0_0 + 10 Droga__0_1 + 10 Droga__0_2
 + 20 Droga__1_0 + 20 Droga__1_1 + 15 Droga__1_2 + 15 Droga__2_0
 + 10 Droga__2_1 + 15 Droga__2_2
Subject To
Sum_of_Products_into_Distributors_0: Droga__0_0 + Droga__1_0 + Droga__2_0
 >= 40
Sum_of_Products_into_Distributors_1: Droga__0_1 + Droga__1_1 + Droga__2_1
 >= 60
Sum_of_Products_into_Distributors_2: Droga__0_2 + Droga__1_2 + Droga__2_2
 >= 110
Sum_of_Products_out_of_Warehouse_0: Droga__0_0 + Droga__0_1 + Droga__0_2 <= 50
Sum_of_Products_out_of_Warehouse_1: Droga__1_0 + Droga__1_1 + Droga__1_2 <= 85
Sum_of_Products_out_of_Warehouse_2: Droga__2_0 + Droga__2_1 + Droga__2_2 <= 35
Bounds
0 <= Droga__0_0
0 <= Droga__0_1
0 <= Droga__0_2
0 <= Droga__1_0
0 <= Droga__1_1
0 <= Droga__1_2
0 <= Droga__2_0
0 <= Droga__2_1
0 <= Droga__2_2
Generals
Droga__0_0
Droga__0_1
Droga__0_2
Droga__1_0
Droga__1_1
Droga__1_2
Droga__2_0
Droga__2_1
Droga__2_2
End
