#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Person
{
public:
    string name;
    unsigned int age;

public:
    virtual void getdata() = 0;
    virtual void putdata() = 0;
};

class Professor : public Person
{
public:
    static int id_number;
    int cur_id;
    int publications;

public:
    Professor()
    {
        id_number++;
        this->cur_id = id_number;
    }

    void getdata() override
    {
        cin >> name >> age >> publications;
    }
    void putdata() override
    {
        cout << name << ' ' << age << ' ' << publications << ' ' << cur_id << "\n";
    }
};

int Professor::id_number = 0;

class Student : public Person
{
public:
    int marks[6];
    int cur_id;
    static int id_number;
    int marks_sum = 0;

public:
    Student()
    {
        id_number++;
        this->cur_id = id_number;
    }
    void getdata() override
    {
        cin >> name >> age;
        for (int i = 0; i < 6; i++)
        {
            cin >> marks[i];
            marks_sum += marks[i];
        }
    }
    void putdata() override
    {
        cout << name << ' ' << age << ' ' << marks_sum << ' ' << cur_id << "\n";
    }
};

int Student::id_number = 0;

int main()
{

    int n, val;
    cin >> n; // The number of objects that is going to be created.
    Person *per[n];

    for (int i = 0; i < n; i++)
    {

        cin >> val;
        if (val == 1)
        {
            // If val is 1 current object is of type Professor
            per[i] = new Professor;
        }
        else
            per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.
    }

    for (int i = 0; i < n; i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;
}