    //traverse the tree inorderly, put the integers in a list, and check if it's sorted ascendingly
    //(with no repeating values, by definition of a Binary Search Tree)
    
    ArrayList<Integer> nums = new ArrayList<Integer>();

    boolean checkBST(Node root) {
        inorder(root);
        return isSorted(nums);                
    }

    void inorder(Node root){
        if(root.left != null) inorder(root.left);
        nums.add(root.data);
        if(root.right != null) inorder(root.right);
    }

    boolean isSorted(ArrayList<Integer> list){
        for(int i = 0; i < list.size()-1; i++){
            // >= because repeating values are not allowed in a BST
            if(list.get(i) >= list.get(i+1)) return false;
        }
        return true;
    }
