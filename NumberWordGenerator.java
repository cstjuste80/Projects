import java.util.Scanner;
import java.io.PrintWriter;
import java.io.FileNotFoundException;

public class NumberWordGenerator {

private static String[] two = {"a", "b", "c"};
private static String[] three = {"d", "e", "f"};
private static String[] four = {"g", "h", "i"};
private static String[] five = {"j", "k", "l"};
private static String[] six = {"m", "n", "o"};
private static String[] seven = {"p", "r", "s"};
private static String[] eight = {"t", "u", "v"};
private static String[] nine = {"w", "x", "y"};
private static char[] numArray;
private static String[] wordList = new String[2187];


}

public static void main(String[] args) {

    //initialize output file name and PrintWriter object
    String fileName = "output.txt";
    PrintWriter outputStream = null;
    String output = "";

    //try and catch exception
    try {
        outputStream = new PrintWriter(fileName);
    }
    catch (FileNotFoundException e){
        System.out.println("Error opening file " + fileName + ".");
        System.exit(0);
    }

    //initialize scanner and wordList array
    Scanner kb = new Scanner(System.in);
    for (int i=0; i < 2187; i++){
        wordList[i] = "";
    }


    System.out.println("input a 7 digit phone number.");
    String num = kb.next();
    numArray = num.toCharArray();
    for (int p = 0; p < 2187; p++){
        System.out.println(wordList[p]);
    }
}

}
