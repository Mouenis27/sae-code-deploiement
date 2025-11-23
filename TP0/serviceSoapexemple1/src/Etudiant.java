import javax.xml.bind.annotation.XmlRootElement;
import java.io.Serializable;
@XmlRootElement
public class Etudiant implements Serializable {
    private String nom;
    private int identiifant;
    private double moyenne;

    public Etudiant() {
    }

    public Etudiant(String nom, int identifant, double moyenne) {
        this.nom = nom;
        this.identiifant = identifant;
        this.moyenne = moyenne;
    }

    public int getIdentiifant() {
        return identiifant;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public void setIdentiifant(int identiifant) {
        this.identiifant = identiifant;
    }

    public double getMoyenne() {
        return moyenne;
    }

    public void setMoyenne(double moyenne) {
        this.moyenne = moyenne;
    }
}
