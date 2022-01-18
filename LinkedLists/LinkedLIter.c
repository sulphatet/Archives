#include <stdio.h>
#include <stdlib.h>


struct Node{
  int data;
  struct Node* next;
};

struct Node* head;

void Insert(int data, int n){
  struct Node* temp1 = malloc(sizeof(struct Node));
  temp1 -> data = data;
  temp1 -> next = NULL;
  if (n==1){
    temp1->next = head;
    head = temp1;
    return;
  }
  struct Node* temp2 = head;
  for(int i = 0; i <n-2;i++){
    temp2 = temp2 -> next;

  }
  temp1->next = temp2->next;
  temp2->next = temp1;

  
}

void Delete(int n){
  struct Node* temp1 = head;
  if(n==1){
    temp1 -> next = head;
    free(temp1);
    return;
  }
  for(int i =0; i<n-2;i++){
    temp1 = temp1->next; // n-1 Node
  }
  struct Node* temp2 = temp1 ->next; //neth Node
  temp1 -> next = temp2 -> next;
  free(temp2);
}


void Reverse(){
  struct Node *current,*prev,*next;
  current = head;
  prev = NULL;
  while(current != NULL){
    next = current -> next;
    current -> next = prev;
    prev = current;
    current = next;
  }
  head = prev;

}


void Print(){
  struct Node* temp = head;
  while (temp != NULL){
    printf("%d ",temp->data);
    temp = temp->next;
  }
  printf("\n");
}

//Recursively Reverse list.
void RReverse(struct Node* p){
  if (p-> next == NULL{
    head = p;
    return;
  }
  RReverse(p->next);
  struct Node* q = p->next;
  q->next = p;
  p->next = NULL;

}

int main(void) {
  head = NULL;
  Insert(2,1);
  Insert(1,2);
  Insert(3,3);
  Insert(5,4);
  Print();
  Insert(0,3);
  Print();
  //int d;
  //printf("Enter Position")
  //scanf("%d",&d)
  Delete(3);
  Print();
  Reverse();
  Print();
  RReverse(head);

}