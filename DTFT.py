import math
select = input("Select your option\n1.Time -> Frequency\n2.Frequency -> Time\n") #Allows user to select conversion from one domain to other
a = int(input("Enter number of Input domain samples "))
Input_Domain_Samples = list()
Output_Domain_Samples = [0 for i in range(0, a)]
angle = math.degrees((2*math.pi)/a)
s_arr = [[complex(math.ceil(math.cos(angle)), -(math.ceil((math.sin(angle))))) for i in range(a)] for i in range(a)]
if select == 2:
    s_arr = [[complex.conjugate(complex(math.ceil(math.cos(angle)), -(math.ceil((math.sin(angle)))))) for i in range(a)] for i in range(a)]

print "Enter Input Domain Samples "
for i in range(0, a):
    Input_Domain_Samples.append(input())

for i in range(0, a):
    for j in range(0, a):
        s_arr[i][j] = s_arr[i][j]**(i*j)

for i in range(0, a):
    sums = complex(0, 0)
    for j in range(0, a):
        sums = sums + (s_arr[i][j]*Input_Domain_Samples[j])
    if select == 2:
        Output_Domain_Samples[i] = sums/a
    else:
        Output_Domain_Samples[i] = sums

print "Output Domain Samples ", Output_Domain_Samples


