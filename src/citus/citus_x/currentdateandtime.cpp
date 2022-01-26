// CPP program to print current date and time
// using chronos.
#include <chrono>
#include <ctime>
#include <iostream>
  
using namespace std;
  
int main()

{
    // Here system_clock is wall clock time from
    // the system-wide realtime clock
    auto timenow =
      chrono::system_clock::to_time_t(chrono::system_clock::now());
  
    cout << ctime(&timenow) << endl;
    return 0;
}
