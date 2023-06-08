public class Teste {

    public static void calculaFolhaSalarial(Funcionario arr[], int n) {
        System.out.println("--------------------");

        double folhaSalarial = 0;
        for (int i = 0; i < n; i++) {
            try {
                double salarioFunc = arr[i].calculaSalario();
                folhaSalarial += salarioFunc;
    
                System.out.printf("nome: %s | salario: %.2f\n", arr[i].getNome(), salarioFunc);
                System.out.println("--------------------");
            }
            catch (NullPointerException e) {
                continue;
            }
        }

        System.out.printf("Folha salarial: %.2f\n", folhaSalarial);
    }

    public static void main(String args[]) {
        int n = 7;

        Funcionario arrayFunc[] = new Funcionario[n];
        String arrayCPF[] = new String[n];
        String arrayNomes[] = new String[n];

        arrayCPF[0] = "59382082034";
        arrayNomes[0] = "Lionel Messi";

        arrayCPF[1] = "47910702086";
        arrayNomes[1] = "Farid Tari";

        arrayCPF[2] = "85841264060";
        arrayNomes[2] = "Cristiano Ronaldo";

        arrayCPF[3] = "32347464000";
        arrayNomes[3] = "Lebron James";

        arrayCPF[4] = "43355267090";
        arrayNomes[4] = "Lewis Hamilon";

        arrayCPF[5] = "21198182075";
        arrayNomes[5] = "Tiger Woods";

        arrayCPF[6] = "12345678901";
        arrayNomes[6] = "Nikola Kovac";

        for (int i = 0; i < n; i++) {
            int tipoFunc = i % 3;

            if (Funcionario.verificaCPF(arrayCPF[i])) {
                 
                if (tipoFunc == 0)
                    arrayFunc[i] = new Gerente(arrayNomes[i], arrayCPF[i]);

                else if (tipoFunc == 1)
                    arrayFunc[i] = new Assistente(arrayNomes[i], arrayCPF[i]);

                else if (tipoFunc == 2)
                    arrayFunc[i] = new Vendedor(arrayNomes[i], arrayCPF[i], 1202.56);
            }
        }

        Teste.calculaFolhaSalarial(arrayFunc, n);
    }
}
