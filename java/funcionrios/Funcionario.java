public abstract class Funcionario {
    private String nome;
    private String CPF;
    static private double salarioBase = 5000.00;

    public Funcionario(String nome, String CPF) {
        this.nome = nome;
        this.CPF = CPF;
    }

    public String getNome() {
        return this.nome;
    }

    public double getSalarioBase() {
        return Funcionario.salarioBase;
    }
    
    abstract double calculaSalario();

    public static boolean verificaCPF(String CPF) {
        try {
            int lenCPF = CPF.length();

            // alocando o utimo digito em uma variavel
            char aux = CPF.charAt(lenCPF - 1);
            int ultDig = Character.getNumericValue(aux);

            // alocando o penutimo digito em uma variavel
            aux = CPF.charAt(lenCPF - 2);
            int penultDig = Character.getNumericValue(aux);

            // verificacao do penultimo digito
            int soma = 0;
            for (int i = 10, k = 0; i >= 2; i--, k++) {
                aux = CPF.charAt(k);
                int algarismo = Character.getNumericValue(aux);

                soma += (i * algarismo);
            }

            int resto = ((soma * 10) % 11);
            if (resto == 10 || resto == 11)
                resto = 0;

            if (resto != penultDig)
                return false;

            // verficacao do ultimo digito
            soma = 0;
            for (int i = 11, k = 0; i >= 2; i--, k++) {
                aux = CPF.charAt(k);
                int algarismo = Character.getNumericValue(aux);

                soma += (i * algarismo);
            }

            resto = (soma * 10) % 11;
            if (resto == 10 || resto == 11)
                resto = 0;

            if (resto != ultDig)
                return false;

             return true;
        }
        catch (NumberFormatException e) {
            System.out.println("Formato de CPF invalido !!");
            return false;
        }
    }
}
