#include <stdio.h>

#define LEN 1000

FILE *file;

int main(void)
{
    fflush(file);
    float X[LEN], Y[LEN];

    file = fopen("dados.dat", "w+");


    float alpha = 0.1, L0 = 1.0, T0 = 10.0, Tf = 50.0, dt = (Tf - T0)/LEN;
    float L = L0;

    for(float t = T0; t < Tf; t += dt){
        fprintf(file, "%f %f\n", t, L);
        L += L * alpha * dt;
    }
    fclose(file);

    file = fopen("dados.dat", "r");

    for (int i = 0; i < LEN; i++)
    {
        fscanf(file, "%f %f", &X[i], &Y[i]);
    }
    fclose(file);


    //gnuplot args

	FILE *gnuplotPipe = popen ("gnuplot -persistent", "w");

	fprintf(gnuplotPipe,"reset\n");

	fprintf(gnuplotPipe,"set title \"%s\t L0=%.1f, alpha=%.1f, t0=%.1f, tf=%.1f, dt=%.2f\" \n","Dilatacao termica",L0, alpha, T0, Tf, dt);             //set title
	fprintf(gnuplotPipe,"set xlabel \" tempo\"\n set ylabel \"Dilatacao\"\n");    //set labels

	fprintf(gnuplotPipe,"plot '-' w lp pt 7  t \"\"\n");
	for(int i=0; i<LEN; ++i)
		fprintf(gnuplotPipe, "%lf %lf\n", X[i], Y[i]);
	fprintf(gnuplotPipe, "e\n");
	fclose(gnuplotPipe);

	return 0;
}