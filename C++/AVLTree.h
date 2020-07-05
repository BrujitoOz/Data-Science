#pragma once
#include <functional>
#define max(a,b) (a > b ? a : b)  
using namespace std;
typedef unsigned int uint;
template<typename T>
struct Node {
	T Elem;
	int h;
	int n;
	Node<T>* left;
	Node<T>* right;
	Node(T Elem) : Elem(Elem), left(nullptr), right(nullptr), h(0), n(1) {}
};
template<typename T, typename Comparable = T, T NONE = 0>
class AVLTree {
	Node<T>* root;
	function<Comparable(T)> Key;
	void Destroy(Node<T>* node) {
		if (node != nullptr) {
			Destroy(node->left);
			Destroy(node->right);
			delete node;
		}
	}
	Node<T>* Add(Node<T>* node, T Elem) {
		if (node == nullptr) {
			node = new Node<T>(Elem);
		}
		else {
			if (Key(Elem) < Key(node->Elem)) {
				node->left = Add(node->left, Elem);
			}
			else {
				node->right = Add(node->right, Elem);
			}
			node = Balance(node);
		}
		return node;
	}
	T Find(Node<T>* node, Comparable val) {
		if (node == nullptr) {
			return NONE;
		}
		else if (val == Key(node->Elem)) {
			return node->Elem;
		}
		else if (val < Key(node->Elem)) {
			return Find(node->left, val);
		}
		else {
			return Find(node->right, val);
		}
	}
	void Preorder(Node<T>* node, function<void(T)> Prnt) {
		if (node != nullptr) {
			Prnt(node->Elem);
			Preorder(node->left, Prnt);
			Preorder(node->right, Prnt);
		}
	}
	void Postorder(Node<T>* node, function<void(T)> Prnt) {
		if (node != nullptr) {
			Postorder(node->left, Prnt);
			Postorder(node->right, Prnt);
			Prnt(node->Elem);
		}
	}
	void Inorder(Node<T>* node, function<void(T)> Prnt) {
		if (node != nullptr) {
			Inorder(node->left, Prnt);
			Prnt(node->Elem);
			Inorder(node->right, Prnt);
		}
	}
	int Height(Node<T>* node) { return node == nullptr ? -1 : node->h; }
	int Lenght(Node<T>* node) { return node == nullptr ? 0 : node->n; }
	void UpdateHeight(Node<T>* node) {
		node->h = 1 + max(Height(node->left), Height(node->right));
		node->n = 1 + Lenght(node->left) + Lenght(node->right);
	}
	Node<T>* RotLeft(Node<T>* node) {
		Node<T>* NodeAux = node->right;
		node->right = NodeAux->left;
		NodeAux->left = node;
		UpdateHeight(NodeAux->left);
		UpdateHeight(NodeAux);
		return NodeAux;
	}
	Node<T>* RotRight(Node<T>* node) {
		Node<T>* NodeAux = node->left;
		node->left = NodeAux->right;
		NodeAux->right = node;
		UpdateHeight(NodeAux->right);
		UpdateHeight(NodeAux);
		return NodeAux;
	}
	Node<T>* Balance(Node<T>* node) {
		int hl = Height(node->left);
		int hr = Height(node->right);
		if (hl - hr > 1) {
			if (Height(node->left->right) > Height(node->left->left)) {
				node->left = RotLeft(node->left);
			}
			node = RotRight(node);
		}
		else if (hl - hr < -1) {
			if (Height(node->right->left) > Height(node->right->right)) {
				node->right = RotRight(node->right);
			}
			node = RotLeft(node);
		}
		else {
			UpdateHeight(node);
		}
		return node;
	}
public:
	AVLTree(function<Comparable(T)> Key = [](T a) {return a; }) : root(nullptr), Key(Key) {}
	~AVLTree() { Destroy(root); }
	void Add(T Elem) { root = Add(root, Elem); }
	T Find(Comparable val) { return Find(root, val);}
	bool Remove(Comparable val) {
		Node<T>* NodeAux = root;
		Node<T>* Parent;
		bool Left;
		while (NodeAux != nullptr) {
			if (val == Key(NodeAux->Elem)) {
				break;
			}
			Parent = NodeAux;
			if (val < Key(NodeAux->Elem)) {
				Left = true;
				NodeAux = NodeAux->left;
			}
			else {
				Left = false;
				NodeAux = NodeAux->right;
			}
		}
		if (NodeAux == nullptr) {
			return false;
		}
		if (NodeAux->left == nullptr) { 
			if (NodeAux == root) {
				root = NodeAux->right;
			} 
			else if (Left) {
				Parent->left = NodeAux->right;
			} 
			else {
				Parent->right = NodeAux->right;
			}
			delete NodeAux;
		}
		else {
			Node<T>* NodeAux2 = NodeAux->left; 
			while (NodeAux2->right != nullptr) {
				Parent = NodeAux2;
				NodeAux2 = NodeAux2->right;
			}
			if (NodeAux2 == NodeAux2->left) {
				NodeAux->left = NodeAux2->left;
			}
			else {
				Parent->right = NodeAux2->left;
			}
			NodeAux->Elem = NodeAux2->Elem;
			delete NodeAux2;
		}
		return true;
	}
	void Preorder(function<void(T)> proc) { Preorder(root, proc); }
	void Postorder(function<void(T)> proc) { Postorder(root, proc); }
	void Inorder(function<void(T)> proc) { Inorder(root, proc); }
	uint Size() { return Lenght(root); }
	int Height() { return Height(root); }
};