void decode(String S ,Node root){
    Node temp = root;
    for(int i = 0; i < S.length(); i++){
        if(S.charAt(i) == '0'){
            temp = temp.left;
        }
        else{
            temp = temp.right;
        }
        if(temp.left == null && temp.right == null){
            System.out.print(temp.data);
            temp = root;
        }
    }
    
}
