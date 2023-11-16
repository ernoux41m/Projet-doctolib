from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from authentification.models import Utilisateur, medecinPatient
from application.models import FormulaireSante
from application.forms import FormulaireSanteForm 
import os
from django.http import HttpResponse
import datetime
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport

@login_required
def accueil(request):
    prenom = request.user.username
    return render(request,"accueil.html",
                  context={"prenom": prenom})

@login_required
def comptes(request):
    regexMDP = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+-]).{8,}$"
    message = ""
    if request.method == "POST":
        ancienMDP = request.POST["ancienMDP"]
        nouveauMDP1 = request.POST["nouveauMDP1"]
        nouveauMDP2 = request.POST["nouveauMDP2"]
        
        verification = authenticate(username = request.user.username,
                                    password = ancienMDP)
        if verification != None:
            if nouveauMDP1 == nouveauMDP2:
                utilisateur = Utilisateur.objects.get(username = request.user.username)
                #utilisateur = Utilisateur.objects.get(id=request.user.id)
                utilisateur.set_password(request.POST.get("nouveauMDP1"))
                utilisateur.save()
                return redirect("accueil")
            else:
                message = "⚠️ Les deux mot de passe ne concordent pas ⚠️"
        else:
            message = "L'ancien mot de passe n'est pas bon. T'es qui toi ? 😡"
    return render(request,
                  "comptes.html",
                  {"regexMDP" : regexMDP, "message" : message})



 # Importez votre modèle ApplicationFormulaire
@login_required
def edaia(request):
    if request.user.role == "patient":
        return redirect("https://media.tenor.com/2euSOQYdz8oAAAAj/this-was-technically-illegal-maclen-stanley.gif")
    else:
        # Récupérez les données de la table ApplicationFormulaire
        queryset = FormulaireSante.objects.all()  
        df = pd.DataFrame(list(queryset.values()))

        # Chemin absolu vers le répertoire où sera stocké le rapport
        report_directory = '/home/matthieu/Formation_IA/Cours_formation_2_année/tobibsimplon/doctolibbydjango/application/templates/'

        # Générer le rapport EDA avec pandas_profiling
        profile = ProfileReport(df, title='Rapport EDA', explorative=True)
        report_path = os.path.join(report_directory, 'eda_report.html')
        profile.to_file(report_path)

        # Rediriger vers le rapport EDA s'il est généré
        if os.path.exists(report_path):
            return render(request, "eda_report.html", {'rapport_eda': '/home/matthieu/Formation_IA/Cours_formation_2_année/tobibsimplon/doctolibbydjango/eda_report.html'})
        else:
            # Dans votre vue Django
            return render(request, "eda_report.html", {'rapport_eda': '/home/matthieu/Formation_IA/Cours_formation_2_année/tobibsimplon/doctolibbydjango/eda_report.html'})

@login_required
def historique(request):

    role = request.user.role

    if role not in ["responsable", "patient", "medecin"]:
        return redirect("accueil")

    champsFormulaireSante = [field.name for field in FormulaireSante._meta.get_fields()]

    if role == "responsable":
        idDesFormulaires = [valeur.id for valeur in FormulaireSante.objects.all()]
        dataFormulaireSante = [FormulaireSante.objects.filter(id=id).values()[0].values() for id in idDesFormulaires]


    elif role == "medecin":
        # Je récupère les objets patients du médecin connecté
        idpatients = medecinPatient.objects.filter(idMedecin=Utilisateur.objects.filter(username=request.user.username)[0].id).values_list('idPatient', flat=True)
        dataFormulaireSante = [form.values for idpatient in idpatients for form in FormulaireSante.objects.filter(patient=idpatient).values()]

    elif role == "patient":
        dataFormulaireSante = [form.values for form in FormulaireSante.objects.filter(patient=Utilisateur.objects.filter(username=request.user.username)[0].id).values()]

    context = {"dataFormulaireSante" : dataFormulaireSante, "champsFormulaireSante" : champsFormulaireSante}

    print(context)
    return render(request, "historique.html", context)

    

@login_required
def associationMedecinPatient(request):
    # 1- Récupérer la liste des id des médecins et des patients
    # 2- Ensuite on ne garde que les patients qui ne sont pas dans la table medecinPatient
    # 3- On créé ensuite un template qui contiendra une liste déroulante
    # 4- Dans cette liste déroulante on va afficher d'un côté les médecins
    # et de l'autre les patients filtrés (voir étapge 2)
    # https://developer.mozilla.org/fr/docs/Web/HTML/Element/select
    
    medecins = [medecin for medecin in Utilisateur.objects.filter(role="medecin")]
    patients = [patient for patient in Utilisateur.objects.filter(role="patient")]
    listePatientsAssocies = [ligne.idPatient for ligne in medecinPatient.objects.all()]
    #print("listePatientsAssocies :", listePatientsAssocies)
    listePatientsNonAssocies = [patient for patient in patients if patient not in listePatientsAssocies]
    tableAssociationMedecinPatient = medecinPatient.objects.all()

    if request.method == "POST":
        medecin = request.POST["medecin"]
        patient = request.POST["patient"]
        #print("medecin", type(medecin), medecin)
        medecinPatient(idMedecin = Utilisateur.objects.filter(username=medecin)[0], 
                       idPatient = Utilisateur.objects.filter(username=patient)[0]).save()
        return redirect("associationMedecinPatient")
    return render(request, "associationMedecinPatient.html",
                  {"listePatientsNonAssocies" : listePatientsNonAssocies,
                   "medecins" : medecins,
                   "tableAssociationMedecinPatient" : tableAssociationMedecinPatient})


@login_required
def formulaireSante(request):
    if request.method == "POST":
        formulaire = FormulaireSanteForm(request.POST)
        if formulaire.is_valid():
            sauvagarde = formulaire.save()  
    else:
        formulaire = FormulaireSanteForm()  
    return render(request, "formulaireSante.html", {"formulaire": formulaire})


#class ApplicationWizardView(SessionWizardView):
#    form_list = [InfoGeneraleForm, EtatDeSanteForm]
#    template_name = "formulaireSante.html"
#    def done(self, form_list, **kwargs):
#            return HttpResponse('Formulaire envoyé')


       #form = form_list[0]
       #if form.cleaned_data.get('patient'):    
       #     form.save()
       
       # form = form_list
        #for form in form_list:
        #    print(form.cleaned_data.get('patient'))
        #for form in form_list:
        #    instance = form.save(commit=False)
        #return HttpResponse("Formulaire soumis !")

    
