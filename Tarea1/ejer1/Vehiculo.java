package ejer1;

public class Vehiculo {
    private String marca;
    private String modelo;
    private int anio;
    private int kilometraje;
    private String color;

    public Vehiculo(String marca, String modelo, int anio, int kilometraje, String color) {
        this.marca = marca;
        this.modelo = modelo;
        this.anio = anio;
        this.kilometraje = kilometraje;
        this.color = color;
    }

    public void mostrarDatos() {
        System.out.println("Auto: " + marca + " " + modelo + " (" + anio + ") - Color: " + color);
    }

    public void mostrarKilometraje() {
        int km = this.kilometraje / 1000;
        int m = this.kilometraje % 1000;
        System.out.println("Kilometraje de " + marca + ": " + km + " km y " + m + " metros.");
    }

    public void cambiarColor(String nuevoColor) {
        this.color = nuevoColor;
        System.out.println("El nuevo color del auto es: " + this.color);
    }

    public static void main(String[] args) {
        Vehiculo auto1 = new Vehiculo("Toyota", "Corolla", 2020, 15500, "Rojo");
        Vehiculo auto2 = new Vehiculo("Nissan", "Sentra", 2019, 8200, "Azul");
        
        auto1.cambiarColor("Negro");
        auto1.mostrarKilometraje();
        auto1.mostrarDatos();
        
        auto2.cambiarColor("Blanco");
        auto2.mostrarKilometraje();
        auto2.mostrarDatos();
    }
}