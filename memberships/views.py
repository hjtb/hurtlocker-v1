from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Membership
from activities.models import Activity


# Create your views here.


def all_memberships(request):
    """A view to show all memberships"""

    memberships_list = get_list_or_404(Membership)

    context = {'memberships_list': memberships_list}

    return render(request, 'memberships/all_memberships.html', context)

# individual membership page not working properly


def membership_page(request, key):
    """ A view to return the membership page """

    current_membership = get_object_or_404(Membership, pk=key)

    activities_list = get_list_or_404(Activity)

    context = {
        'current_membership': current_membership,
        'activities_list': activities_list,
    }
    return render(request, 'memberships/membership_page.html', context)
