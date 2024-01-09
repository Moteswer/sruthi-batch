# views.py
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CustomerRegistrationForm, PINVerificationForm
# ottapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, JsonResponse
from .models import Customer, CustomerProfile, movie
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.views import View
from .models import Customer, CustomerProfile, KidProfile
from .forms import CustomerProfileForm, KidProfileForm

def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                customer = Customer.objects.get(username=username)
                if customer.password == password:
                    # Get the customer ID and redirect to the profile detail page
                    customer_id = customer.id
                    return redirect('profile_detail', customer_id=customer_id)
                else:
                    form.add_error(None, 'Invalid credentials')
            except Customer.DoesNotExist:
                form.add_error(None, 'User not found')

    return render(request, 'user/login.html', {'form': form})






def home_view(request):
    return render(request, 'home.html')



def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page 
    else:
        form = CustomerRegistrationForm()

    return render(request, 'registration.html', {'form': form})


def profile_list(request):
    # Assuming the user is logged in and has a related customer object
    if request.user.is_authenticated:
        customer = request.user.customer  # Assuming a one-to-one relationship between User and Customer
        profiles = CustomerProfile.objects.filter(customer=customer)
        return render(request, 'user/profile_list.html', {'profiles': profiles})
    else:
        # Handle the case where the user is not authenticated (e.g., redirect to login)
        return render(request, 'error.html', {'error_message': 'User is not authenticated'})





class ProfileDetailView(View):
    template_name = 'profile_detail.html'

    def get(self, request, customer_id):
        customer = Customer.objects.get(id=customer_id)
        profile = customer.profile.all()  # Assuming there's only one profile per customer
        kid_profiles = customer.kid_profiles.all()
        return render(request, self.template_name, {'customer': customer, 'profile': profile, 'kid_profiles': kid_profiles})
    

def list_profiles(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    profiles = customer.customerprofile.all()  # Assuming your profile model is named CustomerProfile

    return render(request, 'profile_list.html', {'customer': customer, 'profiles': profiles})


def profile_registration_view(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    template_name = 'profile_registration.html'

    # Check the existing number of profiles for the customer
    total_profiles = CustomerProfile.objects.filter(customer=customer).count()

    if total_profiles >= 4:
        # Return an error message or handle the limit reached scenario
        return render(request,'error.html')

    if request.method == 'POST':
        profile_form = CustomerProfileForm(request.POST, request.FILES)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.customer = customer
            profile.save()

            return redirect('profile_detail', customer_id=customer.id)

    else:
        profile_form = CustomerProfileForm()

    return render(request, template_name, {'customer': customer, 'profile_form': profile_form})

def kid_profile_registration_view(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    template_name = 'kid_registration.html'

    # Check the existing number of profiles for the customer
    total_profiles = KidProfile.objects.filter(customer=customer).count()

    if total_profiles >= 2:
        # Return a JSON response with the error message
        return render(request,'error.html')

    if request.method == 'POST':
        profile_form = KidProfileForm(request.POST, request.FILES)

        if profile_form.is_valid():
            kid_profile = profile_form.save(commit=False)
            kid_profile.customer = customer
            kid_profile.save()

            # Optionally, return a success message or an empty JSON response
            return JsonResponse({})

    else:
        profile_form = KidProfileForm()

    return render(request, template_name, {'customer': customer, 'profile_form': profile_form})



def profile_details(request, customer_id, profile_id):
    customer = get_object_or_404(Customer, id=customer_id)
    profile = get_object_or_404(CustomerProfile, id=profile_id, customer=customer)

    if request.method == 'POST':
        pin_form = PINVerificationForm(request.POST)

        if pin_form.is_valid():
            entered_pin = pin_form.cleaned_data['pin']

            if entered_pin == profile.pin:
                # PIN is correct, redirect to the movie_list function
                return redirect('movie_list')
            else:
                # PIN is incorrect, show an error message
                pin_form.add_error('pin', 'Incorrect PIN. Please try again.')

    else:
        # If the request is not a POST, initialize an empty form
        pin_form = PINVerificationForm()

    return render(request, 'pin_verification.html', {'customer': customer, 'profile': profile, 'pin_form': pin_form})

def kidprofile_details(request, customer_id, profile_id):
    customer = get_object_or_404(Customer, id=customer_id)
    profile = get_object_or_404(KidProfile, id=profile_id, customer=customer)

    return render(request, 'hellokids.html', {'customer': customer, 'profile': profile})

def movie_list(request):
    movies = movie.objects.all()
    return render(request, 'hello.html', {'movies': movies})