

shopping_archive = []


def archive_shopping_list(shop_list):
    def archive_store(*args):
        list_to_archive = shop_list(*args)
        if list_to_archive:
            shopping_archive.append(list_to_archive)
        else:
            print(f'No shopping list to add to archive')
    return archive_store
