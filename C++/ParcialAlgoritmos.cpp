#include <iostream>
#include <functional>
using namespace std;
template<typename T>
struct Node{
  T Elem;
  Node<T>* next;
  Node<T>* prev;
  Node(T Elem) : Elem(Elem), next(nullptr), prev(nullptr) {}
};
template<typename T>
class Iterator{
  Node<T>* nodeaux;
  int posi;
  public:
  Iterator(int posi, Node<T>* nodeaux) : posi(posi), nodeaux(nodeaux) {}
  void operator++ ()
  {
    posi++;
    nodeaux = nodeaux->next;
  }
  bool operator!= (Iterator x)
  {
    return posi != x.posi;
  }
  T operator* ()
  {
    return nodeaux->Elem;
  }
};
template<typename T>
class DobuleLinkedList{
  private:
  Node<T>* Head;
  Node<T>* Last;
  int size;
  public:
  DobuleLinkedList() : Head(nullptr), Last(nullptr), size(0) {}
  void AddFirst(T Elem)
  {
    Node<T>* newnode = new Node<T>(Elem);
    if (IsEmpty())
    {
      Last = newnode;
      Head = newnode;
      newnode->next = nullptr;
      newnode->prev = nullptr;
    }
    else
    {
      newnode->next = Head;
      newnode->prev = nullptr;
      Head = newnode;
      newnode->next->prev = newnode;
    }
    size++;
  }
  void AddPosi(T Elem, int posi)
  {
    
    if (posi == 0)
    {
        AddFirst(Elem);
    }
    else if(posi > 0 && posi < size)
    {
        Node<T>* newnode = new Node<T>(Elem);
        Node<T>* aux = Head;
        for (int i = 0; i < posi-1; i++)
        {
            aux = aux->next;
        }
        aux->next->prev = newnode;
        newnode->next = aux->next;
        aux->next = newnode;
        newnode->prev = aux;
        size++;
    }
    else if (posi == size)
    {
        AddLast(Elem);
    }
  }
  void AddLast(T Elem)
  {
    Node<T>* newnode = new Node<T>(Elem);
    if (Last->next == nullptr)
    {
      Last->next = newnode;
      newnode->prev = Last;
      Last = newnode;
      newnode->next = nullptr;
      size++;
    }
  }
  void RemovePos(int posi)
  {
    if (posi >= 0 && posi <= size) {
			Node<T>* NodeAux1 = GetNode(posi);
			Node<T>* NodeAux2 = GetNode(posi - 1);
			NodeAux2->next = NodeAux1->next;
			delete NodeAux1;
			size -= 1;
		}
  } 
  DobuleLinkedList<T>* Search(DobuleLinkedList<T>* ml, function<DobuleLinkedList<T>*(DobuleLinkedList<T>*)>lb)
  {
    return lb(ml);
  }
  int Size()
  {
    return size;
  }
  bool IsEmpty()
  {
    return size == 0;
  }
  Node<T>* GetNode(int pos) {
		int cont = 0;
		Node<T>* NodeAux = Head;
		while (cont<pos) {
			NodeAux = NodeAux->next;
			cont += 1;
		}
		return NodeAux;
	}
  Iterator<T> Begin() 
  {
		return Iterator<T>(0, Head);
	}
	Iterator<T> End() {
		return Iterator<T>(size, Last);
	}
};
class Weapon{
    public:
    string name;
    int mindmg;
    int maxdmg;
    int speed;
};
#include <cstdlib>
int main()
{
  // Test de la lista
  DobuleLinkedList<int>* test = new DobuleLinkedList<int>();
  test->AddFirst(1);
  test->AddFirst(2);
  test->AddFirst(3);
  test->AddFirst(4);
  test->AddPosi(6,2);
  test->AddLast(9);
  test->AddFirst(100);
  test->AddFirst(200);
  Iterator<int> aux = test->Begin();
  // imprime usando iterador
  for (Iterator<int> aux = test->Begin(); aux != test->End(); ++aux)
  {
      cout << *aux << " ";
  }
  test->RemovePos(3); // probar remover
  for (Iterator<int> aux = test->Begin(); aux != test->End(); ++aux)
  {
      cout << *aux << " ";
  }

  cout<<endl;
  // lambda
  auto lb = [](DobuleLinkedList<int>* ml)
  {
    DobuleLinkedList<int>* aux = new DobuleLinkedList<int>();
    for (Iterator<int> a = ml->Begin(); a != ml->End(); ++a)
    {
      if (*a < 30) aux->AddFirst(*a);
    }
    return aux;
  };
  DobuleLinkedList<int>* filtro = test->Search(test, lb);
  // imprime coincidencias
  for (Iterator<int> f = filtro->Begin(); f != filtro->End(); ++f)
  {
      cout << *f << " ";
  }
  
  DobuleLinkedList<Weapon*> armas;
  for (int i = 0; i < 10000;i++)
  {
      Weapon* w = new Weapon();
      w->name = "C";
      w->mindmg = rand() % 300;
      w->maxdmg = rand() % 700 + 301;
      w->speed = rand() % 10000;
      armas.AddFirst(w);
  }
  return 0;
}


