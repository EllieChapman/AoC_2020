#include <iostream>
#include <fstream>
#include <string>
#include <list>
using namespace std;

   int main()
   {
     string line;
     list<int> nums;
     ifstream myfile ("day1_part1.txt");
     if (myfile.is_open())
     {
       while ( getline (myfile,line) )
       {
         long int num = std::stoi (line,nullptr,10);
         nums.push_back(num);
         // cout << num << '\n';
       }
       myfile.close();
     }
     else cout << "Unable to open file";

     for(auto it = nums.begin(); it != nums.end(); it++) {
       for(auto it2 = nums.begin(); it2 != nums.end(); it2++) {
         if((*it) + (*it2) == 2020) {
           cout << ((*it) * (*it2)) << endl;
         }
       }
     }

     return 0;
   }
