#include <iostream>
#include <functional>
using namespace std;
void ExchangeSort(float* arr, int n) {
	for (int i = 0; i < n - 1; i++) {
		for (int j = i + 1; j < n; j++) {
			if (arr[i] > arr[j])
				swap(arr[i], arr[j]);
		}
	}
}
void BubbleSort(float* arr, int n) {
	for (int i = 0; i < n - 1; i++) {
		bool sorted = true;
		for (int j = 0; j < n - i - 1; j++) {
			if (arr[j] > arr[j + 1]) {
				sorted = false;
				swap(arr[j], arr[j + 1]);
			}
		}
		if (sorted) break;
	}
}
void SelectionSort(float* arr, int n) {
	for (int i = 0; i < n - 1; ++i) {
		int p = i;
		for (int j = i + 1; j < n; ++j) 
			if (arr[j] < arr[p])
				p = j;
		if (p != i) {
			float temp = arr[p];
			arr[p] = arr[i];
			arr[i] = temp;
		}
	}
}
void InsertionSort(float* arr, int n) {
	for (int i = 1; i < n; i++) {
		int j = i;
		float e = arr[i];
		while (j > 0 && e < arr[j - 1]) 
			arr[j--] = arr[j - 1];
		if (i != j) 
			arr[j] = e;
	}
}
void ShellSort(float* arr, int n) {
	for (int gap = n / 2; gap > 0; gap /= 2) {
		for (int i = gap; i < n; i++) {
			int j = i;
			float e = arr[i];
			while (j >= gap && e < arr[j - 1]) {
				arr[j] = arr[j - gap];
				j -= gap;
			}
			if (i != j) 
				arr[j] = e;
		}
	}
}
void Merge(float* arr, int ini, int fin) {
	int len = (fin - ini) + 1;
	float* fifi = new float[len];
	int mid = (fin + ini) / 2;
	int i = ini;
	int j = mid + 1;
	for (int k = 0; i <= mid || j <= fin; k++) 
  		if (i > mid || j <= fin && arr[j] < arr[i])
			fifi[k] = arr[j++];
		else
			fifi[k] = arr[i++];
	for (int k = 0; k < len; k++) 
		arr[ini + k] = fifi[k];
	delete fifi;
}
void Sort(float* arr, int i, int f) {
	if (i < f) {
		int mid = (i + f) / 2;
		Sort(arr, i, mid);
		Sort(arr, mid + 1, f);
		Merge(arr, i, f);
	}
}
void MergeSort(float* arr, int n) {
	Sort(arr, 0, n - 1);
}
int Pivot(float* arr, int i, int f) {
	float pivot = arr[i];
	int left = i + 1;
	int right = f;
	while (left <= right) {
		if (arr[left] <= pivot)
			left++;
		else if (pivot <= arr[right])
			right--;
		else {
			float fifi = arr[right];
			arr[right] = arr[left];
			arr[left] = fifi;
			left++; right--;
		}
	}
	if (right != i) {
		float fifi2 = arr[right];
		arr[right] = arr[i];
		arr[i] = fifi2;
	}
	return right;
}
void Quick(float* arr, int i, int f) {
	if (i < f) {
		int p = Pivot(arr, i, f);
		Quick(arr, i, p - 1);
		Quick(arr, p + 1, f);
	}
}
void QuickSort(float* arr, int n) {
	Quick(arr, 0, n - 1);
}
void SiftDown(float* arr, int start, int end) {
	for (int root = start; root * 2 + 1 <= end;) {
		int child = root * 2 + 1;
		int parent = root;
		if (arr[parent] < arr[child]) {
			parent = child;
		}
		if (child + 1 <= end && arr[parent] < arr[child + 1]) {
			parent = child + 1;
		}
		if (parent == root) {
			return;
		}
		else {
			swap(arr[root], arr[parent]);
			root = parent;
		}
	}
}
void Heapify(float* arr, int end) {
	for (int i = (end - 1) / 2; i >= 0; i--) {
		SiftDown(arr, i, end);
	}
}
void HeapSort(float* arr, int n) {
	Heapify(arr, n);
	for (int end = n - 1; end > 0; end--) {
		swap(arr[end], arr[0]);
		SiftDown(arr, 0, end - 1);
	}
}
void ShowArr(float* arr) {
	for (int i = 0; i < 6; i++) {
		cout << arr[i] << " ";
	}
}
int main() {
	auto Compare = [](auto a, auto b) { return a > b; };  
	float* arr = new float[6]; 
	arr[0] = 700; arr[1] = 200; arr[2] = 900; arr[3] = 1000; arr[4] = 300; arr[5] = 600;
	
	ShowArr(arr);
	delete arr;
	system("pause");
	return 0;
}