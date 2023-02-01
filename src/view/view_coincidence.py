class viewCoincidence:

    def __init__(self, results: dict):
        self.results = results

    
    def show_matches(self):
        print('*******************************************************')
        for names, matches in self.results.items():
            #name_list = list(names)
            #print(name_list[0]+'-'+name_list[1]+': '+ str(matches))
            print(names+': '+ str(matches))