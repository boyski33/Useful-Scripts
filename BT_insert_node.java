static Node Insert(Node root,int value){
    if(root == null){
        Node temp = new Node();
        temp.data = value;
        root = temp;
    }
    else if(value > root.data){
        if(root.right != null) Insert(root.right, value);
        else{
            Node temp = new Node();
            temp.data = value;
            root.right = temp;
        }
    }       
    else{
        if(root.left != null) Insert(root.left, value);
        else{
            Node temp = new Node();
            temp.data = value;
            root.left = temp;
        }
    }
    
    return root;
}