typedef unsigned int uint;
template<typename T>
class ArrayQueue {
	T *arr;
	uint Size;
	uint N; // tamanio maximo del arr
	uint Front;
	uint Back;
public:
	ArrayQueue(uint N) {
		Front = 0;
		Back = -1;
		Size = 0;
		this->N = N;
		arr = new T[N];
	}
	~ArrayQueue() = default;
	void push(T Element) {
		if (empty()) {
			arr[0] = Element;
			Front = 0;
			Back = 0;
		}
		else {
			arr[++Back] = Element;
		}
		Size += 1;
	}
	void pop() {
		if (!empty()) {
			arr[Front] = nullptr;
      // arr[Front] = -1; reemplazar con dato basura
			Front += 1;
      if (Front == N) Front = 0;
      Size--;
		}
	}
	T front() {
		return arr[Front];
	}
	T back() {
		return arr[Back];
	}
	uint size() {
		return Size;
	}
	bool empty() {
		return Size == 0;
	}

};
template<typename T>
class Node {
	Node<T>* Next;
	T Element;
public:
	Node(T Element) {
		this->Element = Element;
	}
	~Node() = default;
	void SetNext(Node* Next) {
		this->Next = Next;
	}
	Node<T>* GetNext() {
		return Next;
	}
	void SetElement(T Element) {
		this->Element = Element;
	}
	T GetElement() {
		return Element;
	}
};



typedef unsigned int uint;
template<typename T>
class LinkedQueue {
	uint Size;
	Node<T>* Front;
	Node<T>* Back;
public:
	LinkedQueue() {
		Size = 0;
		Front = nullptr;
		Back = nullptr;
	}
	~LinkedQueue() = default;
	void push(T Element) {
		Node<T>* NodeNew = new Node<T>(Element);
		if (empty()) {
			Front = NodeNew;
			Back = NodeNew;
		}
		else {
			Back->SetNext(NodeNew);
			Back = NodeNew;
		}
		Size += 1;
	}
	void pop() {
		if (!empty()) {
			Node<T>* NodeAux = Front;
			Front = Front->GetNext();
			delete NodeAux;
			Size -= 1;
		}
	}
	Node<T>* front() {
		if (!empty())
			return Front;
	}
	Node<T>* back() {
		if (!empty())
			return Back;
	}
	uint size() {
		return Size;
	}
	bool empty() {
		return Size == 0;
	}
};
class Cliente{
  public:
  string name;
  int dni;
};
int main()
{
  Cliente* c1 = new Cliente();
  c1->name = "Rodrigo";
  c1->dni = 1233412;
  Cliente* c2 = new Cliente();
  c2->name = "Hernan";
  c2->dni = 948542;
  
  ArrayQueue<Cliente*> firstq = ArrayQueue<Cliente*>(5);
  firstq.push(c1);
  firstq.push(c2);
  // probando la cola estatica
  
  while (!firstq.empty())
  {
    cout << firstq.front()->dni << " ";
    firstq.pop();
  }
  // probando linked queue
  LinkedQueue<Cliente*>* secondq = new LinkedQueue<Cliente*>();
  secondq->push(c1);
  secondq->push(c2);
  return 0;
}