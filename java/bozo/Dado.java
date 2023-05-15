import java.util.concurrent.ThreadLocalRandom;

public class Dado {
    private int numLados;
    private int ultimoLado;

    public Dado() {
        numLados = 6;
    }
    public Dado(int n) {
        numLados = n;
    }

    public int getLado() {
        return ultimoLado;
    }

    public int rolar() {
        Random r = new Random();
        return r.getIntRand(numLados+1);
    }

    @Override
    public java.lang.String toString() {
        int num = rolar();
        ultimoLado = num;


        if (num == 1) {
            String s = new String("+-----+\n|     |\n|  *  |\n|     |\n+-----+\n");
            return s;
        }
        else if (num == 2) {
            String s = new String("+-----+\n|  *  |\n|     |\n)|    |\n+-----+\n");
            return s;
        }
        else if (num == 3) {
            String s = new String("+-----+\n|*    |\n|  *  |\n|    *|\n+-----+\n");
            return s;
        }
        else if (num == 4) {
            String s = new String("+-----+\n|*   *|\n|     |\n|*   *|\n+-----+\n");
            return s;
        }
        else if (num == 5) {
            String s = new String("+-----+\n|*   *|\n|  *  |\n|*   *|\n+-----+\n");
            return s;
        }
        else if (num == 6) {
            String s = new String("+-----+\n|* * *|\n|     |\n|* * *|\n+-----+\n");
            return s;
        }

        String nulo = new String("Nao existe um dado com esse lado\n");
        return nulo;
    }

    public static void	main(java.lang.String[] args) {
        Dado d = new Dado();
        //System.out.println(d.rolar());
        String s = d.toString();
        System.out.println(s);
        System.out.println(d.getLado());
        return;
    }


}
