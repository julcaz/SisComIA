import java.util.Random;

public class VectoresNumerosPar{
    public static void main(String[] args) {
        Random random = new Random();

        int numeros[]=new int[10];

        for(int i=0;i<numeros.length;i++){
            numeros[i]=random.nextInt(i);
        }
        numerosAleatorios(numeros);

    }
    public static void  numerosAleatorios(int numeros[]){
        for(int i=0;i<numeros.length;i++){
            System.out.println("Vector posicion " + i + " = " + numeros[i]) ;
        }
    }
    public static void contarEImprimir(){

    }
}