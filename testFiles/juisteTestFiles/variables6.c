#include <stdio.h>

// Should print the number 10 three times

int main(){
	int x = 10;
	int* xp = &x;
	int** xpp = &xp;
	int*** xppp = &xpp;
	printf("%d; %d; %d", x, *xp, **xpp, ***xppp);
	return 1;
}
