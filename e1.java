import java.io.*;
import java.util.*;
public class e1 {
    public static void main(String[] args) throws IOException {
        String folderPath = "123";
        List<File> txtFiles = findTxtFiles(folderPath);

        //out
        for (File file : txtFiles) {
            System.out.println(file.getAbsolutePath());
        }
    }

    public static List<File> findTxtFiles(String folderPath) {
        List<File> txtFiles = new ArrayList<>();
        File folder = new File(folderPath);

        if(folder.exists() && folder.isDirectory()) {
            searchForTxtFiles(folder,txtFiles);
        }
        return txtFiles;
    }

    public static void searchForTxtFiles(File folder,List<File> txtFiles) {
        File[] files = folder.listFiles();

        if(files != null) {
            for(File file : files) {
                if(file.isFile() /*&& file.getName().endsWith(".txt")*/) {
                    txtFiles.add(file);
                    if(file.getName().equals("5.txt"))
                        System.out.println(file.delete());
                } else if(file.isDirectory()) {
                    txtFiles.add(file);
                    searchForTxtFiles(file,txtFiles);
                }
            }
        }
    }


}
