from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { "my_list":[{
    "restaurant_name": "Pizza_Hut",
    "food_type": "Pizza"
    },
    {
    "restaurant_name": "Burger Makers",
    "food_type": "Burger"
    },
    {
    "restaurant_name": "The Golden Meal",
    "food_type": "Shawerma"
    }
    ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = { "my_object":{"restaurant_name":"Shawerma Saj", "food_type":"Shawerma"}

    }
    return render(request, 'detail.html', context)
