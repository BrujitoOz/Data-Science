#include <iostream>
#include <fstream>
using namespace std;
struct Proceso { int id, bt, at, wt, ct; };
int main()
{
    // ifstream fin("in.txt");
    int cantidad = 5;
    Proceso* fcfs = new Proceso[cantidad];
    for (int i = 0; i < cantidad; i++)
    {
        cout << "Ingrese ID, BT, AT: ";
        cin >> fcfs[i].id >> fcfs[i].bt >> fcfs[i].at;
    }
    cout << "\nLos procesos ingresados son:" << endl;
    cout << "ID" << "\t" << "BT" << "\t" << "AT:" << endl;
    for (int i = 0; i < cantidad; i++)
    {
        cout << fcfs[i].id << "\t" << fcfs[i].bt << "\t" << fcfs[i].at << endl;
    }

    for (int i = 0; i < cantidad - 1; i++)
    {
        bool sorted = true;
        for (int j = 0; j < cantidad - i - 1; j++)
        {
            if (fcfs[j].at > fcfs[j + 1].at)
            {
                sorted = false;
                swap(fcfs[j], fcfs[j + 1]);
            }
        }
        if (sorted) break;
    }
    cout << "\nLos procesos ordenados por AT son:" << endl;
    cout << "ID" << "\t" << "BT" << "\t" << "AT:" << endl;
    for (int i = 0; i < cantidad; i++)
    {
        cout << fcfs[i].id << "\t" << fcfs[i].bt << "\t" << fcfs[i].at << endl;
    }
    
    int start, end;
    cout << "\nEl diagrama de Gaant es:" << endl;
    int* fp = new int[cantidad];
    for (int i = 0; i < cantidad; i++)
	{
		if (i==0) start = fcfs[0].at;
		else
			if (fcfs[i].at <= end)
				start = end;
			else
				start = fcfs[i].at;
		end = start + fcfs[i].bt;
        fp[i] = end;							
		cout << "[" << start << "-P" << fcfs[i].id << "-" << end << "]";			
	}

	float pCT = 0;
	for (int i = 0; i < cantidad; i++)
	{
        fcfs[i].ct = fp[i] - fcfs[i].at;
        pCT += fcfs[i].ct;
	}

	float pWT = 0;
	for (int i = 0; i < cantidad; i++)
	{
        fcfs[i].wt = fcfs[i].ct - fcfs[i].bt;
		pWT += fcfs[i].wt;
	}

    for (int i = 0; i < cantidad - 1; i++)
    {
        bool sorted = true;
        for (int j = 0; j < cantidad - i - 1; j++)
        {
            if (fcfs[j].id > fcfs[j + 1].id)
            {
                sorted = false;
                swap(fcfs[j], fcfs[j + 1]);
            }
        }
        if (sorted) break;
    }


    cout << "\nLos procesos ordenados por ID y sus WT y CT son:" << endl;
    cout << "ID" << "\t" << "WT" << "\t" << "CT:" << endl;
    for (int i = 0; i < cantidad; i++)
    {
        cout << fcfs[i].id << "\t" << fcfs[i].wt << "\t" << fcfs[i].ct << endl;
    }
	cout << "El AWT es: " << pWT / cantidad << endl;
	cout << "El ACT es: " << pCT / cantidad << endl;
    return 0;
}