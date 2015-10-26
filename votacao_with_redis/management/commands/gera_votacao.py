# coding: utf-8
from django.core.management.base import BaseCommand
from ...models import Poll, Option


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        Poll.objects.filter(id=1).delete()
        Option.objects.filter(id__in=[1, 2, 3, 4]).delete()

        question = Poll.objects.create(id=1, title="Quem deve ser o vencedor")

        option1 = Option.objects.create(id=1, name="Mario", pool=question, votes=0)
        option2 = Option.objects.create(id=2, name="Luigi", pool=question, votes=0)
        option3 = Option.objects.create(id=3, name="Yoshi", pool=question, votes=0)
        option4 = Option.objects.create(id=4, name="Princesa", pool=question, votes=0)

        question.save()
        option1.save()
        option2.save()
        option3.save()
        option4.save()
        print "Pesquisa e Opções cadastradas com sucesso"
