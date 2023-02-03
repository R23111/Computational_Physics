#include <vector>
#include<iostream>
#include<fstream>
#include<string>
#include<math.h>

int main(){

    std::vector<double> f;

    
    int L = 50;
    double M1 = L/4;
    double M2 = 3*L/4;
    double dt = 0.25;
    double dx = 1.0;
    double D = 1.0;
    double k = D*dt/dx/dx;
    std::ofstream file;

for(float i = 0; i <= 1000; i+=dt){
    std::vector<double> g;
    if(i == 0){
        for (int i = 0; i < L; i++)
        {
            if(i >= M1 && i <= M2){
                f.push_back(1.0);
            }
            else{
                f.push_back(1.0);
            }
        }
    }else{
        g.push_back(0);
        for(int j = 1; j < (L-1); j++){
            g.push_back(f[j] + k*(f[j-1] - 2*f[j] + f[j+1]));
        }
        g.push_back(0);
        f = g;
    }

    if(i == 0 || i == 10 || i == 50 || i == 100 || i == 500 || i == 1000)
    {        
        std::string filename = "ftcs_t=";
        filename += std::to_string(i) + ".dat";
        file.open(filename);
        for(int j = 0; j < f.size(); j++){
            file << j << " " << f[j] << std::endl;
        }
        file.close();
    }
}  

    return 0;    
}