n=int(input())
l=list(map(int,input().split()))
li=[]
for i in l:
    if i not in li:
        li.append(i)
print(sum(li))
# #include<bits/stdc++.h>
# using namespace std;
# int main()
# {
#     int n;
#     cin>>n;
#     int arr[n];
#     int sum=0;
#     for(int i=0;i<n;i++)
#     {
#         cin>>arr[i];
#     }
#     for(int i=0;i<n;i++)
#     {
#         sum=sum+arr[i];
#     }
#     cout<<sum<<endl;
    
# }