#include <stdio.h>
#include <stdlib.h>


struct Node{
  int data;
  struct Node* next;
};

struct Node* head;

void Insert(x){
  struct Node* temp = malloc(sizeof(struct Node)); //We are creating a pointer to a Node, called temp
  temp -> data = x;
  //temp -> next = NULL; 
  //if (head != NULL){
    //temp -> next = head;
  //}
  temp -> next = head;
  head = temp;
}

void Print(){
  struct Node* temp = head;
  while (temp != NULL){
    printf("%d ",temp->data);
    temp = temp->next;
  }
  printf("\n");
}

int main(void) {
  struct Node* A;
  A = NULL;
  head = NULL;
  int n,x;
  printf("Add to list");
  scanf("%d",&n);
  for (int i = 0; i < n; i++){
    printf("Insert num \n");
    scanf("%d",&x);
    Insert(x);
    Print();
  }

}