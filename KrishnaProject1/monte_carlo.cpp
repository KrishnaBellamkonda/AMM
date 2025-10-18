#include <iostream>
#include <random>
#include <vector>
#include <fstream>

int main(){

	// Setup 
	//
	std::random_device rd{};
	std::seed_seq ss{rd(), rd(), rd(), rd(), rd(), rd(), rd(), rd()};
	std::mt19937 mt(ss);

	// Uniform Distribution
	int n = 100000; // Number of random numbers in the vectors
	double x_min = 0.0;
	double x_max = 1.0;
	std::uniform_real_distribution<double> rng(x_min, x_max);

	// Vectors to store the random numbers
	std::vector<double> x_coords(n, 0.0);
	std::vector<double> y_coords(n, 0.0);

	// Generatre random numbers using uniform distribution	
	std::ofstream file("points.csv"); 
	for (int i=0; i<n; i++){
		x_coords[i] = rng(mt);
		y_coords[i] = rng(mt);
		
		file << x_coords[i] << "," << y_coords[i] << "\n";
	}

	file.close();

return 0;
}
