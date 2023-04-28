# from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect
from listings.models import Band, Listing
from listings.forms import ContactUsForm, BandForm


def band_list(request):
    bands = Band.objects.all()

    return render(request, "listings/band_list.html",
                  {'bands': bands})


def band_detail(request, id):  # notez le paramètre id supplémentaire
    band = Band.objects.get(id=id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band}
                  )  # nous passons l'id au modèle


def listings(request):
    listings = Listing.objects.all()
    return render(request, "listings/listing.html",
                  {'listings': listings})


def about(request):
    return render(request, 'listings/about.html')


def contact(request):    

    if request.method == 'POST':
        form = ContactUsForm(request.POST)        

        if form.is_valid():
            subject = 'Message from '
            subject += f'{form.cleaned_data["name"] or "anonyme"} '
            subject += 'via MerchEx Contact Us form'
            send_mail(
                subject=subject,
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
        return redirect('listings:email-sent') 
    else:
        form = ContactUsForm()  # ajout d’un nouveau formulaire ici

    return render(request,
                  'listings/contact.html',
                  {'form': form})  # passe ce formulaire au gabarit


def email_sent(request):
    return render(request, 'listings/email_sent.html')


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe
            # que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments
            # à la fonction de redirection
            return redirect('listings:band-detail', band.id)

    else:
        form = BandForm()

    return render(request,
                  'listings/band_create.html',
                  {'form': form})


def band_update(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe
            # que nous venons de mettre à jour
            return redirect('listings:band-detail', band.id)
    else:
        form = BandForm(instance=band)
    return render(request,
                  'listings/band_update.html',
                  {'form': form})


def band_delete(request, id): 
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes
        return redirect('listings:band-list')
    
    return render(request,
                  'listings/band_delete.html',
                  {'band': band})
