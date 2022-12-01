#include<iostream>
#include<random>
#include<ctime>
using namespace std;
void QuickSort(int array[],int L,int R)
{
    if(L>R)
        return;
    int left = L,right = R;
    int pivot = array[left];
    while(left<right)
    {
        while(array[right]>=pivot&&right>left){
            right--;
        }
        if(left<right){
            array[left]=array[right];
        }
        while(array[left]<=pivot&&right>left){
            left++;
        }
        if(left<right){
            array[right]=array[left];
        }
        if(left==right){
            array[left] = pivot;
        }
        QuickSort(array,L,right-1);
        QuickSort(array,left+1,R);
    }
}
int main()
{
    int arry[10];
    default_random_engine e;
    uniform_int_distribution<int> u(1,100);
    e.seed(time(0));
    for(int i=0;i<10;i++){
        arry[i]=u(e);
    }
    cout<<"排序前：";
    for(int i=0;i<10;i++){
        cout<<arry[i]<<"\t";
    }
    cout<<endl<<"排序后：";
    QuickSort(arry,0,10);
    for(int i=0;i<10;i++){
        cout<<arry[i]<<"\t";
    }
    return 0;
}