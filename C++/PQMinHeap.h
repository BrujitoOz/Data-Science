#pragma once
#include <iostream>
#include <functional>
#include <vector>
using namespace std;
template<typename T, typename Compare = T>
class MinHeap {
	vector<T> arr;
	int Left(int i) { return i * 2 + 1; }
	int Right(int i) { return Left(i) + 1; }
	int Parent(int i) { return (i - 1) / 2; }
	function<Compare(T, T)>Key;
	void MinHeapify(int i) {
		int l = Left(i);
		int r = Right(i);
		int smallest;
		if (l < arr.size() && Key(arr[l], arr[i])) {
			smallest = l;
		}
		else {
			smallest = i;
		}
		if (r < arr.size() && Key(arr[r], arr[smallest])) {
			smallest = r;
		}
		if (i != smallest) {
			swap(arr[i], arr[smallest]);
			MinHeapify(smallest);
		}
	}
	T HeapMinimum() { return arr[0]; }
public:
	MinHeap(function<Compare(T, T)>Key = [](T a, T b) { return a < b; }) : Key(Key) {}
	~MinHeap() {}
	T HeapExtractMin() {
		if (arr.size() < 1) {
			return 0.f; // manejar error
		}
		T min = arr[0];
		arr[0] = arr[arr.size() - 1];
		arr.pop_back();
		MinHeapify(0);
		return min;
	}
	void IncreaseKey(int i, T k) {
		if (k < arr[i]) {
			return;
		}
		arr[i] = k;
		while (0 < arr.size() && Key(arr[i], arr[Parent(i)])) {
			swap(arr[i], arr[Parent(i)]);
			i = Parent(i);
		}
	}
	void MinHeapInsert(int k) {
		arr.push_back(-1e6);
		IncreaseKey(arr.size() - 1, k);
	}
	unsigned int Size() { return arr.size(); }
};