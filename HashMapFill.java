Map<Integer, Integer> map = new HashMap<Integer, Integer>();
Integer freq; //not int becase of possible NULL value
for(int i=0; i < n; i++){
    c[i] = in.nextInt();
    freq = map.get(c[i]);
    socks.put(c[i], (freq == null ? 1 : freq+1)); //if no entries yet, set frequency to 1
}
