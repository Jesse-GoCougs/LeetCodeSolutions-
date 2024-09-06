// Definition for singly-linked list.
 struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(head == nullptr || head->next == nullptr){
            return head;
        }
        ListNode * previous = head;
        ListNode * current = head->next;

        while(current){
            // duplicate found remove node
            if (previous->val == current->val){
                previous->next = current->next;
                current = previous->next;
            }else{
                previous= current;
                current = current->next;
            }
        }
        return head;
    }
};
