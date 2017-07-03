import java.io.BufferedReader;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.*;

Path file = Paths.get("C:\\Users\\BoyanKushlev\\Desktop\\input.txt");

try {
    BufferedReader br = Files.newBufferedReader(file, Charset.forName("US-ASCII"));
    String line;
    while ((line = br.readLine()) != null) {
        // do something
    }
} catch (IOException e) {
    System.err.println(e);
}
