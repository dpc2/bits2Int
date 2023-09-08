#include <iostream>
#include <cmath>

using namespace std;

int main(){

	int signedTotal = 0;
	int unsignedTotal = 0;

	int input;
	cout << "How many bits? (q to exit)\n";
	cin >> input;
	if (input == 'q'){
		return 0;
	}

	for (int i = 0; i < input; i++){
		int x = pow(2, i);
		unsignedTotal += x;

		if (i < input - 1){
			signedTotal += x;
		}
	}


	cout << "The largest number you can represent with a signed "
	     << input << " bit integer is: " << signedTotal << endl;

	cout << "The largest number you can reprsent with an unsigned "
	    << input << " bit integer is: " << unsignedTotal << endl;
}
