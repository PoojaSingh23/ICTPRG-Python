randomstring=input("Enter a random string")
if(len(randomstring)>7):
    mid=int(len(randomstring)/2)
    print(randomstring[mid-1]+randomstring[mid]+randomstring[mid+1])