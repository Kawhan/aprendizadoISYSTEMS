#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;



int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */     
    vector<int> numbers;
    int len;
    int number;
    cin >> len;
    for (int i = 0; i < len; i++) {
        cin >> number;
        numbers.insert(numbers.begin(), number);
    }

    int first_number = numbers[0];
    bool nao_passou = true;

    for (int number : numbers) {
        if (number == first_number && nao_passou) {
            cout << number;
            nao_passou = false;
        }
        else {
            cout << " " <<number;
        }
    }
    
    return 0;
}