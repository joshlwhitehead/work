#include <iostream>

using namespace std;

int main()
{
    double x = 9.1 , z=1.1 , aa = 4;
    // int y = 13;
    // y =y+15;
    // cout << x<<y<<z<<aa;

    // int josh = 45;
    // cout <<++++josh;
    // cin>>josh;   
    // cout<<josh;
    
    // cout<<(x<y);
    // string string1 = "stuff";
    // if (x<z) {
    //     cout << "'true'";
    // } else if (x>10) {
    //     cout << "more than 10";
    // };
    int b;
    cout<<"1 through 3";
    cin >>b;
    // cout <<b;
    switch(b) {
        case 1:
            cout<<"yes";
            break;
        case 2:
            cout<<"no";
            break;
        case 3:
            cout<< "maybe";
            break;
        default:
            cout<<"idk";
    }
    int stuff[3] = {1,2,3};
    cout<<stuff[0];
}
