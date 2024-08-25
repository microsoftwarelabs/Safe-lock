   import java.io.BufferedReader;
   import java.io.InputStreamReader;
   import java.io.IOException;

   public class GoIntegration {

       public static void main(String[] args) {
           try {
               // Caminho para o executável Go
               String goExecutable = "./safe lock blockchain";

               // Cria o processo para executar o executável Go
               ProcessBuilder processBuilder = new ProcessBuilder(goExecutable);
               processBuilder.redirectErrorStream(true);

               // Inicia o processo
               Process process = processBuilder.start();

               // Captura a saída do processo
               BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
               String line;
               while ((line = reader.readLine()) != null) {
                   System.out.println("Output: " + line);
               }

               // Aguarda o término do processo e obtém o código de saída
               int exitCode = process.waitFor();
               System.out.println("Process exited with code: " + exitCode);

           } catch (IOException | InterruptedException e) {
               e.printStackTrace();
           }
       }
   }