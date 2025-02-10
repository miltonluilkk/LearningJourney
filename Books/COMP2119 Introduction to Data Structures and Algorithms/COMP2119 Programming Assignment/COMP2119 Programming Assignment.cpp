//COMP2119A Introduction to Data Structures and Algorithms
//Programming Assignment
//Lau Hei Yeung
//3035108203
#include<iostream>
#include<string>
#include<fstream>
using namespace std;

//structure of data in a node
struct data{
	int key;
	string s;
};

//structure of node in a tree
struct Node{
	Node* left;
	Node* right;
	Node* parent;
	int balanceFactor; //height difference
	data content; //data of the node
};

//class declaration of the AVL tree
class Tree{
	public:
		Node* root;
		Tree(){root=NULL;} //constructor
		void inorder(Node* t);
		void insert(data d);
		void Search(int k);
		void Delete(int k);
		void leftRotate(Node* a);
		void rightRotate(Node* a);
		void deleteLeave(Node* n);
		Node* successor(Node* n);
		Node* locate(int k);
		void deleteNode(Node* n);
};

//Print the tree in-order
//Traverse the left sub-tree, root, right sub-tree
//Print the output to ouput.txt
void Tree:: inorder(Node* t){
	ofstream out;
	out.open("output.txt",ios::app);
	if (root == NULL) out<<-1<<endl;
	else{
		if(t != NULL){
			inorder(t->left);
			out << t->content.key << "," << t->content.s <<endl;
			out.close();
			inorder( t->right );
		}	
	}
}

//left rotation
void Tree:: leftRotate(Node* a){

	Node* c = a->right;

	a->right = c->left;
	c->left = a;

	if(a == root){
		c->parent = NULL;
		root = c;
	}
	else{
		c->parent = a->parent;
		if(a == a->parent->left)
			a->parent->left = c;
		else
			a->parent->right = c;
	}

	a->parent = c;
}

//right rotation
void Tree:: rightRotate(Node* a){

	Node* b=a->left;

	a->left=b->right;
	b->right=a;

	if(a==root){
		b->parent=NULL;
		root=b;
	}
	else{
		b->parent=a->parent;
		if(a==a->parent->left)
			a->parent->left=b;
		else
			a->parent->right=b;
	}

	a->parent=b;
}

//insert a node to the tree
void Tree:: insert(data d){
	
	Node* n=new Node;
	n->left=n->right=n->parent=NULL;
	n->content= d;
	n->balanceFactor=0;

	if(root==NULL){
		root=n;
	}

	else{
		Node* t=root;
		Node* y;
		
		while(t!=NULL){
			y=t;
			if(d.key<t->content.key)
				t=t->left;
			else 
				t=t->right;
		}
		
				n->parent=y;
		if(d.key<y->content.key)
			y->left=n;
		else
			y->right=n;
		
		t=n;
		Node* subtree=NULL;
		while(y!=NULL){
			if(t==y->left){
				y->balanceFactor++;
				
				if(y->balanceFactor==0) break;
				if(y->balanceFactor>1){
					
					if(subtree==t->left){
						rightRotate(y);
						y->balanceFactor=0;
						t->balanceFactor=0;
					}
					else{
						leftRotate(t);
						rightRotate(y);
						if(subtree->balanceFactor==1){
							t->balanceFactor=0;
							y->balanceFactor=-1;
						}
						else if(subtree->balanceFactor==0){
							t->balanceFactor=0;
							y->balanceFactor=0;
						}
						else{
							t->balanceFactor=1;
							y->balanceFactor=0;
						}
						subtree->balanceFactor=0;
					}
					break;
				}
			}
			else{
				y->balanceFactor--;
				if(y->balanceFactor==0) break;
				if(y->balanceFactor<-1){
					if(subtree==t->right){
						leftRotate(y);
						y->balanceFactor=0;
						t->balanceFactor=0;
					}
					else{
						rightRotate(t);
						leftRotate(y);
						if(subtree->balanceFactor==1){
							t->balanceFactor=-1;
							y->balanceFactor=0;
						}
						else if(subtree->balanceFactor==0){
							t->balanceFactor=0;
							y->balanceFactor=0;
						}
						else{
							t->balanceFactor=0;
							y->balanceFactor=1;
						}
						subtree->balanceFactor=0;
					}
					break;
				}
			}
			subtree=t;
			t=y;
			y=y->parent;
		}
	}
}

