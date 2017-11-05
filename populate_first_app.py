import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from first_app.models import Topic, AccessRecord, WebPage
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Science', 'Art', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N = 5):
    for entry in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        wbpg = WebPage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name = wbpg, date = fake_date)[0]

if __name__ == '__main__':
    print("populating...")
    populate(20)
    print("completed")
