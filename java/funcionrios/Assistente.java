public class Assistente extends Funcionario{
    public Assistente(String nome, String CPF) {
        super(nome, CPF);
    }

    public double calculaSalario() {
        return this.getSalarioBase();
    }
}
