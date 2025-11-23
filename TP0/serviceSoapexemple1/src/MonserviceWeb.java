import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.jws.WebService;
/*
 SOAP : Simple Object Acces Protocol ...
 JAX-WS (Java Annotation XML for Web Service)
 JAXB (JAVA Architecture XML Building)
*/

/*
 URL : Uniform Resource Locator
 URN : Uniform Resource Name
 URI : Unifrom Resource Identifier
 URN + URL = URI
*/

import javax.jws.WebService;

@WebService(targetNamespace = "http://www.polytech.fr")
public class MonserviceWeb {

    @WebMethod(operationName = "convertir")
    public double conversion(double mt){
        return mt * 0.9;
    }

    public double somme(@WebParam(name = "parametre1") double a , double b){
        return a+b;
    }

    public Etudiant getEtudiant(int identifiant){
        return new Etudiant("Mario" , 1 , 19);
    }
}