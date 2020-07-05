#pragma once
#include <iostream>
#include <functional>
#include <vector>
using namespace std;
template<typename T, typename Compare = T>
class MaxHeap {
	vector<T> arr;
	int Left(int i) { return i * 2 + 1; }
	int Right(int i) { return Left(i) + 1; }
	int Parent(int i) { return (i - 1) / 2; }
	function<Compare(T, T)> Key;
	void MaxHeapify(int i) {
		int l = Left(i);
		int r = Right(i);
		int largest;
		if (l < arr.size() && Key(arr[l], arr[i]))
			largest = l;
		else
			largest = i;
		if (r < arr.size() && Key(arr[r], arr[largest]))
			largest = r;
		if (largest != i) {
			swap(arr[i], arr[largest]);
			MaxHeapify(largest);
		}
	}
	T HeapMaximum() { return arr[0]; }
public:
	MaxHeap(function<Compare(T, T)>Key = [](T a, T b) {return a > b; }) : Key(Key) {}
	~MaxHeap() {}
	T HeapExtractMax() { // pop
		if (arr.size() < 1)
			return 0.f; // Manejar error	
		T max = arr[0];
		arr[0] = arr[arr.size() - 1];
		arr.pop_back();
		MaxHeapify(0);
		return max;
	}
	void HeapIncreaseKey(int i, T k) {
		if (k < arr[i])
			return;
		arr[i] = k;
		while (0 < i && Key(arr[i], arr[Parent(i)])) {
			swap(arr[i], arr[Parent(i)]);
			i = Parent(i);
		}
	}
	void MaxHeapInsert(T k) { // Push
		arr.push_back(-1e20);
		HeapIncreaseKey(arr.size() - 1, k);
	}
	unsigned int Size() { return arr.size(); }
};