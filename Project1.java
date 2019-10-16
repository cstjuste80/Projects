//Cliff St. Juste Class
//CIS 213 2018 Fall
//Dr.Cooper
//PA 1


// Questionaire up to 10 questions that decides what type of video game console you should purchase. Whether its an Playstation, Xbox, or Wii U.
// The Main choice is between ps4 and xbox.
// If your answers come out to be even then you will be most likely to end up with an Wii U based of your responses.

// Also some questions don't come with points towards any system.

import java.util.Scanner;

public class project1
{
   public static void main(String []args)
   {



int xboxScore = 0;
int ps4Score = 0;

      
      Scanner scan = new Scanner (System.in);
         String in;

      String[] questions = new String[10];

      //Starting the array elements
      questions[0] = "1) Enter a number between (1 - 4)";

      //QUESTION 1
      // No point question
      System.out.println(questions[0]);



      //in READS INPUT FROM USER
      in = scan.nextLine();

      if(in.equals(""))
      {
         System.out.println(" \n");





      }



      else
      {
         System.out.println(" \n");

      }

      //QUESTION 2
      // No point question
	  System.out.println("2) Please enter the number of years of gaming experience. ");



      in = scan.nextLine();

      if(in.equals(""))
      {

         System.out.println(" \n");

      

      }
      else
      {
         System.out.println("  \n");
      }

      //QUESTION 3
      
	  System.out.println("3) What type of phone do you currently own?");





      in = scan.nextLine();

      if(in.equals("iphone"))
      {
         System.out.println("+1 ps4  \n");

         ps4Score++;
      System.out.println( " 1 points towards console p4 ");


      }
      else
      {
         System.out.println("+1 xbox \n");
         xboxScore++;

          System.out.println( " 1 points towards console xbox");

      }

 
      questions[3] = "4) Rank the games in order. Gears of War,call of duty,nba2k,madden,fortnite,battlegrounds";

      //QUESTION 4
      // no point question
      System.out.println(questions[3]);



    
      in = scan.nextLine();

      if(in.equals(""))
      {
         System.out.println("  \n");



      }
      else
      {
         System.out.println(" \n");
      }

   //inniitialize array elements
      questions[4] = "5) Whats a better number choice between odds and evens";

      //QUESTION 5

      System.out.println(questions[4]);



      //in READS INPUT FROM USER
      in = scan.nextLine();

      if(in.equalsIgnoreCase("evens"))

      {
         System.out.println("+1 ps4  \n");
         ps4Score++;
      System.out.println( " 1 Points towards console p4");

      }
      else
      {
         System.out.println("+1 xbox \n");
         xboxScore++;

      System.out.println( " 1 points towards console xbox \n");

      }

      //inniitialize array elements
      questions[5] = "6) Have you ever played on a Playstation 2? Yes/No ";

      //QUESTION 6

      System.out.println(questions[5]);



      //in READS INPUT FROM USER
      in = scan.nextLine();

      if(in.equals("yes"))
      {
         System.out.println(" +1 PS  \n");
         ps4Score++;
      System.out.println( " 1 Points towards console p4  ");

      }
      else
      {
         System.out.println(" +1 xbox \n");
         xboxScore++;
         System.out.println(  " 1 Points towards console xbox ");


      }


      questions[6] = "7) What type of gamer are you? (First person shooter/Racing) ";

      //QUESTION 7

      System.out.println(questions[6]);


      
      in = scan.nextLine();

      if(in.equals("racing"))
      {
         System.out.println("+1 ps4  \n");
         ps4Score++;
      System.out.println( " 1 Points toward console p4 ");

      }
      else
      {
         System.out.println(" +1 xbox \n");
         xboxScore++;
           System.out.println(  " 1 Points toward console xbox ");

      }



      questions[7] = "8) Whats a better game controller in your opinion? (xbox / ps4) ";

      //QUESTION 8

      System.out.println(questions[7]);



     
      in = scan.nextLine();

      if(in.equals("ps4"))
      {
         System.out.println("+1 ps4 \n");
         ps4Score++;
      System.out.println( " 1 Points towards console p4 ");

      }
      else
      {
         System.out.println("+1 xbox \n");
         xboxScore++;
         System.out.println(  " 1 Points towards console xbox ");


      }

      
      questions[8] = "9)Choose one between the two colors(blue/green) ";

      //QUESTION 9

      System.out.println(questions[8]);



     
      in = scan.nextLine();

      if(in.equals("blue"))
      {
         System.out.println("+1 ps4 \n");
         ps4Score++;
      System.out.println(  " 1 Points towards console p4 ");

      }
      else
      {
         System.out.println("+1 xbox\n");
         xboxScore++;
         System.out.println(  " 1 Points towards console xbox ");

      }

 
      questions[9] = "10) Are you willing to pay almost 300$ for a console?(yes/no) ";

      //QUESTION 10

      System.out.println(questions[9]);



   
      in = scan.nextLine();

      if(in.equals("yes"))
      {
         System.out.println("+1 ps4 \n");
         ps4Score++;
      System.out.println(  " 1 Points towards console ps4 ");

      }
      else
      {
         System.out.println("+1 xbox \n");
         xboxScore++;
         System.out.println(  " 1 Points towards console xbox ");


      }

if (ps4Score > xboxScore){

  System.out.println("\n you should buy an Ps4!!!!");

}

else if (xboxScore > ps4Score){

System.out.println("\n you should buy an xbox 1 !");

}
 else{

   System.out.println("\n you should buy an Wii U!! ");
 }

   }

}