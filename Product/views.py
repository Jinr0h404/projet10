from django.shortcuts import render, redirect, get_object_or_404
from Product.models import Product
from User.models import CustomUser
from Favorite.models import Favorites
from django.core.paginator import Paginator


# Create your views here.
def search(request):
    """get the keyword in query and do a search in the product name column for all products that contain this word.
    uses paginator to create a presentation of 6 products per page"""
    query = request.GET.get("query")
    products_list = Product.objects.filter(product_name__icontains=query).order_by("id")
    paginator = Paginator(products_list, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "nom_produit": page_obj,
        "paginate": True,
        "query": query,
    }
    return render(request, "Product/search.html", context)


def count_to_dict(lst):
    """loop on the list of id's to create a dictionary of key = product id / value = count how many common categories"""
    return {k: lst.count(k) for k in lst}


def substitute_getter(id_product):
    """We create a list of all the product objects having a common category with the requested product.
    For each product of the object list a new list is filled with the corresponding id.
    Returns a list of tuple (productID, nbrCategory in common) sorted in descending order of values nbr Common Category"""
    product = get_object_or_404(Product, pk=id_product)
    list_brut = Product.objects.filter(category__in=product.category.all()).exclude(
        pk=id_product
    )
    list_order_value = []
    for prod in list_brut:
        list_order_value.append(prod.pk)

    list_count_common = count_to_dict(list_order_value)
    valeur_sub = sorted(list_count_common.items(), key=lambda x: x[1], reverse=True)
    return valeur_sub


def search_substitute(request):
    """get the id in query and use substitute_getter function for returns a list of tuple (productID, nbrCategory
    in common) and uses paginator to create a presentation of 6 products per page"""
    query = request.GET.get("query")
    query_id = Product.objects.filter(pk=query)
    products_tuple = substitute_getter(query)
    products_list = []
    for i in products_tuple:
        products_list.append(Product.objects.get(pk=i[0]))
    paginator = Paginator(products_list, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "nom_produit": page_obj,
        "paginate": True,
        "query": query,
        "query_id": query_id,
    }

    return render(request, "Product/search_substitute.html", context)


def save_substitute(request):
    """get the id of product and id of his substitute in query with post method and save it with the id of connected
    user. Redirect the user on the favorite page"""
    query_substitute = request.POST["save"]
    query_list = query_substitute.split(",")
    if request.method == "POST":
        query = Product.objects.get(pk=query_list[1])
        user_connected = CustomUser.objects.get(pk=request.user.id)
        substitute_id = Product.objects.get(pk=query_list[0])
        favorite_substitute = Favorites.objects.create(
            substitute_id=substitute_id,
            product_id=query,
            user_id=user_connected,
        )

    return redirect("/favoris")


def product_info(request, product_id):
    """get the id of product in the url. Display product info page with nutriscore"""
    query = product_id
    query_id = Product.objects.filter(pk=query)
    context = {
        "nom_produit": query_id,
        "query": query,
        "query_id": query_id,
    }
    return render(request, "Product/product_info.html", context)
