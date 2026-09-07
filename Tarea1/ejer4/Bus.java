package ejer4;

public class Bus {
    private int capacidadMaxima;
    private int pasajerosActuales;
    private double dineroRecaudado;

    public Bus(int capacidadMaxima) {
        this.capacidadMaxima = capacidadMaxima;
        this.pasajerosActuales = 0;
        this.dineroRecaudado = 0.0;
    }

    public void subirPasajeros(int x) {
        if (this.pasajerosActuales + x <= this.capacidadMaxima) {
            this.pasajerosActuales += x;
            System.out.println("Han subido " + x + " pasajeros al bus.");
        } else {
            System.out.println("El bus está lleno. No pueden subir " + x + " pasajeros.");
        }
    }

    public void cobrarPasaje(int cantidadPasajeros) {
        double total = cantidadPasajeros * 1.50;
        this.dineroRecaudado += total;
        System.out.println("Se ha cobrado pasaje a " + cantidadPasajeros + " pasajeros. Ingreso: Bs. " + total);
        System.out.println("Dinero total acumulado en el bus: Bs. " + this.dineroRecaudado);
    }

    public void mostrarAsientosDisponibles() {
        int disponibles = this.capacidadMaxima - this.pasajerosActuales;
        System.out.println("Asientos disponibles en el bus: " + disponibles);
    }

    public static void main(String[] args) {
        Bus miBus = new Bus(40);
        miBus.subirPasajeros(10);
        miBus.cobrarPasaje(10);
        miBus.mostrarAsientosDisponibles();
    }
}