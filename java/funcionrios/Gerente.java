public class Gerente extends Funcionario{
    public Gerente(String nome, String CPF) {
        super(nome, CPF);
    }

    public double calculaSalario() {
        return this.getSalarioBase() * 2;
    }
}
