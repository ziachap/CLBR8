from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import loader, Context
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from App.forms import UserForm, UserProfileForm
from App.models import *

# Create your views here.
#@login_required
def index(request):
    print("index view")
    # get all users
    user_list = User.objects.all()
    # get current user
    c_user = request.user

    # obtain the context for the user's request.
    context = RequestContext(request, {
                'user_list': user_list,
                'c_user': c_user,
            })

    print("1")
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        print("POST method")

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(username=username, password=password)
        print("2")
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                print("3")
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                print("4")
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        print("5")
        t = loader.get_template('App/index.html')
        return HttpResponse(t.render(context))

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'App/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def profile(request, username):

    # get all users
    user_list = User.objects.all()
    # get current user
    c_user = request.user
    # get recipient user whose profile is being viewed
    r_user = User.objects.get(username=username)

    t = loader.get_template('App/profile.html')
    c = Context({
            'user_list': user_list,
            'c_user': c_user,
            'r_user': r_user,
        })

    return HttpResponse(t.render(c))

def browse_map(request):

    # get all users
    user_list = User.objects.all()
    # get current user
    c_user = request.user

    t = loader.get_template('App/browse_map.html')
    c = Context({
            'user_list': user_list,
            'c_user': c_user,
        })

    return HttpResponse(t.render(c))