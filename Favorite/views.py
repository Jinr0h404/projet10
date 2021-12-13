from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Favorite.models import Favorites
from User.models import CustomUser
from django.core.paginator import Paginator
from Product.models import Product


# Create your views here.
@login_required
def index(request):
    """requires user authentication. Displays the list of all products saved in the favorites table for
    the user who is logged in. Use paginator to display the result on several pages in groups of 6"""
    user_connected = CustomUser.objects.get(pk=request.user.id)
    query_list = Favorites.objects.filter(user_id=user_connected)
    products_list = []
    substitute_product = []
    bad_product = []
    all_product = Product.objects.all()
    favorite_regroup = []

    for i in query_list:
        """For each element of the favorites table whose user id is that of the connected person"""
        substitute_product.append((i.substitute_id_id, i.product_id_id))
        bad_product.append(Product.objects.get(pk=i.product_id_id))
        products_list.append(Product.objects.get(pk=i.substitute_id_id))
        favorite_regroup.append(
            {
                "user_id": user_connected.id,
                "product_id": Product.objects.get(pk=i.product_id_id),
                "substitute_id": Product.objects.get(pk=i.substitute_id_id),
            }
        )
    paginator = Paginator(favorite_regroup, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "nom_produit": page_obj,
        "paginate": True,
        "substitute_product": substitute_product,
        "bad_product": bad_product,
        "all_product": all_product,
        "favorite_regroup": favorite_regroup,
    }

    return render(request, "Favorite/index_favoris.html", context)
