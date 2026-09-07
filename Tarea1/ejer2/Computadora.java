package ejer2;

public class Computadora {
    private String marca;
    private String procesador;
    private int ram;
    private int almacenamiento;

    public Computadora(String marca, String procesador, int ram, int almacenamiento) {
        this.marca = marca;
        this.procesador = procesador;
        this.ram = ram;
        this.almacenamiento = almacenamiento;
    }

    public Computadora() {
    }

    public void setMarca(String marca) { this.marca = marca; }
    public void setProcesador(String procesador) { this.procesador = procesador; }
    public void setRam(int ram) { this.ram = ram; }
    public void setAlmacenamiento(int almacenamiento) { this.almacenamiento = almacenamiento; }

    public int getAlmacenamiento() { return almacenamiento; }

    public boolean esRamIgualA(int x) {
        return this.ram == x;
    }

    public void mostrarDatos() {
        System.out.println("Computadora: " + marca + " | Proc: " + procesador + " | RAM: " + ram + "GB | Almacenamiento: " + almacenamiento + "GB");
    }

    public static void mostrarMayorAlmacenamiento(Computadora c1, Computadora c2) {
        System.out.println("--- Computadora con mayor almacenamiento ---");
        if (c1.getAlmacenamiento() > c2.getAlmacenamiento()) {
            c1.mostrarDatos();
        } else if (c2.getAlmacenamiento() > c1.getAlmacenamiento()) {
            c2.mostrarDatos();
        } else {
            System.out.println("Ambas tienen la misma capacidad de almacenamiento.");
        }
    }

    public static void main(String[] args) {
        Computadora compu1 = new Computadora("HP", "Core i5", 8, 512);
        
        Computadora compu2 = new Computadora();
        compu2.setMarca("Dell");
        compu2.setProcesador("Core i7");
        compu2.setRam(16);
        compu2.setAlmacenamiento(1024);

        System.out.println("¿La RAM de la primera compu es igual a 8GB? " + compu1.esRamIgualA(8));

        Computadora.mostrarMayorAlmacenamiento(compu1, compu2);
    }
}