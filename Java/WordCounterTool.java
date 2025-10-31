import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class WordCounterTool {

    public static void main(String[] args) {
        // Check if a file path as argument
        if (args.length == 0) {
            System.out.println("Usage: java WordCounterTool <file_path>");
            return; // Exit the program if no file path is given
        }
        
        // Get the file path
        String path = args[0]; 
        
        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            int charCount = 0;
            int lineCount = 0;
            int wordCount = 0;
            String line;

            while ((line = br.readLine()) != null) {
                lineCount++;
                charCount += line.length();
                
                // Split the line by whitespace
                String[] words = line.split("\\s+");
                wordCount += words.length;
            }

            System.out.println("Analysis of the file: " + path);
            System.out.println("-----------------------------------");
            System.out.println("Number of characters: " + charCount);
            System.out.println("Number of words: " + wordCount);
            System.out.println("Number of lines: " + lineCount);

        } catch (IOException e) {
            System.err.println("An error occurred while reading from file: " + e.getMessage());
        }
    }
}
