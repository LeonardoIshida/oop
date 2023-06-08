public class Vendedor extends Funcionario{
    private double comissao;

    public Vendedor(String nome, String CPF, double comissao) {
        super(nome, CPF);
        this.comissao = comissao;
    }

    public double calculaSalario() {
        return this.getSalarioBase() + this.comissao;
    }
}
