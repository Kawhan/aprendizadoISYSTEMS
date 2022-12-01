#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;



int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */     
    int number_values;
    int sum = 0;
    vector<string> numbers;
    cin >> number_values;
    string values;
        
    for (int i = 0; i < number_values * 3; i ++) 
    {
        cin >> values;
        numbers.push_back(values);
        values = "";
    }
    
    for (int i = 0; i < numbers.size(); i++) {
        if (numbers[i] == "standard") {
            int num1 = stoi(numbers[i+1]);
            int num2 = stoi(numbers[i+2]);
            
            sum += (num1 * 50) + (num2 * 100);
        }
        if (numbers[i] == "apartment") {
            int num1 = stoi(numbers[i+1]);
            int num2 = stoi(numbers[i+2]);
            sum += (num1 * 50) + (num2 * 100) + 100;
        }
       
    }
    
    cout << sum << endl;
        
    return 0;
}
