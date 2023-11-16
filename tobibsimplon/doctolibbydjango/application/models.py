from django.db import models
from authentification.models import Utilisateur

class FormulaireSante(models.Model):
    patient = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date_remplissage = models.DateField()
    periodicite_jours = models.IntegerField()
    is_late = models.BooleanField(default=False)
    poids = models.FloatField()
    tour_de_taille_cm = models.FloatField()
    frequence_cardiaque_min = models.IntegerField()
    tension_arterielle_systolique_matin = models.FloatField()
    tension_arterielle_systolique_soir = models.FloatField()
    tension_arterielle_diastolique_matin = models.FloatField()
    tension_arterielle_diastolique_soir = models.FloatField()
    symptomes_cardiovasculaires = models.TextField()
    nb_medicaments_jour = models.IntegerField()
    
    def get_username(self):
        return self.patient.username

    """
    oublie_medicament_matin = models.BooleanField(default=False)
    oublie_medicament_soir = models.BooleanField(default=False)
    effets_secondaires = models.BooleanField(default=False)
    symptomes_particuliers = models.TextField()
    consommation_alcool = models.BooleanField(default=False)
    grignotage_sucre = models.BooleanField(default=False)
    grignotage_sale = models.BooleanField(default=False)
    nb_repas_jour = models.IntegerField()
    quantite_eau_litres = models.FloatField()
    quantite_alcool_litres = models.FloatField()
    activite_physique = models.BooleanField(default=False)
    nature_activite_physique = models.TextField()
    duree_activite_physique_min = models.IntegerField()
    dyspnee = models.BooleanField(default=False)
    oedeme = models.BooleanField(default=False)
    pre_episode_ir = models.BooleanField(default=False)
    fievre = models.BooleanField(default=False)
    palpitation = models.BooleanField(default=False)
    douleur_thoracique = models.BooleanField(default=False)
    malaise = models.BooleanField(default=False)
    heure_debut_palpitations = models.TimeField(null=True, blank=True)
    duree_total_palpitations_min = models.IntegerField(null=True, blank=True)
    heure_debut_douleurs_thoraciques = models.TimeField(null=True, blank=True)
    duree_total_douleurs_thoraciques_min = models.IntegerField(null=True, blank=True)
    heure_debut_malaises = models.TimeField(null=True, blank=True)
    duree_total_malaises_min = models.IntegerField(null=True, blank=True)
    natremie_mmol_per_l = models.FloatField()
    potassium_mmol_per_l = models.FloatField()
    creatinine_umol_per_l = models.FloatField()
    clairance_creatinine_ml_per_min = models.FloatField()
    nt_probnp_ng_per_l = models.FloatField()
    fer_serique_mg_per_l = models.FloatField()
    hemoglobine_g_per_100_ml = models.FloatField()
    vitesse_sedimentation_mm = models.FloatField()
    proteine_c_reactive_mg_per_l = models.FloatField()
    troponine_ug_per_l = models.FloatField()
    vitamine_d_ng_per_ml = models.FloatField()
    acide_urique_mg_per_l = models.FloatField()
    inr = models.FloatField()
    """