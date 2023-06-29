// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        // Press Alt+Enter with your caret at the highlighted text to see how
        // IntelliJ IDEA suggests fixing it.
//        System.out.printf("Hello and welcome!");

        Prova.printar();
        Prova p = new Prova(5);
        try {
            p.erro(p.getNum());
        }
        catch (Exception e) {
            System.out.println("entrei no catch");
            System.out.println(e.getMessage());
        }

        Fila<Integer> f = new Fila(10);
        f.add(1);
        f.add(2);
        f.add(3);
        f.add(4);
        f.printa();
        f.printa();

        Generica.nsei(15);
        Generica.nsei("Chuchu com abobrinha");


    }
     
}

class Prova {

    private int num;

    public Prova(int num) {
        this.num = num;
    }

    public int getNum() {
        return this.num;
    }

    public static void printar() {
        System.out.println("acessei um metodo estico");
    }

    public void erro(int num) throws Exception {
        if (num == 5) {
            throw new Exception("Deu pau", null);
        }
        else {
            System.out.println("Deu bom");
        }
    }
}

class Fila<T> {
    private int tam;
    private int inicio;
    private int fim;
    public List<T> fila;

    public Fila(int tam) {
        this.tam = tam;
        this.fila = new ArrayList<T>(tam);
        this.inicio = 0;
        this.fim = -1;
    }

    public void printa() {
        System.out.println(this.fila.get(inicio++));
    }

    public void add(T toAdd) {
        this.fim++;
        fila.add(toAdd);
    }
}

class Generica {
    public static <T> void nsei(T param) {
        System.out.println(param);
    }
}