void Tree:: deleteLeave(Node* n){

	if(n==root){
		if(n->left==NULL && n->right==NULL){
			root=NULL;
			delete n;
		}
		else{
			if(n->left==NULL){
				n->right->parent=NULL;
				root=n->right;
				delete n;
			}
			else{
				n->left->parent=NULL;
				root=n->left;
				delete n;
			}
		}
		return;
	}

	Node* t=n;
	Node* y=n->parent;

	while(y!=NULL){
		if(t==y->left){
			y->balanceFactor--;
			
			if(y->balanceFactor==-1){
				deleteNode(n);
				return;
			}
			
			if(y->balanceFactor<-1){
				Node* a=y->right;
				if(a->balanceFactor==0){
					leftRotate(y);
					y->balanceFactor=-1;
					a->balanceFactor=1;
				}
				else if(a->balanceFactor==-1){
					leftRotate(y);
					y->balanceFactor=0;
					a->balanceFactor=0;
				}
				else{
					Node* b=a->left;
					rightRotate(a);
					leftRotate(y);
					if(b->balanceFactor==0){
						a->balanceFactor=0;
						y->balanceFactor=0;
					}
					else if(b->balanceFactor==1){
						a->balanceFactor=-1;
						y->balanceFactor=0;
					}
					else{
						a->balanceFactor=0;
						y->balanceFactor=1;
					}
					b->balanceFactor=0;
				}

				deleteNode(n);
				return;
			}
		}

		else{
			y->balanceFactor++;

			if(y->balanceFactor==1){
				deleteNode(n);
				return;
			}

			if(y->balanceFactor>1){
				Node* a=y->left;
				if(a->balanceFactor==0){
					rightRotate(y);
					a->balanceFactor=-1;
					y->balanceFactor=1;
				}
				else if(a->balanceFactor==1){
					rightRotate(y);
					a->balanceFactor=0;
					y->balanceFactor=0;
				}
				else{
					Node* b=a->right;
					leftRotate(a);
					rightRotate(y);
					if(b->balanceFactor==0){
						a->balanceFactor=0;
						y->balanceFactor=0;
					}
					else if(b->balanceFactor==1){
						a->balanceFactor=0;
						y->balanceFactor=-1;
					}
					else{
						a->balanceFactor=1;
						y->balanceFactor=0;
					}
					b->balanceFactor=0;
				}
				deleteNode(n);
				return;
			}
		}
		t=y;
		y=y->parent;
	}
	
	deleteNode(n);
	return;
}

Node* Tree:: successor(Node* n){

	if(root==NULL || n->right==NULL)
		return NULL;

	else{

		Node* y=n->right;
		Node* t=y->left;
		while(t!=NULL){
			y=t;
			t=t->left;
		}

		return y;
	}
}

Node* Tree:: locate(int k){

	if(root==NULL)
		return NULL;

	Node* y=root;

	while(y!=NULL && y->content.key!=k){
		if(y->content.key<k)
			y=y->right;
		else
			y=y->left;
	}

	return y;
}

void Tree:: Search(int k){
	ofstream fout;
	fout.open("output.txt",ios::app);
	Node* y=locate(k);
	if(y!=NULL)
		fout<<y->content.key<<','<<y->content.s<<endl;
	fout.close();
}

void Tree:: Delete(int k){

	Node* y=locate(k);

	if(y==NULL) return;

	if(y->left!=NULL && y->right!=NULL){//y has two child
		Node* t=successor(y);
		y->content.key=t->content.key;
		y->content.s=t->content.s;
		deleteLeave(t);
	}
	else
		deleteLeave(y);
}

void Tree:: deleteNode(Node* n){
	if(n->left==NULL && n->right==NULL){//n has no child
		if(n->content.key<n->parent->content.key){
			n->parent->left=NULL;
			delete n;
		}
		else{
			n->parent->right=NULL;
			delete n;
		}
	}
	else{//n has one child
		if(n->left==NULL){
			if(n->content.key<n->parent->content.key){
				n->parent->left=n->right;
				n->right->parent=n->parent;
				delete n;
			}
			else{
				n->parent->right=n->right;
				n->right->parent=n->parent;
				delete n;
			}
		}
		else{
			if(n->content.key<n->parent->content.key){
				n->parent->left=n->left;
				n->left->parent=n->parent;
				delete n;
			}
			else{
				n->parent->right=n->left;
				n->left->parent=n->parent;
				delete n;
			}
		}
	}
}

int main(){

	ifstream in;
	in.open("input.txt");
	Tree t;
	int code;

	while(in>>code){
		if(code==0)
			t.inorder(t.root);
		else if(code==1){
			data temp;
			in>>temp.key>>temp.s;
			t.insert(temp);
		}
		else if(code==2){
			int k;
			in>>k;
			t.Delete(k);
		}
		else if(code==3){
			int k;
			in>>k;
			t.Search(k);
		}
	}

	in.close();
	
	return 0;
}

