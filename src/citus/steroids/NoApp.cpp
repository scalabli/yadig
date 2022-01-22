#include <iostream>

using namespace std;

int main()
{
	clog << "Could not locate a Citus application.\n";
	clog <<	"You did not provide the `CITUS_APP` environment variable, and a `wsgi.pyʼ or `app.py`\n";
	clog << "module was not found in the current directory" << endl;
	return 0;
}
