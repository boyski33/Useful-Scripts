static Node lca(Node root,int v1,int v2){
    if(v1 > root.data && v2 > root.data){
        root = lca(root.right, v1, v2); //have to assign the value to root, otherwise the value is getting lost
    }
    else if(v1 < root.data && v2 < root.data){
        root = lca(root.left, v1, v2);
    }
    
    return root;
    
}
