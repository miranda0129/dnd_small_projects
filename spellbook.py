import requests
import json


def display_spell(spell_data):
    url = "https://www.dnd5eapi.co" +  spell_data['url']
    headers = {'Accept' : 'application/json'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        spell_data = response.json()
        spell_description = spell_data['desc']

        print(f"Name: {spell_data['name']}")

        json_str = json.dumps(spell_description, indent=2)
        new_list = json_str.replace("[", "").replace("]", "").replace('"', '')
        print(new_list)

        
    else:
        print(f"Name: {spell_data['name']}")
        print(f"Index: {spell_data['index']}")
        print(f"URL: {url}")
        print()

def main():
    url = "https://www.dnd5eapi.co/api/spells"
    headers = {'Accept' : 'application/json'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        spells_data = response.json()
        spells = spells_data['results']

        print("Welcome to the D&D %e Spellbook!")
        print(f"Total Spells: {spells_data['count']}\n")

        while True:
            print("Commands:")
            print("1 - List all spells")
            print("2 - Search for a spell by name")
            print("3 - Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                print("\nList of Spells:")
                for spell in spells:
                    display_spell(spell)
            elif choice == '2':
                spell_name = input("Enter the spell name: ").lower()
                matching_spells = [spell for spell in spells if spell_name in spell['name'].lower()]
                print("\nMatching Spells:")
                for spell in matching_spells:
                    display_spell(spell)
            elif choice == '3':
                print("Goodbye!")
                break  
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
