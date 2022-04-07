#include <iostream>
class Geek{
	public:
		void myFunction(){
			std::cout << "Hello Geek!!!" << std::endl;
		}
};
int main()
{
	// Creating an object
	Geek t;

	// Calling function
	t.myFunction();

	return 0;
}
extern "C" {
	Geek* Geek_new(){ return new Geek(); }
	void Geek_myFunction(Geek* geek){ geek -> myFunction(); }
}
