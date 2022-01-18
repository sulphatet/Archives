#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h> 
#include <math.h>

//Macros give a range to values allowed in tree
#define MIN_VALUE 0
#define MAX_VALUE 50

//data structure
struct bstNode{
  int data;
  struct bstNode* left;
  struct bstNode* right;

};

//create a new node
struct bstNode* getNewNode(int data){
  struct bstNode* newNode = malloc(sizeof(struct bstNode));
  newNode -> data = data;
  newNode -> left = NULL;
  newNode ->right = NULL;
  return newNode;
}

//insert given value into the tree at correct position
struct bstNode* Insert(struct bstNode* root,int data){
  if (root == NULL){
    root = getNewNode(data);
    return root;
  }
  else if(data <= root ->data){
    root ->left = Insert(root->left,data);
  }
  else{
    root -> right = Insert(root->right , data);
  }
  return root;
}

//search for given value in tree
bool Search(struct bstNode* root,int data){
  if (root == NULL) {return false;}
  else if (root -> data == data) return true;
  else if (data <= root ->data) return Search(root ->left,data);
  else return Search(root -> right,data);

}

//return least (or leftmost) value from given branch root
int MinValue(struct bstNode* root){
  
  while (root -> left != NULL){
    root = root -> left;
  }
  return root -> data;
}

int rMinValue(struct bstNode* root){
  if (root == NULL){
    return -1;
  }else if(root -> left == NULL){
    return root -> data;
  }
  return rMinValue(root -> left);
}

int FindHeight(struct bstNode* root){
  if (root == NULL) return -1;
  return fmax(FindHeight(root -> left),FindHeight(root->right))+1;
}

//depth first search print root; travel left; travel right
void Preorder(struct bstNode* root){
  if (root == NULL) return;
  printf("%d ",root->data);
  Preorder(root->left);
  Preorder(root->right);
}

//
void Postorder(struct bstNode* root){
  if (root == NULL) return;
  Postorder(root->left);
  //printf here for inorder
  Postorder(root->right);
  printf("%d ",root->data);
}

//if this returns sorted => it is a isBST
void Inorder(struct bstNode* root){
  if (root == NULL) return;
  Inorder(root->left);
  printf("%d ",root->data);
  Inorder(root->right);
}

//helper func, returns true if given subtree has values ONLY < given int
bool IsSubtreeLesser(struct bstNode* root,int value){
  if(root == NULL) return true;
  if(root->data <= value && IsSubtreeLesser(root->left,value) && IsSubtreeLesser(root->right,value)){
    return true;
  }
  return false;
}

bool IsSubtreeGreater(struct bstNode* root, int value){
  if(root == NULL) return true;
  if(root->data > value && IsSubtreeGreater(root->left,value) && IsSubtreeGreater(root->right,value)){
    return true;
  }
  return false;
}

//Check if BST
bool isBST(struct bstNode* root){
  if (root == NULL) return true;
  if(IsSubtreeGreater(root->right,root->data) && IsSubtreeLesser(root->left,root->data) && isBST(root->left)&&isBST(root->right)){
    return true;
  }
  return false;
}

bool isBSTbetter(struct bstNode* root,int minRange, int maxRange){
  if (root == NULL) return true;
  if(root->data>minRange &&root->data < maxRange && isBSTbetter(root->left,minRange,root->data)&&isBSTbetter(root->right,root->data,maxRange)){
    return true;
  }
  return false;
}

bool BinarySearchTree(struct bstNode* root){
  return isBSTbetter(root, MIN_VALUE, MAX_VALUE); 
}


struct bstNode* FindMin(struct bstNode* root){
  struct bstNode* temp = root;
  while (temp && temp ->left != NULL){
    temp = temp ->left;
  }
  return temp;

}

//Delete form the BinarySearchTree
struct bstNode* Delete(struct bstNode* root, int data){
  if (root == NULL) return root;
  else if (root -> data > data) Delete(root -> left, data);
  else if (root ->data < data) Delete(root ->right,data);
  else{ //case 1: 0 childe
    if (root -> left == NULL && root -> right == NULL){
      free(root);
      root = NULL;
      //case 2: 1 childe
    }else if(root ->left == NULL){
      struct bstNode* temp = root;
      root = root -> right;
      free(temp);
     
    }else if(root ->right == NULL){
      struct bstNode* temp = root;
      root = root -> left;
      free(temp);
    }//case 3: 2 children
    else{
      struct bstNode* temp = FindMin(root->right);
      root -> data = temp->data;
      root ->right = Delete(root->right, temp->data);
    }
  }
  return root;
}

//////// INORDER TRAVERSAL PSUDOCODE
// struct bstNode* Find(struct bstNode* root, int data);

// struct bstNode* getSucc(struct bstNode* root,int data){
//   //Search the node
//   struct bstNode* current = Find(root,data);
//   if (current == NULL) return NULL;
//   if (current ->right != NULL){
//     struct bstNode* temp = current ->right;
//     while (temp ->left != NULL) temp = temp ->left;
//     return temp;
//   }else{
//     struct bstNode* succ = NULL;
//     struct bstNode* ance = root;
//     while(ance != current){
//       if (current->data < ance ->data){
//         succ = ance;
//         ance = ance ->right;
//       }else{
//         ance = ance ->left;
//       }
//       return succ;
//     }
//   }
// }
///////

int main(void){
  struct bstNode* root = NULL;
  root = Insert(root,15);
  root = Insert(root,10);
  root = Insert(root,20);
  root = Insert(root,25);
  root = Insert(root,8);
  root = Insert(root,12);
  //if(Search(root,12)) printf("Hello");
  int x = FindHeight(root);
  printf("%d",x);
  printf("\n");
  Preorder(root);
  printf("\n");
  Inorder(root);
  printf("\n");
  if(isBST(root)) printf("IS BST\n");
  if(BinarySearchTree(root)) printf("IS BST\n");
  
}



