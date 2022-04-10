from factories import Mysqlfactory

if __name__ == '__main__':
    print("Running... \n")
    
    usecase = Mysqlfactory.create()
    response = usecase.first_rule(True)
    print(response)
    
    