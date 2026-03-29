class MinStack {
    public LinkedList<Pair> liste;
    public MinStack() {
        this.liste= new LinkedList<Pair>() ;
    }
    
    public void push(int val) {
        if( this.liste.size()==0){
            this.liste.push(new Pair(val,val));
            return;
        }
        if (this.liste.getFirst().get_b()>val){
            this.liste.push(new Pair(val,val));
            return;
        }
        this.liste.push(new Pair(val,this.liste.getFirst().get_b()));
    }
    
    public void pop() {
       this.liste.pop();
    }
    
    public int top() {
        Pair e=this.liste.pop();
        this.liste.push(e);
        return e.get_a();
    }
    
    public int getMin() {
        return this.liste.getFirst().get_b();
    }
}
class Pair{
    public int a;
    public int b;
    Pair(int a, int b){
        this.a=a;
        this.b=b;
    }
    public int get_a(){
        return this.a;
    }
    public int get_b(){
        return this.b;
    }

    

    

}
