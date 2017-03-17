void decode(String s, Node root){
    for(int i = 0; i < s.length(); i++){
        if(s.charAt(i) == '0'){
            if(root.left != null){
                decode(s.substring(i+1), root.left);
            }
            else{
                System.out.print(root.data);
            }
        }
        else{
            if(root.right != null){
                decode(s.substring(i+1), root.right);
            }
            else{
                System.out.print(root.data);
            }
        }
    }
}
