
# Pulls recipes information down from Satisfactory gamepedia page.
# Uses known list of items to pull down. Currently only pulls component items.

import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://satisfactory.gamepedia.com/{0}'
INGREDIENT_STYLE = 'border:0; line-height:1; padding:0.5em'


def parse():
    with open('../resources/components.txt', 'r') as f:
        components = f.readlines()
        for component in components:
            component = component.rstrip('\n').replace(' ', '_')
            print('\nCollecting: {0}'.format(component))

            component_url = BASE_URL.format(component)
            html_text = requests.get(component_url).text
            soup = BeautifulSoup(html_text, 'html.parser')

            # do not do find_all since first table is always recipe
            recipe_table = soup.find('table', {'class': 'wikitable'})

            if recipe_table is not None:
                recipes = recipe_table.find('tbody').find_all('tr', {'class': 'firstRow'})
                for recipe in recipes:
                    recipe_td = recipe.find_all('td')  # 5 long

                    # recipe name
                    recipe_name = recipe_td[0].text.replace('Alternate', ' Alternate')

                    # recipe ingredients
                    ingredients_text = ''
                    building_start_index = 1
                    ingredients = []
                    for i in range(1, len(recipe_td)):
                        if recipe_td[i].has_attr('style'):
                            if recipe_td[i]['style'] == INGREDIENT_STYLE:
                                ingredients.append(recipe_td[i])
                        else:
                            building_start_index = i
                            break
                    for ingredient in ingredients:
                        divs = ingredient.find_all('div')
                        ingredient_text = '{0} @ {1}'.format(divs[0].text, divs[3].text)
                        if ingredients_text == '':
                            ingredients_text = ingredient_text
                        else:
                            ingredients_text = '{0} and {1}'.format(ingredients_text, ingredient_text)

                    # recipe building
                    building = recipe_td[building_start_index].find('span').text
                    building_time_text = recipe_td[building_start_index].find(text=True, recursive=False)
                    building_text = '{0} @ {1}'.format(building, building_time_text)

                    # products
                    products_text = ''
                    products_start_index = building_start_index + 1
                    products = []
                    for i in range(products_start_index, len(recipe_td)):
                        if recipe_td[i].has_attr('style'):
                            if recipe_td[i]['style'] == INGREDIENT_STYLE:
                                products.append(recipe_td[i])
                        else:
                            break
                    for product in products:
                        divs = product.find_all('div')
                        product_text = '{0} @ {1}'.format(divs[0].text, divs[3].text)
                        if products_text == '':
                            products_text = product_text
                        else:
                            products_text = '{0} and {1}'.format(products_text, product_text)

                    print('{0}: {1} in {2} per {3}'.format(recipe_name, ingredients_text, building_text, products_text))


if __name__ == "__main__":
    parse()
