package com.example.spring1;

import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.Collection;
// JPA
// H2 en memoire

@RestController
public class MyApi {

    public static ArrayList<Etudiant> liste = new ArrayList();
    static {
        liste.add(new Etudiant(0,"A",19));
        liste.add(new Etudiant(1,"B",19));
        liste.add(new Etudiant(2,"C",19));
        liste.add(new Etudiant(3,"D",19));
    }
    @GetMapping(value = "/liste")
    public Collection<Etudiant> getAllEtudiant() {
        return liste;
    }

    @GetMapping(value = "/getEtudiant")
    public Etudiant getEtudiant(int id) {
        return liste.get(id);
    }

    //Get renvoie d'une ressource
    //Post creer une nouvelle ressource
    //PUT modifier une ressource
    //DELETE supprimer une ressource

    @PostMapping(value = "/addEtudiant")
    public Etudiant addEtudiant(Etudiant etudiant) {
        liste.add(etudiant);
        return etudiant;
    }

    @DeleteMapping(value="/delete")
    public void supprimerEtudiant(int id) {
        liste.remove(id);
    }

    @PutMapping(value = "/modifier")
    public void modifierEtudiant(int identifiant , String nom) {
        liste.get(identifiant).setNom(nom);
    }

    @GetMapping(value = "/b")
    public String bonjour() {
        return "Bonjour !";
    }
    @GetMapping(value = "/bn")
    public String bonsoir() {
        return "Bonsoir !";
    }

    @GetMapping(value="/etudiant")
    public Etudiant getEtudiant() {
        return new Etudiant(1, "A", 19);
    }

    @GetMapping(value ="/somme" )
    public double somme(double a, double b) {
        return a + b;
    }
}
