#include <iostream>
const int NUME_PROC = 5;
using namespace std;

typedef struct proceso{
	int id;
	int bt;
	int at;		
};

void ingresar_procesos(proceso *proc)
{
	int i;
	// Ingresar procesos
	for (i=0; i<NUME_PROC; i++)
	{
		cout << "Ingrese ID, BT, AT: ";
		cin >> proc[i].id >> proc[i].bt >> proc[i].at;
	}
}

void mostrar_procesos(proceso *proc)
{
	int i;
	// Mostrar procesos
	cout << "ID" << "\t" << "BT" << "\t" << "AT" << endl;
	for (i=0; i<NUME_PROC; i++)	
		cout << proc[i].id << "\t" << proc[i].bt << "\t" << proc[i].at << endl;	
}

void ordenar_procesos(proceso *proc)
{
	int i, j;
	proceso proc_aux;
	// Ordenar procesos
	for (i=0; i<NUME_PROC-1; i++)				
	{
		for (j=i+1; j<NUME_PROC; j++)
		{
			if (proc[j].at < proc[i].at)
			{
				proc_aux = proc[i];
				proc[i] = proc[j];
				proc[j] = proc_aux;
			}
		}
	}	
}

void diagrama_gantt(proceso *proc)
{
	int i, msini, msfin;
	for (i=0; i<NUME_PROC; i++)
	{
		if (i==0)
			msini = proc[i].at;
		else
			if (proc[i].at<=msfin)
				msini = msfin;
			else
				msini = proc[i].at;
		msfin = msini + proc[i].bt;									
		cout << "[" << msini << "-P" << proc[i].id << "-" << msfin << "]";			
	}
}

int main()
{
	int i, j;
	proceso *proc, proc_aux;
	proc = new proceso[NUME_PROC];
	
	ingresar_procesos(proc);
	cout << "Los procesos ingresados son: " << endl;
	mostrar_procesos(proc);
	
	ordenar_procesos(proc);
	cout << "Los procesos ordenados son: " << endl;
	mostrar_procesos(proc);	
	
	diagrama_gantt(proc);
	
	return 0;
}