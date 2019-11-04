import java.util.List;
import java.util.Dictionary;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Collections;

public class Logic {
    private ArrayList<ArrayList<String>> _items;

    public Logic(ArrayList<ArrayList<String>> items){
        _items = items;
    }

    public ArrayList<ArrayList<String>> sortItOptimal(){
        HashMap<Double, String> bofa = new HashMap<Double, String>();
        HashMap<Double, String> nameLoc = new HashMap<Double, String>();
        ArrayList<Double> sortOrdered = new ArrayList<Double>();
        ArrayList<String> optimal = new ArrayList<String>();
        ArrayList<String> optimal2 = new ArrayList<String>();
        //for(int i = 0; i < _items.size(); i++){
            //bofa.put(Integer.parseInt(_items.get(i).get(2)) * 1.0, _items.get(i).get(1));
        //}
        for(int i = 0; i < _items.size(); i++){
            double lil = (i*1.0)/_items.size();
            int total = Integer.parseInt(_items.get(i).get(2));
            double sortNum = total + lil;
            sortOrdered.add(sortNum);
            bofa.put(sortNum, _items.get(i).get(1));
            nameLoc.put(sortNum, _items.get(i).get(0));
        }
        Collections.sort(sortOrdered);

        for(int i = 0; i < _items.size(); i++){
            String current = bofa.get(sortOrdered.get(i));
            String muck = nameLoc.get(sortOrdered.get(i));
            optimal.add(current);
            optimal2.add(muck);
            //int easy = (int) Math.round(sortOrdered.get(i)-.5);
        }
        ArrayList<ArrayList<String>> boyo = new ArrayList<ArrayList<String>>();
        boyo.add(optimal);
        boyo.add(optimal2);

        return boyo;
    }

    public ArrayList<ArrayList<String>> sortItUnoptimal(){
        HashMap<Double, String> bofa = new HashMap<Double, String>();
        HashMap<Double, String> nameLoc = new HashMap<Double, String>();
        ArrayList<Double> sortOrdered = new ArrayList<Double>();
        ArrayList<String> optimal = new ArrayList<String>();
        ArrayList<String> optimal2 = new ArrayList<String>();
        //for(int i = 0; i < _items.size(); i++){
        //bofa.put(Integer.parseInt(_items.get(i).get(2)) * 1.0, _items.get(i).get(1));
        //}
        for(int i = 0; i < _items.size(); i++){
            double lil = (i*1.0)/_items.size();
            int total = Integer.parseInt(_items.get(i).get(2));
            double sortNum = total + lil;
            sortOrdered.add(sortNum);
            bofa.put(sortNum, _items.get(i).get(1));
            nameLoc.put(sortNum, _items.get(i).get(0));
        }
        Collections.sort(sortOrdered);
        int counter = 0;
        for(int i = 0; i < _items.size(); i++){
            if(i % 2 == 1){
                String current = bofa.get(sortOrdered.get(i/2));
                String muck = nameLoc.get(sortOrdered.get(i/2));
                optimal.add(current);
                optimal2.add(muck);
                //bofa.remove(sortOrdered.get(0));
                //nameLoc.remove(sortOrdered.get(0));
            }
            else{
                String current = bofa.get(sortOrdered.get(bofa.size()-1-i/2));
                String muck = nameLoc.get(sortOrdered.get(nameLoc.size()-1-i/2));
                optimal.add(current);
                optimal2.add(muck);
                //bofa.remove(sortOrdered.get(bofa.size()-1));
                //nameLoc.remove(sortOrdered.get(nameLoc.size()-1));
            }
            //int easy = (int) Math.round(sortOrdered.get(i)-.5);
        }
        ArrayList<ArrayList<String>> boyo = new ArrayList<ArrayList<String>>();
        boyo.add(optimal);
        boyo.add(optimal2);

        return boyo;

    }
}
