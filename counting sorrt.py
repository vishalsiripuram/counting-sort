import copy
def CountingSort(arr,size,rang):
    input_arr=arr.copy()
    print(input_arr)
    output_arr=arr

    count_arr=[]
    for i in range(0, rang):
        count_arr.append(0)
    for i in range(0, size):
        count_arr[input_arr[i]] += 1
    print(count_arr)
    for i in range(1, rang):
        count_arr[i] = count_arr[i] + count_arr[i - 1]
    print(count_arr)
    for i in range(0, size):

        output_arr[(count_arr[input_arr[i]] - 1)]=input_arr[i]
        count_arr[input_arr[i]]-=1
    print(output_arr)
rang=int(input("enter range of elements you awant to enter:"))
rang+=1
size=int(input('size'))
arr=[]
for i in range(0,size):
    val=int(input())
    if val>rang:
        print('please enter values in a range of {}'.format(rang))
        quit()
    else:
        arr.append(val)
print("elemetns you entered",arr)
CountingSort(arr,size,rang)


