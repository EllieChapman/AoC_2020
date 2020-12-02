#include <iostream>
#include <fstream>
#include <string>
#include <list>
using namespace std;

int my_func(string line) {
  int first_space = 0;

  for (int ii = 0; ii < line.size(); ii++) {
    if (line.substr(ii, 1) == " ") {
      first_space = ii;
      break;
    }
  }

  string bounds = line.substr(0, first_space);
  string letter = line.substr(first_space+1, 1);
  string password = line.substr(first_space+4, line.size());

  int colon_position = 0;
  for (int ii = 0; ii < bounds.size(); ii++) {
    if (bounds.substr(ii, 1) == "-") {
      colon_position = ii;
      break;
    }
  }
  string lo = (bounds.substr(0, colon_position));
  int lower = std::stoi (lo,nullptr,10);
  string up = (bounds.substr(colon_position+1, bounds.size()));
  int upper = std::stoi (up,nullptr,10);

  int no_correct = 0;
  if ( (letter == password.substr(lower-1, 1)) ^ (letter == password.substr(upper-1, 1)) ) {
    return 1;
  } else {
    return 0;
  }
}


int main()
{
 string line;

 list<string> lines;

 ifstream myfile ("day2_part1.txt");
 if (myfile.is_open())
 {
   while ( getline (myfile,line) )
   {
     lines.push_back(line);
   }
 }
 myfile.close();


 int no_correct = 0;
 for(auto it = lines.begin(); it != lines.end(); it++) {
   no_correct = no_correct + my_func(*it);
 }

 cout << no_correct << endl;

 return 0;
}
