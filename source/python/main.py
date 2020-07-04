
# Pulls recipes information down from Satisfactory gamepedia page.
# Uses known list of items to pull down. Currently only pulls component items.

import json
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://satisfactory.gamepedia.com/{0}'
INGREDIENT_STYLE = 'border:0; line-height:1; padding:0.5em'

AVG_MINER_RATE = 1

def parse():
    json_data = {}

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
                if 'Ore' in component:
                    cmp_name = component.replace('_', ' ')
                    json_data[cmp_name] = {}
                    json_data[cmp_name]['building'] = {}
                    json_data[cmp_name]['building']['type'] = 'Miner'
                    json_data[cmp_name]['building']['time'] = str(AVG_MINER_RATE)
                else:
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

                        # recipe building
                        building = recipe_td[building_start_index].find('span').text
                        building_time_text = recipe_td[building_start_index].find(text=True, recursive=False)

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

                        # add to json table
                        json_data[recipe_name] = {}

                        json_data[recipe_name]['ingredients'] = {}
                        for ingredient in ingredients:
                            divs = ingredient.find_all('div')
                            parts_zero = divs[0].text.split('\u00d7')
                            ingredient_name = parts_zero[1].strip()
                            json_data[recipe_name]['ingredients'][ingredient_name] = {}
                            json_data[recipe_name]['ingredients'][ingredient_name]['amount'] = parts_zero[0].strip()
                            json_data[recipe_name]['ingredients'][ingredient_name]['rate'] = divs[3].text.split('/')[0].strip()

                        json_data[recipe_name]['building'] = {}
                        json_data[recipe_name]['building']['type'] = building
                        json_data[recipe_name]['building']['time'] = building_time_text

                        json_data[recipe_name]['products'] = {}
                        for product in products:
                            divs = product.find_all('div')
                            parts_zero = divs[0].text.split('\u00d7')
                            product_name = parts_zero[1].strip()
                            json_data[recipe_name]['products'][product_name] = {}
                            json_data[recipe_name]['products'][product_name]['amount'] = parts_zero[0].strip()
                            json_data[recipe_name]['products'][product_name]['rate'] = divs[3].text.split('/')[0].strip()

    pretty_json = json.dumps(json_data, sort_keys=True, indent=4)
    print(pretty_json)
    with open('../resources/components.json', 'w') as f:
        f.write(pretty_json)


if __name__ == "__main__":
    parse()
