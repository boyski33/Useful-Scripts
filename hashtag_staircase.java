    static void StairCase(int n) {
        StringBuilder sb = new StringBuilder();
        for(int i = n; i > 0; i--){
            for(int j = 0; j < (i-1); j++){
                sb.append(" ");
            }
            for(int j = 0; j < (n-(i-1)); j++){
                sb.append("#");
            }
            sb.append("\n");
        }
        
        System.out.print(sb);

    }


/*
    #
   ##
  ###
 ####
#####
*/
