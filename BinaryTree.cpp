
#include <iostream>

struct TreeNode
{
	int data;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int value) : data (value), left(nullptr), right(nullptr){}
};

class BinaryTree
{
private:
	TreeNode *root;

	void inorder(TreeNode *node){
		if(!node)
			return;
		inorder(node->left);
		std::cout << node->data << " ";
		inorder(node->right);
	}

public:
	BinaryTree() : root(nullptr){}
	void insert(int value)
	{
		if (!root){
			root = new TreeNode(value);
			return ;
		}
		TreeNode *temp = root;
		while (true){
			if (value < temp->data) {
			if (!temp->left) {
				temp->left = new TreeNode(value);
				break;
			}
			temp = temp->left;
			} else {
			if (!temp->right) {
				temp->right = new TreeNode(value);
				break;
			}
			temp = temp->right;
		}
	}
	}
	void inorderTraversal()
	{
		inorder(root);
		std::cout << std::endl;
	}
};


int main() {
    BinaryTree tree;

    // Insert some values
    tree.insert(10);
    tree.insert(5);
    tree.insert(15);
    tree.insert(3);
    tree.insert(7);
    tree.insert(13);
    tree.insert(17);

    // Print inorder traversal of the tree
    std::cout << "Inorder Traversal: ";
    tree.inorderTraversal();  // Should print: 3 5 7 10 13 15 17

    return 0;
}
