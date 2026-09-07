package ejer3;

public class CuentaBancaria {
    private String titular;
    private String nroCuenta;
    private double saldo;

    public CuentaBancaria(String titular, String nroCuenta, double saldo) {
        this.titular = titular;
        this.nroCuenta = nroCuenta;
        this.saldo = saldo;
    }

    public void depositar(double monto) {
        if (monto <= 0) {
            System.out.println("Error: No se puede depositar un monto negativo o 0.");
        } else {
            this.saldo += monto;
            System.out.println("Depósito de " + monto + " exitoso. Saldo actual: " + this.saldo);
        }
    }

    public void retirar(double monto) {
        if (monto > this.saldo) {
            System.out.println("Error: Saldo insuficiente. Intenta retirar más dinero del disponible.");
        } else {
            this.saldo -= monto;
            System.out.println("Retiro de " + monto + " exitoso. Saldo actual: " + this.saldo);
        }
    }

    public void mostrarDatos() {
        System.out.println("Cuenta de: " + titular + " | Nro: " + nroCuenta + " | Saldo: Bs. " + saldo);
    }

    public static void main(String[] args) {
        CuentaBancaria cuenta = new CuentaBancaria("Juan Perez", "100200300", 500.0);
        cuenta.mostrarDatos();
        cuenta.retirar(600.0);
        cuenta.depositar(-50.0);
        cuenta.depositar(200.0);
        cuenta.retirar(100.0);
    }
}