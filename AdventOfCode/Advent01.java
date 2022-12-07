package AdventOfCode;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Advent01{

    public static void main(String[] args){
        ArrayList<Integer> elfes = new ArrayList<>();
        int count = 0;
        try{
            File input = new File("/Users/jo/development/adventOfCode22/input/01.txt");
            Scanner scanner = new Scanner(input);    

            while(scanner.hasNextLine()){
                String line = scanner.nextLine();
                if(line.equals("")){
                    elfes.add(count);
                    count = 0;
                }else {
                    int num = Integer.parseInt(line);
                    count += num;
                }
            }
            scanner.close();
        }catch(FileNotFoundException e){
            System.out.println("FILE NOT FOUND");
            e.printStackTrace();
        }catch(NumberFormatException e){
            System.out.println("NUMBER FORMAT EXCEPTION");
            e.printStackTrace();
        }
        
        Collections.sort(elfes);
        int biggestThree = elfes.get(elfes.size()-1) + elfes.get(elfes.size()-2) +elfes.get(elfes.size()-3);
        System.out.println("Biggest three Value: " + biggestThree);
    }    
}