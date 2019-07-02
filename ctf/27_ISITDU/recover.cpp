#include <iostream>
#include <vector>
#include <stack>
#include <unordered_map>
using namespace std;

// Recursive function to find preorder traversal of a binary tree
// from its inorder and postorder sequence.
void printPreorder(int start, int end,
				vector<int> const &postorder, int &pIndex,
				unordered_map<int,int> &map, stack<int> &stack)
{
	// base case
	if (start > end)
		return;
	
	// The next element in postorder sequence from the end will be the root node
	// of subtree formed by inorder[start, end]
	int value = postorder[pIndex--];

	// get the index of current node in inorder sequence to determine the
	// boundary of its left and right subtree
	int index = map[value];
cout << "haha" << endl;
	// recur for right subtree
	printPreorder(index + 1, end, postorder, pIndex, map, stack);

	// recur for left subtree
	printPreorder(start, index - 1, postorder, pIndex, map, stack);

	// push the value of current node into the stack
	stack.push(value);
}

// Find preorder traversal of a binary tree from its inorder and
// postorder sequence. This function assumes that the input is valid
// i.e. given inorder and postorder sequence forms a binary tree
void findPreorder(vector<int> const &inorder, vector<int> const &postorder)
{
	// map is used to efficiently find the index of any element in
	// given inorder sequence
	unordered_map<int,int> map;

	// fill the map
	for (int i = 0; i < inorder.size(); i++)
		map[inorder[i]] = i;

	// lastIndex stores the index of next unprocessed node from the end
	// of postorder sequence
	int lastIndex = inorder.size() - 1;

	// construct a stack to store the preorder sequence
	stack<int> stack;

	// fill the stack
	printPreorder(0, lastIndex, postorder, lastIndex, map, stack);

	// print stack
	cout << "Preorder Traversal is: ";
	while (!stack.empty()) {
		cout << stack.top() << ' ';
		stack.pop();
	}
}

// main function
int main()
{
	/* Consider below tree
              1
            /   \
           /     \
          2       3
         /       / \
        /       /   \
       4       5     6
              / \
             /   \
            7     8
	*/

	vector<int> inorder	= { 9, 11, 33, 35, 38, 40, 44, 48, 61, 85, 89, 101, 106, 110, 135, 150, 159, 180, 188, 200, 201, 214, 241, 253, 268, 269, 275, 278, 285, 301, 301, 327, 356, 358, 363, 381, 396, 399, 413, 428, 434, 445, 449, 462, 471, 476, 481, 492, 496, 497, 509, 520, 526, 534, 540, 589, 599, 613, 621, 621, 623, 628, 634, 650, 652, 653, 658, 665, 679, 691, 708, 711, 716, 722, 752, 756, 764, 771, 773, 786, 807, 808, 826, 827, 836, 842, 856, 867, 875, 877, 879, 889, 892, 922, 946, 951, 965, 980, 993, 996 };
	vector<int> postorder = { 35, 33, 44, 40, 38, 48, 11, 85, 89, 61, 110, 150, 159, 135, 188, 200, 180, 106, 101, 214, 268, 275, 269, 253, 241, 201, 9, 301, 301, 285, 327, 356, 363, 396, 413, 399, 445, 434, 462, 449, 428, 471, 481, 492, 496, 497, 476, 381, 358, 278, 534, 526, 520, 613, 599, 623, 621, 621, 589, 540, 628, 650, 653, 652, 665, 691, 679, 711, 756, 752, 722, 716, 807, 786, 773, 771, 826, 808, 827, 764, 856, 875, 867, 842, 836, 708, 879, 892, 889, 922, 877, 951, 946, 658, 980, 996, 993, 965, 634, 509};

	findPreorder(inorder, postorder);

	return 0;
}
