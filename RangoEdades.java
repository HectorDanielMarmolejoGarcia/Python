/*
Author       :Hector Daniel Marmoeljo Garcia 
Fecha        :20211019
*/
import java.util.scanner;
public class RangoEdades {//Inicio clase principal 
	public static void main(String[] args) {//Inicio metodo principal 

		//Declaracion de variables 
	        int fecha_Nacimiento;
		int fecha_Actual = 2021;
		int diferencia =0;
		Scaner teclado = new Scaner (System.in);

		System.out.print("Digite su año de nacimiento:");
		fecha_Nacimiento = teclado.nextInt();

		diferencia = (fecha_Actual - fecha_Nacimiento);

		if (diferencia >= 18){
			System.out.print ("El usuario tiene " + diferencia + ",por lo tanto es mayor de edad");
		}
	        else {
		         System.out.print ("El usuario tiene " + diferencia + ",por lo tanto es menor de edad");
		}
	}//Fin del metodo pmetodo principall
}//Fin de la calse proncipal 	
