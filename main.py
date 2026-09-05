import init_django_orm  # noqa: F401

from django.db.models import QuerySet
from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for genre in genres:
        Genre.objects.create(name=genre)

    for actor_name, actor_surname in actors:
        Actor.objects.create(
            first_name=actor_name,
            last_name=actor_surname
        )

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(last_name="Kianu").update(last_name="Keanu")
    Actor.objects.filter(last_name="Reaves").update(last_name="Keanu")

    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(name="Scarlett").delete()

    return Genre.objects.filter(last_name="smith").order_by("first_name")
