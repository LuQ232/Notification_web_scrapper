import scrapper as scrap

class List_of_posts:
    title_list =[]
    describtion_list=[]
    time_list=[]
    answears_number_list=[]
    views_number_list=[]
    authors_list=[]

    def __init__(self):
        for elem in scrap.list_of_last_posts():
            self.title_list.append(scrap.title_of_post(elem))
            self.describtion_list.append(scrap.describtion_of_post(elem))
            self.time_list.append(scrap.time_of_post_exist(elem))
            self.answears_number_list.append(scrap.number_of_answears(elem))
            self.views_number_list.append(scrap.number_of_views(elem))
            self.authors_list.append(scrap.author_of_post(elem))

    def print_all_data(self):
        for elem in scrap.list_of_last_posts():
            print("_______________________TITLE_________________________")
            print(scrap.title_of_post(elem))
            print("_____________________________________________________")

            print("_______________________DESCRIBTION_________________________")
            print(scrap.describtion_of_post(elem))
            print("_____________________________________________________")

            print("_______________________TIME_OF_EXIST_________________________")
            print(scrap.time_of_post_exist(elem))
            print("_____________________________________________________")

            print("_______________________AUTHOR_________________________")
            print(scrap.author_of_post(elem))
            print("_____________________________________________________")

            print("_______________________VIEWS_________________________")
            print(scrap.number_of_views(elem))
            print("_____________________________________________________")

            print("_______________________ANSWEARS_________________________")
            print(scrap.number_of_answears(elem))
            print("_____________________________________________________")
            print()
            print()
            print()
            print()
            print()
            print()

    def is_new_post(self):
        for index, elem in enumerate(scrap.list_of_last_posts()):
            if(self.title_list[index] != scrap.title_of_post(elem)):
                return True
        return False

    def update(self):
        for index,elem in enumerate(scrap.list_of_last_posts()):
            self.title_list[index] = scrap.title_of_post(elem)
            self.describtion_list[index] = scrap.describtion_of_post(elem)
            self.time_list[index] = scrap.time_of_post_exist(elem)
            self.answears_number_list[index] = scrap.number_of_answears(elem)
            self.views_number_list[index] = scrap.number_of_views(elem)
            self.authors_list[index] = scrap.author_of_post(elem)




