from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Recipe
from .forms import RecipeForm


@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "recipes/recipe_list.html", {"recipes": recipes})


@login_required
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, "recipes/recipe_detail.html", {"recipe": recipe})


@login_required
def recipe_create(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            # Set user if available; allow anonymous recipes
            if request.user and request.user.is_authenticated:
                recipe.user = request.user
            recipe.save()
            form.save_m2m()
            return redirect("recipe_detail", recipe.id)
    else:
        form = RecipeForm()
    return render(request, "recipes/recipe_form.html", {"form": form, "create": True})


@login_required
def recipe_edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("recipe_detail", recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    return render(
        request,
        "recipes/recipe_form.html",
        {"form": form, "create": False, "recipe": recipe},
    )


@login_required
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == "POST":
        recipe.delete()
        return redirect("recipe_list")
    return render(request, "recipes/recipe_confirm_delete.html", {"recipe": recipe})
